# TelegramBotReaderBook
A telegram bot book reader. 

目前仅支持txt和epub的图书

## how to run
### docker

```shell
docker run -d --name telegram-reader-bot -e BOT_TOKEN="" -e ADMIN_ID="" -e BOOK_PATH="/path/yourbook.txt" -e PAGE_SIZE=500 -v "/path/yourbook.txt":"/path/yourbook.txt" jp0id/telegram-reader-bot
```

## TODO
- add docker-compose 　✔️
- more book type

forked from https://github.com/DmitryDruzh/TelegramBotReaderBook
