# TelegramBotReaderBook
A telegram bot book reader. 

## how to run
### docker

```shell
docker run -d --name telegram-reader-bot -e BOT_TOKEN="" -e ADMIN_ID="" -e BOOK_PATH="/root/test.txt" -e PAGE_SIZE=500 jp0id/telegram-reader-bot
```

forked from https://github.com/DmitryDruzh/TelegramBotReaderBook