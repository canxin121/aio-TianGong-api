# aio-TianGong-api
 昆仑天工api，提供aiohttp的异步client

 现在存在一个严重的问题没有解决，过一段时间后Invitetoken会过期，提示等待但无法成功

```python
import asyncio
from aio_TianGongClient import aio_TGClient
#注意INVITE_TOKEN持久化储存，经过一段时间后会过期，需要重新等待之后获取新的才可以使用
TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiVS~~~~"
COOKIE = "acw_tc=b640864ff056257d8f790215f72d3333ec~~~~~"
INVITE_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9~~~~"

tgclient = aio_TGClient.TiangongClient(COOKIE,TOKEN,INVITE_TOKEN)

async def main():
    #创建一个新的session
    session_id,message_id = await tgclient.new_session("在吗")
    #获取创建时的返回消息
    msg = await tgclient.get_msg(message_id)
    print(msg)
    #向已有的session发送消息
    message_id = await tgclient.send_msg("你是谁",session_id)
    #获取消息
    msg = await tgclient.get_msg(message_id)
    print(msg)
    
asyncio.run(main())
```
