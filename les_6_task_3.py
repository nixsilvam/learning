def l_6_t_3(spsk):
    index_s = [spsk.index(x) for x in spsk]
    wow_dict = dict(zip(index_s, spsk))
    print(wow_dict)


spsk1 = ['a', 'b', 'c', 'd', 'e']
l_6_t_3(spsk1)
