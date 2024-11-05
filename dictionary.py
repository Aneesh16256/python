d={'name':'sankary',
   'age':21,
   'qualification':'psychology'}
print(d.keys()) #prints the key only=(['name', 'age', 'qualification'])
print(d.values()) #prints the values =(['sankary', 27, 'psychology'])
print(d.items()) #dict_items([('name', 'sankary'), ('age', 27), ('qualification', 'psychology')])
print(d['age']) # 21
print(d.get('name')) #sankary
print(d['salary']) #error
print(('salary',25000))