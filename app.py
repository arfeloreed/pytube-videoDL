from pytube import YouTube


# Youtube video url
link = "https://www.youtube.com/watch?v=duC7TZ1UlsQ"

# creating Youtube object with url
yt = YouTube(
    link,
    on_progress_callback=lambda stream, chunk, bytes_remaining: print(
        round((1-bytes_remaining/stream.filesize)*100, 2), "% done"),
    on_complete_callback=lambda stream, file_path: print("Download complete")
)

# getting all the available streamss
streams = yt.title
print(streams)

# printing the available streamss
# stream_list = []
# for i in range(len(streams)):
#     # print(streams[i].resolution)
#     if streams[i].resolution == '720p':
#         print(streams[i])
#         print(f"{streams[i].title} \n")
#         stream_list.append(streams[i])

# print(stream_list)
# download the first stream from the list
# stream_list[0].download("/home/reed/Downloads/")

# print the title of video and views to check if it's correct
# print("Title: ", yt.title)
# print("Views: ", yt.views)
