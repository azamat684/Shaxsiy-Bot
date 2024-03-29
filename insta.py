import requests
import json

def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"    
    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "bb6699699emsh97298a41c6cf5a7p1ddcc8jsn0cfc50572209",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Bad'
    else:
        dict = {}
        if rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            dict['title'] = rest['title']
            return dict
        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            dict['title'] = rest['title']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            dict['title'] = rest['title']
            return dict
        elif rest['Type'] == 'Story-Video':
            dict['type'] = 'story'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Story-Image':
            dict['type'] = 'story_image'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Bad'
    
# print(instadownloader(link="https://www.instagram.com/tv/CqDy41putKn/?igshid=YmMyMTA2M2Y="))
