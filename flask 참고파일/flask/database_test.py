# user_dao.py 코드 테스트를 위한 py파일

#### 1. 접속 테스트
# from database import connector
# conn = connector.get_connection()
# print(conn)
# conn.close() # 접속하고 바로 연결 끊기(오류가 나는지 안 나는지 확인용)

'''
- 커맨드 창에서 $ python database_test.py
    - 결과: <pymysql.connections.Connection object at 0x000001672D73FC88>
    - 연결이 잘 됐다는 의미!
'''
from database import user_dao
#### 2. 사용자 정보 저장 테스트
# from database import user_dao
# user_dao.insertUserData('홍길동', 'Gildong', '1234')
# user_dao.insertUserData('김각생', 'Kim', '1234')
# user_dao.insertUserData('박두철', 'ParkDu', '1234')
# print('DB 저장완료')

#### 3. 모든 사용자 데이터 전부 가져오기
data = user_dao.selectUserDataAll()
print(data) # [ {} ] 리스트의 딕셔너리 형태로 출력된다.
print('출력 완료')

#### 4-1. 사용자 한 명의 정보를 수정하는 함수
# user_idx = 1
# user_pw = 9999
# result = user_dao.updateUserData(user_idx, user_pw)
# print('변경완료')

#### 4-2. 사용자 한 명의 데이터만 가져오기
# user_idx = 1
# data = user_dao.selectUserDataOne(user_idx)
# print(data) # {} : 딕셔너리 형태로 출력
# print('출력완료')

#### 4-3. 사용자 데이터 삭제
# user_idx = 1
# data = user_dao.deleteUserData(user_idx)
# print(data)
# print('삭제되었습니다.')
