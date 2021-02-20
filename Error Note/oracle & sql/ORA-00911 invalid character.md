# ORA-00911: invalid character

### 발생 상황

다음의 코드를 입력하였을 때 에러가 발생

```sql
CREATE TABLE girl_group ( 
    _id INT PRIMARY KEY,
    name VARCHAR2(32) NOT NULL,
    debut DATE NOT NULL,
    hit_song_id INT
);
```

---

### 에러 원인

잘못된 문자가 들어있다는 뜻. JAVA와 Oracle을 연동할 때 발생하기도 하는 이슈이다.

![image-20210220193646535](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210220193646535.png)

---

### 결과

**_id -> id **로 수정하였다.

```sql
CREATE TABLE girl_group ( 
    id INT PRIMARY KEY,
    name VARCHAR2(32) NOT NULL,
    debut DATE NOT NULL,
    hit_song_id INT
);
```

---

### Reference

- None