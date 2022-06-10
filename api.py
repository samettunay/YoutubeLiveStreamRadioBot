from googleapiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_API_KEY = "" 

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=YOUTUBE_API_VERSION)


def search(query):
    request = youtube.search().list(
        part='id,snippet',
        q=query,
        maxResults=1,
        type='video'
    )

    response = request.execute()
    search_results = []

    for video in response['items']:
        item = {
            'name': video["snippet"]["title"],
            'value': 'https://www.youtube.com/watch?v=' + video["id"]["videoId"]
        }

        search_results.append(item)

    return search_results
