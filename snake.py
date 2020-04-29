import random
import curses
import locale

locale.setlocale(locale.LC_ALL, '')

message1 = '       _(\_/)\n      ((((^.\ \n    ((((  (6 \ \n   ((((( .    \ \n (((((  / ._  ,`, \n((((   /    `-.- \n((((   / '
message2 = '               ,%%%, \n             ,%%%` % \n            ,%%`( `| \n           ,%%@ /\_/ \n ,%.-"""--%%% "@@__ \n %%/   ' \
    '          |__`\ \n.%`\     |   \   /  // \n,%` >   .`----\ |  [/ \n  < <<`       || \n    `\\\       || ' \
        '\n      )\\      )\ \n '

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = int(sw/4)
snk_y = int(sh/2)
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addstr(0, 0, message2)
w.addstr(int(sh/4) + 10, 0, message1)
w.addstr(int(food[0]), int(food[1]), '@')

key = curses.KEY_RIGHT
counter = 0

sent1 = list(' PONIES PONIES PONIES...')
sent2 = list(' saddle up partner')
sent3 = list(' all hat no cattle')
sent4 = list(' PONY UP BUCKAROO!!!')
sent5 = list('I LOVE YOU!!!!')
sent6 = list(' BUTTMOUSE BUTTMOUSE BUTTMOUSE')


my_dict = {'0': sent1, '1':sent2, '2': sent3, '3': \
           sent4, '4': sent5, '5': sent6}
dict_vals = 0
dict_keys = 0
reverse = False

while True:
    
    if dict_vals < len(my_dict[str(dict_keys)]) - 1:
        dict_vals += 1
    else:
        dict_vals = 0

    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]


    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        reverse = True
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        reverse = False
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        if dict_keys < len(my_dict.keys()) - 1:
            dict_keys += 1
        else:
            dict_keys = 0

        dict_vals = 0
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(int(sw/4) + 3, sw-1)
            ]
            food = nf if nf not in snake else None
#        w.addch(food[0], food[1], curses.ACS_DIAMOND)
        w.addstr(int(food[0]), int(food[1]), '@')
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    if reverse:
        my_dict = {'0': sent1[::-1], '1':sent2[::-1], '2': sent3[::-1], '3': sent4[::-1], '4': sent5[::-1]}
        w.addch(int(snake[0][0]), int(snake[0][1]), my_dict[str(dict_keys)][dict_vals])
    else:
        my_dict = {'0': sent1, '1':sent2, '2': sent3, '3': sent4, '4': sent5}
        w.addch(int(snake[0][0]), int(snake[0][1]), my_dict[str(dict_keys)][dict_vals])
