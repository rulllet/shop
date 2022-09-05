import requests
import telebot
import time
import jsondiff


bot = telebot.TeleBot('5127888912:AAEGv8yK5iufHfYoTLzm--ipPGCQxTDIA7Q')
chat_id = '@testingpypy'


def get_data(url):
    # Получаем новости json по API
    news_data_get = url
    resp = requests.get(news_data_get)
    resp = resp.json()
    return resp


def get_edit_text_message(data_save, result_json):
    # Поиск редактированных новостей
    try:  
        result = jsondiff.diff(data_save[-1], result_json, syntax='symmetric')  
        return result[0]["title"] 
    except:
        pass


def get_id_json_edit_text_message(get_text_edit, result_json):
    # Подготовка данных к отправке отредактированной новости
    try:
        for i in result_json:
            if i["title"] == get_text_edit[1]:
                return i['id'], i["title"], i["thesis"]
    except:
        pass


def send_data(result_json):
    # Отправляем новость в телеграмм, и возвращием id новости из чата
    message = bot.send_message(chat_id,  result_json[0]['title'] + '\n' + result_json[0]['thesis'] + '\n' 
                        + '<a href="http://127.0.0.1:8000/news/">Читать далее...</a>',parse_mode="HTML").message_id
    return message


def edit_data(number_message, get_id_text_edit):
    # Редактирование новости
    bot.edit_message_text(get_id_text_edit[1] + '\n' + get_id_text_edit[2] + '\n' 
                        + '<a href="http://127.0.0.1:8000/news/">Читать далее...</a>', chat_id, number_message, parse_mode="HTML")

         
if __name__ == '__main__':

    data_save = []
    id_news_telegram = [0,]
    id_news_api = [0,]
    
    while True:

        result_json = get_data('http://127.0.0.1:8000/apinews-tool/')
        get_text_edit = get_edit_text_message(data_save, result_json)  
        get_id_text_edit = get_id_json_edit_text_message(get_text_edit, result_json)
        
        if  result_json[0]["id"] > int(id_news_api[-1]):
            number_message = send_data(result_json)
            id_news_telegram.append(number_message)
            id_news_api.append(result_json[0]["id"])

        else:
            try:
                for i, k in enumerate(id_news_api):
                    if k == get_id_text_edit[0]:
                        edit = edit_data(id_news_telegram[i], get_id_text_edit)
            except:
                continue
        data_save.clear()
        data_save.append(result_json) 
        time.sleep(2)

                
