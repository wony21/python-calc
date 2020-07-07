class Unit:
    name = 'Unit'
    max_hp = 100
    max_mp = 100
    hp = 100
    mp = 100
    attack = 10
    defence = 0

    def __init__(self, name, hp, mp, attack, defence):
        # print('__init__')
        self.name = name
        self.max_hp = hp
        self.max_mp = mp
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defence = defence
        
    def attacked(self, damage):
        real_damage = damage - self.defence
        if real_damage < 0 :
            real_damage = 0
        self.hp = self.hp - real_damage
        if self.hp <= 0:
            self.hp = 0
            print(self.name, ' 죽음.')
    
    def recoveryMP(self):
        self.mp = self.mp + 5
        if self.mp >= self.max_mp:
            self.mp = self.max_mp
    
    def print_status(self):
        print('Status :', self.name)
        if self.hp > 0:
            print('HP :', self.hp)
            print('MP :', self.mp)
            print('ATT :', self.attack)
            print('DEF :', self.defence)
        else:
            print('HP가 모두 소모되어 죽었습니다.')
