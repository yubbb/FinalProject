from flask import Flask
from flask import redirect

# Blueprint 불러오기
from blueprint.main_blueprint import main_blue
from blueprint.board_blueprint import board_blue
from blueprint.user_blueprint import user_blue

# 서버역할을 할 객체 생성
# template_folder: 렌더링할 html문서가 있는 곳(기본=templates, 우리는 views라는 파일을 사용)
app = Flask(__name__, template_folder='views', static_folder='static')

# 세션영역 사용을 위한 암호화 키를 설정한다.
# 아무렇게나 넣으면 된다. flask에선 세션처리할 때 암호화 처리를 한다.
app.secret_key='dsgdkjwegknk' 

# Blueprint 등록
app.register_blueprint(main_blue)
app.register_blueprint(board_blue)
app.register_blueprint(user_blue)

# 주소만 입력하고 들어왔을 경우 호출될 부분
@app.route('/')
def index() :
    # 브라우저에게 main.py을 요청하는 응답 결과를 브라우저로 전달한다.(redirect)
    # 따라서 localhost로 들어가면(주소를 입력하고 들어가면) 자동으로 main을 요청하면서
    # 주소가 localhost\main으로 변경된다.
    # 요청 명령을 브라우저가 받아서 하는거다. 브라우저가 요청하기 때문에 주소창의 주소가 바뀜
    return redirect('main')

# 서버 가동
# port : 80, 요청할 때 포트번호를 생략하고 요청할 수 있다.
# debug=True : 코드를 수정하면 서버가 재 가동한다.
app.run(port=80, debug=True)