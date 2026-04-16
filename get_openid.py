import urllib.request
import urllib.parse
import json

APP_ID = "cli_xxxxxxxxxxxxxx"
APP_SECRET = "xxxxxxxxxxxxxxxx"
YOUR_EMAIL = "你的邮箱@xxx.com"

def main():
 url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
 data = json.dumps({"app_id": APP_ID, "app_secret": APP_SECRET}).encode()
 req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
 with urllib.request.urlopen(req) as resp:
 result = json.loads(resp.read())
 token = result.get("tenant_access_token")
 if not token:
 print(f"获取 token 失败: {result}")
 return
 print(f"token 获取成功: {token}\n")

 url2 = "https://open.feishu.cn/open-apis/contact/v3/users/batch_get_id?user_id_type=open_id"
 payload = {"emails": [YOUR_EMAIL]}
 data2 = json.dumps(payload).encode()
 req2 = urllib.request.Request(url2, data=data2, headers={
 "Authorization": f"Bearer {token}",
 "Content-Type": "application/json"
 })
 with urllib.request.urlopen(req2) as resp2:
 result2 = json.loads(resp2.read())

 print("API 返回结果：")
 print(json.dumps(result2, ensure_ascii=False, indent=2))

 if result2.get("code") == 0:
 users = result2.get("data", {}).get("user_list", [])
 if users:
 for u in users:
 print(f"\n你的 open_id 是: {u['user_id']}")
 else:
 print("\n未查到用户信息")
 else:
 print(f"\n失败: code={result2.get('code')} msg={result2.get('msg')}")

if __name__ == "__main__":
 main()
