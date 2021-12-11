#(4) 리스트에서 사용 가능한 함수들

lst = ['물', '이온음료','탄삼음료']

print('리스트의 길이' , len(lst)) # 리스트 전체의 길이를 확인 가능


print(1 in lst) # 값 in 리스트명을 통해 해당 값이 리스트 안에 있는지 확인 가능
print(1 not in 1st) # 값 not in 리스트명을 통해 해당 값이 리스트 안에 없는지 확인 가능
lst.sort() #리스트 정렬 가능
print(' 리스트 정렬 ', lst)
lst.reverse() #요소의 순서를 뒤집음
print('역순 처리', lst)

drink = input(' 추가할 음료수의 종류를 작성해주세요.')
lst.append(drink) #리스트에 값을 추가합니다. 맨 마지막 값으로
print('추가 후 lst', lst)

#리스트 삽입
insert = int(input('추가할 위치에 값을 입력해주세요.'))
drink = input('추가할 음료수의 종류를 작성해주세요.')
lst.insert(insert, drink)
print(f'추가한 위치 = {insert}, 추가한 값 = {drink}')
print('현재 리스트 : ' , lst)

#리스트 제거
drink = input('제거할 음료수의 종류를 작성해주세요.')
lst.remove(drink)
print('제거 후 리스트', lst)
lst.pop() # pop안에 인덱스 값을 넣을 경우 해당 값이 삭제됩니다.
# pop 안에 값을 넣지 않을 경우 가장 마지막 요소 (인덱스 -1번)이 삭제됩니다.
print('pop!',lst)
lst.clear() # 리스트 안에 있는 모든 요소를 제거합니다. (빈 리스트로 만들어줌)
print('전체 제거 후 리스트', lst)
del lst # 리스트 자체를 삭제합니다
print('del 기능에 의해 리스트가 삭제되었습니다.')

'''
pop이란?
자료구조 스(stack)에서 사용하는 개념으로, 가장 위에 있는 데이터를 반환하고
삭제하는 기능

스택과 같이 가장 마지막에 입력한 값이 가장 먼저 빠져나가는 방식은
LIFO (Last in First Out) 후입반출이라 부른다.

'''










