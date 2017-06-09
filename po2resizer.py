from __future__ import print_function
import sys
import warnings
from PIL import Image

sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]


def get_closest(y):
    return min(sizes, key=lambda x: abs(x - y))


def po2(image, threshold=0.25):
    width, height = image.size
    largest_dim = max(width, height)
    new_dim = max(get_closest(width), get_closest(height))

    if new_dim < largest_dim:
        if (largest_dim - new_dim) > int(new_dim * threshold):
            new_dim = sizes[sizes.index(new_dim) + 1]
            return image.resize((new_dim, new_dim), resample=Image.BICUBIC)
        else:
            return image.resize((new_dim, new_dim), resample=Image.LANCZOS)
    else:
        return image.resize((new_dim, new_dim), resample=Image.BICUBIC)


def main():
    threshold = 0.25
    try:
        with open('config.txt', 'r') as config:  # if in same directory
            for line in config:
                if "THRESHOLD=" in line.upper():
                    try:
                        threshold = float(line.upper().replace('THRESHOLD=', ''))
                    except ValueError:
                        print('Invalid threshold in config.txt')
    except IOError:
        print("Cannot open config.txt")

    try:
        warnings.simplefilter('ignore', Image.DecompressionBombWarning)
        if len(sys.argv) > 1:
            try:
                im = Image.open(sys.argv[1])
                po2(im, threshold).save(sys.argv[1], im.format.lower())
            except IOError:
                print("IO ERROR: Is file an image? -> ", sys.argv[1])
    except MemoryError:
        print("OOM")

main()
