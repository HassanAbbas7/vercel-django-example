from datetime import datetime
from pytube import YouTube
from django.http import HttpResponse


def index(request):
    link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(link)
    except:
        print("Connection Error") #to handle exception
    
    # filters out all the files with "mp4" extension
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path="/tmp/", filename="myfile")
    with open(f"/tmp/myfile.mp4", "rb") as f:
        video_data = f.read()
        
    response = HttpResponse(video_data, content_type="video/mp4")
    response["Content-Disposition"] = f"attachment; filename='myfile.mp4'"
    #to set the name of the file
    
    # get the video with the extension and
    print('Task Completed!')
    return response
