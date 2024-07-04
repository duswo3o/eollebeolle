# [완료] 비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
import hashlib

# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.nusername = username
        self.password = hashlib.sha256(b"password").hexdigest()  # [완료] b는 (normally bytes) using the
        # https://docs.python.org/ko/3/library/hashlib.html
    
    def display(self):
        print('이름 :',self.name) 
        print('아이디 :',self.nusername)

##### 예지님이 작성하신 코드입니다#####
class Post:  # 클래스 선언
    def __init__(self, title, content, username):  # 생성자 정의
        self.title = title  # author, content 등은 클래스의 속성
        self.content = content
        self.author = username

    def display_post(self): # 디스플레이
        print(f'제목 : {self.title}')
        print(f'닉네임 : {self.author}')
        print(f'글 내용 : {self.content}')
#####################################


# ----- 코드 실행 ------
members = []
posts = []

# [완료] 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요

members_1 = Member ('홍길동','hong','abc123')
members_2 = Member ('이순신','lee','abc123')
members_3 = Member ('박첨지','park','abc123')

members.append(members_1)
members.append(members_2)
members.append(members_3)

# Many_post = Post("Many's word", "냉정과 열정 사이", members_1)
# Tony_post = Post("Tony's word", "점프 투 파이썬", members_2)
# Kona_post = Post("Kona's word", "점심 메뉴를 고민중입니다", members_3)

# posts.append(Many_post)
# posts.append(Tony_post)
# posts.append(Kona_post)

# [완료] input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
name = input("이름: ")
username = input("아이디: ")
password = input("패스워드: ")
members.append(Member(name=name, username=username, password=password))

# [완료] members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
for Member in members:
    print(Member.name)

#코드 융합
for Member in members:
    # for Posts in posts:
        print(f"멤버: {Member.name}")

        # for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
        # print(f"제목: {Posts.title} 멤버: {Member.name}")

# for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요


# [완료] input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
# 2. post도 터미널에서 생성할 수 있게 해주세요.
# [완료] (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.


