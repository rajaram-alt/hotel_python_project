def top_three_menu(file):
    with open (file,'r') as f:
        food_items = {"1":"chappathi","2":"parotta","3":"coffee","4":"dosa","5":"pasta","6":"idly"}
        dic_1 = {"1": 0, "2": 0,"3": 0,"4":0,"5":0,"6":0}
        lis = f.read().split()
        lsi = set(lis)
        if len(lsi) != len(lis):
            return 'eater_id and foodmenu_id matches once more ..!'
        else:
            for i in lis:
                dic_1[str(i[2])] += 1
            res=sorted(dic_1.items(), key=lambda x: x[1])
            res.reverse()
            top_menu=[]
            for i in res[:3]:
                top_menu.append(food_items[i[0]])
            return top_menu