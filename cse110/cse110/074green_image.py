from PIL import Image
import random
print("The library is loaded correctly")
#The command: python -m pip install pillow --user actually works for python3


image_original = Image.open("./cse110_images/beach.jpg")

image_original.show()

pixels_original = image_original.load()


#Find out how many pixels the image has on its width
pixels_width = 0
while True:
    try:
        pixels_original[0, pixels_width]
        pixels_width += 1
    except:
        break

#Find out how many pixels the image has on its height
pixels_height = 0
while True:
    try:
        pixels_original[pixels_height, 0]
        pixels_height += 1
    except:
        break

#Displaying pixels from an image

#Creating new image
new_image = Image.new("RGB", image_original.size)
pixels_new = new_image.load()

i=0
j=0
pixels_looped = 0
print("Printing 5 pixels as requested")
while i <= pixels_width:
    while j <= pixels_height:
        try:
            r, g, b = pixels_original[j, i]
            if i == 0 and j < 5:
                print(f"{r}, {g}, {b}")
            j+= 1
            pixels_looped += 1
            
            #I modify both the red and the blue from each pixel.
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            pixels_new[j, i] = (r, g, b)
        except: 
            break
    j = 0
    i += 1
assert pixels_looped == image_original.size[0]*image_original.size[1], "programis not printing correct number of pixels :["

new_image.show()
new_image.save("./my_random_image.jpg")

#Ask for the images
bk_image = input("What is the background image? ")
gr_image = input("What is the green image? ")

#Load the green and background image
green_image_original = Image.open(f"./cse110_images/{gr_image}")
green_pixels_image = green_image_original.load()

background_original = Image.open(f"./cse110_images/{bk_image}")
background_pixels = background_original.load()

height_green, width_green = green_image_original.size
#width_green, height_green = green_image_original.size
width_background, height_background = background_original.size

#Check the value of the [0,0] from the green image to use it as a default for rgb.
red_default,green_default,blue_default = green_pixels_image[0,0]

new_green = Image.new("RGB", green_image_original.size)
pixels = new_green.load()

#Make the changes in the green image to have the rgb from the background at specific pixels
i=0
j=0
while i <= width_green:
    while j <= height_green:
        try:
            r, g, b = green_pixels_image[j, i]
            if g >= green_default and b <= blue_default and r<=red_default: 
              green_pixels_image[j,i] = background_pixels[j,i]  
            pixels[j,i] = green_pixels_image[j,i]
            j+= 1
        except: 
            break
    j = 0
    i += 1
    
#Show the image
new_green.show()
#Save the image
new_green.save("./new_backgroung.jpg")
