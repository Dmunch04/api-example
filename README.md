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

# Stackoverflow Search API:
This is the attributes you can get from the class, StackOverflow:
- title ; The title of the post
- sender ; The author/sender of the post
- tags ; The tag(s) on the post
- url ; The URL for the post
- answers ; The amount of answers posted to the post
- answered ; A bool (True or False), of if the post/question has been answered

Example of use:
```python
import stackoverflow as so

def mySearch (searchItem):
  result = so.search("Python: How to match a string with generic date in middle")

  print(result.title)           # Prints the title of the result post
  print(result.sender)          # Prints the author's name of the result post
  print(result.tags)            # Prints the tag(s) of the result post
  print(result.url)             # Prints the URL of the result post
  print(result.answers)         # Prints the amount of answers to the result post
  print(result.answered)        # Prints a bool whether the post has been answered
```
