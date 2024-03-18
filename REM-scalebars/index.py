import os
from PIL import Image, ImageDraw

# Specify the directory path
#folder_path = ''

folder_path = 'e:\Dokumente\Ausbildung\\03-Promotion\Messdaten-automatisieren\ECETO_11\\test-ordner'
new_folder_path = folder_path + '\scalebars'

#create target directory to store images with scalebars
os.makedirs(new_folder_path, exist_ok=True)

def add_scale_bar(image_path, output_path, bar_length_px, scale_label, my_font_size = 40):
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Define scale bar position and size
    image_width, image_height = image.size
    bar_height_px = 20  # Height of the scale bar in pixels
    bar_start = (image_width - bar_length_px - 30, image_height - bar_height_px - 75)  # Bottom-right corner
    bar_end = (image_width - 38, image_height - 75)
    box_height_px = 70 # Height of surrounding box in pixels
    box_start = (image_width - bar_length_px - 60, image_height - box_height_px - 38)  # Bottom-right corner
    box_end = (image_width - 10, image_height - 10)

    # Draw the surrounding rectangle
    draw.rectangle([box_start, box_end], fill="black")

    # Draw the scale bar
    draw.rectangle([bar_start, bar_end], fill="white")

    # Get xy-parameters to center the label
    bar_middle = bar_start[0] - (bar_start[0] - bar_end[0]) / 2
    text_height = bar_end[1] + 20

    # Add centered scale label
    draw.text((bar_middle, text_height), scale_label, fill="white", font_size = my_font_size, anchor = "mt", stroke_width = 1)

    # Save or display the modified image
    image.save(output_path)
    image.show()


# List all files in the directory
for filename in os.listdir(folder_path):
    # Construct full file path
    file_path = os.path.join(folder_path, filename)
    file_path_save = os.path.join(folder_path, 'scalebar', filename)
    if os.path.isfile(file_path):  # Make sure it's a file, not a directory
        add_scale_bar(
            image_path = file_path,
            output_path = file_path_save, 
            bar_length_px = 100,
            scale_label = '100nm'
        )

