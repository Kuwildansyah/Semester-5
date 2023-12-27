from PIL import Image

def load_image(path):
    return Image.open(path)

def convert_to_rgb(image):
    return image.convert("RGB")

def resize_image(image, width, height):
    return image.resize((width, height))

def calculate_center(background_image, overlay_image):
    x_center = (background_image.width - overlay_image.width) // 2
    y_center = (background_image.height - overlay_image.height) // 2
    return x_center, y_center

def paste_image(background_image, overlay_image, coordinates):
    background_image.paste(overlay_image, coordinates)
    return background_image

def save_image(image, path):
    image.save(path)

def show_image(image):
    image.show()

def main():
    background_image = load_image('D:\Design\Game\hasil\livvi.png')
    overlay_image = load_image('D:\Design\Game\hasil\kokom.png')
    overlay_image = convert_to_rgb(overlay_image)
    overlay_image = resize_image(overlay_image, 1000, 2000)
    coordinates = calculate_center(background_image, overlay_image)
    background_image = paste_image(background_image, overlay_image, coordinates)
    save_image(background_image, "hasil_edit.png")
    show_image(background_image)

main()