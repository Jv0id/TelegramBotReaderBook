# TelegramBotReaderBook
A telegram bot book reader. 

## how to run
### docker

```shell
docker run -d --name telegram-reader-bot -e BOT_TOKEN="" -e ADMIN_ID="" -e BOOK_PATH="/path/yourbook.txt" -e PAGE_SIZE=500 -v /path/yourbook.txt:/path/yourbook.txt jp0id/telegram-reader-bot
```

forked from https://github.com/DmitryDruzh/TelegramBotReaderBook
