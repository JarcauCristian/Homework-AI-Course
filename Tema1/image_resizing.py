import numpy as np

with open('imag.txt', 'r') as data_in:
    data = data_in.read()

img = []
for i in data:
    if i != '\n':
        img.append(i)
img = np.array(img).reshape(32, 32)

print(img)
mask = []
lst = []
for i in range(0, 32, 2):
    inn_lst = []
    if i+1 <= 31:
        for j in range(0, 32, 2):
            if j+1 <= 31:
                mask.append(img[i][j])
                mask.append(img[i][j+1])
                mask.append(img[i+1][j])
                mask.append(img[i+1][j+1])
                if len([e for e in mask if e == '0']) >= 3:
                    inn_lst.append(0)
                else:
                    inn_lst.append(1)
                mask.clear()
        lst.append(inn_lst)

img_resize = ""
for i in lst:
    for dt in i:
        img_resize = img_resize + str(dt)
    img_resize = img_resize + '\n'

with open('resize-img.txt', 'w') as data_out:
    data_out.write(img_resize)
