import praw
import requests
import datetime
from moviepy.editor import VideoFileClip
import os


current_date = datetime.datetime.now()
output_folder = current_date.strftime("%Y-%m-%d")
final_output_folder = output_folder

suffix = 1
while os.path.exists(final_output_folder):
    final_output_folder = f"{output_folder}-{suffix}"
    suffix += 1

os.makedirs(final_output_folder)









def create_cropped_video_from_url(url,name):
    response = requests.get(url, stream=True)
    video_path = final_output_folder + "/video.mp4"
    if response.status_code == 200:
        # Open a file in write mode and write the response's content to it
        with open(video_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                # Filter out keep-alive chunks
                if chunk:
                    file.write(chunk)

    clip = VideoFileClip(final_output_folder + "/video.mp4")

    # Get video dimensions
    width, height = clip.size

    # Desired (TikTok) aspect ratio
    aspect_ratio = 9 / 16

    # Calculate new width and height
    new_width = min(width, int(height * aspect_ratio))
    new_height = min(height, int(width / aspect_ratio))

    # Calculate cropping area
    left = (width - new_width) / 2
    top = (height - new_height) / 2
    right = (width + new_width) / 2
    bottom = (height + new_height) / 2

    # Crop video
    cropped_clip = clip.crop(x1=left, y1=top, x2=right, y2=bottom)

    # write the result to a file
    cropped_clip.write_videofile(final_output_folder +'/'+ name + ".mp4")

    if os.path.exists(video_path):
        # Delete the file
        os.remove(video_path)
    else:
        print("File does not exist.")



# Initialize the Reddit instance
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='praw v7.3.0 for /u/your_username',
)



# set the subreddit you're interested in
subreddit = reddit.subreddit("TOTK")



# get the top submissions of the past week
top_submissions = subreddit.top('week')
all_urls = dict()

for submission in top_submissions:
    # check if it's a video or a link to YouTube
    if submission.is_video or 'youtube.com' in submission.url:
        video_url = submission.media['reddit_video']['fallback_url']
        print(f"Title: {submission.title}")
        print(f"URL: {video_url}")
        all_urls[submission.title] = video_url

for key,value in all_urls.items():
    print(key, value)
    create_cropped_video_from_url(value,key)


