import os
from random import choice, seed
from time import sleep
seed(10)

rules = {
    'e': 'пустота',
    's': 'креветка',
    'f': 'рыба',
    'm': 'скала'
}



class ocean:
    def __init__(self, size=10, fish_frec=0.25, shrim_frec=0.25, mount_frec=0.25, emp_frec=0.25):
        self.m = [[0 for _ in range(size + 3)]for _ in range(size + 3)]
        self.m = [[Emptyness([i, j], self.m) for i in range(size + 3)] for j in range(size + 3)]
        list_to_distr = [('f ' * int((fish_frec * (size**2)))).split(), ('s ' * int((shrim_frec * (size**2)))).split(), ('m ' * int((mount_frec * (size**2)))).split(),
                                ('e ' * int( (size**2) * emp_frec)).split()]
        gen_list = []
        for i in list_to_distr:
            for j in i:
                gen_list.append(j)
        for i in enumerate(self.m[2:-1]):
            for j in enumerate(self.m[2:-1][2:-1]):
                a = choice(gen_list)
                if a == 'e':
                    self.m[i[0]+2][j[0]+2] = Emptyness([i[0]+2, j[0]+2], self.m)
                elif a == 's':
                    self.m[i[0]+2][j[0]+2] = Shrim([i[0]+2, j[0]+2], self.m)
                elif a == 'f':
                    self.m[i[0]+2][j[0]+2] = Fish([i[0]+2, j[0]+2], self.m)
                else:
                    self.m[i[0]+2][j[0]+2] = Mount([i[0]+2, j[0]+2], self.m)
        
    def __str__(self):
        string = ''
        for i in self.m[2:-1]:
            for j in i[2:-1]:
                string += str(j) + ' '
            string += '\n'
        return string
    def clean(self):
        os.system('cls') if os.name == 'nt' else os.system('clear')

    def step(self):
        for i in self.m[2: -1]:
            for j in i[2: -1]:
                try:
                    j.parse_ocean()
                except:
                    pass

class obj:
    def __init__(self, status, ocean_pos, ocean):
        self.status = status
        self.ocean_pos = ocean_pos
        self.ocean = ocean

        self.ocean[ocean_pos[0]][ocean_pos[1]] = self.status
    def __str__(self):
        return self.status


        ocean[ocean_pos[0]][ocean_pos[1]] = self.status
    def parse_ocean(self):
        list_of_sames = []
        c_pos = [self.ocean_pos[0] - 1, self.ocean_pos[1] - 1]
        #print(self.status, '-')
        for i in range(3):
                for j in range(3):
                    #print(self.ocean[c_pos[0] + i][c_pos[1] + j], end=' ')
                    if str(self.ocean[c_pos[0] + i][c_pos[1] + j]) == self.status:
                        list_of_sames.append(1)
                #print()
        #print(len(list_of_sames))
        #print()

        if len(list_of_sames) > 4 or len(list_of_sames) <= 2:
            self.ocean[self.ocean_pos[0]][self.ocean_pos[1]] = Emptyness([self.ocean_pos[0], self.ocean_pos[1]], self.ocean)
            del self
        



class Emptyness(obj):
    def __init__(self, ocean_pos, ocean):
        super().__init__('e', ocean_pos, ocean)
    def parse_ocean(self):
        list_of_fishes, list_of_shrims = [], []
        c_pos = [self.ocean_pos[0] - 1, self.ocean_pos[1] - 1]
        for i in range(3):
            for j in range(3):
                if self.ocean[c_pos[0] + i][c_pos[1] + j] == 'f':
                    list_of_fishes.append(1)
                elif self.ocean[c_pos[0] + i][c_pos[1] + j] == 's':
                    list_of_shrims.append(1)
        if len(list_of_shrims) >= 3:
            self.ocean[self.ocean_pos[0]][self.ocean_pos[1]] = Shrim(self.ocean_pos, self.ocean)
        elif len(list_of_fishes) >= 3:
            self.ocean[self.ocean_pos[0]][self.ocean_pos[1]] = Fish(self.ocean_pos, self.ocean)
            
class Shrim(obj):
    def __init__(self,ocean_pos, ocean):
        super().__init__('s', ocean_pos, ocean)


class Fish(obj):
    def __init__(self, ocean_pos, ocean):
        super().__init__('f', ocean_pos, ocean)
class Mount(obj):
    def __init__(self, ocean_pos, ocean):
        super().__init__('m', ocean_pos, ocean)
    def parse_ocean(self): pass

Ocean = ocean(size=10, fish_frec=0.3, shrim_frec=0.3)
while True:
    Ocean.clean()
    for key, value in rules.items():
        print(key, '-', value)
    print(Ocean)
    Ocean.step()
    sleep(1)

