# content_dao.py 코드 테스트를 위한 py파일

from database import content_dao

#### 1. 게시글 입력하기
# content_subject, content_writer_idx,content_text, content_file, content_board_idx
# content_dao.insertContentData('테스트제목', 2, '테스트내용', 'aaa.jpg', 10)
''' 주의** 
    content_writer_idx는 FK로 user_table의 정보를 '참조'한다. 그래서 user_table에 없는 값을 넣으려고 하면
    오류가 난다. 마찬가지로 content_board_idx역시 FK로 board_table 정보를 참조하기 때문에, board_table에 
    없는 값을 입력하면 오류가 난다.
'''
# print('입력되었습니다.')

#### 2. 게시글 전부를 가져오기
# result = content_dao.selectContentDataAll()
# print(result)

#### 3. 게시글 하나를 가져오기
# result = content_dao.selectContentDataOne(1)
# print(result)

#### 4. 게시글 수정하기
# (content_subject, content_writer_idx, content_text, content_file, content_board_idx, content_idx)
# content_dao.updateContentData('수정한 제목', 2, '테스트 내용을 수정해본다.', 'bbb.jpg', 10, 1)
# print('수정되었습니다.')

#### 5. 글 삭제하는 함수
# content_dao.deleteContentData(1)
# print('삭제되었습니다. ')

#### 6. 방금 작성한 글의 번호(글 번호가 제일 큰 것)을 가져오기.
# res = content_dao.getMaxContentIdx(content_board_idx=2)
# print(res)

#### 7. 전체 글 개수 가져오기
res = content_dao.getContentCnt(1)
print(res)