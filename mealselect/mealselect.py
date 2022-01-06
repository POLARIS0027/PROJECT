import random

def mealwirte(): #음식을 추가할떄 쓰는 함수 
    f = open("./매운음식.txt", 'a')
    mealname = input('음식이름 :') #밀네임 변수 입력받음 
    if mealname != "":
         print(str(mealname)+'을 추가합니다.') #안내물 출력
         f.write(mealname) #매운음식.txt 에 값 저장
         f.write('\n')
         f.close()
         print(str(mealname)+'을 추가했습니다.') #안내물 출력
    else :
        print('음식을 추가하지 않습니다') #안내물 출력
    

def mealread(): #음식 목록을 읽어올떄 쓰는 함수 
    f = open("./매운음식.txt", 'r') #매운음식.txt 읽기모드로 열기
    content= f.read().splitlines() #한줄씩 읽어와서 리스트로 만들기
    f.close() #파일 닫기
    print(content) # 결과 출력. content는 자체로 리스트임 
    numb = len(content)
    print(str(numb)+"개의 음식이 목록에 있습니다") #음식 갯수 알려줌 
 
def mealpick(): 
    howmany = input('몇개나 뽑을까?')
    f = open("./매운음식.txt", 'r') #매운음식.txt 읽기모드로 열기
    content= f.read().splitlines() #한줄씩 읽어와서 리스트로 만들기
    f.close() #파일 닫기
    sampleList = random.sample(content,int(howmany)) #리스트에서 랜덤으로 X개만큼 뽑음 
    print(sampleList) #결과값 출력

mealwirte()
mealread()
mealpick()


