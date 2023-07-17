#1-2
def create_youtube_video (title ,description):
	d1={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return d1 
#3
def like (youtube_video):
	if "likes" in youtube_video:
	 	youtube_video["likes"]+=1
	return youtube_video

#4
def dislike (youtube_video):
	if "dislikes" in youtube_video1:
	 	youtube_video["dislikes"]+=1
	return youtube_video

#5
def add_comment(youtube_video,username,comment_text):
	youtube_video["comments"][username]=comment_text
	return youtube_video

#6
ved=create_youtube_video("hello","hello again")
print(ved)
