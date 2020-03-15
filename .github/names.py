names = ['mark', 'kevin', 'paul', 'frank', 'fan', 'sparky', 'jimmy', 'cliff']
print(names[0].title(),names[1].title(),names[2].title()) #想让每一个名字都分行显示，但是不知道用什么
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(names[5].title())
message = 'Hello,' + ' '+ names[0].title() + ' ' + 'How are you?'
print(message)
names[0] = 'vicky'
print(names)
names.insert(1, 'heliu')
print(names)
del names[1]
print(names)