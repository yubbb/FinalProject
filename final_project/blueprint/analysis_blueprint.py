from flask import Blueprint
from flask import render_template
from flask import session

# blueprint 객체 생성 : 주소 세팅
analysis_blue = Blueprint('analysis', __name__)

@analysis_blue.route('/analysis')
def analysis():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('index.html')
