from PIL import Image

def make_square_image(image_path, output_path):
    image = Image.open(image_path)
    width, height = image.size
    max_dimension = max(width, height)
    square_size=max_dimension

    new_image = Image.new('RGB', (max_dimension, max_dimension), color=(255, 255, 255))
    offset = ((max_dimension - width) // 2, (max_dimension - height) // 2)
    new_image.paste(image, offset)

    new_image.thumbnail((square_size, square_size))
    new_image.save(output_path)

# Example usage:
input_image_path = '/Users/farshid/Desktop/OpenVINO.png'
output_square_image_path = 'output_square_image.jpg'
make_square_image(input_image_path, output_square_image_path )