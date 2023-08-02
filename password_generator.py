# import random
# def generate_password():
#     n= int(input('what length should your password be:  '))
#     random_password=''
#     alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyxz0123456789/_+-*!#%'
#     for items in range(n):
#         random_password+=random.choice(alphabets)
#     return f'your generted password is:{random_password}'
#
# print(generate_password())

# score = int(input('Enter your score: '))
#
# f = 40
# if 100 >= score >= 70:
#     print(f'{score} is an A')
# if 69 >= score >= 60:
#     print(f' the {score} is a B')
# if 59 >= score >= 50:
#     print(f'the {score} is a C')
# if 49 >= score >= 40:
#     print(f'the {score} is a D')
# if score < f:
#     print(f'{score} is an F')


def add():
    for items in range(20):
        print(items)
    for items in range(50):
        print(items)


print(add())