from PIL import Image, ImageEnhance

def load_image(path):
    return Image.open(path)

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def save_image(image, path):
    image.save(path)

def show_image(image):
    image.show()

def main():
    gambar = load_image('D:\Design\Game\hasil\mamah raiden.png')
    gambar = adjust_brightness(gambar, 1.5)
    gambar = adjust_contrast(gambar, 1.2)
    save_image(gambar, "brightness_contrast_image.png")
    show_image(gambar)

main()