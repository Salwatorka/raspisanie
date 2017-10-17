import requests
import misc
import json

token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'
#https://api.telegram.org/bot412939085:AAEOqcBuBUEc94J6Rq73JeueuQUABbcFOGc/sendmessage?chat_id=333255225&text=


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']

    message = {'chat_id': chat_id,
               'text': message_text}
    return message



def send_message(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    #    d = get_updates()
    #    with open('updates.json', 'w') as file:
    #        json.dump(d, file, indent = 2, ensure_ascii=False)
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['text']
    #  faculties = {'rtf': rtf,
    #              'fet': fet,
    #             'fsu': fsu,
    #            'fvs': fsu,
    #           'gf': gf,
    #          'ef': ef,
    #         'fit': fit,
    #        'uf': uf,
    #       'fb': fb}

    if text == '/start':
            send_message(chat_id, 'Приветствую тебя! Твой факультет?')
    if text == '/rtf':
            send_message(chat_id, 'Номер группы?')
    if text == '125':
            send_message(chat_id, 'https://timetable.tusur.ru/faculties/rtf/groups/125')
    if text == '1b5':
            send_message(chat_id, 'https://timetable.tusur.ru/faculties/rtf/groups/1v5')
    if text == '145-1':
            send_message(chat_id, 'https://timetable.tusur.ru/faculties/rtf/groups/145-1')
    if text == '145-2':
            send_message(chat_id, 'https://timetable.tusur.ru/faculties/rtf/groups/145-2')
    if text == '145-3':
            send_message(chat_id, 'https://timetable.tusur.ru/faculties/rtf/groups/145-3')
    if text == '1a5' or '1А5':
            send_message(chat_id, 'https://timetable.tusur.ru/faculties/rtf/groups/1a5')




if __name__ == '__main__':
    main()