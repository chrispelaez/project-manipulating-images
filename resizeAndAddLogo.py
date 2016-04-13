import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open( LOGO_FILENAME )
logoWidth, logoHeight = logoIm.size


os.makedirs('withLogo', exist_ok=True)
os.chdir('./originals')
#TODO: Loop over all files in the working directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
    or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

#TODO: Check if file image needs to be resized
#TODO: Calculate the new width and height to resize to.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

#TODO: Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

#TODO: Save changes.
    im.save(os.path.join('../withLogo', filename))#TODO: Loop over all files in the working directory



#TODO: Loop over all files in the working directory
#TODO: Check if file image needs to be
#TODO: Calculate the new width and height to resize to.
#TODO: Add the logo.
#TODO: Save changes.
