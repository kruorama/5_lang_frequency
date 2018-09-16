# Frequency Analysis of Words

The script reads a text file, splits it by space and returns selected number of top frequent words.


### Description
* Accepts 2 arguments: path to text file and (optional, -c) number of top frequent words to display
* Works with any language that divides words with spacings (e.g. won't work with Chinese)
* Uses only word characters for analysis
* Will return an error if fails to read file
* Will return an error if there are no words in file
* If there are less then 10 different words in the text, will print and additional message stating the number of different words.


### How to launch

Example of script launch on Linux, Python 3.5:

```
bash

$ python lang_frequency.py -f <filepath>
# possibly requires call of python3 executive instead of just python
Top 10 most frequent words in file:
the: 192
of: 112
i: 91
and: 62
my: 61
in: 50
a: 49
to: 47
had: 40
was: 39
```


### Project goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
