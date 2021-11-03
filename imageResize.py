from PIL import Image
from pathlib import Path
from pathlib import PurePath
from tqdm import tqdm

Image.init()

imageDir = input('Directory you wish to resize: ')
outputDir = input('Directory you wish to copy to: ')
width = input('Size of square you\'d like to resize to: ')
height = width
extensionType = input('Output image extension: ')

dirPath = Path(imageDir)
imgPaths = []
for ext in Image.EXTENSION.keys():
  glob = '**/*' + ext
  imgPaths.extend(dirPath.glob(glob))

print('Found ' + str(len(imgPaths)) + ' images in directory.')

print('Resizing images...')
pbar = tqdm(imgPaths)
for imgPath in pbar:
  with Image.open(imgPath) as img:
    #Keep aspect ratio
    size = min(img.width, img.height)
    offsetX = 0
    offsetY = 0
    if(img.width > img.height):
      offsetX = (img.width - size) / 2
    elif (img.width < img.height):
      offsetY = (img.height - size) / 2

    #Resize image
    imgResized = img.resize((int(width), int(height)), box=(offsetX, offsetY, offsetX + size, offsetY + size))
  
    #Figure out save path and create directory
    saveDirPath = Path(PurePath(outputDir) / PurePath(PurePath(imgPath).parent).relative_to(dirPath))
    saveDirPath.mkdir(parents=True, exist_ok=True)

    #Save image
    savePath = saveDirPath / PurePath(imgPath).name
    resSavePath = Path(savePath.with_suffix(extensionType))
    imgResized.save(resSavePath)
