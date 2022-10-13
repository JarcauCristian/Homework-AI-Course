import numpy as np

with open('optdigits-orig.tra', 'r') as data_in:
    bl_data = []
    fl_data = []
    counter = 0
    for i, line in enumerate(data_in):
        ln_data = list()
        for j in line:
            if j != '\n':
                ln_data.append(j)
        if i % 32 == 0 and i != 0:
            np_arr = np.array(bl_data).reshape(32, 32)
            fl_data.append(np_arr)
            bl_data.clear()
        bl_data.append(ln_data)

img_resize = ""
for img in fl_data:
    mask = []
    lst = []
    for j in range(0, 32, 2):
        inn_lst = []
        if j+1 <= 31:
            for k in range(0, 32, 2):
                if k+1 <= 31:
                    mask.append(img[j][k])
                    mask.append(img[j][k + 1])
                    mask.append(img[j + 1][k])
                    mask.append(img[j + 1][k + 1])
                    if len([e for e in mask if e == '0']) >= 3:
                        inn_lst.append(0)
                    else:
                        inn_lst.append(1)
                mask.clear()
            lst.append(inn_lst)

    for i in lst:
        for dt in i:
            img_resize = img_resize + str(dt)
        img_resize = img_resize + '\n'
    img_resize = img_resize + '\n'

with open('resize-img.txt', 'w') as data_out:
    data_out.write(img_resize)
