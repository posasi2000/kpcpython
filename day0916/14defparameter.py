#  함수생성 매개인자있음, 리턴값없음

def board_write(title, email, phone, cnt):
    print("board_write함수")
    print(f'{title} 메일={email} 핸폰={phone} 조회수={cnt} ')
    print()


def board_update(user, num) :
    print("board_update함수")
    print(f'유저={user}')
    print(f'유저={num}')
    print()



board_write('고객게시판', 'master@est.com', '010-000-9999', 0)
user ='sky'
pwd = 9876

board_update(user,pwd)