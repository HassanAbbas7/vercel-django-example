from datetime import datetime
from pytube import YouTube
from django.http import HttpResponse
import glob
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(('GET',))
def index(request):
    link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(link)
    except:
        print("Connection Error") #to handle exception

    try:
        # filters out all the files with "mp4" extension
        stream = yt.streams.get_highest_resolution()
        stream.download("/tmp/")
        with open(glob.glob("/tmp/*.mp4")[0], "rb") as f:
            video_data = f.read()
    
    
        response = HttpResponse(video_data, content_type="video/mp4")
        response["Content-Disposition"] = f"attachment; filename='myfile.mp4'"
        #to set the name of the file
        print(f"Video data \n {video_data}")
        return Response(video_data)
    except Exception as e:
        print(e)
        return HttpResponse("error")
