from PIL import Image, ImageDraw, ImageFont

def calculate_text_size(text, font_path, target_width):
    font_size = 50
    height = 500

    img = Image.new("RGB", (target_width, height), color="white")
    draw = ImageDraw.Draw(img)

    def text_fits(font_size):
        font = ImageFont.truetype(font_path, font_size)
        text_width, _ = draw.textsize(text, font=font)
        return text_width <= target_width

    min_size, max_size = 1, 500
    while min_size <= max_size:
        mid_size = (min_size + max_size) // 2
        if text_fits(mid_size):
            font_size = mid_size
            min_size = mid_size + 1
        else:
            max_size = mid_size - 1

    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = font.getsize(text)

    return font_size, text_height
