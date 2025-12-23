


class beta():

    BaseHeader = {
        "isSkipSign": "true",
        "client-id": "edu_b_web",
        "content-type": "application/json",
        "Authorization": "Basic ZWR1X2Jfd2ViOmVkdV9iX3dlYl9zZWNyZXQ="
    }

    C_uniappBaseHeader ={
        "isSkipSign": "true",
        "client-id": "edu_c_applet",
        "content-type": "application/json",
        "Authorization": "Basic Y191bmlhcHA6Y191bmlhcHBfc2VjcmV0"

    }

    prod_c_uniapp_url = "https://api.groupyushun.com"

    webhook = {
        "online": 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d233fe90-3e8b-4a85-8d82-5bb3df7878be',
        "test": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=bc8a210b-0ebd-4b64-b665-e89b8a405d3f"

    }

config = beta