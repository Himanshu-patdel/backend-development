import uuid
from PIL import Image,ImageChops

# def trim_white_space(input_image_path, output_image_path):
#     img = Image.open(input_image_path)
#     img = img.convert("RGB")

    
#     bg_color = (255, 255, 255)  # RGB for white
    
#     # Get bounding box of non-white areas
#     bg = Image.new("RGB", img.size, bg_color)
#     diff = ImageChops.difference(img, bg)
#     bbox = diff.getbbox()

#     if bbox:
#         trimmed_img = img.crop(bbox)
#         trimmed_img.save(output_image_path)

 
# trim_white_space("output_image_ans.png", "output_image_ans1.png")

def trim_white_space(input_image_path, padding=150):
    img = Image.open(input_image_path)
    img = img.convert("RGB")

    bg_color = (255, 255, 255)   
 
    bg = Image.new("RGB", img.size, bg_color)
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    print(bbox)
    if bbox:
        #adding padding
        left = max(0, bbox[0] - padding)
        upper = max(0, bbox[1] - padding)
        right = min(img.size[0], bbox[2] + padding)
        lower = min(img.size[1], bbox[3] + padding)
        
        # Crop the image with the adjusted bounding box
        trimmed_img = img.crop((left, upper, right, lower))
        image_filename = f"temp_{uuid.uuid4().hex[:5]}_{padding}.png"
        print(image_filename)
        trimmed_img.save(image_filename)
# for i in range(5): 
trim_white_space("img2.png")

 

# def trim_white_space(input_image_path, output_image_path, padding=0):
#     try:
#         # Open the image
#         img = Image.open(input_image_path)
#         img = img.convert("RGB")
#     except FileNotFoundError:
#         print(f"Error: File '{input_image_path}' not found.")
#         return
#     except IOError:
#         print(f"Error: Cannot open or read the image '{input_image_path}'.")
#         return

#     bg_color = (255, 255, 255)
#     bg = Image.new("RGB", img.size, bg_color)
#     diff = ImageChops.difference(img, bg)
#     bbox = diff.getbbox()
#     print(bbox)
#     if bbox:
#         # Add padding and ensure the new bounding box does not exceed image dimensions
#         left = max(0, bbox[0] - padding)
#         upper = max(0, bbox[1] - padding)
#         right = min(img.size[0], bbox[2] + padding)
#         lower = min(img.size[1], bbox[3] + padding)
        
#         # Crop the image with the adjusted bounding box
#         trimmed_img = img.crop((left, upper, right, lower))
#     else:
#         # No whitespace found, use the original image but add padding
#         trimmed_img = img

#     # Create a new image with padding
#     new_width = trimmed_img.size[0] + 2 * padding
#     new_height = trimmed_img.size[1] + 2 * padding
#     padded_img = Image.new("RGB", (new_width, new_height), bg_color)
#     padded_img.paste(trimmed_img, (padding, padding))
#     padded_img.save(output_image_path)
  

# trim_white_space("img1.png", "output_image134.png")
