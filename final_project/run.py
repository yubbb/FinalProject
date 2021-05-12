# -*- coding: utf-8 -*-
# 기본 템플릿
from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify

import os

app = Flask(__name__)

@app.route('/')
def home():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('index.html')

@app.route('/predict')
def predict():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('index.html')

# 은서
@app.route('/prediction')
def prediction():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('prediction.html')
# /은서

@app.route('/analysis')
def analysis():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('index.html')


# ################################
if __name__ == '__main__':
    app.run(debug=True)
    # [4] 소켓io를 이용하여 서버가동 (래핑해서 가동)
    # socketio.run( app,  debug=True)