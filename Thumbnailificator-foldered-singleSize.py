#!/usr/bin/python

from PIL import Image
from glob import glob
import os.path
import os


# Define desired sizes
listSizes = [16, 24, 32, 48, 64, 96, 128, 256]

os.chdir('./input')
listIcons = glob(r'**/*.png')
outputPath = '../output'


def main():
    for iconPath in listIcons:
        # splitting input path
        iconType, iconName = iconPath.split('/')
        for sizeItem in listSizes:
            # concatenating
            dirNameFormated = f'{sizeItem}'
            # output format
            outputPathFormated = f'./{outputPath}/{dirNameFormated}/{iconType}/'
            # making directories
            os.makedirs(os.path.dirname(outputPathFormated), exist_ok=True)
            # image ratio concatenation
            sizeFormated = (sizeItem)
            # open & resize & save to the appropriate directory
            im = Image.open(iconPath)
            im.thumbnail(sizeFormated, Image.ANTIALIAS)
            im.save(f'./{outputPathFormated}/{iconName}')


if __name__ == '__main__':
    main()
