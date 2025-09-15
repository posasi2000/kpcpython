# 함수 매개인자 

def dic_method(**p):
    #print('타입 ', type(p)) <class 'dict'>
    for i in p.keys():
        print(i,':', p[i])
    print()

dic_method(code=2025, title='kpc', flag=False)


def menu_method(menu):
    # print('타입 ', type(menu))  <class 'dict'>
    print(f"code: {menu['code']}")
    print(f"title: {menu['title']}")
    print(f"flag: {menu['flag']}")

menu = {
    'code' : 7700, 
    'title' : 'blue', 
    'flag' :False
}
menu_method( menu )  #  함수의 매개인자를 1개 전달