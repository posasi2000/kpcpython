# 함수 매개인자 


def profile(name, age, *language):
    print(f'이름:{name} {age}세')
    for lang in language:
        print(lang, end = ' ')

    print()
    print()
    
profile("유재석", 30, "python",  "numpy", "pandas", "llm", "opencv2")   
profile("조세호", 34, "react",  "html")     
