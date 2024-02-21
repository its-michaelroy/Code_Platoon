def get_line(num):
    # kldjsfalkfdajalskdfjdfls
    output = f'{num} bottles of beer on the wall, {num} bottles of beer.\n' \
        f'Take one down and pass it around, {
            num-1} bottles of beer on the wall.'
    return output


def two_left():
    output = f'2 bottles of beer on the wall, 2 bottles of beer.\n' \
        f'Take one down and pass it around, 1 bottle of beer on the wall.'
    return output


def one_left():
    output = f'1 bottle of beer on the wall, 1 bottle of beer.\n' \
        f'Take one down and pass it around, no more bottles of beer on the wall.'
    return output


def last_line():
    output = 'No more bottles of beer on the wall, no more bottles of beer.'
    return output


def go_to_the_store(num):
    output = f'Go to the store and buy some more, {
        num} bottles of beer on the wall.'
    return output


def bottle_song(num):
    # write your code here!
    # for bottles_remaining in range(num, 2, -1):
    #     print(get_line(bottles_remaining))
    if num >= 3:
        print(get_line(num))
        bottle_song(num-1)
    else:
        print(two_left())
        print(one_left())
        print(last_line())
        print(go_to_the_store(num))


bottle_song(12)
