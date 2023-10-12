import requests
import json
import msal

# 配置应用程序
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
scopes = ['https://graph.microsoft.com/.default']
authority = 'https://login.microsoftonline.com/YOUR_TENANT_ID'

app = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

# 获取访问令牌
result = app.acquire_token_silent(scopes, account=None)

if not result:
    result = app.acquire_token_for_client(scopes=scopes)

if "access_token" in result:
    access_token = result['access_token']

    # 使用访问令牌来调用Microsoft Graph API
    graph_url = 'https://graph.microsoft.com/v1.0/me/events'
    headers = {'Authorization': 'Bearer ' + access_token}

    response = requests.get(graph_url, headers=headers)

    if response.status_code == 200:
        events = response.json()
        print(json.dumps(events, indent=4))
    else:
        print(f'请求失败，状态码：{response.status_code}')
        print(response.text)
else:
    print("未能获取访问令牌")
