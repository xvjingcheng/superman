"""
6.编写“商品管理系统”，要求如下：
必须使用自定义函数，完成对程序的模块化
商品信息至少包含：商品名称、日期、物流码，除此以外可以适当添加
必须完成的功能：添加、删除、修改、查询（单个查询/显示所有）、退出（quit）

"""
list_Warehouse = []


# 添加商品
def add_produce(list_Warehouse):
    produce_name = input("请输入商品名称:")
    produce_date = input("请输入商品生产日期:")
    produce_code = input("请输入商品物流码:")
    # 把所有商品信息做成字典
    dict_produce = {"商品名称": produce_name, "生产日期": produce_date, "物流码": produce_code}

    # 把商品信息放入仓库
    list_Warehouse.append(dict_produce)


while True:
    print("欢迎使用天狗商品管理系统:1.添加、2.删除、3.修改、4.查询（单个查询/显示所有）、0.退出（quit）")
    select = input("请选择您需要的服务:")
    if select.isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            print("欢迎使用添加功能:")
            add_produce(list_Warehouse)
        elif select == 2:
            print("欢迎使用删除功能:")

        elif select == 3:
            print("欢迎使用修改功能:")

        elif select == 4:
            print("欢迎使用查询功能:")
            print(list_Warehouse)
        else:
            print("输入有误，请重新输入")

    else:
        print("输入有误，请重新输入")
