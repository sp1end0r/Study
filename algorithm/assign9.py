#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# filename : assign9.py
# 이진탐색트리

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    #    print ("Sucessfully create binary serch tree !!")

    def convertToTree(self, data): # List를 Tree로 변환
        data = list(set(data)) # Tree에 중복이 있으면 안되므로, 리스트의 중복을 먼저 제거
        for i in data:
            self.insert(i)
    #    print ("Succesfully convert list to tree :) ")

    
    def convertToList(self): ## Tree를 List로 변환
        data = list()
        def _in_order_traversal(root): # BinarySearchTree의 걍우 중위순위탐방(In-order-Traversal)할 경우, 정렬이 됨
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                data.append(root.data)
                _in_order_traversal(root.right)
        
            return data

        data = _in_order_traversal(self.root)
    #    print ("Succesfully convert tree to list :) ")
        return data
    
    def insert(self, data): #User Interface로 제공
        self.root = self._insert_data(self.root, data)
        return self.root is not None

    def _insert_data(self, node, data): #Recursive call을 이용한 트리에 데이터 삽입
        if node is None : 
            node = Node(data)
        #    print("Successfully insert %d in Tree!" % data)

        else : 
            if data < node.data : node.left = self._insert_data(node.left, data)
            else : node.right = node.right = self._insert_data(node.right, data)

        return node


    def find(self, key): #User-Interface로 제공
        if self.root is None : 
            print ("Tree is empty ...")
            return False
        else : 
            return self._find_data(self.root, key)

    def _find_data(self, node, key): #Recursive call을 이용한 트리에 데이터 찾기
        if node is None : #찾는 데이터를 가진 노드가 없을 때 
            print("%d is not found in tree :( " % key)
            exit(0)
        elif node.data == key:
            print("%d is found in List!!" % key)
            return True
        elif node.data > key:
            return self._find_data(node.left, key)
        elif node.data < key : 
            return self._find_data(node.right, key)

    def delete(self, key): # User-Interface로 제공
        if self.root is None :
            print ("Tree is empty ...")
            return False
        #else :
        #    if self.find(key) == False :
        #        return False
        else :
            print ("%d is deleted in tree !" % key)
            self.root = self._delete_data(self.root, key)
            return True

    def _delete_data(self, node, key): #Recursive call을 이용한 Delete Node
        if node is None : 
                return node  
        Parent = node #현재 위치의 노드를 부모노드로 지정
        Left_child = node.left # 부모노드의 왼쪽을 지정
        Right_child = node.right # 부모노드의 오른쪽을 지정

        if key == node.data:
            if Left_child and Right_child: # 부모노드의 Left_child와 Rigth_child가 모두 존재
                while Right_child.left is not None:
                    Parent = Right_child
                    Right_child = Right_child.left
                Right_child.left = node.left
                if Parent != node:
                    Parent.left = Right_child.right
                    Right_child.right = node.right
                node = Right_child
            elif Left_child or Right_child: # 부모노드의 Left_child나 Rigth_child 둘중 하나만 존재 
                node = Left_child or Right_child
                Parent = None
            
            else: # 부모노드의 Left_child와 Rigth_child가 모두 존재 하지 않음
                node = None
        elif key < node.data: # 현재 node의 data가 key보다 크다면 현재 노드를 왼쪽에 있는 노드로 변경
            node.left = self._delete_data(node.left, key)
        else:                 # 현재 node의 data가 key보다 작다면 현재 노드를 오른에 있는 노드로 변경
            node.right = self._delete_data(node.right, key)
        return node

#if __name__ == "__main__":
#    print ("============================================")
#    data = [1,2,3,4,5,6,7,8,8]
#    print (data)
#    print ("============================================")
#    BST = BinarySearchTree()
#    BST.convertToTree(data)
#    print ("============================================")
#    BST.insert(13)
#    print ("============================================")
#    BST.find(1)
#    BST.find(8)
#    #BST.find(11) #없는 값을 찾을 때는 종료
#    print ("============================================")
#    BST.delete(8)
#    BST.delete(1)
#    print ("============================================")
#    data = BST.convertToList()
#    print (data)
#    print ("============================================")


