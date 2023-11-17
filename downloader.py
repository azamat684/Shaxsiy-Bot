import requests
import json


def tk(url1):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":url1}

    headers = {
        "X-RapidAPI-Key": "1228981466msh104b9c0a688abe1p1dcbd3jsne2eb18bf9656",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    rest = json.loads(result)
    return {"video":rest['video'][0],"music":rest['music']}
# print(tk(url1="https://www.tiktok.com/@khaby.lame/video/7217831447254682885?is_from_webapp=1&sender_device=pc"))
