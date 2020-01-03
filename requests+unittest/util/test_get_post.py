import requests

class Runmain:
    sess = requests.session()
    sess.get('https://as-test.topchitu.com/callback.shtml?top_appkey=12090519&top_parameters=c3ViX3Rhb2Jhb191c2VyX25pY2s9sMK25LzSys7Tw8a3xuy9orXqJnRzPTE0ODAzMTI0MDcyMTgmdmlzaXRvcl9pZD0xMDA3MjczNzMmdmlzaXRvcl9uaWNrPbDCtuS80srO08PGt8bsvaK16g%3D%3D&top_session=6100308ba2bcefc817ffc15338f8e2c29ef13a18a4e6d23100727373&timestamp=2016-11-28+13%3A53%3A27&agreement=true&agreementsign=12090519-23224472-436003520-F10E5819E2EBDEEABA333BA5B2C8C1CE&top_sign=eHpcgcdlruICJSFbvis5cw%3D%3D')
    def send_post(self,url,data,headers):
        response = self.sess.post(url=url,data=data,headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4)

    def send_get(self,url,params,headers):
        response = self.sess.get(url=url,params=params,headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4)

    def run_main(self,url,params,data,headers,method):
        respose = None
        if method == 'GET':
            respose = self.send_get(url,params,headers)
        else:
            respose = self.send_post(url,data,headers)
        return respose