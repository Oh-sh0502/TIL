# Oracle 면접 스터디 2주차

## 강의순서

1. 면접 질문 소개
2. 각 면접 질문 영역 개념 설명
3. 면접질문 풀기



## 1. 면접 질문 소개

### 둘째마당_09: SQL문 속 또 다른 SQL문, 서브쿼리

1. **인라인뷰, 서브쿼리, 스칼라서브쿼리 이런게 뭔지 아시나요?**
2. **아신다면 각각의 차이점에 대해서 말씀해 주세요.**

### 둘째마당_10: 데이터를 추가, 수정, 삭제하는 데이터 조작어

1. **Insert문은 무엇입니까?**

2. **데이터베이스에서 레코드는 어떻게 삭제합니까?(DELETE문)**

3. **다음 테이블을 참고하여 질문에 해당하는 SQL문을 작성하라.**

   | 이름(name) | 학번(num) | 폰번호(pnum)  | 주소(address) | 이메일(email) | 성별(sex) |
   | ---------- | --------- | ------------- | ------------- | ------------- | --------- |
   | 홍길동     | 10        | 010-1111-1111 | 서울시        | hong@com      | 남        |
   | 민수       | 11        | 010-2222-2222 | 경기도        | m@com         | 남        |
   | 유관순     | 12        | 010-3333-3333 | 경상도        | yu@com        | 여        |

   

   **3-1. 테이블 생성 - 테이블 명은 'student'로 할 것**

   create table student ( name varchar(10) not null, num int not null, pnum int not null, address varchar(10) not null, email varchar(10) not null, sex varchar(2) not null, primary key(num) );

   **3-2. 테이블 수정 - 대학교(university)를 추가하고 null 값을 허용해라**

   ​	alter table student add university varchar(10) null;

   **3-3. 데이터 삽입 - 임의의 데이터 2개를 추가하라.**

   - - insert into student(name, num, pnum, address, email, sex) value('김사또', 11, 01022222222, '경기도', 'kim@com', '남');
     - insert into student(name, num, pnum, address, email, sex) value('강민수', 13, 01077777777, '서울', 'kang@com', '남');

   **3-4. 데이터 수정 - 홍길동의 핸드폰 번호를 010-5555-5555로 변경**

   ​	update student set pnum = 010-5555-5555 where name = '홍길동';

   **3-5. 데이터 검색**

   - - 전체 자료 조회 : select * from student;
     - 학번이 3번보다 이상인 사람들의 이름과 학번을 조회 : select name, num from student where = num >= 3 order by num desc;
     - 김자로 시작하는 학생의 이름을 조회 : select name from student where name like '김%';
     - ORDER BY xx DESC(내림차순)
     - ORDER BY xx ASC(오름차순)

   **3-6. 데이터 삭제**

   - - 모든 자료(행) : delete from student;
     - 특정 자료(행) : delete from student where name = '홍길동';

### 둘째마당_11

1. **DB Transaction(트랜잭션) 이란?**
- 데이터의 무결성으로 인하여 데이터 작업시에 문제가 생기면, 데이터 작업을 하기 이전 시점으로 모든 데이터를 원상 복구 하는 것을 말한다.
- 즉, 모두 실행되거나 모두 실행되지 않거나를 뜻한다.



### 둘째마당_12

1. **테이블을 드롭(DROP)하는 것과 자르는 것(Truncate), 그리고 테이블 내 모든 레코드를 삭제(Delete)하는 것의 차이점은 무엇입니까?**

### 둘째마당_13

1. DB에서 Index를 사용하는 이유는?

- 인덱스(Index)는 데이터를 논리적으로 정렬하여 검색과 정렬 작업의 속도를 높이기 위해 사용된다.
- 예를 들면, 책에서 가장 빨리 내용을 찾는 방법은 책의 뒤편의 색인을 보는 것.
- 기본키에 대해서는 항상 DBMS가 내부적으로 정렬된 목록을 관리하기에 특정 행을 가져올 때 빠르게 처리된다. 하지만, 다른 열의 내용을 검색하거나 정렬시에는 하나하나 대조를 해보기 때문에 시간이 오래걸린다. (이를 인덱스로 정의해두면 검색속도가 향상된다.)
- 단점: 인덱스를 사용하면 데이터를 가져오는 작업의 성능은 향상시킬 수 있지만 데이터 삽입, 변경 등이 일어날 때 매번 인덱스가 변경되기 때문에 성능이 떨어질 수 있다.
- 사용대상 : 데이터 필터링과 정렬에 사용되므로, 데이터를 특정한 순서로 자주 정렬한다면 인덱스를 사용하기에 적합

### 둘째마당_14

1. **기본키(Primary Key)와 유일키(Unique Key)의 차이점은 무엇입니까?**
2. 

### 둘째마당_19

1. **트리거란?**
2. 

