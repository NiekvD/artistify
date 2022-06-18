from PIL import Image
img = Image.new('RGB', (500, 500), 'cyan')
img.save('main.png')
img.show()