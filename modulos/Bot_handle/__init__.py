from telebot import types
from modulos.funcoes import saudacao
from datetime import datetime
import locale 

locale.setlocale(locale.LC_TIME,'Portuguese_Brazil,1252')

def setup(bot):
    
    @bot.message_handler(func= lambda msg:True)
    def introducao(msg):
        
        semana = datetime.now().strftime("%A")
        
        atual = datetime.now().strftime("%d/%m/%Y")
        
        txt = f"""
        {saudacao()}, 
Me chamo Kara sou sua bot assistente =]
Hoje é {semana}, dia {atual}. Como posso te ajudar hoje??"""
        
        markup = types.InlineKeyboardMarkup()
        botao1 = types.InlineKeyboardButton("Consultas", callback_data="consulta")
        botao2 = types.InlineKeyboardButton("Histórico",callback_data="historico")
        botao3 = types.InlineKeyboardButton("Dicas", callback_data="dicas")
        botao4 = types.InlineKeyboardButton("Agenda",callback_data="agenda")
        botao5 = types.InlineKeyboardButton("Configuração",callback_data="configuracao")
        markup.add(botao1,botao2,botao3,botao4,botao5)
        
        bot.reply_to(msg,txt,reply_markup = markup)        