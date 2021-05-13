from flask import Blueprint
from flask import render_template
from flask import request
from flask import session

from database import board_dao
from database import content_dao

import os
import time

# 주소부터 setting하고 시작하기
board_blue = Blueprint('board', __name__)

# 게시글 리스트
@board_blue.route('/board_main')
def board_main():
    # 파라미터 데이터를 추출( ?뒤에 있는 파라미터 )
    board_idx = request.args.get('board_idx')

    # page번호를 파라미터로 넘겨주는 과정
    page = request.args.get('page')
    if page == None:
        page = '1'
    page = int(page)

    # 페이지 번호가 0보다 작으면
    if page < 1:
        page = 1

    # 전체 글의 개수 가져오기(게시판마다)
    contentCnt = content_dao.getContentCnt(board_idx)
    # print('Total Content=', contentCnt)

    # 전체 글의 개수를 이용해 전체 **페이지수를 구하기
    pageCnt = (contentCnt // 10)
    if contentCnt % 10 > 0: # 전체 글의 개수를 10개씩 나눈 나머지가 0보다 크면(글이 더 있다면)
        pageCnt = pageCnt + 1 # 페이지수에 1을 더함

    # 현재 페이지 번호가 전체 페이지 개수보다 크면? 전체 페이지 개수로 넣어준다.
    if page > pageCnt:
        page = pageCnt

    # 게시판 정보 가져오기
    board_data = board_dao.selectBoardNameOne(board_idx) 
    # print(board_data) # 결과가 딕셔너리

    # 현재 게시판의 글 목록을 가져온다.
    content_list = content_dao.selectContentDataAll(board_idx, page)
    # print(content_list)

    # 현재 페이지 번호를 이용해 pagination 시작 값을 구한다.
    start_page = ((page - 1) // 10 * 10) + 1

    # 전체 페이지 수를 이용해 pagination 종료 값을 구한다.
    end_page = start_page + 9
    if end_page > pageCnt: # 전체 페이지수가 마지막 페이지수가 될 수 있도록 하는 과정.
        end_page = pageCnt

    # 응답 결과를 렌더링
    html = render_template('board/board_main.html', board_data=board_data, 
                            board_idx=board_idx, content_list=content_list, 
                            start_page=start_page, end_page=end_page, 
                            pageCnt=pageCnt, page=page)
    return html

# 게시글 상세보기
@board_blue.route('/board_read')
def board_read():

    # 파라미터 데이터를 추출
    content_idx = request.args.get('content_idx') # 게시글 인덱스 번호
    board_idx = request.args.get('board_idx') # 게시판 인덱스 번호
    page = request.args.get('page') # 페이지 번호를 가져오기('목록보기'를 눌렀을 때 기존 페이지 화면으로 넘어가도록)
    # print(content_idx, board_idx)

    # 현재 글 정보를 가져오기
    content_data = content_dao.selectContentDataOne(content_idx)
    # print(content_data)

    # 응답 결과를 렌더링
    html = render_template('/board/board_read.html', content_data=content_data, 
                            board_idx=board_idx, page=page, content_idx=content_idx)
    return html

# 게시글 수정
@board_blue.route('/board_modify')
def board_modify():
    # 파라미터 추출
    content_idx = request.args.get('content_idx')
    board_idx = request.args.get('board_idx')
    page = request.args.get('page')

    # print('content_idx=',content_idx)
    # print('board_idx=',board_idx)
    # print('page=',page)

    # 현재 글 정보를 가져오기
    content_data = content_dao.selectContentDataOne(content_idx)
    # print(content_data) # Dictionary

    # 응답 결과를 렌더링
    html = render_template('/board/board_modify.html', content_data=content_data,
                            content_idx=content_idx, board_idx=board_idx, page=page)
    return html

# 글쓰기
@board_blue.route('/board_write')
def board_write():

    # 파라미터 추출
    board_idx = request.args.get('board_idx') 
    # print('board_idx =', board_idx)

    # 응답 결과를 렌더링
    html = render_template('/board/board_write.html', board_idx=board_idx)
    return html

# 글 작성 처리
@board_blue.route('/board_write_pro', methods=['POST'])
def board_write_pro():

    # 데이터 추출
    content_subject = request.form.get('content_subject')
    content_writer_idx = session.get('login_user_idx')
    content_text = request.form.get('content_text')
    content_board_idx = request.form.get('content_board_idx')

    # print(content_subject)
    # print(content_writer_idx)
    # print(content_text)
    # print(content_board_idx)

    # 업로드 처리 예시
    # a1 = request.files.get('content_file')
    # print(a1.filename) # 파일이름만 추출

    # (1) 첨부한 파일이 있을 경우
    if request.files.get('content_file').filename != '':
        # content_file로 넘어오는 파일 데이터를 추출한다.
        content_file = request.files.get('content_file')

        # 중복을 방지하기 위해 파일 이름에 시간을 붙여준다.
        file_name = str(int(time.time())) + content_file.filename # 현재 시간 구하기
        # print(filename) # ex) 1615264745unnamed.jpg

        # 경로를 포함한 파일 이름을 생성
        a1 = os.getcwd() + '/static/upload/' + file_name
        # print(a1) 

        # 저장하기
        content_file.save(a1)

    # (2) 첨부하지 않은 경우
    else:
        file_name = None # DB에 저장할 때 Null으로 저장하는 과정

    # DB에 게시글 정보 저장
    content_dao.insertContentData(content_subject, content_writer_idx, content_text,
                                    file_name, content_board_idx)

    # 방금 작성한 글의 인덱스를 가져온다.
    now_content_idx = content_dao.getMaxContentIdx(content_board_idx)
    # print('latest content index number=', now_content_idx)

    return f'''
            <script>
                alert('작성되었습니다')
                location.href = 'board_read?content_idx={now_content_idx}&board_idx={content_board_idx}'
            </script>
            '''

# 게시글 삭제
@board_blue.route('/board_delete')
def board_delete():
    content_idx = request.args.get('content_idx')
    board_idx = request.args.get('board_idx')
    page = request.args.get('page')

    # print('content_idx=',content_idx)
    # print('board_idx=',board_idx)
    # print('page=',page)

    # 삭제하기
    content_dao.deleteContentData(content_idx)
    return f'''
            <script>
                alert('삭제되었습니다.')
                location.href = 'board_main?board_idx={board_idx}&page={page}'
            </script>
            
            '''

# 글 수정 처리
@board_blue.route('/board_modify_pro', methods=['POST'])
def board_modify_pro():

    # 데이터 추출(제목, 텍스트)
    content_subject = request.form.get('content_subject')
    content_text = request.form.get('content_text')

    # hidden type으로 보낸 데이터 추출
    content_idx = request.form.get('content_idx')
    board_idx = request.form.get('board_idx')
    page = request.form.get('page')
    
    # (1) 첨부한 파일이 있을 경우
    if request.files.get('content_file').filename != '':
        # content_file로 넘어오는 파일 데이터를 추출한다.
        content_file = request.files.get('content_file')

        # 중복을 방지하기 위해 파일 이름에 시간을 붙여준다.
        file_name = str(int(time.time())) + content_file.filename # 현재 시간 구하기
        # print(filename) # ex) 1615264745unnamed.jpg

        # 경로를 포함한 파일 이름을 생성
        a1 = os.getcwd() + '/static/upload/' + file_name
        # print(a1) 

        # 저장하기
        content_file.save(a1)

    # (2) 첨부하지 않은 경우
    else:
        file_name = None # DB에 저장할 때 Null으로 저장하는 과정
        
    # print('content_subject=',content_subject)
    # print('content_text=',content_text)
    # print('content_idx=', content_idx)
    # print('board_idx=',board_idx)
    # print('page=', page)
    # print('file_name=',file_name)

    # 수정처리하는 함수 호출
    content_dao.updateContentData(content_subject, content_text, file_name, content_idx)

    return f'''
            <script>
                alert('수정되었습니다.')
                location.href = 'board_read?content_idx={content_idx}&board_idx={board_idx}&page={page}'
            </script>
            '''
