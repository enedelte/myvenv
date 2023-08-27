import os
import webbrowser
import msal
from msal import PublicClientApplication

application_id = '3d37761d-12e6-41be-981c-b87b360fc014'
client_secret = '3oC8Q~CnXhs6cacDfhosW-.LxPxwILYqR6oyXaMA'
authority_url = 'https://login.microsoftonline.com/'
base_url = 'https://graph.microsoft.com/v1.0/me'

endpoint = base_url + 'me'
SCOPES = ['User.Read', 'User.Export.All']


#method 1: auth
client_instance = msal.ConfidentialClientApplication(
    client_id= application_id,
    client_credential= client_secret,
    authority= authority_url
  )

authorization_request_url = client_instance.get_authorization_request_url
print(authorization_request_url)

webbrowser.open(authorization_request_url, new=True)