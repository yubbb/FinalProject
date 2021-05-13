from database import connector

# 사용자 정보 저장
def insertUserData(user_name, user_id, user_pw):
    sql = '''
            insert into user_table
            (user_name, user_id, user_pw)
            values(%s, %s, %s)
          '''
    # **값의 타입에 상관없이 %s 주기

    # 데이터 베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s 부분에 대입될 값을 튜플로 생성한다.
    # **쿼리문의 %s 순서에 맞춰준다.
    data = user_name, user_id, user_pw

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터 베이스 접속을 끊어주기
    conn.close()

# 모든 회원 정보를 반환하는 함수
def selectUserDataAll():
    # 쿼리문
    sql = '''
            select * from user_table
          '''
    # DB 접속
    conn = connector.get_connection()
    cursor = conn.cursor()  

    # %s에 대입할 값 지정(없음)

    # 쿼리문 실행
    cursor.execute(sql)
    result = cursor.fetchall() # SELECT해서 가져올 row의 수가 1개 초과면 fetchall 사용
    
    # DB 접속 해제
    conn.close()

    # 결과 리턴
    return result

# 회원 한 명의 데이터를 가져오는 함수
def selectUserDataOne(user_idx):
    # 쿼리문 작성
    sql = '''
            select * from user_table
            where user_idx = %s
          '''
    # DB 연결 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입될 값 지정
    data = (user_idx) # 하나만 있더라고 튜플로 묶어줘야함

    # 쿼리문 실행
    cursor.execute(sql,data)
    result = cursor.fetchone()

    # DB 접속 해제
    conn.close()

    return result

# 특정 회원의 데이터(pw)를 수정하는 함수
def updateUserData(user_idx, user_pw):
    # 쿼리문
    sql = '''
            update user_table
            set user_pw = %s
            where user_idx = %s
    '''

    # DB 연결 
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값 설정
    data = (user_pw, user_idx)
    
    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()
    
    # DB 접속 해제
    conn.close()

# 회원정보 삭제 함수
def deleteUserData(user_idx):
    # 쿼리문 작성
    sql = '''
            delete from user_table
            where user_idx = %s    
    '''
    # DB 연결 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    
    # %s에 들어갈 값 설정
    data = (user_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # DB 접속 해제
    conn.close()

# 아이디 중복 확인을 위해 아이디 확인하는 함수(+조건절)
def checkInputUserId(new_id):
    # 쿼리문 작성
    sql = '''
        select * from user_table
        where user_id = %s
    '''
    # DB 연결
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s 값 설정
    data = (new_id)

    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone() # 존재하지 않으면 result에는 None이 들어있다.

    # DB 접속 해제
    conn.close()

    # 조건절로 중복된 아이디 확인
    if result is None:
        # (1) DB에 존재하지 않는 경우(None)
        return True
    else:
        # (2) DB에 존재하는 경우
        return False

# 로그인 처리를 위해 회원 존재 여부를 확인
def check_login_user(user_id, user_pw):
    # 쿼리문 작성
    sql = '''
        select * from user_table
        where user_id = %s and user_pw = %s
    '''

    # DB 연결
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s값 설정
    data = (user_id, user_pw)

    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()

    # DB 연결 해제
    conn.close()
    return result
