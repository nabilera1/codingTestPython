import random

행맨그림 = [

    '''
  +---+

  |   |

      |

      |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

      |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

  |   |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

 /|   |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

 /|\  |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

 /|\  |

 /    |

      |

=========''',

    '''
  +---+

  |   |

  O   |

 /|\  |

 / \  |

      |

=========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra \
cougar coyote crow deer dog donkey duck eagle ferret fox frog \
goat goose hawk lion lizard llama mole monkey moose mouse mule \
newt otter owl panda parrot pigeon python rabbit ram rat raven \
rhino salmon seal shark sheep skunk sloth snake spider stork swan \
tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def 행맨게임소개():
    print('*' * 30)
    print('행맨 게임을 시작합니다.')
    print('게임 기회는 총 6번입니다.\n 행운을 빕니다.')
    print('*' * 30)


# 행맨게임소개()

def 비밀단어생성(words):
    n = random.randint(0, len(words) - 1)
    return words[n]


def 게임화면생성(행맨그림, 틀린단어, 맞춘단어, 비밀단어):
    print(행맨그림[len(틀린단어)])
    print()
    print('틀린 단어 표시 : ', end=' ')
    for i in 틀린단어:
        print(i, end=' ')
    print()

    밑줄 = '_' * len(비밀단어)

    for i in range(len(비밀단어)):
        if 비밀단어[i] in 맞춘단어:
            밑줄 = 밑줄[:i] + 비밀단어[i] + 밑줄[i + 1:]
    for i in 밑줄:
        print(i, end=' ')
    print()


def 알파벳한글자리턴(단어목록):  # 단어목록 == 틀린단어 + 맞춘단어
    while True:
        guess = input('한 단어를 입력하세요 :')
        guess = guess.lower()
        if len(guess) != 1:
            print('한 글자만 입력해 주세요')
        elif guess in 단어목록:
            print('그 글자는 먼저 입력했어요. 다시 입력해 주세요')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('알파벳 한 글자를 입력해 주세요')
        else:
            return guess


def 게임재실행():
    print('다시 게임하실래요?(yes or no)')
    return input().lower().startswith('y')
############################################################################

#######################
행맨게임소개()
틀린단어 = ''
맞춘단어 = ''
비밀단어 = 비밀단어생성(words)
게임종료 = False

# print(비밀단어)
while True:
    게임화면생성(행맨그림, 틀린단어, 맞춘단어, 비밀단어)
    guess = 알파벳한글자리턴(틀린단어 + 맞춘단어)
    if guess in 비밀단어:
        맞춘단어 = 맞춘단어 + guess

        모두맞춤 = True
        for i in range(len(비밀단어)):
            if 비밀단어[i] not in 맞춘단어:
                모두맞춤 = False
                break
        if 모두맞춤:
            print('축하합니다' + 비밀단어 + '당신이 이겼어요.')
            게임종료 = True
    else:
        틀린단어 = 틀린단어 + guess
        if len(틀린단어) == len(행맨그림) - 1:
            게임화면생성(행맨그림, 틀린단어, 맞춘단어, 비밀단어)
            print('기회를 다 놓쳤어요')
            print(str(len(틀린단어)) + '번 틀림')
            print(str(len(맞춘단어)) + '번 맞춤')
            print('비밀단어는 ' + 비밀단어)

    if 게임종료:
        if 게임재실행():
            틀린단어=''
            맞춘단어=''
            게임종료=False
            비밀단어=비밀단어생성(words)
        else:
            break


#다음 시간 람다함수부터 할 차례

