import random
# class Board:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

class User:
    def __init__(self, x=6, y=4, allow_dup='yes'): #allow dup
        self.x = x
        self.y = y
        self.allow_dup = allow_dup
        self.__my_sol = []

    # @property
    # def my_sol(self):
    #     return self._my_sol

    @property
    def x(self):
        """"getter x called"""
        return self._x

    @x.setter
    def x(self, x):
        """setter x called"""
        if isinstance(x, int):
            self._x = x
        else:
            print('Please enter valid value(int)')

    @property
    def y(self):
        """"getter y called"""
        return self._y

    @y.setter
    def y(self, y):
        """"setter y called"""
        if isinstance(y, int):
            self._y = y
        else:
            raise TypeError

    @property
    def allow_dup(self):
        """getter allow_dup called"""
        return self._allow_dup

    @allow_dup.setter
    def allow_dup(self, allow_dup):
        """"setter allow_dup called"""
        if isinstance(allow_dup, str) and allow_dup in ['yes','no']:
            self._allow_dup = allow_dup
        else:
            raise TypeError


    # x = property(get_x, set_x)
    # y = property(get_y, set_y)
    # allow_dup = property(get_allow_dup, set_allow_dup)



    # def allow_dup_on(self):
    #     self.sol()
    #
    # def allow_dup_off(self):
    #     pass

    def __check(self,guess):
        my_list = []
        for i in guess:
            # temp = []
            # temp.extend([i, int(guess[i])])
            my_list.append(i)
        # print('my_list',my_list)

        if my_list == self.__my_sol:
            return True
        # print(my_list)

    def __hint(self,guess):
        # self.check(guess)
        my_list = []
        for i in range(len(guess)):
            temp = []
            # temp.extend([i, int(guess[i])])
            my_list.append(str(guess[i]))
        # print('my_lisy',my_list)
        # print('my_sol', self.my_sol)
        # print(self.my_sol[0][1])
        #y =index 0 x =index1
        hint = ''
        # my_hint = []

        for i in range(len(self.__my_sol)):
            # print('i',i)
            # print(my_list[j],self.my_sol[i])
            # print(i,my_list[i:len(self.my_sol)],self.my_sol)
            # , self.my_sol[i:len(self.my_sol)]
            if self.__my_sol[i] == my_list[i]:
                hint += '*'
            elif my_list[i:len(self.__my_sol)][0] in self.__my_sol:
                hint += 'o'


        # for i in range(len(self.my_sol)):
        #     for j in range(len(my_list)):
        #         # print(i,j)
        #         # print(my_list[j],self.my_sol[i])
        #         if self.my_sol[i] == my_list[j] and i == j:
        #             hint += '*'
        #         elif self.my_sol[i] in my_list[j]:
        #             hint += 'o'

        print(hint)

    def __sol(self):
        # dup on
        if self.allow_dup == 'yes':
            for index in range(self.y):
                my_list = []
                color = random.randint(1, self.x)
                # my_list.append(color)
                # my_list.extend([index,color])
                self.__my_sol.append(str(color))
            print(self.__my_sol)
        else:
            print('no dup')
            temp = []
            for index in range(self.y):
                # my_list = []  # temp
                color = random.randint(1, self.x)
                # my_list.extend([index,color])
                temp.append(color)
            # print(temp)
        #     for i in range(len(temp)):
        #         # if temp[i] in self.my_sol:
        #         while temp[i] in self.my_sol:
        #             color = random.randint(1, self.x)
        #             temp[i] = color
        #             self.my_sol.append(temp[i])
        #
        #             # while z not in self.my_sol:
        #             #     z = random.randint(1, self.x)
        #             #     temp[i] = z
        #                 # if z not in self.my_sol:
        #                 #     self.my_sol.append(z)
        #                 #     break
        #         self.my_sol.append(temp[i])
        # print(self.my_sol)
        # print(self.my_sol)


            # print(self.my_sol)



    def set_up(self):
        print(f'Rn your x(colors) is {self.x} and y(positions) is {self.y}.')
        print(f'Allow duplicate setting is {self.allow_dup}.')
        print('+++++++++++')
    #
    #     pick = input('What do you want to change?(x/y/allow_dup): ')
    #     if pick not in ['x','y','allow_dup']:
    #         while True:
    #             print('Please enter valid choice ')
    #             pick = input('What do you want to change?(x/y/allow duplicate): ')
    #             if pick in ['x','y','allow_dup']:
    #                 break
    #     elif pick in ['x','y','allow_dup']:
    #         if pick == 'x':
    #             print('setting x')
    #             x = int(input('x = '))
    #             self.set_x(x)
    #             print('RN x status: ', self.x)
    #         elif pick == 'y':
    #             print('setting y')
    #             y = int(input('y = '))
    #             self.set_y(y)
    #             print('RN y status: ', self.y)
    #         elif pick == 'allow_dup':
    #             print('setting allow_dup')
    #             allow_dup = input('allow_dup = ')
    #             self.set_allow_dup(allow_dup)
    #             print('RN allow_dup status: ', self.allow_dup)
    #         #might have to fix setter later with value type


    def play(self):
        print('--Welcome to Play Mastermind--')
    #     rules = int(input('DO YOU KNOW HOW TO PLAY?????:0, Yes(1)/No(2) '))
    #     if rules == 2:
    #         print("""Simple, all you have to do is...
    #             """)
    #     pick = int(input('Do you want to set up your board?, Yes(1)/No(2) '))
    #     if pick == 1:
    #         self.set_up()
    #         check = int(input('Are you satisfied with your setup?, Yes(1)/No(2) '))
    #         while check != 1:
    #             self.set_up()
    #             check = int(input('Are you satisfied with your setup?, Yes(1)/No(2) '))
    #     print('+++++++++++')
    #     print('ok let\'s start!')
        print(f'Playing Mastermind with {self.x} colors and and {self.y} positions')
        self.__sol()
        count = 0
        # while guess != self.my_sol:
        while True:
            count+=1
            while True:
                guess = input('What is your guess?: ')
                if len(guess) == len(self.__my_sol):  # STOP ASKING
                    break
            print(f'Your guess is {guess}')
            if self.__check(guess): #T LEAVEEEEE

                print('*'*len(guess))
                print(f'You solved it after {count} rounds')
                break

            self.__hint(guess)


# my_game = Mastermind(6, 4)
# my_game.play()
# my_game.summarize()




        # generate sol










x = User()
# x.set_up()
x.play()
# user
# x = int(input('Enter color range from 1-8: '))
# y = int(input('Enter positions range from 1-8: '))
# game = Board(x,y)
# game setup
# game = User()
# game.play()


# print(f'Playing Mastermind with {game.x} and {game.y} positions')
# guess = int(input('What is your guess?: '))