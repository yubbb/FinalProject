from flask import Blueprint
from flask import render_template
from flask import session

from database import board_dao
from database import content_dao
# blueprint 객체 생성
main_blue = Blueprint('main', __name__)

# main을 요청하면 호출되는 함수
@main_blue.route('/main')
def main(): # 브라우저가 main을 요청하면 이 함수가 호출된다.

    # 세션처리: 로그인한 후 메인으로 돌아왔을 때 사용자 인덱스 번호
    # print(session.get('login_user_idx')) 

    # 게시판 이름을 가져오기
    board_data = board_dao.selectBoardNameAll()
    # print(board_data) # [ {} ]: 리스트의 딕셔너리 형태

    # 각 게시판별 상위 5개 데이터를 담을 리스트
    content_top5_list = [] # 딕셔러니 for문
    for i in board_data:
        # 게시판별 첫 페이지 게시글을 가져오기
        a1 = content_dao.selectContentDataAll(i['board_idx'],1)
        # print(a1[:5])

        # 리스트에 담기
        content_top5_list.append(a1[:5])
    # print(len(content_top5_list)) # 4게(자유게시판~스포츠게시판)

        # i['board_name']

    # 응답결과를 렌더링
    html = render_template('main/main.html', board_data=board_data,
                            content_top5_list=content_top5_list)

    # html 데이터를 렌더링한다: 브라우저에게 브라우저가 사용할 데이터를 만들어서 보내는 것.
    return html