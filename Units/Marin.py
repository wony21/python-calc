from Units.Unit import Unit

class Marin(Unit):
    attack = 5
    steampack_mp = 10
    steampack = False

    def __init__(self, name):
        # print('margin : __init__ ')
        super().__init__(name, 150, 80, 5, 1)
        
    def doSteampack(self):
        if int(self.mp) >= int(self.steampack_mp):
            self.mp = self.mp - self.steampack_mp
            self.hp = round(float(self.hp) - (float(self.hp) * 0.1))
            self.steampack = True
            print('스팀팩을 사용 하였습니다. MP:{}/{}'.format(self.mp, self.max_mp))
        else:
            self.steampack = False
            print('MP가 부족 합니다.')
    
    def doAttack(self, unit):
        damege = self.steampack and self.attack * 2 or self.attack
        unit.attacked(damege)
        self.steampack = False
    
    def print_status(self):
        print('Status :', self.name)
        if self.hp > 0:
            print('HP : {}/{}'.format(self.hp, self.max_hp))
            print('MP : {}/{}'.format(self.mp, self.max_mp))
            print('ATT :{}'.format(self.steampack and self.attack * 2 or self.attack))
            print('DEF :{}'.format(self.defence))
        else:
            print('HP가 모두 소모되어 죽었습니다.')
    

