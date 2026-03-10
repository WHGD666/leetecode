# ------------------------------
# 1. 定义与基本结构
# ------------------------------
# 列表：[] 包裹，元素是「单个值」，可重复、类型混合
my_list = [10, "Python", True, 3.14]
print("1. 列表定义:", my_list)  # 输出: [10, 'Python', True, 3.14]

# 字典：{} 包裹，元素是「键值对 key:value」，键唯一且不可变
my_dict = {"name": "张三", "age": 20, "is_student": True}
print("1. 字典定义:", my_dict)  # 输出: {'name': '张三', 'age': 20, 'is_student': True}


# ------------------------------
# 2. 元素访问方式
# ------------------------------
# 列表：通过「索引」访问（从0开始），支持切片
print("\n2. 列表第1个元素:", my_list[0])  # 输出: 10
print("2. 列表切片[1:3]:", my_list[1:3])  # 输出: ['Python', True]

# 字典：通过「键」访问，无索引（用get()可避免键不存在报错）
print("2. 字典中'name'的值:", my_dict["name"])  # 输出: 张三
print("2. 字典中'grade'的值:", my_dict.get("grade", "未找到"))  # 输出: 未找到


# ------------------------------
# 3. 有序性对比
# ------------------------------
# 列表：始终有序，索引对应位置固定
my_list.append("新元素")
print("\n3. 列表添加元素后:", my_list)  # 输出: [10, 'Python', True, 3.14, '新元素']

# 字典：Python 3.7+ 保持「插入顺序」，但仍通过键访问（非索引）
my_dict["grade"] = 85
print("3. 字典添加键值对后:", my_dict)  # 输出按插入顺序排列


# ------------------------------
# 4. 可变性规则
# ------------------------------
# 列表：元素可直接修改
my_list[0] = 100
print("\n4. 修改后的列表:", my_list)  # 输出: [100, 'Python', True, 3.14, '新元素']

# 字典：键不可变（如不能用列表当键），但值可修改
my_dict["age"] = 21
print("4. 修改值后的字典:", my_dict)  # 输出: {'name': '张三', 'age': 21, ...}

# 尝试用列表当键会报错（演示不可变规则）
try:
    my_dict[[1,2]] = "错误"
except TypeError as e:
    print("4. 字典键错误:", e)  # 输出: unhashable type: 'list'


# ------------------------------
# 5. 常用操作演示
# ------------------------------
# 列表操作：append（追加）、pop（删除末尾）、extend（扩展）
my_list.pop()  # 删除最后一个元素
print("\n5. pop后的列表:", my_list)  # 输出: [100, 'Python', True, 3.14]
my_list.extend([5, 6])  # 追加多个元素
print("5. extend后的列表:", my_list)  # 输出: [100, 'Python', True, 3.14, 5, 6]

# 字典操作：keys（键）、values（值）、items（键值对）
print("5. 字典的键:", my_dict.keys())  # 输出: dict_keys(['name', 'age', 'is_student', 'grade'])
print("5. 字典的值:", my_dict.values())  # 输出: dict_values(['张三', 21, True, 85])
print("5. 字典的键值对:", my_dict.items())  # 输出: dict_items([('name', '张三'), ...])