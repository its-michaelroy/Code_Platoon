import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Qu', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

list_of_rows = []
def letter_generator():
  random_number = random.randrange(0,25,1)
  random_letter = alphabet[random_number]
  return random_letter

class BoggleBoard:
  def __init__(self, one='_', two='_', three='_', four='_', five='', six=''):
    self.one = one
    self.two = two
    self.three = three
    self.four = four
    self.five = five
    self.six = six
    for  _ in range (4): #Toggle for number of columns
      print(f'{self.one}{self.two}{self.three}{self.four}{self.five}{self.six}')

  def shake(self):
    for  _ in range (4): #Toggle for number of columns
        random_letter = letter_generator()
        self.one = random_letter
        random_letter = letter_generator()
        self.two = random_letter
        random_letter = letter_generator()
        self.three = random_letter
        random_letter = letter_generator()
        self.four = random_letter

        print(f'{self.one}{self.two}{self.three}{self.four}')
        # random_row = [self.one, self.two, self.three, self.four]
        # list_of_rows.append(random_row)

  def board_generator_6x16(self):
    for  _ in range (16): #Toggle for number of columns
        random_letter = letter_generator()
        self.one = random_letter
        random_letter = letter_generator()
        self.two = random_letter
        random_letter = letter_generator()
        self.three = random_letter
        random_letter = letter_generator()
        self.four = random_letter
        random_letter = letter_generator()
        self.five = random_letter
        random_letter = letter_generator()
        self.six = random_letter

        print(f'{self.one}{self.two}{self.three}{self.four}{self.five}{self.six}')
        random_row = [self.one, self.two, self.three, self.four, self.five, self.six]
        list_of_rows.append(random_row)

#BEARS!!!!
def smart_board_4x4():
  def smart_board_generator():
    random_number = random.randrange(0,5,1)
    return random_number

  smart_four_by_four = []
  for x in range (16):
    random_number = smart_board_generator()
    random_letters = (list_of_rows[x][random_number])
    smart_four_by_four.append(random_letters)

  print(f'''
    {smart_four_by_four[0]} {smart_four_by_four[1]} {smart_four_by_four[2]} {smart_four_by_four[3]}
    {smart_four_by_four[4]} {smart_four_by_four[5]} {smart_four_by_four[6]} {smart_four_by_four[7]}
    {smart_four_by_four[8]} {smart_four_by_four[9]} {smart_four_by_four[10]} {smart_four_by_four[11]}
    {smart_four_by_four[12]} {smart_four_by_four[13]} {smart_four_by_four[14]} {smart_four_by_four[15]}''')

board = BoggleBoard()
board.shake()
board.board_generator_6x16()
smart_board_4x4()
