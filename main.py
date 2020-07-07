import os
from Units.Marin import Marin


marinA = Marin('marin-A')
marinB = Marin('marin-B')
print('마린을 생성 하였습니다.')


input_char = ''
while input_char != '4':
    os.system('cls')
    marinB.print_status()
    input_char = input('[1] 공격 [2] 스팀팩 [3] MP회복 [4] 종료 : ')
    if input_char == '1':
        marinA.doAttack(marinB)
    elif input_char == '2':
        marinA.doSteampack()
    elif input_char == '3':
        marinA.recoveryMP()
    else:
        pass

