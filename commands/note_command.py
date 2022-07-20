from telegram import Update
from telegram.ext import ContextTypes
from note import Note

note = Note("note")


async def note_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    inner_command = context.args[0]
    if inner_command == "add":
        text_note = ' '.join(context.args[1:])
        note.add(text_note)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Note %s added!" % text_note)
    elif inner_command == "list":
        await context.bot.send_message(chat_id=update.effective_chat.id, text=note.list_str())
    elif inner_command == "remove":
        value_to_remove = ' '.join(context.args[1:])
        remove_text = "Note %s removed!" % value_to_remove if note.remove(value_to_remove) else "Note not found!"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=remove_text)
    elif inner_command == "clear":
        note.clear()
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Note cleared!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Sorry, I didn't understand that command.")
