import re

textStr = "From john.doe@ab.etc Thu Jun 15 02:04:09 2010"

# Extract 'ab.etc'
result = re.findall(r'.*@(.*?) ', textStr)
print(result)

# Extract 'john.doe@ab.etc'
result = re.findall(r'(\S*@.*?) ', textStr)
print(result)

# Extract 'From: Using the :'
x = 'From: Using the : character'
result = re.findall(r'(\S*.*?:)', x)
print(result)

# Extract {'Ann': '99', 'Maria': '95', 'David': '84', 'Jose': '21'}
mathScores = '''
Ann got 99 and Maria got 95,
David got 84 and Jose got 21
'''

keys = re.findall(r'([A-Z]\w+)', mathScores)
print(keys)
values = re.findall(r'(\d+)', mathScores)
print(values)

dictionary = dict(zip(keys, values))
print(dictionary)
