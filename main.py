import requests
from PIL import Image
import os


def create_page(token, title):
    response = requests.post('https://api.telegra.ph/createPage',
                             data={'access_token': token,
                                   'title': title,
                                   'content': '[{"tag":"p","children":["Content"]}]'})
    data = response.json()
    print('Page created!\nurl: {}'.format(data['result']['url']))
    return data['result']['path']


def create_content(image_folder):
    content = '['
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            with open(image_path, 'rb') as file:
                response = requests.post('https://telegra.ph/upload', files={'file': file})
                image_data = response.json()
                print(image_data)
                src = image_data[0]['src']

            img_tag = '{"tag": "img", "attrs": {"src": "%s"}},' % src
            content += img_tag
            print('Picture "{}" complete!'.format(filename))
    content = content[:-1] + ']'
    return content


def add_pictures(token, path, content, title):
    update_response = requests.post('https://api.telegra.ph/editPage',
                                    data={'access_token': token,
                                          'path': path,
                                          'title': title,
                                          'content': content})
    update_data = update_response.json()
    print('url: {}'.format(update_data['result']['url']))


def start():
    print('Hello! Put here some beutiful text.')
    token = input('Enter your token:\n>>> ')
    folder = input('Enter your folder path:\n>>> ')
    title = input('Enter your title:\n>>> ')

    add_pictures(token, create_page(token, title), create_content(folder), title)


start()

# 1b6254f700588948642aefa7ffa48f693364152901a6f281a07e3f2ec171
