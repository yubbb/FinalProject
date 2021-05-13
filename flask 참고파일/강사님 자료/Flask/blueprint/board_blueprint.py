from flask import Blueprint
from flask import render_template

board_blue = Blueprint('board', __name__)

# 게시글 리스트
@board_blue.route('/board_main')
def board_main() :

    # 응답결과를 랜더링한다.
    html = render_template('board/board_main.html')

    return html

# 게시글 보는 페이지
@board_blue.route('/board_read')
def board_read() :

    # 응답결과를 랜더링한다.
    html = render_template('board/board_read.html')

    return html

# 글 수정 페이지
@board_blue.route('/board_modify')
def board_modify() :

    # 응답 결과를 랜더링한다.
    html = render_template('board/board_modify.html')
    return html

# 글 작성 페이지
@board_blue.route('/board_write')
def board_write() :

    # 응답 결과를 랜더링한다.
    html = render_template('board/board_write.html')
    return html
