import csv

tup_1 = tuple()
ls_1 = []
with open('./Files/TB-Export.csv', 'r', encoding='UTF-8') as tb:
    tb_csv = csv.reader(tb)
    # headers = next(tb_csv)
    for row in tb_csv:
        clean_tb = ' '.join(row)
        ls_1.append(row)
print(ls_1)




