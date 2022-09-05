import requests
import telebot
import time


bot = telebot.TeleBot('5127888912:AAEGv8yK5iufHfYoTLzm--ipPGCQxTDIA7Q')
chat_id = '@testingpypy'

def get_data(url):
    # Получаем новости по API
    news_data_get = url
    resp = requests.get(news_data_get)
    resp = resp.json()
    return resp

def send_data(result_json):
    #  отправляем новость в телеграмм
    bot.send_message(chat_id,  result_json[0]['title'] + '\n' + result_json[0]['thesis'] + '\n' 
                    + '<a href="http://127.0.0.1:8000/news/">Читать далее...</a>',parse_mode="HTML")
        
        
if __name__ == '__main__':

    id_news_api = [0,]
    number_iterations = 0
    
    while True:
        result_json = get_data('http://127.0.0.1:8000/apinews-tool/')
        number_iterations += 1

        if  result_json[0]["id"] > int(id_news_api[-1]):
            number_message = send_data(result_json)
            id_news_api.append(result_json[0]["id"])

        elif result_json[0]["id"] <= id_news_api[-1]:
            pass
                
        time.sleep(2)
