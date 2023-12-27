from PIL import Image, ImageDraw, ImageFont

# TODO 0: Import library lain yang dibutuhkan
# No additional libraries mentioned in the comment.

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('D:\Design\Game\hasil\livvi.png')

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
direktoriFont = 'C:/Windows/Fonts/Arial.ttf'  # Adjust the font directory accordingly
font_size = 20
font = ImageFont.truetype(direktoriFont, font_size)
text = "Kukuh Wildan Yuliansyah 202110370311194"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
text_x = (gambarBW.width - text_width) // 2
text_y = 20
draw.text((text_x, text_y), text, font=font, fill='white')   # Adjust fill color if needed

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('result_image.jpg')

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()