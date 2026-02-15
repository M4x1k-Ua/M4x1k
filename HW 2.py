import random

class Student:

    def __init__(self, full_name, year):
        self.name = full_name
        self.year = year
        self.skills = random.randint(1,5)
        self.money = random.randint(1, 5)

    def grow_up(self):
        self.year += 1

    def study(self):
        self.skills += 0.5

    def chill(self):
        self.skills -= 0.3
        self.money -= random.randint(100,500)

    def working(self):
       self.money += (300 + random.randint(50,200))
    def introduce(self):
        print(f'My name is {self.name}')
        print(f'I am {self.year} year old')
        print(f'My skills is {self.skills:.2f}')
        print(f'I have {self.money:.2f} MONEY')


nick_mark = Student('Nick Mark,', 17)

nick_mark.introduce()

for day in range(1,365):
    print(f'======= {day} =======')

    choice = random.randint(0,2)

    if choice == 0:
        nick_mark.chill()
        print('Chilling..😎😊💎')
    elif choice == 1:
        nick_mark.working()
        print('Working..🥲')
    else:
        nick_mark.study()
        print('Studying..📚😒')
    print()

nick_mark.grow_up()
nick_mark.introduce()