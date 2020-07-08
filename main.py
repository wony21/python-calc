import os
import msvcrt
from Units.Marin import Marin

# 마린 2기 생성
marinA = Marin('marin-A')
marinB = Marin('marin-B')
print('마린을 생성 하였습니다.')

# 게임 시작
input_char = ''
while input_char != '4':
    os.system('cls')
    marinB.print_status()
    input_char = input('[0] 내정보 [1] 공격 [2] 스팀팩 [3] MP회복 [4] 종료 : ')
    if input_char == '0':
        marinA.print_status()
    elif input_char == '1':
        marinA.doAttack(marinB)
    elif input_char == '2':
        marinA.doSteampack()
        marinA.print_status()
    elif input_char == '3':
        marinA.recoveryMP()
    else:
        pass
    print('Press any key...', end='')
    msvcrt.getch()

