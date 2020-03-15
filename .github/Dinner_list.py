dinner_list = ['changsheng', 'felix', 'lei']
print(dinner_list[0].title() + ', '+ '我们一起吃个饭吧？')
print(dinner_list[1].title() + ', '+ '我们一起吃个饭吧？')
print(dinner_list[2].title() + ', '+ '我们一起吃个饭吧？')

del dinner_list[2]
print(dinner_list)

dinner_list.append('paul')
print(dinner_list)

print(dinner_list[0].title() + ', '+ '我找到一个更大的餐桌，我再叫几个人。')
print(dinner_list[1].title() + ', '+ '我找到一个更大的餐桌，我再叫几个人。')
print(dinner_list[2].title() + ', '+ '我找到一个更大的餐桌，我再叫几个人。')
dinner_list.insert(0, 'mark')
print(dinner_list)
dinner_list.insert(2, ' darren')
print(dinner_list)
dinner_list.append('yang')
print('總共邀請了' + str(len(dinner_list)) + '人')
print('Latest dinner persons list is: ' , dinner_list)
print(dinner_list[0].title(), '能一起吃个饭吗？我邀请了几个朋友.')
print(dinner_list[1].title(), '能一起吃个饭吗？我邀请了几个朋友.')
print(dinner_list[2].title(), '能一起吃个饭吗？我邀请了几个朋友.')
print(dinner_list[3].title(), '能一起吃个饭吗？我邀请了几个朋友.')
print(dinner_list[4].title(), '能一起吃个饭吗？我邀请了几个朋友.')
print(dinner_list[5].title(), '能一起吃个饭吗？我邀请了几个朋友.')
message = '由于新的餐桌无法及时送到，现在只能请两个人来吃饭了,抱歉不能邀请你'
print(message)
popped_person = dinner_list.pop()
print(popped_person + ',' + message)
popped_person = dinner_list.pop(0)
print(popped_person + ',' + message)
print(dinner_list)
popped_person = dinner_list.pop(1)
print(popped_person + ',' + message)
print(dinner_list)
popped_person = dinner_list.pop(1)
print(popped_person + ',' + message)
print(dinner_list, '你们都在我的邀请人之列，晚上见')
del dinner_list[0] 
del dinner_list[0]
print(dinner_list)
