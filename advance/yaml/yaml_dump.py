import yaml

slogan=['welcome','to','51zxw']
website={'url':'www.51zxw.net'}

print(slogan)
print(website)

print(yaml.dump(slogan))#将python数据转化为yaml数据类型
print(yaml.dump(website))