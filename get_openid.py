import urllib.request
import urllib.parse
import json

# ===== 在这里填入你的信息 =====
APP_ID = "cli_xxxxxxxxxxxxxx" # ① App ID（飞书开放平台 → 你的应用 → 凭证与基础信息）
APP_SECRET = "xxxxxxxxxxxxxxxx" # ② App Secret（同上页面）
YOUR_EMAIL = "你的邮箱@xxx.com" # ③ 你的飞书账号邮箱（二选一）
# YOUR_MOBILE = "13800000000" # 或者用手机号，把上面那行注释掉，换这行
# ==================================

def main():
 # 1. 获取 tenant_access_token
 url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
 data = json.dumps({"app_id": APP_ID, "app_secret": APP_SECRET}).encode()
 req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
 with urllib.request.urlopen(req) as resp:
 result = json.loads(resp.read())
 token = result.get("tenant_access_token")
 if not token:
 print(f"获取 token 失败: {result}")
 return
 print(f"✅ token 获取成功\n")

 # 2. 调用 batch_get_id 获取 open_id
 url2 = "https://open.feishu.cn/open-apis/contact/v3/users/batch_get_id?user_id_type=open_id"
 payload = {"emails": [YOUR_EMAIL]} # 改用手机号就是 {"mobiles": [YOUR_MOBILE]}
 data2 = json.dumps(payload).encode()
 req2 = urllib.request.Request(url2, data=data2, headers={
 "Authorization": f"Bearer {token}",
 "Content-Type": "application/json"
 })
 with urllib.request.urlopen(req2) as resp2:
 result2 = json.loads(resp2.read())

 print("API 返回结果：")
 print(json.dumps(result2, ensure_ascii=False, indent=2))

 # 3. 提取 open_id
 if result2.get("code") == 0:
 users = result2.get("data", {}).get("user_list", [])
 if users:
 for u in users:
 print(f"\n✅ 你的 open_id 是：{u['user_id']}")
 else:
 print("\n⚠️ 未查到用户信息，可能是邮箱/手机号不匹配，或应用没有通讯录权限")
 else:
 print(f"\n❌ 失败：code={result2.get('code')}，msg={result2.get('msg')}")

if __name__ == "__main__":
 main()
