from json.decoder import JSONDecodeError
import requests
import telebot
import time


bot = telebot.TeleBot('5127888912:AAEGv8yK5iufHfYoTLzm--ipPGCQxTDIA7Q')
chat_id = '@testingpypy'

def get_data(url, last_news):
    
    try:
        news_data_get = url
        resp = requests.get(news_data_get)
        try:
            resp = resp.json()
            resp_id = resp[0]["id"]
            
            if resp_id != last_news[-1]:
                last_news.clear()
                last_news.append(resp_id)
                #bot.send_photo(chat_id, resp[0]['image'])
                bot.send_message(chat_id, resp[0]['image'], resp[0]['title'] + '\n' + resp[0]['thesis'] + '\n' + '<a href="http://127.0.0.1:8000/news/">Читать далее...</a>',parse_mode="HTML")
                return resp[0]
            else:
                return False

        except (JSONDecodeError, IndexError, KeyError):
            print("JSON ERROR")   
    except Exception :
        print("ERROR Connection")
        
        
if __name__ == '__main__':

    last_news = [' ']
    number_iterations = 0
    
    while True:
        res = get_data('http://127.0.0.1:8000/apinews-tool/', last_news)
        number_iterations += 1
        if number_iterations % 10 == 0:
            print(res)
            print(number_iterations)
        elif res != False:
            print(res)
            print(number_iterations)
        time.sleep(2)