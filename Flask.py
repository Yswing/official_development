import requests
from requests.auth import HTTPBasicAuth

# 替换以下信息为你的应用程序凭证和重定向URL
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'your_redirect_uri'

# 获取访问令牌的URL
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

# Microsoft Graph API的基本终结点
graph_api_endpoint = 'https://graph.microsoft.com/v1.0/'

# 用户同意的权限范围，可以根据你的需求进行修改
scope = ['User.Read']

# 获取访问令牌的函数
def get_access_token(code):
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': ' '.join(scope)
    }

    response = requests.post(token_url, data=token_data)

    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Failed to retrieve access token. {response.text}")

# 获取用户信息的函数
def get_user_info(access_token):
    user_info_url = graph_api_endpoint + 'me'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }

    response = requests.get(user_info_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve user information. {response.text}")

# 主函数
def main():
    # 在这里获取Authorization Code的流程省略，你可以使用Flask等工具创建一个简单的Web应用来处理登录和获取Code的过程

    # 这里假设你已经获取到Authorization Code
    authorization_code = 'your_authorization_code'

    # 获取访问令牌
    access_token = get_access_token(authorization_code)

    # 使用访问令牌获取用户信息
    user_info = get_user_info(access_token)

    # 打印用户信息
    print("User Information:")
    print(f"User ID: {user_info['id']}")
    print(f"User Display Name: {user_info['displayName']}")
    print(f"User Email: {user_info['mail']}")

if __name__ == "__main__":
    main()
