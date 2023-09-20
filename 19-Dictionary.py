# Dictionary = A changeable, unordered collection of unique key: value pairs
#               It's fast because they use hashing which allow use to access value quickly
capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

print(capitals['India'])

print(capitals['Germany'])
print(capitals.get('Germany'))

# Print Keys only
print(capitals.keys())
# Print Values only
print(capitals.values())
# Print Items with key and values
print(capitals.items())

for key,value in capitals.items():
    print(key,value)

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})

capitals.pop('China')
capitals.clear()
