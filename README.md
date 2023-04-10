# automatic_manga_cards
Makes prebuilt japanese manga anki decks. 

Uses kumiko for slicing images and mokuro for getting sentences.

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
+ images for pasting into .collection-media

