import json
import os
import csv
import shutil

def main(manga_name):

    # mokuro OCR directory with .json files
    input_path = fr".\output\_ocr\{manga_name}"

    json_files = [f for f in os.listdir(input_path) if f.endswith('.json')]
    json_files = sorted(json_files)

    print( f"Number of .json: {len(json_files)}")

    # Delete content within files
    with open(input_path + f'\KanjiSent.txt', 'w', encoding="utf-8") as f:
        f.write("")
    with open(input_path + f'\Pictures.txt', 'w', encoding="utf-8") as f:
        f.write("")

    for filename in json_files:

        with open(os.path.join(input_path, filename), encoding="utf-8") as f:
            data = json.load(f)
            blocks = data["blocks"]

            # Go through each manga bubble
            for block in blocks:
                lines = block["lines"]
                result = ' '.join(lines)
                

                # Export the data to a text file
                kanji_sent = input_path + f'\KanjiSent.txt'
                with open(kanji_sent, 'a', encoding="utf-8") as f:
                    f.write(result + "\n")

                if len(blocks) !=0:

                    # Export filename to imagelist file
                    base_name, extension = os.path.splitext(filename)
                    pictures = input_path + f'\Pictures.txt'
                    with open(pictures, 'a', encoding="utf-8") as f:
                        f.write(base_name + ".png \n")

    # Make .csv
    print("Making .csv...")
    with open(kanji_sent, 'r', encoding="utf-8") as f:
        kanji_list = f.readlines()
    kanji_list = [line.strip() for line in kanji_list]

    with open(pictures, 'r', encoding="utf-8") as f:
        picture_list = f.readlines()
    picture_list = ['<img src="{}">'.format(picture.strip()) for picture in picture_list]


    # Write the contents of both files into a CSV file with two columns
    with open(input_path + f'..\..\..\{manga_name}.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['KanjiSent', 'Picture'])
        for kanji, picture in zip(kanji_list, picture_list):
            writer.writerow([kanji, picture])
    os.remove(kanji_sent)
    os.remove(pictures)
    os.remove("./output/" + manga_name+".html")
    shutil.rmtree("./output/_ocr")
    print("Done!")
