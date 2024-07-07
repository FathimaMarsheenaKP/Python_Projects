from PIL import Image

def resize_Img(input_Img, output_Img, size):
    original = Image.open(input_Img)
    resized = original.resize(size)
    resized.save(output_Img)

input_Img = r"C:\Users\fathi\OneDrive\Desktop\Coding\Python\Projects\static\red-white-cat-i-white-studio.jpg"
output_Img = r"C:\Users\fathi\OneDrive\Desktop\Coding\Python\Projects\static\output.jpg"

new_size = (500, 500)
resize_Img(input_Img=input_Img, output_Img=output_Img, size=new_size)
