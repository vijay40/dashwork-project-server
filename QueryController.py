import urllib.request


class QueryController:
  items = [] 

  def __init__(self) -> None:
    # load the data one time when the server starts up. Ideally this data should be in elastic search for efficient query. 
    req = urllib.request.Request("http://www.cim.mcgill.ca/~dudek/206/Logs/AOL-user-ct-collection/user-ct-test-collection-01.txt")
    res = urllib.request.urlopen(req)
    raw_lines = res.readlines()
    for raw_line in raw_lines:
      line = raw_line.decode()
      self.items.append(line.split('\t')[1])

  def getMatchingQueries(self, query):
    res = set()
    for item in self.items:
      if item.startswith(query):
        res.add(item)
        if(len(res) > 9):
          break
    print('res: ', res)
    return res
