from aiogram import Dispatcher, types
from lexicon.lexicon_ru import LEXICON_RU_COMMAND


# Функция для настройки кнопки Menu бота
async def set_main_menu(dp: Dispatcher):
    main_menu_commands = []
    for command, description in LEXICON_RU_COMMAND.items():
        main_menu_commands.append(types.BotCommand(command=f'{command}', description=f'{description}'))
    await dp.bot.set_my_commands(main_menu_commands)

