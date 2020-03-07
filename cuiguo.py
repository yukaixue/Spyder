from sys import argv

script, user_name = argv
prompt = '> '

print(f"你好 {user_name} , 我是 {script} script.身无彩凤双飞翼，心有灵犀一点通，那就叫彩凤吧")
print("你今年多大了？请在下面输入！")
age = input(prompt)
print(f"你真的有{age}？")

print("果郡王娇嫩，你如今几岁了？")
print("翠果！.")
print(f"给我打烂 {user_name}的嘴！")

print(f"Do u like me?")
likes = input(prompt)

print(f"你在干嘛 {user_name}?")
doing = input(prompt)

print("你最喜欢甄嬛传里哪个人物？")
people = input(prompt)

print(f'''
你说你喜欢 {likes} ？翠嘴，给我打烂她的果！
你{doing}？啊我的瓜棚，我的瓜棚呢！我的瓜棚怎么没了？是你，一定是你这个贱人！
我就知道你最喜欢{people}这个小贱蹄子！
''')

