from aiogram import Dispatcher, types


async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start',
                         description='这是一个机器人，在这里你可以阅读你指定的书！\n\n要查看可用命令列表-输入 /help'),
        types.BotCommand(command='/beginning', description='开始阅读本书'),
        types.BotCommand(command='/continue', description='继续阅读'),
        types.BotCommand(command='/bookmarks', description='我的书签'),
        types.BotCommand(command='/help', description='帮助'),
    ]
    await dp.bot.set_my_commands(main_menu_commands)
