import re

def hangman(answer, letters=None, count=0):
    if letters == None:
        letters = []
        print('먼저 글자의 개수를 알려주지.\n' + len(answer) * '*')
    return hangman_input(answer, letters, count)

def hangman_input(answer, letters, count):
    while True:
        try:
            input_str = input('소문자로 알파벳 하나만 말하여라: ')
            assert len(input_str) == 1
            if not re.match('^[a-z]*$', input_str):
                raise ValueError
            break
        except ValueError:
            print("알파벳 소문자를 모르나?")
        except AssertionError:
            print("하나만이다, 하나만. 제대로 말해.")
                    
    if input_str in letters:
        print('방금 전에 같은 알파벳을 말하였다.')
        return hangman_input(answer, letters, count)
    
    letters.append(input_str)
    return status(answer, letters, count)

def is_answer(answer, letters, count):
    count += 1
    if set(answer) == set(letters):
        print(f'{count}번만에 맞추었군.')
    elif count == 9:
        print('"틀렸어"\n당신의 목에 서늘한 칼이 스며듭니다.')
    else:
        print(f'이제 기회는 {9 - count}번 남았어.')
        return hangman(answer, letters, count)
    
def status(answer, letters, count):
    show_answer = answer
    for letter in show_answer:
        if letter not in letters:
            show_answer = show_answer.replace(letter, '*')
    print(show_answer)
    return is_answer(answer, letters, count)

hangman('apple')