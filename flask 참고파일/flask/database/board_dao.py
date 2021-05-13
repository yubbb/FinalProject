from database import connector

# 게시판 이름을 입력하는 함수(관리자용)
def insertBoardName(board_name):
    # 쿼리문 작성
    sql = '''
        insert into board_table
        (board_name)
        values(%s)
    ''' 
    # DB 연결
    conn = connector.get_connection()
    cursor = conn.cursor() 
    # cursor는 쿼리문을 실행할 수 있도록 만드는 것

    # %s에 들어갈 값 설정
    data = (board_name) # 데이터는 하나만 있더라도 튜플로 만들어주기

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # DB 연결 해제
    conn.close()

# 게시판 이름을 전부 가져오는 함수
def selectBoardNameAll():
    # 쿼리문 작성
    sql = '''
            select * from board_table
            order by board_idx
    '''
    # DB 연결
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 들어갈 값 설정(없음. 전부 불러옴)

    # 쿼리문 실행
    cursor.execute(sql)
    result = cursor.fetchall() # select해서 가져올 데이터가 1개 이상이면 fetchall
    # DB 연결 해제
    conn.close()

    return result

# 특정 게시판 이름을 가져오는 함수
def selectBoardNameOne(board_idx):
    # 쿼리문 
    sql = ''' 
            select * from board_table
            where board_idx = %s
    ''' 
    # DB 연결
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s값 설정
    data = (board_idx) # 값이 하나여도 튜플로 생성하기

    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()

    # DB 연결 해제
    conn.close()
    return result
    
# 게시판 정보를 수정하는 함수
def updateBoardData(board_name, board_idx):
    # 쿼리문 작성
    sql = '''
        update board_table
        set board_name = %s
        where board_idx = %s
    
        '''
    # DB 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 지정될 값 설정
    data = (board_name, board_idx)

    # 쿼리문 실행
    cursor.execute(sql,data)
    conn.commit()

    # 데이터 베이스 접속 해제
    conn.close()

# 게시판 정보를 삭제하는 함수
def deleteBoardData(board_idx):
    # 쿼리문 작성
    sql = '''
            delete from board_table
            where board_idx = %s
    '''
    # DB 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 지정될 값 설정
    data = (board_idx)

    # 쿼리 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터 베이스 접속 해제
    conn.close()