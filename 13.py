t = ("周杰伦", "哇哈哈", "爽歪歪", "酸酸乳", "三鹿奶粉", "AD钙奶")
print(t[1])
print(t[1:5]) # 切片的结果是一个元组
print(t[1:5:2])

#元组的不可变. 元组的不可变指的是元组内部第一层元素的内存地址
t = ("张无忌", "周芷若", "赵敏")
t = ("周润发", "周星驰", ["渣渣辉","古天绿","陈小春"])
t[2].append("李嘉诚")
print(t)
lst1 = [] # 新列表
lst2 = list() # 新列表
print(lst1, lst2)
t1 = () # 元祖
t2 = tuple() # 元祖
print(t1, t2)
# 元组如果只有一个元素。必须加逗号
t1 = (1, 3, 5, 7, 9,) # () 运算符  优先级
lst = ["哈哈", ]
print(t1)
print(lst)