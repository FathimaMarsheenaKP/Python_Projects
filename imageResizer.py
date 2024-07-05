from PIL import Image

def resize_Img(input_Img, output_Img, size):
    original = Image.open(input_Img)
    resized = original.resize(size)
    resized.save(output_Img)

input_Img = './red-white-cat-i-white-studio.jpg'
output_Img = 'output.jpg'

new_size = (200, 200)
resize_Img(input_Img = input_Img, output_Img= output_Img, size=new_size)


