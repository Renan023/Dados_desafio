from telebot import TeleBot, types
from datetime import datetime
import locale

TOKEN = '7600937178:AAFaUpnRPG31kPRqVbNTaDt2O9RE1KgEitE'

bot = TeleBot(TOKEN)

locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')

def saudacao():
    hora = datetime.now().hour
    
    if hora < 12:
        return "Bom dia ☀️"
    elif hora < 18:
        return "Boa tarde ⛅"
    else:
        return "Boa noite 🌜"
    
@bot.message_handler(func=lambda msg: True)
def Boas_vindas(msg):
    
    saud = saudacao()
    
    semana = datetime.now().strftime("%A")
    
    atual = datetime.now().strftime("%d/%m/%Y")
    
    txt = f"""{saud}, 
Me chamo Kara sou sua bot assistente.
Hoje é {semana} dia {atual}. Em que posso te ajudar?"""
    
    markup = types.InlineKeyboardMarkup()
    botao1 = types.InlineKeyboardButton("Ver Consultas", callback_data="ver_consultas")
    botao2 = types.InlineKeyboardButton("Meu Histórico", callback_data="Meu_Historico")
    markup.add(botao1, botao2)
    
    bot.reply_to(msg,txt,reply_markup=markup)
    
    @bot.callback_query_handler(func=lambda call: True)
    def responder(call):
        
        if call.data == "ver_consultas":
            markup = types.InlineKeyboardMarkup()
            botaopf = types.InlineKeyboardButton("Pessoa Física",callback_data="pf")
            botaopj = types.InlineKeyboardButton("Pessoa Jurídica",callback_data="pj")
            markup.add(botaopf, botaopj)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text = 'Como gostaria de realizar a consulta',reply_markup=markup)
            
bot.infinity_polling()