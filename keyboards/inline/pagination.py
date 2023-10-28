import requests

"""
import requests
from googletrans import Translator
# API ni istalgan joydan oling (masalan, History API)
api_url = "https://history.muffinlabs.com/date"

response = requests.get(api_url)
translator = Translator()
if response.status_code == 200:
    data = response.json()
    events = data["data"]["Events"]
    
    print(f"Bugungi kun tarixda sodir bo'lgan voqealar:")
    
    all = []
    for event in events[:5]:
        malumotlar = translator.translate(event['text'],dest='uz')
        
        all.append(malumotlar.text)
    print(event["year"], "-", malumotlar.text)
else:
    print("Ma'lumotlarni olishda xatolik sodir bo'ldi.")
"""
def get_quran_surahs(step, count):
    url = "https://history.muffinlabs.com/date"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        events = data["data"]["Events"]
        
        chapters = response.get("chapters")
        data = {}
        start = (step - 1) * count 
        stop = count * step
        for chapter in chapters[start:stop]:
            data[chapter.get("name")] = chapter.get("chapter")
        return data