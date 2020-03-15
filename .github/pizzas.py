pizzas = ['土豆牛肉披薩','小番茄里脊肉披薩','榴蓮風味披薩']
friend_pizzas = pizzas[:]
pizzas.append('牛排披萨')
friend_pizzas.append('酸黄瓜披萨')
for pizza in pizzas:
    print('我喜歡' + pizza +'.')
print('我就是喜歡吃披薩，哈哈。\n')
for friend_pizza in friend_pizzas:
    print('我朋友喜欢' + friend_pizza + '.')
print('我朋友也喜欢吃披萨，所以我们是朋友')

