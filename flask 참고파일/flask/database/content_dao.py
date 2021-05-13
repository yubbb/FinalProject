from database import connector

# 게시글 정보를 추가하는 함수
def insertContentData(content_subject, content_writer_idx,
                      content_text, content_file, content_board_idx) :

    # 이 함수에 넣는 값은 content_date가 없다(sysdate()로 바로 현재 날짜 및 시간을 저장할 것이기 때문)
    
    # 쿼리문 작성
    sql = '''
            insert into content_table
            (content_subject, content_date, content_writer_idx, 
            content_text, content_file, content_board_idx)
            values
            (%s, sysdate(), %s, %s, %s, %s)
          '''
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 지정될 값 설정
    ''' 
    # [많은 글을 저장해서 paging 실험하기 위한 코드]
    for idx in range(500):
    data = (content_subject + str(idx), content_writer_idx, content_text,
            content_file, content_board_idx)
    '''
    data = (content_subject, content_writer_idx, content_text,
            content_file, content_board_idx)
    # 쿼리 실행
    cursor.execute(sql, data)
    conn.commit()
    # 데이터 베이스 접속 종료
    conn.close()

# 모든 글 정보를 가져오는 함수 -> 특정 게시판의 모든 글 정보를 가져오는 함수
def selectContentDataAll(content_board_idx, page):
    # page 번호에 따른 시작위치 계산
    start = (page-1)*10

    # 쿼리문 작성
    # **limit 0,10 -> 0번 위치에서 10개씩 가져오기(시작위치부터 개수만큼의 row만 가져오는 키워드) => 페이징 구현에 사용
    sql = '''
        SELECT  a1.content_idx, a1.content_subject, 
                a2.user_name, a1.content_date
        FROM content_table a1, user_table a2
        WHERE a1.content_writer_idx = a2.user_idx 
            AND a1.content_board_idx=%s 
        ORDER BY a1.content_idx desc
        limit %s,10
        '''
    
    # DB 연동
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 들어갈 값 설정(없음 -> 게시판 번호 인덱스)
    data = (content_board_idx, start)

    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchall()

    # DB 연결 해제
    conn.close()
    return result

# 글 하나만 가져오는 함수
def selectContentDataOne(content_idx):
    # 쿼리문 작성
    sql = '''
        SELECT  a2.user_name, a1.content_date, 
		        a1.content_subject, a1.content_text, 
                a1.content_file, a1.content_writer_idx
        FROM content_table a1, user_table a2
        WHERE a1.content_writer_idx = a2.user_idx 
        AND a1.content_idx = %s;
    '''
    # DB 연동
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s 값
    data = (content_idx)

    # 쿼리문 실행
    cursor.execute( sql, data )
    result = cursor.fetchone()

    # DB 연결 해제
    conn.close()
    return result

# 게시글 정보를 수정하는 함수
def updateContentData(content_subject, content_text,
                        content_file, content_idx) : 
    # Q. 뭘 수정?! 
    # A. '첨부 이미지'와 '내용'만 수정!

    # 쿼리문 작성  
    sql = '''
        update content_table
            set content_subject = %s, content_text = %s
        where content_idx = %s

        '''
    # DB 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s 값 설정
    data  = (content_subject, content_text, content_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    
    # 첨부 파일이 존재한다면
    if content_file != None:
        sql2 = '''
                update content_table
                    set content_file = %s
                where content_idx = %s
        '''
        data2 = (content_file, content_idx)
        cursor.execute(sql2, data2)

    conn.commit()

    # 데이터 베이스 접속 종료
    conn.close()

# 글 하나를 삭제하는 함수
def deleteContentData(content_idx):
    # query
    sql = ''' 
            delete from content_table
            where content_idx = %s
    '''
    # connect DB 
    conn = connector.get_connection()
    cursor = conn.cursor()

    # assign %s values
    data = (content_idx)
    
    # execute query
    cursor.execute(sql, data)
    conn.commit()

    # disconnect DB 
    conn.close

# 방금 작성한 글의 번호(글 번호가 제일 큰 것)을 가져오기.
def getMaxContentIdx(content_board_idx):
    # 쿼리문
    sql = '''
            select max(content_idx) from content_table
            where content_board_idx = %s
        '''
    # DB 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s값 설정
    data = (content_board_idx)
    
    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()

    # DB 접속해제
    conn.close()

    return result['max(content_idx)']

# 전체 글의 개수를 가져오는 함수(board_main에서 '다음'버튼을 처리하기 위해)
def getContentCnt(content_board_idx): # 게시판 인덱스 번호를 받겠다.
    # 쿼리문 작성
    sql = '''
            select count(*) from content_table
            where content_board_idx = %s
    '''

    # DB 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s 값 설정
    data = (content_board_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone() # row 하나만 나오기 때문에 fetchone
     
    # DB 접속 해제
    conn.close()
    return result['count(*)']