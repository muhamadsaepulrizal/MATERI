#access modifier

# __ -> priver access modifier
# _ -> protected
# __dict__ buat kita tahu isi apa dalam bentuk dictionary

# 1 usage
class Player:
    #konstraktor 
    def __init__(self,name, health = 100, energy = 100): #nilai default health 100
        self.name = name
        self.health = health
        self.energy = energy

    # 1 usage    
    def attact(self, target, damage = 1 ): #penyerangan terhadap target(mosnter) dgn damage 1
        self.energy -= damage # self.energy = self.energy - damage
        target.health -= damage #targetnya damage darah monster
        print(f"{self.name} attack {damage} damage to {target.name}")
        if target.is_attacked(player_name=self.name):
            self.health -= target.damage

    def show_info(self):
        print(f"{self.name} health: {self.health}")
        print(f"{self.name} energy: {self.energy}")


class Monster:
    def __init__(self,name, health=100):
        self.name = name
        self.health = health #dinamis (berubah ubah)
        self.health_init = self.health #menampung nilai healtnya 500
        self.damage = 10

    

    def is_attacked(self, player_name):
        print(f"{self.name} attack {self.damage} damage to {player_name}")     
        return self.health < self.health_init
    
    def show_info(self):
        print(f"{self.name} health: {self.health}")


player1 = Player(name="balmond")
player2 = Player(name="chou")
iblis = Monster(name="lucifer",health=500) #health monster diubah jadi 500 dari 100
animal = Monster(name="tiger" )

player1.attact(target=iblis, damage=80)
player2.attact(target=animal, damage=20)

# lucifer.attact()

player1.show_info()
player2.show_info()
iblis.show_info()
animal.show_info()




