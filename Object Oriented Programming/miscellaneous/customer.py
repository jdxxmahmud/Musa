def fruit_Number_Update(num, fruitname):
    for i in fruit_list:
        if i.name == fruitname:
            i.quantity = i.quantity - num


