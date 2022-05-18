import os
from numpy import *
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
from PIL import Image
import numpy as np
import scipy.misc
import glob
from scipy.ndimage import filters

def cjy_gaosi3(src,tt):
    NoiseImg=src
    cc=src.shape
    im2=zeros(cc)
    for i in range(3):
        im2[:,:,i]=filters.gaussian_filter(src[:,:,i],tt)
    im2=uint8(im2)
    
##        print(len(src[:,j,i])/t)
##        print(im)
    
    
    return im2

def cjy_gaosi2(src,tt):
    NoiseImg=src
    cc=src.shape
    im2=zeros(cc)
    im2=filters.gaussian_filter(src,tt)
    im2=uint8(im2)
    
##        print(len(src[:,j,i])/t)
##        print(im)
    
    
    return im2
if __name__=='__main__':
    orig_test_folder = "./dat000_all_gray_dub_jt_png/"		# Old - original folder
    dest_test_folder = "./dat000_all_mohu_dub_jt_png/"
    if not os.path.exists(dest_test_folder):
        os.mkdir(dest_test_folder)
    aa1=[]
    for root,file_list,files in os.walk(orig_test_folder):
        aa=root
        aa1+=[os.path.join(root,file_path) for file_path in file_list]
##        print(aa1)
####        image_path01=sub_folder
##        print('woo:',sub_folder,files)
##    print(dirs)
    #print(aa1)
    ioc=0
    for im in aa1:
        print(im)
        im2=im.replace(orig_test_folder,dest_test_folder)
        
        if not os.path.exists(im2):
            os.mkdir(im2)
        imagemores=glob.glob(im+'/'+'*.png')
        ioc2=0
        for ic0 in range(int(len(imagemores)/2),len(imagemores),1):
##            print(ic)
            ic=imagemores[ic0]
            img=array(Image.open((ic)))
            Img2=cjy_gaosi2(img,2.5)
##            print(Img2)
            #print(im2+'/'+str(ioc)+str(ioc2)+'_cjygaosi1.png')
            scipy.misc.imsave(im2+'/'+str(ioc)+str(ioc2)+'_mohu1.5.png',Img2)
            ioc2+=1
        for ic0 in range(0,len(imagemores),1):
##            print(ic)
            ic=imagemores[ic0]
            img=array(Image.open((ic)))
            Img2=cjy_gaosi2(img,2)
##            print(Img2)
            #print(im2+'/'+str(ioc)+str(ioc2)+'_cjygaosi1.png')
            scipy.misc.imsave(im2+'/'+str(ioc)+str(ioc2)+'_mohu2.png',Img2)
            ioc2+=1
        

        #for ic0 in range(0,len(imagemores),1):
##            print(ic)
         #   ic=imagemores[ic0]
          #  img1=mpimg.imread(ic)
           # Img3=cjy_gaosi3(img1)
            #print(im2+'/'+str(ioc)+str(ioc2)+'_cjygaosi1.png')
            #scipy.misc.imsave(im2+'/'+str(ioc)+str(ioc2)+'_gao3.png',Img3)
            #ioc2+=1
        ioc+=1
##    im = Image.fromarray(Img2)
##    plt.imshow(Img2)
####    print(Img2[:,20,0])
##    plt.show()
##    im.savefig('test01.png')
   
