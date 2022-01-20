lst = ["가", "나", "다"]
# 리스트의 몇번째에 무슨 값이 있는지 순회해서 알려주는게 enumerate
for lst_idx, lst_val in enumerate(lst):
    print(lst_idx, lst_val)