# -*- coding: utf-8 -*-
# 기본 템플릿
from flask import Blueprint
from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify
from flask import Flask
from flask import redirect
import os

# Blueprint 불러오기
from blueprint.main_blueprint import main_blue
from blueprint.analysis_blueprint import analysis_blue
from blueprint.predict_blueprint import predict_blue

# 서버역할을 할 객체 생성
app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(main_blue)
app.register_blueprint(analysis_blue)
app.register_blueprint(predict_blue)

# 주소만 입력하고 들어왔을 경우 호출될 부분
@app.route('/')
def home():    
    return redirect('main')

if __name__ == '__main__':
    app.run(debug=True)
    # [4] 소켓io를 이용하여 서버가동 (래핑해서 가동)
    # socketio.run( app,  debug=True)