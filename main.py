import sys
import calculator as calc

# 사용자 값 입력 
a = input('첫 번째 값을 입력 하세요 :')
b = input('두 번째 값을 입력 하세요:')
oper = input('연산자를 입력 하세요:')
# a, oper, b = input(' 계산식 입력 :').split()

# 숫자형인지 판단, 숫자형이 아닌 경우 종료
if not a.isdecimal() :
    print('첫 번째 값이 숫자가 아닙니다.', a)
    sys.exit(1)

if not b.isdecimal():
    print('두 번째 값이 숫자가 아닙니다.', b)
    sys.exit(1)

# 형 변환
a, b = float(a), float(b)

# 해당되는 연산자에 맞게 연산
if oper == '+':
    ret = calc.add(a, b)
elif oper == '-':
    ret = calc.sub(a, b)
elif oper == '*':
    ret = calc.mul(a, b)
elif oper == '/':
    ret = calc.div(a, b)
elif oper == '^':
    ret = calc.sqr(a, b)
else:
    print('잘못된 연산자를 입력 하였습니다.')
    sys.exit(1)

# 최종 결과 출력
print('결과 :', a, oper, b, '=', ret)

