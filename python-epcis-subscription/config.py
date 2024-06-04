# Config file to connect to Keycloak and WebSocket
import os

# Keycloak configuration associated to Local environment
TOKEN_ENDPOINT = os.getenv('TOKEN_ENDPOINT', 'http://localhost:9080/realms/openepcis/protocol/openid-connect/token')
WS_URL = os.getenv('WS_URL', 'ws://localhost:8080/queries/TemperatureAlert/events?stream=true')
USERNAME = os.getenv('USERNAME', 'XXXXXXX')
PASSWORD = os.getenv('PASSWORD', 'XXXXXXX')
CLIENT_ID = os.getenv('CLIENT_ID', 'XXXXXXX')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', 'XXXXXXX')
GRANT_TYPE = os.getenv('GRANT_TYPE', 'XXXXXXX')
SCOPE = os.getenv('SCOPE', 'XXXXXXX')
REDIRECT_URI = os.getenv('REDIRECT_URI', 'http://localhost:5000/callback')
AUTHORIZATION_ENDPOINT = os.getenv('AUTHORIZATION_ENDPOINT','http://localhost:9080/realms/openepcis/protocol/openid-connect/auth')

# Keycloak configuration associated to Production environment