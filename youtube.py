import requests
from configs.dev import YT_API_KEY

youtube = "https://www.googleapis.com/youtube/v3/"

def youtube_endpoint(page_token=''):
     return "{}playlistItems?part=snippet&maxResults=50&pageToken={}&playlistId=UUYkldEK001GxR884OZMFnRw&key={}".format(youtube, page_token, YT_API_KEY)

def request_api(page_token=''):
    r = requests.get(youtube_endpoint(page_token))
    try:
        return r.json()
    except:
        return []
