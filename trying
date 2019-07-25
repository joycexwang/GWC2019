# Rename this file to be "filters.py"
# Add commands to import modules here.

from PIL import Image

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
    darkBlue = (0,51,76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    new_img = []
    pixels = list(winking_cat.getdata())

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_img.append(darkBlue)
        elif intensity >= 182 and intensity <364:
            new_img.append(red)
        elif intensity >= 364 and intensity < 546:
            new_img.append(lightBlue)
        elif intensity >=546:
            new_img.append(yellow)

    newim = Image.new("RGB", (500,427))
    newim.putdata(new_img)
    newim.show()

    winking_cat= Image.open("winking_cat.jpg")


im = load_img("winking_cat.jpg")
show_img(im)

newpic = obamicon(im)
