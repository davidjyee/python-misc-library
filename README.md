# python-misc-library
Library of all my miscellaneous python scripts

## imageResize.py
Resizes all images in a directory and subdirectories and copies into a new directory with the subdirectory tree intact. Only resizes into a square shape, and keeps images their aspect ratio (cuts off parts of the image that isn't in a square).

### Steps to use
1. Ensure that you have Python 3.10.0 installed (only tested with that version).
2. Ensure that you have Pillow installed, if not use the command below:
```
pip install Pillow
```
3. Ensure that you have tqdm installed, if not use the command below:
```
pip install tqdm
```
4. Run imageResize.py
