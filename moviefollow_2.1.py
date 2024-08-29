a = (str(input()))
b = (list(input()))     #创建一个空列表
c = (tuple(input()))    #创建一个空元组
d = (set(input()))      #创建一个空集合
e = {}  #创建一个空字典
e_ElementName = input("请输入名称:")
e_ValueContent = input("请输入内容:")
e[e_ElementName] = e_ValueContent
print("您输入的字串符:",a)
print("列表结果:",b)
print("元组结果:",c)
print("集合结果:",d)
print("字典结果:",e)
