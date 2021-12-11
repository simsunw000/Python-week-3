#리스트레서 사용되는 문법, 연산

#(1) 리스트 복사

List = [1,2,3,4,5]
List2 = List
print(List2)

#(2) 리스트 연산
# 파이썬에서 리스트끼리의 연산( 더하기, 곱하기)가 가능.

print(List + List2)

print(List*3)

# print(List*2 - List) : 리스트 끼리의 빼기는 불가능 에러 발생

#(3) 리스트 컴프리헨션(List comprehension)
#[] 내부에 for문 if문을 사용해 만족되는 조건으로 리스트 생성 가능
# 사용 이유 : 직관적이고 간결한 표현

'''
작성 순서
리스트명 = [ 변수 for문 if 문]
'''
List = [x for x in range(1,11) if x%2 == 0]
print('1부터 10까지 중 짝수인 값에 대한 리스트' , List)

# (2) if문이 왼쪽에 있는 경우 (else 사용)
List = [x if x %2 == 0 else '홀수' for x in range(1,11)]
# x는 짝수일 조건 , 그게 아니면 홀수, 어디서? for문 범위에서(1~10 사이)
print('1부터 10까지 중 짝수인 값 출력, 아니면 "홀수" 출력', List)
