import cv2

source = "sunny.jpeg"
destination = "newImage.png"
# percent by which to resize
scale_percent = 400

# read the image
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# calculate the new dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize the image
output = cv2.resize(src, dsize)

# write the output image to file
cv2.imwrite(destination, output)
