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
    print('행맨게임을 시작합니다.')
    print('숨겨진 단어를 맞춰보세요.')
    print('행운을 빕니다.')
    print('*' * 30)


def 비밀단어생성(words):
    n = random.randint(0, len(words) - 1)
    return words[n]


def 게임화면생성(행맨그림, 틀린단어, 맞춘단어, 비밀단어):
    # print(행맨그림[0])
    print(행맨그림[len(틀린단어)])
    print()
    print('틀린 단어 표시: ', end=' ')
    for i in 틀린단어:
        print(i, end=' ')
    print()
    밑줄 = '_' * len(비밀단어)
    for i in range(len(비밀단어)):
        if 비밀단어[i] in 맞춘단어:
            밑즐 = 밑줄[ :i]+비밀단어[i]+밑줄[i+1: ]
    for i in 밑줄:
        print(i, end =' ')
    print()

def 맞추기도전(먼저맞춘것):
    while True:
        guess = input('글자를 입력하세요 :')
        guess = guess.lower()
        if len(guess) != 1:
            print('1 글자만 입력하세요 ')
        elif guess in 먼저맞춘것:
            print(' 그 글자는 먼저 맞추신 글자입니다. 다시 입력하세요.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('알파벳을 입력하세요.')
        else:
            return guess

def 게임재실행():
    print('다시 게임하실래요? (yes or no)')
    return input().lower().startswith('y')

###### 게임 실행 ##########
행맨게임소개()
틀린단어=''
맞춘단어=''
비밀단어=비밀단어생성(words)
# print(비밀단어)
게임종료=False

while True:
    게임화면생성(행맨그림, 틀린단어, 맞춘단어, 비밀단어)
    guess = 맞추기도전(틀린단어 + 맞춘단어)
    if guess in 비밀단어:
        맞춘단어 = 맞춘단어 + guess

        모두맞춤 = True
        for i in range(len(비밀단어)):
            if 비밀단어[i] not in 맞춘단어:
                 모두맞춤 = False
                 break
        if 모두맞춤:
            print('축하합니다. ' + 비밀단어 + ' 당신이 이겼어요.')
            게임종료 = True
    else:
        틀린단어 = 틀린단어 + guess
        if len(틀린단어) == len(행맨그림) -1 :
            게임화면생성(행맨그림, 틀린단어, 맞춘단어, 비밀단어)
            print('맞출 기회를 다 놓쳤어요.')
            print(str(len(틀린단어))+ '번 틀림')
            print(str(len(맞춘단어))+ '번 맞춤')
            print('비밀단어는 ' + 비밀단어)
            게임종료 = True

    if 게임종료:
        if 게임재실행():
            틀린단어=''
            맞춘단어=''
            게임종료=False
            비밀단어=비밀단어생성(words)
        else:
            break




