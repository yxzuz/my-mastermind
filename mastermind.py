import random



class User:
    def __init__(self, x=6, y=4, allow_dup='no'):
        self._x = x
        self._y = y
        self._allow_dup = allow_dup

    def get_x(self):
        """"getter x called"""
        return self._x

    def set_x(self, x):
        """setter x called"""
        if isinstance(x, int):
            self._x = x
        else:
            print('Please enter valid value(int)')

    def get_y(self):
        """"getter y called"""
        return self._y

    def set_y(self, y):
        """"setter y called"""
        if isinstance(y, int):
            self._y = y
        else:
            raise TypeError

    def get_allow_dup(self):
        """getter allow_dup called"""
        return self._allow_dup

    def set_allow_dup(self, allow_dup):
        """"setter allow_dup called"""
        if isinstance(allow_dup, str) and allow_dup in ['yes','no']:
            self._allow_dup = allow_dup
        else:
            raise TypeError
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    allow_dup = property(get_allow_dup,set_allow_dup)

    def set_up(self):
        print(f'Rn your x(colors) is {self.x} and y(positions) is {self.y}.')
        print(f'Allow duplicate setting is {self.allow_dup}.')
        print('+++++++++++')

        pick = input('What do you want to change?(x/y/allow_dup): ')
        if pick not in ['x','y','allow_dup']:
            while True:
                print('Please enter valid choice ')
                pick = input('What do you want to change?(x/y/allow duplicate): ')
                if pick in ['x','y','allow_dup']:
                    break
        elif pick in ['x','y','allow_dup']:
            if pick == 'x':
                print('setting x')
                x = int(input('x = '))
                self.set_x(x)
                print('RN x status: ', self.x)
            elif pick == 'y':
                print('setting y')
                y = int(input('y = '))
                self.set_y(y)
                print('RN y status: ', self.y)
            elif pick == 'allow_dup':
                print('setting allow_dup')
                allow_dup = input('allow_dup = ')
                self.set_allow_dup(allow_dup)
                print('RN allow_dup status: ', self.allow_dup)
            #might have to fix setter later with value type

    def play(self):
        print('--Welcome to Play Mastermind--')
        rules = int(input('DO YOU KNOW HOW TO PLAY?????:0, Yes(1)/No(2) '))
        if rules == 2:
            print("""Simple, all you have to do is...
                """)
        while True:
            pick = int(input('Do you want to set up your board?, Yes(1)/No(2) '))
            if pick == 1:
                self.set_up()
                check = int(input('Are you satisfied with your setup?, Yes(1)/No(2) '))
                while True:
                    self.set_up()
                    if check == 2:
                        break
            else:
                break
        print('ok let\'s start!')
        print(f'Playing Mastermind with {self.x} colors and and {self.y} positions')
        guess = input('What is your guess?: ')
        Board(self).sol()

    def reset(self):
        pass


class Board(User):
    def __init__(self, x, y, allow_dup):
        super().__init__(x, y, allow_dup)
        self.my_sol = []

    def allow_dup_on(self):
        pass

    def allow_dup_off(self):
        pass

    def check(self):
        pass

    def hint(self):
        pass

    def sol(self):
        # dup on
        for index in range(self.y):
            color = random.randint(1, self.x)
            self.my_sol.extend([index,color])
        print(self.my_sol)







# user
# x = int(input('Enter color range from 1-8: '))
# y = int(input('Enter positions range from 1-8: '))
# game = Board(x,y)
# game setup
game = User()
game.play()
h = Board()
