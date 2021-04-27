
import time
from math import *
from box_plotclock import  *
import re

Z_up=20
Z_work=15
Z_park=35

def run_one_gcode(lx,ly,lz,line):
    line = line.strip()
    res = re.match(r'G\d+ F\d+.\d+ ([XYZ].?\d+.\d+) ([XYZ].?\d+.\d+)', line)
    if res != None:            
        x=float(res.group(1)[1:])
        y=float(res.group(2)[1:])  
        print("x y:",x,y)   
        if(lz<=Z_work):
            ex,ey=drawTo(lx,ly,x,y)  
        else :
            set_XY(x,y)
            ex,ey=x,y
        return ex,ey,lz  
        #plt.plot(Tx,Ty,'ro-')
    res = re.match(r'G\d+ F\d+.\d+ ([XYZ].?\d+.\d+)', line)   
    if res != None:
        z=float(res.group(1)[1:])  
        print("z:",z)    
        if z > 10:
          if z > Z_work:
            if z>= Z_park:
                lift(2)
            else:
                lift(1);
          else :
                   lift(0);
          return lx,ly,z
        else :
          return lx,ly,lz 
        
    else:
        return lx,ly,lz
    


def run_gcode(file_name):
    lx=float(5)
    ly=float(5)
    lz=float(Z_up)
    lift(2);
    set_XY(lx,ly)
    file = open(file_name, 'r')
    try:
        while True:
            text_line = file.readline()
            if text_line:
                print(">",text_line)
                lx,ly,lz=run_one_gcode(lx,ly,lz,text_line)
                print("xyz:",lx,ly,lz)
            else:
                print("no lines")
                break

    finally:
        file.close()


if __name__ == '__main__':
    run_gcode("Peppa_Pig.gcode")
    set_XY(70,20)
 






