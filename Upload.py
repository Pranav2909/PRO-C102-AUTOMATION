import PIL
from PIL import ImageGrab

def Screenshot():
 ss_region = (0, 0, 1920, 1080)
 ss_img = ImageGrab.grab(ss_region)
 ss_img.save(A)
A = input("Enter the name for the screenshot with extension :- ")
Screenshot()
print("Your image " + A + " is saved !!!!")