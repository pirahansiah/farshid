from PIL import Image

def split_image(image_path, output_directory, tile_size):
    image = Image.open(image_path)
    width, height = image.size

    num_tiles = width // tile_size

    for y in range(num_tiles):
        for x in range(num_tiles):
            left = x * tile_size
            upper = y * tile_size
            right = left + tile_size
            lower = upper + tile_size

            tile = image.crop((left, upper, right, lower))
            tile.save(f'{output_directory}/tile_{x}_{y}.png')

# Example usage:
input_square_image_path = '/Users/farshid/Desktop/Llama-v2.png'
output_directory = 'tiles'
tile_size = 1024
split_image(input_square_image_path, output_directory, tile_size)