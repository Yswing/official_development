from flask import Flask, redirect, request, session, url_for
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于加密 session 的密钥，请替换成一个随机且安全的字符串

# 替换以下信息为你的应用程序凭证和重定向URL
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'your_redirect_uri'

# Microsoft Graph API的基本终结点
graph_api_endpoint = 'https://graph.microsoft.com/v1.0/'

# 用户同意的权限范围，可以根据你的需求进行修改
scope = ['User.Read']

# 获取Authorization Code的路由
@app.route('/login')
def login():
    authorize_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'response_type': 'code',
        'scope': ' '.join(scope),
    }

    return redirect(authorize_url + '?' + '&'.join([f'{key}={value}' for key, value in params.items()]))

# 处理回调的路由
@app.route('/callback')
def callback():
    code = request.args.get('code')

    # 获取访问令牌
    access_token = get_access_token(code)

    # 使用访问令牌获取用户信息
    user_info = get_user_info(access_token)

    # 在实际应用中，你可能需要将用户信息存储在数据库中或进行其他操作
    # 这里简单地将用户信息存储在session中
    session['user_info'] = user_info

    # 跳转到用户信息页面或其他需要登录后访问的页面
    return redirect(url_for('user_info'))

# 显示用户信息的路由
@app.route('/user_info')
def user_info():
    # 检查用户是否登录，如果没有则重定向到登录页面
    if 'user_info' not in session:
        return redirect(url_for('login'))

    user_info = session['user_info']

    # 在实际应用中，你可以在这里渲染用户信息的页面
    return f"User Information: {user_info}"

# 获取访问令牌的函数
def get_access_token(code):
    token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
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

# 使用访问令牌获取用户信息的函数
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

if __name__ == "__main__":
    app.run(debug=True)
