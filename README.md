# Reddit2TikTok
Reddit video scrapper to convert into TikTok format

# Reddit Video Downloader & Cropper

This Python script uses the Reddit API to download top weekly video posts from a specified subreddit, then crops them to a TikTok-friendly format (9:16 aspect ratio), and stores them locally.

![My Image](https://github.com/Swipe05/Reddit2TikTok/blob/main/reddit2tiktoktotk.png)

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)

## Installation

This project requires Python 3.6 or later. Dependencies are managed with pip, Python's package installer. You can install the dependencies like so:
```python
pip install moviepy
pip install praw
```

**FFmpeg is necessary for the script to work**

**If the video doesn't start try using VLC Media Player**

Dependencies included:

- praw
- requests
- datetime
- moviepy
- os

## Usage

You'll need to replace 'client_id', 'client_secret' with your actual Reddit app's client_id, client_secret respectively.

You can specify the subreddit you're interested in by changing the line:

```python
subreddit = reddit.subreddit("SUBREDDIT_NAME")
```
Run the script with:

python RedditScrapper.py

The downloaded and cropped videos will be saved in a folder named by the current date (e.g., "2023-06-18").

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.



