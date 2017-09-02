from skimage import io,transform,color
import numpy as np

def convert_size(f,img_num=0):
     rgb=io.imread(f)    #依次读取rgb图片
     dst=transform.resize(rgb,(64,64))  #将灰度图片大小转换为256*256
     return dst
    
str='C:\\Users\\Wr\\Desktop\\cascade\\trainData\\positive_samples\\'+'/*.jpg'
coll = io.ImageCollection(str,load_func=convert_size)
for i in range(len(coll)):
    io.imsave('C:\\Users\\Wr\\Desktop\\cascade\\trainData\\positive_samples\\'+np.str(i)+'.jpg',coll[i])  #循环保存图片