# board_dao.py 코드 테스트를 위한 py파일

from database import board_dao

#### 1. 게시판 정보 추가
# board_name = '테스트 게시판'
# board_dao.insertBoardName(board_name)
# print(f'[{board_name}]이 생성되었습니다.')

### 2. 모든 게시판 이름 불러오기
res = board_dao.selectBoardNameAll()
print(res)
print('모든 게시판 이름 출력 완료')

#### 3. 특정 게시판 이름 불러오기
# res = board_dao.selectBoardNameOne(9)
# print(res)

#### 4. 게시판 정보를 수정하는 테스트
# board_dao.updateBoardData( '구내식당 게시판',9)
# print('게시판 이름이 변경되었습니다.')

#### 5. 게시판 정보를 삭제
# res = board_dao.deleteBoardData(9)
# print(res)