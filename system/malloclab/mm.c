/*
 * mm-naive.c - The fastest, least memory-efficient malloc package.
 * 
 * In this naive approach, a block is allocated by simply incrementing
 * the brk pointer.  A block is pure payload. There are no headers or
 * footers.  Blocks are never coalesced or reused. Realloc is
 * implemented directly using mm_malloc and mm_free.
 *
 * NOTE TO STUDENTS: Replace this header comment with your own header
 * comment that gives a high level description of your soWRITEion.
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

#include "mm.h"
#include "memlib.h"

/*********************************************************
 * NOTE TO STUDENTS: Before you do anything else, please
 * provide your team information in the following struct.
 ********************************************************/
team_t team = {
    /* Team name */
    "ateam",
    /* First member's full name */
    "JaeHyu Lee",
    /* First member's email address */
    "ssinus.zk@gmail.com",
    /* Second member's full name (leave blank if none) */
    "",
    /* Second member's email address (leave blank if none) */
    ""
};

/* single word (4) or double word (8) alignment */
#define W_SIZE 4
#define ALIGNMENT 8
#define CHUNKSIZE (1<<12)

/* rounds up to the nearest multiple of ALIGNMENT */
#define ALIGN(size) (((size) + (ALIGNMENT-1)) & ~0x7)

#define READ(ptr) (*(size_t *)(ptr))
#define READ_SIZE(ptr) (READ(ptr)&~0x7)
#define READ_ALLOC(ptr) (READ(ptr)&~0x1)

#define WRITE(ptr, data) (*(unsigned int *)(ptr) = (data))

#define PACKING(size, alloc) ((size) | (alloc)) 
#define MAX(x,y) ((x)>(y)?(x):(y))

#define HDRP(ptr) ((void *)(ptr)-W_SIZE)
#define FTRP(ptr) ((void *)(ptr)+READ_SIZE(HDRP(ptr))-(2*W_SIZE))

#define NEXT_CHUNK(ptr) ((void *)(ptr)+READ_SIZE((void *)(ptr)-W_SIZE))
#define PREV_CHUNK(ptr) ((void *)(ptr)-READ_SIZE((void *)(ptr)-(2*W_SIZE)))



#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))

void *heap_list = NULL;

static void* coalesc(void *ptr)
{
    size_t prev_alloc = READ_ALLOC(FTRP(PREV_CHUNK(ptr)));
    size_t next_alloc = READ_ALLOC(HDRP(NEXT_CHUNK(ptr)));

    size_t size = READ_SIZE(HDRP(ptr));

    if(prev_alloc && next_alloc) return ptr;

    else if (prev_alloc && !next_alloc)
    {
        size += READ_SIZE(HDRP(NEXT_CHUNK(ptr)));
        WRITE(HDRP(ptr), PACKING(size, 0));
        WRITE(FTRP(ptr), PACKING(size, 0));
    }
    
    else if(!prev_alloc && next_alloc)
    {
        size += READ_SIZE(HDRP(PREV_CHUNK(ptr)));
        WRITE(FTRP(ptr), PACKING(size, 0));
        WRITE(HDRP(PREV_CHUNK(ptr)), PACKING(size,0));
        ptr = PREV_CHUNK(ptr);
    }
    else
    {
        size += READ_SIZE(HDRP(PREV_CHUNK(ptr))) + READ_SIZE(FTRP(NEXT_CHUNK(ptr)));
        WRITE(HDRP(PREV_CHUNK(ptr)), PACKING(size, 0));
        WRITE(FTRP(NEXT_CHUNK(ptr)), PACKING(size,0));
        ptr = PREV_CHUNK(ptr);
        
    }
    
    return ptr;

}
static void* extend_heap(size_t w_size)
{
    void *ptr;
    size_t size;
    
    size = (w_size % 2) ? (w_size + 1) * W_SIZE : w_size * W_SIZE;
    if((long)(ptr = mem_sbrk(size))== -1) return NULL;

    WRITE(HDRP(ptr), PACKING(size,0));
    WRITE(FTRP(ptr), PACKING(size,0));
    WRITE(HDRP(NEXT_CHUNK(ptr)),PACKING(0,1));

    return coalesc(ptr);

}

static void* first_fit(size_t size)
{
    void *ptr;

    for(ptr = heap_list; READ_SIZE(HDRP(ptr)) > 0; ptr = NEXT_CHUNK(ptr))
    {
        if(!READ_ALLOC(HDRP(ptr)) && (size < READ_SIZE(HDRP(ptr)))) return ptr;
    }

    return NULL;

}

static void* place(void* ptr, size_t size)
{
    size_t asize = READ_SIZE(HDRP(ptr));
    
    if((asize - size) >=(4*W_SIZE))
    {
        WRITE(HDRP(ptr), PACKING(size, 1));
        WRITE(FTRP(ptr), PACKING(size, 1));
        ptr = NEXT_CHUNK(ptr);
        WRITE(FTRP(ptr), PACKING(asize-size, 1));
        WRITE(HDRP(ptr), PACKING(asize-size, 1));
    }
    else 
    {
        WRITE(HDRP(ptr), PACKING(asize, 1));
        WRITE(FTRP(ptr), PACKING(asize, 1));

    }

}

/* 
 * mm_init - initialize the malloc package.
 */
int mm_init(void)
{
    if ((heap_list = mem_sbrk(4*(W_SIZE))) == (void *)-1) return -1;

    WRITE(heap_list,0);
    WRITE(heap_list+W_SIZE, PACKING(W_SIZE*2,1)); //heap's prologue header
    WRITE(heap_list+(2*W_SIZE), PACKING(W_SIZE*2,1)); //heap's prlogue footer
    WRITE(heap_list+(3*W_SIZE), PACKING(0,1));

    heap_list += (2*W_SIZE);

    if(extend_heap(CHUNKSIZE/W_SIZE)==NULL) return -1;

    return 0;
}

/* 
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    size_t asize;
    size_t extendsize;
    void *ptr;

    if (size == 0) return NULL;
    if (size <= 2*W_SIZE) 
    {
        asize = 4*W_SIZE;
    }
    else
    {
        asize = (2*W_SIZE)*((size+2*(W_SIZE)+((2*W_SIZE)-1))/(2*W_SIZE));
    }

    if((ptr = first_fit(asize)) != NULL)
    {
        place(ptr, asize);
        return ptr;
    }
    extendsize = MAX(asize,CHUNKSIZE);
    if((ptr = extend_heap(extendsize/W_SIZE)) == NULL) return NULL;

    place(ptr, asize);
    return ptr;
}

/*
 * mm_free - Freeing a block does nothing.
 */
void mm_free(void *ptr)
{
    if(!ptr) return;

    size_t size = READ_SIZE(HDRP(ptr));

    WRITE(HDRP(ptr),PACKING(size,0));

    coalesc(ptr);
    
}

/*
 * mm_realloc - Implemented simply in terms of mm_malloc and mm_free
 */
void *mm_realloc(void *ptr, size_t size)
{
    size_t oldsize;
    void *newptr;
    
    if(size == 0) {
        free(ptr);
        return 0;
    }
    
    if(ptr == NULL) {
        return mm_malloc(size);
    }
    
    newptr = mm_malloc(size);
    
    if(!newptr) {
        return 0;
    }
    
    oldsize = READ_SIZE(ptr);
    if(size < oldsize) oldsize = size;
    memcpy(newptr, ptr, oldsize);
    
    free(ptr);
    
    return newptr;
}














