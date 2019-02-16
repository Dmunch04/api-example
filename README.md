# Example of how to make your own API

# About
I made this to help others start making their own API's. The `example.py` is the most basic one. It should be really easy to work on from there. If you need any help, feel free to contact me.

# Integration:
Wanna test this out yourself? Just add this to your `requirements.txt` (https://pip.pypa.io/en/stable/user_guide/#requirements-files)
```
git://github.com/Dmunch04/api-example.git
```
Does it not work? Try this:
```
git+git://github.com/Dmunch04/api-example.git
```

# Example:
Example of how to use the current example API:
```python
import example as ex

def yourCommand (num):
  result = ex.get(num)
  
  print(result.obj1)
  print(result.obj2)
  print(result.obj3)
  print(result.obj4)
```

# Google Search API:
This is the attributes you can get from the class, GoogleSearch:
- title ; The title of the website/link
- description ; The content of the website. We limit it to be the little description we see on the website block on Google
- url ; The URL for the website

Example of use:
```python
import google as google

def mySearch (searchItem):
  result = google.search(search)[0]
  
  print(result.title)           # Prints the title of the result website
  print(result.description)     # Prints the description of the result website
  print(result.url)             # Prints the URL of the result website
```
