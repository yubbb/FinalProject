# 데이터 베이스 생성
create database pusan_board_db
default character set utf8
collate utf8_unicode_ci;

# 데이터 베이스 사용 설정
use pusan_board_db;

# 회원정보 테이블 생성
create table user_table(
    user_idx int auto_increment,  -- 1부터 자동으로 1씩 증가
    user_name character(10) not null,
    user_id varchar(100) not null,
    user_pw varchar(100) not null,
    constraint user_pk primary key(user_idx), -- 제약조건에 이름 넣기(오류 확인할 때 어떤 제약조건에서 오류가 났는지 확인 위해)
    constraint user_unique unique(user_id)
);
 
# 게시판 테이블 생성
create table board_table(
    board_idx int auto_increment,
    board_name varchar(100) not null,
    constraint board_pk primary key(board_idx),
    constraint board_unique unique(board_name)
);

-- auto_increment는 시도하면 1씩 증가한다. 실패하든 성공하는 상관없다.
-- 이 값은 row를 구분하는 숫자이지 순서가 아님

# 게시글 테이블
create table content_table(
    content_idx int auto_increment, -- 얘는 자동으로 증가되기 때문에 DB에 직접 넣어줄 필요 없다.
    content_subject varchar(500) not null,
    content_date date not null,
    content_writer_idx int not null,
    content_text varchar(500) not null,
    content_file varchar(500), -- null 허용. 이미지 없으면 첨부 안 해도 된다. 
    content_board_idx int not null,
    -- Primary Key
    constraint content_pk primary key(content_idx),
    -- Foreign Key
    constraint content_fk1 foreign key(content_writer_idx)
    references user_table(user_idx),

    constraint content_fk2 foreign key(content_board_idx)
    references board_table(board_idx)

);

# 게시판 테이블 데이터
insert into board_table (board_name) values ('자유 게시판');
insert into board_table (board_name) values ('유머 게시판');
insert into board_table (board_name) values ('정치 게시판');
insert into board_table (board_name) values ('스포츠 게시판');

commit;