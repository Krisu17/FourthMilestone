import os

OAUTH_BASE_URL = "https://andersok.eu.auth0.com"
OAUTH_ACCESS_TOKEN_URL = OAUTH_BASE_URL + "/oauth/token"
OAUTH_AUTHORIZE_URL = OAUTH_BASE_URL + "/authorize"
OAUTH_CALLBACK_URL = "https://localhost:8080/callback"
OAUTH_CALLBACK_URL_COURIER = "https://localhost:8082/callback"
OAUTH_CLIENT_ID = "E0RJRAu4Rn5WygytcLQ6KBUXWs2oEsga"
OAUTH_CLIENT_SECRET = os.environ.get("OAUTH_CLIENT_SECRET")
OAUTH_SCOPE = "openid profile"
SECRET_KEY = os.environ.get("LAB_AUTH_SECRET")
NICKNAME = "nickname"