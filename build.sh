sudo docker build . -t "wordle_spoil_bot"

# add this to cronjob
# 0 16 * * * sudo docker run wordle_spoil_bot
