import os
import urllib
import json

URL_SEARCH = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='

encoded = urllib.quote(ex)

rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encoded).read()

jsonData = json.loads(rawData)
results = jsonData['responseData']['results']

class GoogleSearch (object):
  def __init__ (self, title, description, url):
    self.title = title
    self.description = description
    self.url = url
    
  def __str__ (self):
    return '%s: %s (%d)' % (self.title, self.description[:50], '...' if len(self.definition) > 50 else '', self.url)
    
def get_search_json (url):
  raw = urllib.urlopen(url)
  
  json = json.loads(raw)
  
  results = json
  
  return results
  
def parse_search_json (json):
  results = []

  if json is None or any (e in json for e in ('error', 'errors')):
    raise ValueException('Invalid Search')
    
  for result in json:
    search = GoogleSearch(result['titleNoFormatting'], result['content'], result['url'])
    
    results.append(search)
    
  return results
    
def search (searchItem):
  json = get_search_json(URL_SEARCH + urllib.quite(url))
  return parse_search_json(json)
