#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask 
from flask import request
from UserUtil import get_user_info

import json
import SearchLogic

app = Flask(__name__)

# 判断登录是否有效
@app.route('/login', methods=['POST','GET'])
def login():
	username = request.args.get('username')
	password = request.args.get('password')
	return json.dumps(get_user_info(username,password,False))

# 搜索分裂标题
@app.route('/search', methods=['POST','GET'])
def search():
	username = ''
	password = ''
	key_word = ''
	number = 1
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		key_word = request.form['keyword']
		number = request.form['pagesize']
	elif request.method == 'GET':
		username = request.args.get('username')
		password = request.args.get('password')
		key_word = request.args.get('keyword')
		number = request.args.get('pagesize')
		print(request.args)
	else:
		return json.dumps(())
	result = get_user_info(username,password,True)
	if result['status'] == False:
		return json.dumps(result)
	brand_list = SearchLogic.get_brand_list(key_word)
	results = SearchLogic.get_processed_title(brand_list,SearchLogic.get_title_list_by_total_page(key_word,number))
	result['list'] = results
	return json.dumps(result)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0') 

