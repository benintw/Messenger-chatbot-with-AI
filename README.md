
# Reference:
https://github.com/jellyfangs/messenger-bot-tutorial


## To start Flask server
```bash
uv run python run.py
```

## To start ngrok server
```bash
ngrok http 5001
```

Every time you start ngrok, you will get a new URL. You need to update the webhook URL in the Facebook page settings to the new URL.


https://developers.facebook.com/apps/722282750688539/messenger/messenger_api_settings/

![webhook這邊要改成ngrok的url 加上/webhook/](image.png)

e.g., https://10f17edd5396.ngrok-free.app/webhook/

# TOKENS needed:
- FB_PAGE_ACCESS_TOKEN=(see below)
![get FB_PAGE_ACCESS_TOKEN here](image-1.png)
- FB_VERIFY_TOKEN=this_can_be_anything_but_has_to_match_驗證權杖_in_webhooks_settings
- OPENAI_API_KEY=(from OpenAI)

