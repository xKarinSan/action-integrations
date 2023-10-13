# Telegram automation test.

## Aim
This aims to help automate the process of manually informing our teammates on what we are doing and what changes we made so far.

## Setup Steps
1) Go to @BotFather on Telegram.
2) Type ```/newbot``` in the chat to create a telegram bot.
3) You will then be given a bot token upon completion. **PLEASE DO NOT SHARE THE TOKEN WITH ANYONE**
4) Search for your telegram bot or click ```t.me/<your_bot_name>``` at the completion message in step 3.
5) Add your bot to your team's Telegram chat group and type something there.
6) Click [here](https://clickalgo.com/telegram-chatid) and then paste your bot token.
7) You should get your team chat ID from step 6
8) Go to your project repository. Settings -> Secrets and Variables -> Actions
9) Click "New Repository Secret"
10) Fill in the fields such that:
    - Name: TELEGRAM_TO
    - Secret: Your team chat Id from step 7
12) Click "Add secret"
13) Repeat steps 9 to 12 but the field values are:
    - Name: TELEGRAM_TOKEN
    - Secret: Your telegram bot token from step 4
15) Create a github action by:
    - Create .github inside the root of your project
    - Inside .github, create a new folder "workflows". This is where you will put all your necessary github actions.
    - Inside your "workflows" folder, create a yml file called ```notifier.yml```. Paste the contents from [this link](https://github.com/xKarinSan/action-integrations/blob/main/.github/workflows/notifier.yml) into notifier.yml.
16) You are all set!

**NOTE: This is still work in progress, please stay tuned!**
