with open('optdigits-orig.tra', 'r') as data_in:
    for i, line in enumerate(data_in):
        ln_data = list()
        if i % 32 == 0:
            continue
        for j in line:
            if j != '\n':
                ln_data.append(j)
        print(ln_data)

