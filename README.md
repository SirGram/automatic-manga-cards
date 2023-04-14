# automatic_manga_cards
Makes prebuilt japanese manga anki decks. 
Uses kumiko for slicing images and mokuro for getting sentences.

<kbd><img height = "400" src = "https://user-images.githubusercontent.com/119138378/231021244-6ca0f7ee-9bda-4505-ba5c-03e40d77a803.png"><img height = "400" src = "https://user-images.githubusercontent.com/119138378/231022185-5df3cc14-1bfb-4f76-a693-6878496f7842.png"></kbd>

Generated card with custom template using morphman plus furigana, translate addons.

Tutorial:

{% include youtube.html id="l906iH0R_cM" %}

# Installation
You need Python 3.6, 3.7, 3.8 or 3.9.
```commandline
pip install mokuro
```

# How to use

Make folder inside /input with .jpg manga files.
>input/Oyasumi/images

Run script
```commandline 
python main.py <manga_name> 
```
>*e.g. python main.py Oyasumi*

```commandline
--fullpage - no vignettes
```
Output files:
+ .csv for importing into anki
+ images for pasting into /collection.media

