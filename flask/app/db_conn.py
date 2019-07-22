#file name : db_conn.py
#pwd : /home/sp1end0r/source/cert/project/app

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
import db_module

main = Blueprint('db_conn', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def conn():
	db = db_module.database()
	if db != 0:
        	return render_template('/main/conn.html')

	else :
		return render_template('/main/fail.html')




