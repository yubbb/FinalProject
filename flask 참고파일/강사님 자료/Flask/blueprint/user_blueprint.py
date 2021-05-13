from flask import Blueprint
from flask import render_template
from flask import request

from database import user_dao

# blueprint 객체 생성
user_blue = Blueprint('user', __name__)

# 사용자 로그인
@user_blue.route('/user_login')
def user_login() :

    # 응답 결과를 랜더링한다.
    html = render_template('user/user_login.html')

    return html

# 회원가입
@user_blue.route('/user_join')
def user_join() :

    # 응답 결과를 랜더링한다.
    html = render_template('user/user_join.html')

    return html

# 정보수정
@user_blue.route('/user_modify')
def user_modify() :

    # 응답 결과를 랜더링한다.
    html = render_template('user/user_modify.html')

    return html

# 회원 가입 처리
@user_blue.route('/user_join_pro', methods=['post'])
def user_join_pro() :
    # 브라우저가 전달한 데이터를 추출한다.
    # print(request.form)
    user_name = request.form.get('user_name')
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')

    # print(user_name)
    # print(user_id)
    # print(user_pw)

    # 데이터 베이스에 저장한다.
    user_dao.insertUserData(user_name, user_id, user_pw)

    return '''
            <script>
                alert('가입이 완료되었습니다')
                location.href = 'user_login'
            </script>
           '''

# 아이디 중복확인
@user_blue.route('/check_join_id')
def check_join_id() :
    # 브라우저가 보낸 아이디를 추출한다.
    new_id = request.args.get('new_id')
    # 중복확인
    result = user_dao.checkInputUserId(new_id)

    return f'{result}'