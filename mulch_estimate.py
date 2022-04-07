import os
from time import sleep

# ------- Global Variables-------
color_choice = ''
red_bag_cost = 2.99  # .00086516 per inch
black_bag_cost = 3.79  # .0010966 per inch
bag_cost = 0
bag_cost_per_inch = 0
num_bags = 0


# ------- Classes -------

class MulchCalculator:
    def __init__(self, length, width, height, price_by_inch):
        self.length = length
        self.width = width
        self.height = height
        self.price_by_inch = price_by_inch

    def get_cubic_area(self):
        return self.length * self.width * self.height

    # this helps them to easily measure their space in inches and convert to
    # cubic feet
    def cubic_inches_to_cubic_feet(self):
        return self.length * self.width * self.height / 1728

    def calculate_cost(self):
        area = self.get_cubic_area()
        area_to_float = float(area)
        return area_to_float * self.price_by_inch + bag_cost

# ------- Functions -------


def color_chosen():
    global color_choice
    global bag_cost
    if color_mulch_formatted == 'red':
        color_choice = 'red'
        bag_cost = red_bag_cost
    elif color_mulch_formatted == 'black':
        color_choice = 'black'
        bag_cost = black_bag_cost


def cost_per_inch():
    global bag_cost_per_inch
    if color_choice == 'red':
        bag_cost_per_inch = bag_cost / 3456
    elif color_choice == 'black':
        bag_cost_per_inch = bag_cost / 3456


def format_number_to_2_dec(number):
    return '{:.2f}'.format(number)


def inches_to_cubic_feet(number):
    # # there are 1728 inches in a cubic foot
    # number = cubic_footage / 1728
    pass


print('Home Teapot Mulch Project Calculator (c)')
print('Version .5 Alpha')
print('Running on Python 3.9 Conda')
print('Built by William Bourque')
print('For Home Teapot Corporation\n')  # Welcome Splash

print('Welcome to the Kent Mulch Project Estimator')
print('This handy app will help you come up with the '
      'approximate cost to mulch your intended area.')
#  wait 4 seconds to clear screen
sleep(4)

#  clear screen
os.system('cls')

print('To get us started, what is your name?')
user = input()
user_format = user.capitalize()
print(f'Thank you so much {user_format}!\n')

print(f'Ok {user_format} , let\'s start figuring out how much area '
      'we are trying to cover in mulch.\n')
print('How long is the area in inches that you are trying to cover?')
len_of_area = int(input())
print(f'Great! You said the area you are trying to cover is {len_of_area} '
      f'inches long\n')

print('Now, let\'s get the width of that spot.')
print('How many inches wide is that area?')
width_of_area = int(input())
print(f'Nice! So that spot will be {width_of_area} '
      f'inches wide.\n')

print('And now let\'s figure out how deep you would like the mulch to be.')
print('Approximately how thick would you like your mulch bed to be?')
how_deep = int(input())
print(f'Perfect! You would like the mulch bed to be about {how_deep} inches '
      f'thick.\n')

print(f'So let\'s review the dimensions of the project so we can figure out '
      f'roughly how much it is going to cost you.')
print(f'I have that the mulched area will be:\n'
      f'{len_of_area} inches long,\n'
      f'{width_of_area} inches wide,\n'
      f'and {how_deep} inches thick with mulch.\n')

print('Let\'s first start by deciding which color mulch you would like to use.')
print('Currently, red mulch is $2.99 per 2 cubic foot bag and black mulch is '
      'currently $3.79 per 2 cubic foot bag.')

print('Which color would you like to use? Please type red or black:')
color_mulch = input()
color_mulch_formatted = color_mulch.lower()
color_chosen()
cost_per_inch()

print(f'\nPerfect. So the price of {color_choice} mulch is '
      f'${bag_cost} per bag right now. ')
print('Now let\'s start bringing it all together for a total.\n')

# call the class and use the variables you assigned for user input
est_proj_inputs = MulchCalculator(len_of_area, width_of_area, how_deep,
                                  bag_cost_per_inch)
# this will take those values and use calculate function in MulchCalculator
# it will also call internally a function within the class
project_calc = est_proj_inputs.calculate_cost()
# pretty obvious but changes to 2 decimal places for price
project_calc_2_dec = format_number_to_2_dec(project_calc)

# est_proj_inputs is not assigned MulchCalculator and we can use functions
# from it
cubic_footage = est_proj_inputs.cubic_inches_to_cubic_feet()
cubic_converted_to_int = int(float(cubic_footage))

print(f'The estimated mulch needed for this project would be '
      f'{cubic_converted_to_int} cubic feet.\n'
      f'And bags of mulch come 2 cubic feet per bag.')
print(f'We typically recommend getting at least one additional bag though.\n'
      f'We\'ve added that into the estimate to assist you.\n')

print(f'Given all of this information, your estimate is that it would cost:\n'
      f'${project_calc_2_dec} excluding any applicable sales tax.\n'
      f'And you would need a total of {cubic_converted_to_int + 1} to cover '
      f'your area.\n'
      f'This would be the minimum though and you may want to add at least '
      f'one more.\n'
      f'(Trust me, you\'ll thank me afterwards... Lol) ')