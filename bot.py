# Fufrom telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters

def forward_message(bot: Bot, update: Update):
    # ID del canale di origine
    source_channel_id = -1001939208048

    # ID del canale di destinazione
    destination_channel_id = -1001612504318

    # Leggi il messaggio
    message = update.message

    # Inoltra il messaggio al canale di destinazione
    bot.forward_message(destination_channel_id, source_channel_id, message.message_id)

# Token di accesso del tuo bot
bot_token = '6069252060:AAFHLj0SgFdh5FpX_V0t-L3boz1fJLx4juA'

# Crea un'istanza del bot
bot = Bot(bot_token)

# Crea un'istanza dell'Updater per ricevere gli aggiornamenti
updater = Updater(bot_token)

# Aggiungi un gestore per i nuovi messaggi nel canale di origine
updater.dispatcher.add_handler(MessageHandler(Filters.chat_type.channel & Filters.update.message, forward_message))

# Avvia il bot
updater.start_polling()
updater.idle()  