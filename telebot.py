import telebot

bot = telebot.TeleBot('Тут токен')

@bot.message_handler(commands=['start'])

def start(message):
    def приходи_на_новый_год(n):
        
        for i in range(1, 6):
            if i == 5:
                bot.send_message(message.chat.id,(f'Ваш текст'))
            elif i == 4:
                bot.send_message(message.chat.id,(f'Ваш текст'))
            else:
                bot.send_message(message.chat.id,(f'Ваш текст'))
    приходи_на_новый_год(31)
    
    for i in range(2):
        if i==0:
            k='🌲'
            bot.send_message(message.chat.id, k)
        else:
            k='🎄'
            bot.send_message(message.chat.id, k)


bot.polling(none_stop=True)
# Refactored function for better performance 2025-02-16 14:51:23

# Refactored function for better performance 2025-02-16 14:52:17

# Refactored function for better performance 2025-02-16 14:59:26

# Refactored function for better performance - 2025-02-17 20:02:25

# Refactored function for better performance 2025-02-16 15:02:08

# Refactored function for better performance 2025-02-16 15:11:28

# Refactored function for better performance 2025-02-16 15:11:33

# Refactored function for better performance 2025-02-16 15:15:37

# Refactored function for better performance 2025-02-16 16:43:40
