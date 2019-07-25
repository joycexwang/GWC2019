from filters import *

def main():
    myImg = load_img("winking_cat.jpg")
    newImg = winking_cat(myImg)
    newImg.show()

main()
