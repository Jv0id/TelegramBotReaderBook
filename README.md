# TelegramBotReaderBook
A telegram bot book reader. 

>目前仅支持`txt`和`epub`的图书

>only books in `txt` and `epub` format are supported.

## how to run
### docker

```shell
docker run -d --name telegram-reader-bot -e BOT_TOKEN="" -e ADMIN_ID="" -e BOOK_PATH="/path/yourbook.txt" -e PAGE_SIZE=500 -v "/path/yourbook.txt":"/path/yourbook.txt" jp0id/telegram-reader-bot
```

## TODO
- add docker-compose
- more book type
- persistent storage to local

forked from `https://github.com/DmitryDruzh/TelegramBotReaderBook`
