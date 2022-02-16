# Wordle Spoil Telegram Bot

Auto-post the Wordle answer to the Telegram channel at 12 AM every day.

Build:

```
sudo docker build . -t "wordle_spoil_bot"
```

And add the following in crontab (crontab -e)
```
0 16 * * * /your/path/run_me.sh
```

16 is because the server uses UTC, and 16+8 = 24, so it works at UTC +8, and `run_me.sh` contains the docker timezone "Pacific/Wallis" to prevent the time difference with the server.
