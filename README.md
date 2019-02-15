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
