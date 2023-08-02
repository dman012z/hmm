import random


# starting conditions
chips = int(input('how many chips to start? '))
c_chips = chips
sb = int(input('what is the small blind? '))
hand_counter = 0

# the game
while True:

    deck = ['Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h',
        'As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s',
        'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c',
        'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d']

    print('your stack is: ', chips)
    print('computer stack is: ', c_chips)
    print('blinds are: ', sb, '/', 2 * sb)
    yc = deck.pop(random.randrange(len(deck)))
    yc1 = deck.pop(random.randrange(len(deck)))
    yct = [yc, yc1]
    print('your preflop cards: ', [yc, yc1])
    cc = deck.pop(random.randrange(len(deck)))
    cc1 = deck.pop(random.randrange(len(deck)))
    cct = [cc, cc1]
    pot = 0

    while True:
            hand_counter += 1
            while True:
                chips -= sb
                preflop = input('do you raise, fold or limp: (r/f/l) ')
                if preflop == 'r':
                    p_raise = int(input('what is your bet?'))
                    chips -= (p_raise - sb)
                    pot += p_raise
                    break
                elif preflop == 'l':
                    chips -= sb
                    pot += sb * 4
                    break
                elif preflop == 'f':
                    print('you fold')
                    break
                else:
                    pass

            while True:
                c_chips -= 2 * sb
                c_move = ''
                num1 = random.randint(1, 3)
                if (cc[0] == cc1[0] and num1 == 3) or (cc[0] in ['K', 'Q'] or cc1[0] in ['A', 'K', 'Q']):
                    c_move = 'call'
                    p_call = p_raise
                    c_chips -= (p_call - sb * 2)
                    pot += p_call
                    print('pot is', pot)
                    break
                elif (cc[0] == cc1[0] and num1 < 3) or (cc[0] == 'A'):
                    c_move = 'raise'
                    c_p_raise = 3 * p_raise
                    c_chips -= (c_p_raise - sb * 2)
                    pot += c_p_raise
                    print('raise to: ', c_p_raise)
                    print('pot is', pot)
                    break
                elif preflop == 'l':
                    c_move = 'call'
                    print('pot is', pot)
                    break
                elif preflop == 'f':
                    c_chips += 3 * sb
                    break
                else:
                    c_move = 'fold'
                    chips += pot + 2 * sb
                    print('computers folds', ', computer had: ', cct)
                    break

            if c_move == 'raise':
                reaction1 = input('raise, call or fold? (r/c/f)')
                print('raise by', c_p_raise - p_raise)
                if reaction1 == 'r':
                    pfrr = int(input('what is your re-raise?'))    # ie how many extra chips in pot
                    chips -= pfrr
                    pot += (c_p_raise + pfrr)
                    print('pot is', pot)
                    pass
                elif reaction1 == 'c':
                    chips -= c_p_raise
                    pot += c_p_raise
                    print('pot is', pot)
                elif reaction1 == 'f':
                    preflop = 'f'
                    break

            if preflop == 'f' or c_move == 'fold':
                break
            else:
                pass

            flop = [deck.pop(random.randrange(len(deck))), deck.pop(random.randrange(len(deck))),
                    deck.pop(random.randrange(len(deck)))]
            print('flop is', flop)

            postflop = input('check or bet: (c/b)')
            if postflop == 'c':
                print('pot is', pot)
                pass
            elif postflop == 'b':
                po_raise = int(input('what is your bet?'))
                chips -= po_raise
                c_chips -= po_raise
                pot += 2 * po_raise
                print('pot is', pot)
                pass
            print('your stack is: ', chips)

            turn = [deck.pop(random.randrange(len(deck)))]
            print('turn is', turn)

            post_turn = input('check or bet: (c/b)')
            if post_turn == 'c':
                print('pot is', pot)
                pass
            elif post_turn == 'b':
                po_raise = int(input('what is your bet?'))
                chips -= po_raise
                c_chips -= po_raise
                pot += 2 * po_raise
                print('pot is', pot)
                pass
            print('your stack is: ', chips)

            river = [deck.pop(random.randrange(len(deck)))]
            print('river is', river)

            post_river = input('check or bet: (c/b)')
            if post_river == 'c':
                print('pot is', pot)
                pass
            elif post_river == 'b':
                po_raise = int(input('what is your bet?'))
                chips -= po_raise
                c_chips -= po_raise
                pot += 2 * po_raise
                print('pot is', pot)
                pass

            print('computers hand is:', cct)
            print('your hand is: ', yct)
            print('board: ', flop, turn, river)
            winner = input('did you win, lose or tie? (w/l/t)')
            if winner == 'w':
                chips += pot
            elif winner == 'l':
                c_chips += pot
            elif winner == 't':
                chips += int(0.5 * pot)
                c_chips += int(0.5 * pot)
            else:
                pass
            print('your stack is: ', chips)
            print('computer stack is: ', c_chips)
            pot = 0
            break

    var1 = input('play another hand? type no to cancel or press any key to continue \n').lower()
    if var1 == 'no':
        break
    else:
            pass


print('your final stack:', chips)
print('hands played:', hand_counter)