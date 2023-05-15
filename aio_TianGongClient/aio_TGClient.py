import aiohttp
import asyncio
import json

class TiangongClient:
    def __init__(self, cookie, token, invite_token):
        self.token = token
        self.cookie = cookie
        self.invite_token = invite_token

        try:
            with open("./invite_token.txt", "r") as f:
                self.invite_token = f.read()
        except:
            pass
        
        self.verified = False
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Content-Type': 'application/json',
            'Cookie': self.cookie,
            'Device': 'Web',
            'Invite-Token': self.invite_token,
            'Origin': 'https://neice.tiangong.cn',
            'Referer': 'https://neice.tiangong.cn/interlocutionPage',
            'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Token': self.token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0'
        }

    async def verify(self):
        url = "https://neice.tiangong.cn/api/v1/user/inviteVerify"
        data = {"data": {}} # Replace with your own data
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(url, json=data) as response:
                response_data = await response.json()
                # print(f"verify : {response_data}")
                if response_data["code"] == 200:
                    self.verified =  True
                    return True
                else :
                    return False
    async def wait_access(self):
        url = 'https://neice.tiangong.cn/api/v1/queue/waitAccess'
        self.verified = await self.verify()
        if self.verified:
            return
        while True:
            data = {"token":self.invite_token}
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.post(url, data=json.dumps(data)) as response:
                    response_data = await response.json()
                    print(f"wait :  {response_data}")
                    try:
                        # percent = response_data["resp_data"]["wait_percent"]
                        success = response_data["resp_data"]["success"]
                        invite_token = response_data["resp_data"]["invite_token"]
                        if success and invite_token:
                            with open("./invite_token.txt", "w") as f:
                                f.write(invite_token)
                            return True
                        if invite_token:
                            self.invite_token = invite_token
                    except:
                        pass
                    try:
                        code_msg = response_data["code_msg"]
                        if code_msg == 'refuse service, already get the number':
                            with open("./invite_token.txt", "w") as f:
                                f.write(self.invite_token)
                            return True
                    except:
                        pass
                    
    async def send_msg(self,question,session_id):
        self.verified = await self.verify()
        if not self.verified:
            self.invite_token = ""
            await self.wait_access()
        url = "https://neice.tiangong.cn/api/v1/chat/chat"
        data = {"data": {"content": question, "session_id": session_id}}
        repeat = 0
        while True:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.post(url, json=data) as response:
                    response_json = await response.json()
                    try:
                        id = response_json["resp_data"]["result_message"]["message_id"]
                        return id
                    except:
                        repeat += 1
                        if repeat > 3:
                            raise Exception("发送消息时多次出错")
                    
    async def get_msg(self,message_id):
        # self.verified = await self.verify()
        # if not self.verified:
        #     self.invite_token = ""
        #     await self.wait_access()
        url = "https://neice.tiangong.cn/api/v1/chat/getMessage"
        data = {"data": {"message_id": message_id}}
        repeat = 0
        while True:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url, headers=self.headers, data=json.dumps(data)
                ) as response:
                    response_data = await response.json()
                    # print(response_data)
                    asyncio.sleep(1)
                    try:
                        if response_data["code"] == 200:
                            repeat = 0
                            content = response_data["resp_data"]["result_message"]["content"]
                            # print(content)
                            status = response_data["resp_data"]["result_message"]["status"]
                            if content and status != 1:
                                return content
                        else:
                            repeat += 1
                            if repeat > 3:
                                raise Exception("获取消息时多次网络出错")
                    except:
                        pass
    
    async def new_session(self,content):
        self.verified = await self.verify()
        if not self.verified:
            self.invite_token = ""
            await self.wait_access()
        url = "https://neice.tiangong.cn/api/v1/session/newSession"
        data = {"data": {"content": content}}  # Replace with your actual data
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(url, data=json.dumps(data)) as response:
                response_data = await response.json()
                print(response_data)
                try:
                    session_id = response_data["resp_data"]["session_id"]
                    message_id = response_data["resp_data"]["dialogue"][1]["message_id"]
                    return session_id,message_id
                except:
                    raise Exception("创建新对话时出错")
                
