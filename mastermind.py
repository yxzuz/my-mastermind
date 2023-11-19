import random



class Mastermind:
    def __init__(self, x=6, y=4, allow_dup='yes'): #allow dup
        self.x = x
        self.y = y
        self.allow_dup = allow_dup
        self.__my_sol = []

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


    def __check(self,guess):
        my_list = []
        for i in guess:
            my_list.append(i)
        # print('my_list',my_list)
        print(my_list,self.__my_sol)
        if my_list == self.__my_sol:
            return True
        # print(my_list)

    def __hint(self, guess):
        # self.check(guess)
        my_list = []
        for i in range(len(guess)):
            my_list.append(str(guess[i]))

        hint = ''


        for i in range(len(self.__my_sol)):
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
            # print(self.__my_sol)
        else:
            # print('no dup')
            while True:
                if len(self.__my_sol) == self.y:
                    break
                color = random.randint(1, self.x)
                if color not in self.__my_sol:
                    self.__my_sol.append(str(color))



    def settings(self):
        print(f'Rn your x(colors) is {self.x} and y(positions) is {self.y}.')
        print(f'Allow duplicate setting is {self.allow_dup}.')
        print('+++++++++++')


    # def restart(self):
    #     user_input = int(input('Do you want to play again and restart? Yes(1) / No(2)) '))
    #


    def play(self):
        print('--Welcome to Play Mastermind--')
        print(f'Playing Mastermind with {self.x} colors and and {self.y} positions')
        self.__sol()
        print(self.__my_sol)

        count = 0
        guess = 0
        while True:
            count+=1
            while True:

                guess = input('What is your guess?: ')
                break
                if len(guess) == len(self.__my_sol):  # STOP ASKING
                    break

            print(f'Your guess is {guess}')
            self.__check(guess)
            if self.__check(guess): #T LEAVEEEEE

                print('*'*len(guess))
                print(f'You solved it after {count} rounds')
                break

            self.__hint(guess)


my_game = Mastermind()
my_game.settings()
my_game.allow_dup = 'no'
my_game.play()
# my_game.summarize()





# if __name__ == '__main__':
#     while True:
#         my_game = Mastermind()
#         my_game.play()
#
#         user_input = int(input('Do you want to play again and restart? Yes(1) / No(2)) '))
#         if user_input == 1:
#             my_game.play()
#         elif user_input == 2:
#             break












# game = Board(x,y)
# game setup
# game = User()
# game.play()


# print(f'Playing Mastermind with {game.x} and {game.y} positions')
# guess = int(input('What is your guess?: '))