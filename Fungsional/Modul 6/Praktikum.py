from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

def load_image(path):
    return Image.open(path)

def convert_to_grayscale(image):
    if image.mode == "L":
        return image
    else:
        return image.convert("LA").convert("RGB")

def rotate_image(image, degrees):
    return image.rotate(degrees)

def blur_image(image):
    return image.filter(ImageFilter.BLUR)

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def calculate_center(background_image, overlay_image):
    x_center = (background_image.width - overlay_image.width) 
    y_center = (background_image.height - overlay_image.height) 
    return x_center, y_center

def paste_image(background_image, overlay_image, coordinates):
    background_image.paste(overlay_image, coordinates)
    return background_image

def add_text(image, text, font_path='D:\Font\Be Vietnam\BeVietnam-ExtraBold.ttf', size=24, fill='white'):
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype(font_path, size)
    except IOError:
        font = ImageFont.load_default() 
    
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    
    text_x = (image.width - text_width) 
    text_y = (image.height - text_height) 
    draw.text((100, 100), text, font=font, fill="blue")
    return image

def save_image(image, path):
    image.save(path)

def show_image(image):
    image.show()

def main():
    background_image = load_image('D:\Coding\Semester_5\Semester-5\Fungsional\Modul 6\download.jpeg')
    overlay_image = load_image('D:\Coding\Semester_5\Semester-5\Fungsional\Modul 6\download (1).jpeg')
    # Remove the conversion to grayscale 
    background_image = convert_to_grayscale(background_image)
    background_image = rotate_image(background_image, 90)
    background_image = blur_image(background_image)
    overlay_image = adjust_brightness(overlay_image, 1.9)
    overlay_image = adjust_contrast(overlay_image, 1.5)
    coordinates = calculate_center(background_image, overlay_image)
    background_image = paste_image(background_image, overlay_image, coordinates)
    background_image = add_text(background_image, "Informatika JOSSS!")
    save_image(background_image, "peraktikum enem.jpg")
    show_image(background_image)

main()
