def cal_vol_cir(r,h):  # function defined
    from math import pi # import pi from library
    cir = 2*pi*r    #calculating circumference of cylinder
    v = pi*r*r*h   #calculating volume of cylinder
    return(cir,v) # return circumference and volume
cal_vol_cir(2,3)  #function call
