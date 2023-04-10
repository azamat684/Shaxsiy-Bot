import requests
import json

def tk(url1):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":url1}

    headers = {
        "X-RapidAPI-Key": "bb6699699emsh97298a41c6cf5a7p1ddcc8jsn0cfc50572209",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    rest = json.loads(result)
    return {"video":rest['video'][0],"music":rest['music'][0]}
