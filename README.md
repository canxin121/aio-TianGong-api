# aio-TianGong-api
 昆仑天工api，提供aiohttp的异步client

 现在存在一个严重的问题没有解决，过一段时间后Invitetoken会过期，提示等待但无法成功

```python
import asyncio
from TianGongBot import TianGongBot

# 现在存在一个严重的问题没有解决，过一段时间后Invitetoken会过期，提示等待但无法成功

TOKEN = ""
COOKIE = ""
INVITE_TOKEN = ""
tgbot = TianGongBot.TiangongBot(COOKIE,TOKEN,INVITE_TOKEN)

async def main():
    #创建一个新的session
    session_id,message_id = await tgbot.new_session("在吗")
    #获取创建时的返回消息
    msg = await tgbot.get_msg(message_id)
    print(msg)
    #向已有的session发送消息
    message_id = await tgbot.send_msg("你是谁",session_id)
    #获取消息
    msg = await tgbot.get_msg(message_id)
    print(msg)
    
asyncio.run(main())
```
