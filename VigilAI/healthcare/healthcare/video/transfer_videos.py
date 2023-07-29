import os
from django.core.files import File
from   video.models import vid

def transfer_videos():
    folder_path = 'C:/Users/rudra/Downloads/VigilAI/Eyebase'  # Replace with the actual path to your videos folder

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                video = vid(title=filename)
                video.video_file.save(filename, File(file))
                video.save()