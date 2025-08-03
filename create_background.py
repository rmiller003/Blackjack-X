from PIL import Image, ImageDraw

def create_background_image():
    width = 1024
    height = 768
    image = Image.new('RGB', (width, height), 'darkgreen')
    draw = ImageDraw.Draw(image)
    image.save('background/casino.png')

if __name__ == '__main__':
    create_background_image()
