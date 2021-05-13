from flask import Blueprint
from flask import render_template
from flask import session

# blueprint 객체 생성 : 주소 세팅
predict_blue = Blueprint('predict', __name__)

@predict_blue.route('/predict')
def predict():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('index.html')

# 은서
@predict_blue.route('/prediction')
def prediction():    
    return render_template('predict/prediction.html')

# 석영
@predict_blue.route('/pledge')
def pledge():
    return render_template('predict/pledge.html')