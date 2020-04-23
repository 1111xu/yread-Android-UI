import yaml

file=open('family.yaml','r')
data=yaml.load(file)#解析文件流中的第一个YAML文档并生成相应的Python对

print(data)

print(data['name'])
print(data['age'])

print(data['spouse'])
print(data['spouse']['name'])
print(data['spouse']['age'])

print(data['children'][0]['name'])
print(data['children'][0]['age'])
print(data['children'][1]['name'])
print(data['children'][1]['age'])

data['name']='daming'#数据修改

print(data['name'])