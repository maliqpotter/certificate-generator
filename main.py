from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# File paths
template_path = "templates/sertifikat-peserta.png"
csv_path = "templates/nama-peserta.csv"
output_folder = "output"

# Try reading the CSV with semicolon (;) as a separator
data = pd.read_csv(csv_path, sep=";")

# Font configuration
font_path = "templates/MiriamLibre-SemiBold.ttf"
font_size = 85

# Open the certificate template
template = Image.open(template_path)
draw = ImageDraw.Draw(template)

# Font configuration
font = ImageFont.truetype(font_path, font_size)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get the size of the template image
image_width, image_height = template.size

# Generate certificates
for index, row in data.iterrows():
    # Make sure the column name is "name"
    name = row["nama"]
    
    # Reload the template every iteration
    cert = template.copy()
    draw = ImageDraw.Draw(cert)
    
    # Use textbbox to get the text bounding box
    bbox = draw.textbbox((0, 0), name, font=font)
    text_width = bbox[2] - bbox[0]  # Text width
    text_height = bbox[3] - bbox[1]  # Text height

    # Horizontal position in the center
    text_x = (image_width - text_width) / 2
    # Vertical position (adjust as needed)
    text_y = 500 + 40

    # Write the participant's name with the calculated position
    draw.text((text_x, text_y), name, fill="black", font=font)
    
    # Save the certificate
    output_path = os.path.join(output_folder, f"Sertifikat_{name}.png")
    cert.save(output_path)

print("Certificates have been successfully created!")
