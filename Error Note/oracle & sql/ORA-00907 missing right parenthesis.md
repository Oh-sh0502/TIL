# ORA-00907: missing right parenthesis

### 발생 상황

다음의 코드를 입력하였을 때 에러가 발생

```SQL
CREATE TABLE girl_group ( 
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR2(32) NOT NULL,
    debut DATE NOT NULL,
    hit_song_id INT
);
```



---

### 에러 원인

쿼리문에서 **괄호나 콤마가 빠져서 나는 오류**이다. 즉, 쿼리문에 오타가 났을 때 나오는 오류 중 하나다.

---

### 해결

 위의 경우는 콤마가 문제가 아니라 **AUTO_INCREMENT**라는 옵션 때문이다. AUTO_INCREMENT는 **MySQL이나 MariaDB에서 쓰는 옵션**으로 **인덱스를 체크해 자동으로 올려주는 옵션**이다.



 https://futurists.tistory.com/17 사이트의 테이블을 옮겨쓰려다 발생한 이슈로, MySQL의 쿼리문을 Oracle에 그대로 복붙해서 발생한 해프닝이다. Oracle에는 시퀀스를 생성하여 A부터 B까지 X의 간격으로 인덱스를 설정해줄 수 있다. 수정한 코드는 다음과 같다.



```sql
CREATE TABLE GIRL_GROUP( 
    id INT PRIMARY KEY,
    name VARCHAR2(32) NOT NULL,
    debut DATE NOT NULL,
    hit_song_id INT
);
CREATE SEQUENCE girlgroup_seq START WITH 101 INCREMENT BY 1;
```

---

### Reference

- 시퀀스: https://luji.tistory.com/71