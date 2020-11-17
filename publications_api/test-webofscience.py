from wos import WosClient
import wos.utils

with WosClient('Naitik', '#Aa12345') as client:
    print(wos.utils.query(client, 'AU=Shilpa Sonawani'))
