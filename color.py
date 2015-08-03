from PIL import Image, ImageDraw
import StringIO


def image(color):
    img = Image.new('RGB', (120, 120))
    draw = ImageDraw.Draw(img)

    try:
        draw.rectangle((0, 0, 120, 120), fill=color)
    except ValueError:
        return

    output = StringIO.StringIO()

    img.save(output, 'JPEG')

    return output.getvalue()
