import requests
import json

# 1. 获取 tenant_access_token
app_id = "你的app_id"
app_secret = "你的app_secret"

resp = requests.post(
 "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
 json={"app_id": app_id, "app_secret": app_secret}
)
token = resp.json()["tenant_access_token"]

# 2. 在用户的主日历上创建一个测试日程（用你的 open_id）
open_id = "你的open_id" # 用户在飞书中的 open_id

create_resp = requests.post(
 "https://open.feishu.cn/open-apis/calendar/v4/calendars/primary/events",
 headers={"Authorization": f"Bearer {token}"},
 json={
 "summary": "【测试】第二课堂日程同步测试",
 "description": "这是一条测试消息，如果看到了说明日历同步功能可用",
 "start_time": {
 "timestamp": "1743261600",
 "timezone": "Asia/Shanghai"
 },
 "end_time": {
 "timestamp": "1743265200",
 "timezone": "Asia/Shanghai"
 },
 "attendees": [
 {"type": "user", "user_id": open_id}
 ]
 }
)

print(json.dumps(create_resp.json(), ensure_ascii=False, indent=2))
