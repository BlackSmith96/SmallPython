#coding:utf-8

def combine(img1, img2):
    '''
    param:
    img1 背景图片
    img2 要添加的图片，其除了物体之外为空白
    '''

    if(img1.size != img2.size):
        raise Exception("The size of two images are diffrent.")
    
    width, height = img1.size
    default_color = (255,255,255)
    p1 = img1.load()
    p2 = img2.load()

    for i in range(width):
        for j in range(height):
            if(p2[i,j] != default_color):
                 p1[i,j] = p2[i,j]

    return img1