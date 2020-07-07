from Units.Unit import Unit

class Marin(Unit):
    attack = 5
    steampack_mp = 10
    steampack = False

    def __init__(self, name):
        # print('margin : __init__ ')
        super().__init__(name, 150, 80, 5, 1)
        
    def doSteampack(self):
        if self.mp > self.steampack_mp:
            self.mp = self.mp - self.steampack_mp
            self.steampack = True
        else:
            self.steampack_mp = False
            print('MP가 부족 합니다.')
    
    def doAttack(self, unit):
        damege = self.steampack and self.attack * 2 or self.attack
        unit.attacked(damege)
        self.steampack = False
    

