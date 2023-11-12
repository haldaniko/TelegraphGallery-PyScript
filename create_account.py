import requests


def create_account(short_name, author_name, author_url):
    response = requests.post('https://api.telegra.ph/createAccount',
                             data={'short_name': short_name,
                                   'author_name': author_name,
                                   'author_url': author_url})
    data = response.json()
    print("====================\n"
          "Account created!\n\n"
          "Author name: {}\n"
          "Short name: {}\n"
          "Token: {}\n"
          "Account url: {}\n\n"
          "Use this url to authorize: {}\n"
          "====================".format(data['result']['author_name'],
                                        data['result']['short_name'],
                                        data['result']['access_token'],
                                        data['result']['author_url'],
                                        data['result']['auth_url']))


def start():
    print('Hello! Put here some beutiful text.')
    short_name = input('Enter your short name:\n>>> ')
    author_name = input('Enter your author name:\n>>> ')
    author_url = input('Enter your profile link:\n>>> ')

    create_account(short_name, author_name, author_url)

start()
