import spotipy
import youtube_dl
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_search import YoutubeSearch

def find_url_from_title(track):
    results = YoutubeSearch(track, max_results=10).to_dict()
    ans=results[0]['url_suffix']
    return ans


def download_ytvid_as_mp3(title,url):
    video_url=url
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = (title+".mp3")
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
    

def download_ytvid_as_mp3(title,url):
    video_url=url
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = (title+".mp3")
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
    



client_Id = "" #your spotify client ID
client_Secret = ""#your spotify client secret


playlist_id= "" #your playlist id
spotify=spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_Id, client_secret = client_Secret,))

results=spotify.playlist_tracks(playlist_id)
tracks=results['items']
while results['next']:
    results=spotify.next(results)
    tracks.extend(results['items'])
Ltracks = []
for track in tracks: 
    Ltracks.append(track['track']['name'])

print("Songs found: ")
for i in tracks:
    print(i['track']['name'])




title = []
for titl in Ltracks:
    print("\n gettin URL..\n")
    youtube_url = "https://www.youtube.com"+find_url_from_title(titl)
    print(youtube_url)
    print("\n Downloading... \n")
    download_ytvid_as_mp3(titl,youtube_url)
    


