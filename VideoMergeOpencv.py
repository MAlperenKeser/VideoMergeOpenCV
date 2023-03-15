import cv2

# list of videos

print("enter file count")
size = input()
sizeint = int(size)

print("enter file names in order you want to merge")
strs = [input() for i in range(sizeint)]

# Create a new video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter("output.mp4", fourcc, 60, (1920,1080))

# Concatenate to the new video
for i in strs:
    videocap = cv2.VideoCapture(i)
    while videocap.isOpened():
        cap, frame = videocap.read()
        if cap:
            video.write(frame)
        else:
            break


video.release()
