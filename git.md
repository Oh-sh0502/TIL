# Git == DVCS

> Git은 분산버전관리시스템(DVCS: Distributed Version Control Systems) 중 하나이다.



## 1. Git 사전 준비

> git을 사용하기 전에 커밋을 남기는 사람에 대한 정보를 설정(최초)

```bash
$ git config --global user.name 'edutak'
$ git config --global user.email '{email}'
```

* 추후에 commit을 하면, 작성한 사람(author)로 저장된다.

* email 정보는 github에 등록된 이메일로 설정을 하는 것을 추천(잔디밭)

* 설정 내용을 확인하기 위해서는 아래의 명령어를 입력한다.

  ```bash
  $ git config --global -l
  ```

> git bash 설치 [링크](https://gitforwindows.org/ )



## 2. 기초 흐름

> 작업 -> add -> commit

### 2-1. 저장소 설정

```bash
$ git init
```

* git 저장소를 만들게 되면 해당 디렉토리 내에 `.git/` 폴더가 생성
* git bash에서는 `(master)` 로 현재 작업중인 브랜치가 표기 된다.

### 2-2. `add`

> 커밋을 위한 파일 목록 (staging area)에 Tracking

```bash
$ git add .          # 현재 디렉토리의 모든 파일 및 폴더
$ git add a.txt      # 특정 파일
$ git add md-images/ # 특정 폴더
```

### 2-3. `commit`

> 버전을 기록(스냅샷)

```bash
$ git commit -m '커밋메시지'
```

* 커밋 메시지는 현재 버전을 알 수 있도록 명확하게 작성한다.

* 커밋 이력을 남기기 확인하기 위해서는 아래의 명령어를 입력한다.

* -m은 명령어의 그다음 부분을 메시지로 읽어야 한다는 것을 말한다.

  ```bash
  $ git log
  $ git log -1  # 최근 한개의 버전
  $ git log --oneline # 한줄로 간단하게 표현
  $ git log -1 --oneline
  ```

### 2-4. remote

```bash
$ git remote add origin repository address
```

### 2-5. push

> 커밋한 버전들을 깃으로 보낸다

```bash
$ git push origin master
```

### ※ pull

>push 이 전에는 pull 있다. 깃에서 지정한 repository를 끌어온다.

```bash
$ git pull origin master
```





## 상태 확인

> 현재 git과의 상태, git에 대한 모든 정보는 status에서 확인할 수 있다.

```bash
$ git status
```

