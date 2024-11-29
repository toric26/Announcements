youtube_channel="https://www.youtube.com/@BevFaceyAnnouncements"

from googleapiclient.discovery import build

# API key for YouTube Data API v3
API_KEY = "AIzaSyDzFRbiN0rKEanm12z4wPCpCf_RChYEmxA"

# YouTube channel ID for "@bevfaceyannouncements"
CHANNEL_ID = "UCS8NR4uTYkC86rZsnf6LRCA"

# Create a YouTube Data API service
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Get the latest video for the channel
latest_video = youtube.search().list(part='snippet', channelId=CHANNEL_ID, type='video', order='date', maxResults=1).execute()

# Get the video details including duration
video_id = latest_video['items'][0]['id']['videoId']
video_details = youtube.videos().list(part='contentDetails', id=video_id).execute()
duration = video_details['items'][0]['contentDetails']['duration']

# Print the title, URL, and duration of the latest video
for item in latest_video['items']:
    #print("Latest Video Title:", item['snippet']['title'])
    print("Latest Video URL:", f"https://www.youtube.com/watch?v={item['id']['videoId']}")
    print("Video Duration:", duration)
