import PIL.Image
img = PIL.Image.open('img.jpg')
exif_data = img._getexif()

#print output in dictionary 
from PIL.ExifTags import TAGS
exif = {
    TAGS[k]: v
    for k, v in img._getexif().items()
    if k in TAGS
}
#print data to screen. 
print (exif)
