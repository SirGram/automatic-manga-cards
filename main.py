import json
import sys
from PIL import Image
import os
import subprocess
import get_csv
import shutil

# Folder config
manga_name = ""
input_folder = ""
output_folder = ""
kumiko_json = ""
kumiko_folder =""
mokuro_path = ""
num_screenshots=0

is_fullpage = False

def get_folder(manga_name):
    global input_folder
    global output_folder
    global kumiko_json
    global kumiko_folder
    global mokuro_path
    input_folder = f'./input/{manga_name}/'
    output_folder = f'./output/{manga_name}/'
    kumiko_json = './output.json'
    kumiko_folder = "./kumiko"
    mokuro_path = f".output/_ocr/{manga_name}/"

def compress():
    print("Compressing images...")
    num_files = 0

    for filename in os.listdir(output_folder):
        if filename.endswith(".png"):
            filepath = os.path.join(output_folder, filename)
            with Image.open(filepath) as img:
                if img.mode != "L":
                    img = img.convert("L")
                img.save(filepath, optimize=True)
            num_files += 1
            print(f"\rProcessed {num_files} / {num_screenshots}", end="")

if __name__ == '__main__':

    # Get manga name
    if len(sys.argv) > 1:
        manga_name = sys.argv[1]
        # Full page/vignette
        if "--fullpage" in sys.argv:
            is_fullpage = True
    get_folder(manga_name)

    if is_fullpage == False:

        with open(kumiko_json, 'w') as f:
            f.write("")
        print("Going through kumiko...")
        os.chdir(kumiko_folder)
        command = ["py","kumiko", "-i", f".{input_folder}","-o",f".{kumiko_json}", "--rtl"]
        subprocess.run(command, check=True)
        os.chdir("../")

        print("Making screenshots...")
        # Load the JSON file
        with open(kumiko_json, 'r') as f:
            data = json.load(f)

        for image in data:

            # Open the image file
            filename = image['filename']

            # Extract the screenshot coordinates
            panels = image['panels']

            # Screenshot per panel
            for panel in panels:

                img = Image.open(input_folder + filename)

                x, y, w, h = panels[panels.index(panel)]

                screenshot = img.crop((x, y, x + w, y + h))

                # Create output folder
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                new_filename = filename.replace('.jpg', '').replace('.png', '')
                screenshot.save(output_folder + manga_name + new_filename + '_'+str(image['panels'].index(panel)) + '.png')
                num_screenshots+=1

            print(f"\r{str(data.index(image))}/{str(len(data))} pages. {num_screenshots} screenshots. ", end="")
        print('Saved in ' + output_folder+'. Saved '+ str(num_screenshots) +' images.')
    else:
        print("Copying files to output...")
        file_list = os.listdir(input_folder)

        for file_name in file_list:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            source_file = os.path.join(input_folder, file_name)
            destination_file = os.path.join(output_folder, file_name)
            shutil.copy(source_file, destination_file)

    compress()

    # Execute mokuro
    print("\nExecuting mokuro...")
    command2 = ["mokuro", output_folder, "--disable_confirmation"]
    subprocess.run(command2, check=True)

    #Make .csv
    get_csv.main(manga_name)
