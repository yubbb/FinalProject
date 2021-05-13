from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
# 회원가입 정보를 DB에 저장하기 위해서.
from database import user_dao

# 응답 결과를 "만들어 주는 곳"

# Blueprint 객체 생성
user_blue = Blueprint('user', __name__)

# 사용자 로그인
@user_blue.route('/user_login')
def user_login() :
    # 파라미터 데이터 추출한다.
    login_fail = request.args.get('login_fail')
    # login_fail이라는 이름으로 넘어온 것이 있으면 값을 받고 없으면 None을 가지게 된다.

    # 응답 결과를 렌더링
    html = render_template('user/user_login.html', login_fail=login_fail)
    return html

# 회원가입
@user_blue.route('/user_join')
def user_join():
    # 응답 결과를 렌더링
    html = render_template('user/user_join.html')
    return html

# 정보 수정 페이지로 이동
@user_blue.route('/user_modify')
def user_modify():
    # 세션에 저장된 사용자 인덱스 번호 가져오기
    login_user_idx  = session.get('login_user_idx')

    # 만약 로그인 하지 않았다면 로그인 페이지로 강제이동
    if login_user_idx == None:
        return  '''
                <script>
                    alert('로그인을 해주세요')
                    location.href = 'user_login'
                </script>
            
                '''
    # 로그인한 사용자의 정보를 가져온다.
    login_user_data = user_dao.selectUserDataOne(login_user_idx)
    # print(login_user_data) # 딕셔너리 형태: {'user_idx': 4, 'user_name': '홍길동', 'user_id': 'hhhh', 'user_pw': 'qqqq'}

    # 응답 결과를 렌더링
    html = render_template('user/user_modify.html', login_user_data = login_user_data)
    return html

# 회원가입 처리
@user_blue.route('/user_join_pro', methods=['POST'])
def user_join_pro():
    # 브라우저가 전달한 데이터를 추출한다.
    # print(request.form)
    '''    
    - 결과: ImmutableMultiDict([('user_name', '김은서'), ('user_id', 'sdfsdg'),('user_pw', '1111'), ('user_pw2', '1111')])
    - user_join.html > input 태그의 'name'값들이 key값으로 설정된다.
    '''
    # POST방식
    user_name = request.form.get('user_name') 
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')
    # print(user_name, user_id, user_pw)  

    # 브라우저에서 받아온 데이터를 DB에 저장하기.
    user_dao.insertUserData(user_name, user_id, user_pw)
    return  '''
            <script>
                alert('가입이 완료되었습니다.')
                location.href='user_login'
            </script>
            '''

# 아이디 중복 확인
@user_blue.route('/check_join_id')
def check_join_id():
    # 브라우저각 보낸 아이디를 추출
    new_id = request.args.get('new_id')

    # 중복 확인
    result = user_dao.checkInputUserId(new_id)

    return f'{result}'

# 로그인 처리
@user_blue.route('/user_login_pro', methods=['POST'])
def user_login_pro():
    # 브라우저가 전달한 데이터를 추출한다.
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')

    # print(user_id, user_pw)

    # 사용자 존재 여부를 확인
    result = user_dao.check_login_user(user_id, user_pw)
    # print(result) # 딕셔너리 형태 {'user_idx': 4, 'user_name': '홍길동', 'user_id': 'hhhh', 'user_pw': 'qqqq'}

    # (1) 로그인 실패
    if result == None:
        # 가져온게 아무것도 없다.
        return  '''
                <script>
                    alert('로그인에 실패했습니다.')
                    location.href = 'user_login?login_fail=true'
                </script>
        
                '''
    # (2) 로그인 성공
    else:
        # 세션에 성공한 사용자의 이름을 담아준다.
        session['login_user_idx'] = result['user_idx']
        return '''
                <script>
                    alert('로그인에 성공했습니다.')
                    location.href = 'main'
                </script>
        '''

# 정보 수정 처리
@user_blue.route('/user_modify_pro', methods=['POST'])
def user_modify_pro():
    # 파라미터 추출
    user_pw = request.form.get('user_pw')
    # print(user_pw) # 수정된 비밀번호 값이 출력된다.

    # 세션에서 로그인한 사용자의 인덱스를 가져온다.(사용자를 특정하기 위해)
    login_user_idx = session.get('login_user_idx')
    # print(login_user_idx) # 사용자의 인덱스 번호가 출력된다. 

    # 사용자 정보를 수정한다.
    user_dao.updateUserData(login_user_idx, user_pw)

    return '''
            <script>
                alert('수정되었습니다.')
                location.href = 'user_modify'
            </script>
            '''

# 로그아웃 처리
@user_blue.route('/user_logout')
def user_logout():
    # 세션 영역에서 login_user_idx를 제거하기
    del session['login_user_idx']

    return '''
            <script>
                alert('로그아웃 되었습니다.')
                location.href = 'main'
            </script>

            '''