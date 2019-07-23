# Rename this file to be "filters.py"
# Add commands to import modules here.

from PIL import Image
winking_cat = Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(winking_cat):
    im = Image.open(winking_cat)
    return im
# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(winking_cat):
    winking_cat.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(winkng_cat, kitty):
    winking_cat.save(kitty)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.

def obamicon(winking_cat):
winking_cat.getpixel
    lightBlue = (112,150,158)
    yellow = (252,227,166)
    red = (217, 26, 33)

im = load_img("winking_cat.jpg")
show_img(im)
obamicon(winking_cat)
