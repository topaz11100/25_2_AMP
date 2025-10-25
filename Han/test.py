import numpy as np
import cv2 as cv
import argparse

cli = argparse.ArgumentParser()
cli.add_argument("img_path")
cli.add_argument("animal")
args = cli.parse_args()

def dog_F(src):
    return cv.bitwise_not(src)

def cat_F(src):
    return src

animal = {"dog": dog_F,
          "cat": cat_F}

def main():
    if args.animal not in animal:
        print("No Filter")
        return

    try:
        src = cv.imread(args.img_path, cv.IMREAD_COLOR)
        
    except:
        print("Img File Error")
        return
    
    cv.imshow("src", src)
    cv.imshow(args.animal, animal[args.animal](src))

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()