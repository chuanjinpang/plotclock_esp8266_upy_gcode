from machine import Pin, PWM
import time
from math import *

WISHY =int(3) 



SERVOFAKTORLEFT=int(610)
SERVOFAKTORRIGHT=int(600)
M_PI=float(3.14159265359)
SERVOLEFTNULL=int(2000)
SERVORIGHTNULL=int(520)

LIFT0=int(1100) 
LIFT1=int(1040)  
LIFT2=int(1000) 
LIFTSPEED=60
DRAW_SPEED=15
L1=35
L2=57.1
L3=14
L4=45

# origin points of left and right servo 
O1X=28.7
O1Y=-25
O2X=53.9
O2Y=-25
servoLift = LIFT1

SERVO_PWM_FACTOR=2
class servo(object):
    def __init__(self,name,pin,duty):
        self.pin=pin
        self.name=name
        self.pwm_servo= PWM(Pin(pin), freq=50, duty=int((duty*4096)/20000))
        print("servo %s pin:%d" % (self.name,self.pin))
    def duty(self,vduty):
        self.iduty=int((vduty*4096)/20000 )
        #print("servo %s  pin %d duty %d (%d)" %(self.name,self.pin,self.iduty,vduty))
        self.pwm_servo.duty(self.iduty)


servo_left=servo("left",13,1500)
servo_right=servo("right",15,850)
servo_lift=servo("lift",12,LIFT2)

def number( bx,  by,  num,  scale):

    if 0 == num:
        drawTo(bx + 12 * scale, by + 6 * scale);
        lift(0);
        bogenGZS(bx + 7 * scale, by + 10 * scale, 10 * scale, -0.8, 6.7, 0.5);
        lift(1);   
    elif 1 == num:
        drawTo(bx + 7 * scale, by + 18 * scale);
        lift(0);
        drawTo(bx + 8 * scale, by + 20 * scale);
        drawTo(bx + 8 * scale, by + 0 * scale);
        lift(1);

    elif 2 == num:
        drawTo(bx + 2 * scale, by + 12 * scale);
        lift(0);
        bogenUZS(bx + 8 * scale, by + 14 * scale, 6 * scale, 3, -0.8, 1);
        drawTo(bx + 1 * scale, by + 0 * scale);
        drawTo(bx + 12 * scale, by + 0 * scale);
        lift(1);
    elif 3 == num:
        drawTo(bx + 2 * scale, by + 17 * scale);
        lift(0);
        bogenUZS(bx + 5 * scale, by + 15 * scale, 5 * scale, 3, -2, 1);
        bogenUZS(bx + 5 * scale, by + 5 * scale, 5 * scale, 1.57, -3, 1);
        lift(1);
    elif 4 == num:
        drawTo(bx + 10 * scale, by + 0 * scale);
        lift(0);
        drawTo(bx + 10 * scale, by + 20 * scale);
        drawTo(bx + 2 * scale, by + 6 * scale);
        drawTo(bx + 12 * scale, by + 6 * scale);
        lift(1);
    elif 5 == num:
        drawTo(bx + 2 * scale, by + 5 * scale);
        lift(0);
        bogenGZS(bx + 5 * scale, by + 6 * scale, 6 * scale, -2.5, 2, 1);
        drawTo(bx + 5 * scale, by + 20 * scale);
        drawTo(bx + 12 * scale, by + 20 * scale);
        lift(1);
    elif 6 == num:
        drawTo(bx + 2 * scale, by + 10 * scale);
        lift(0);
        bogenUZS(bx + 7 * scale, by + 6 * scale, 6 * scale, 2, -4.4, 1);
        drawTo(bx + 11 * scale, by + 20 * scale);
        lift(1);
    elif 7 == num:
        drawTo(bx + 2 * scale, by + 20 * scale);
        lift(0);
        drawTo(bx + 12 * scale, by + 20 * scale);
        drawTo(bx + 2 * scale, by + 0);
        lift(1);
    elif 8 == num:
        drawTo(bx + 5 * scale, by + 10 * scale);
        lift(0);
        bogenUZS(bx + 5 * scale, by + 15 * scale, 5 * scale, 4.7, -1.6, 1);
        bogenGZS(bx + 5 * scale, by + 5 * scale, 5 * scale, -4.7, 2, 1);
        lift(1);
    elif 9 == num:
        drawTo(bx + 9 * scale, by + 11 * scale);
        lift(0);
        bogenUZS(bx + 7 * scale, by + 15 * scale, 5 * scale, 4, -0.5, 1);
        drawTo(bx + 5 * scale, by + 0);
        lift(1);
   

def lift_move(target):
    global servoLift;
    if (servoLift >= target) :
       while servoLift >= target : 
         servoLift-=SERVO_PWM_FACTOR;
         servo_lift.duty(servoLift);                
         time.sleep_ms(LIFTSPEED);      
    else :
       while  servoLift <= target:
         servoLift+=SERVO_PWM_FACTOR;
         servo_lift.duty(servoLift);  
         time.sleep_ms(LIFTSPEED);

def lift( lift) :
    
    print("lift:",lift)
    if 0 == lift: 
     lift_move(LIFT0)
    elif 1 == lift: 
        lift_move(LIFT1)
    elif 2== lift :
         lift_move(LIFT2) 
          
    


def  bogenUZS( bx,  by,  radius, start,  ende,  sqee) :
    inkr = -0.05;
    count = 0;    
    while ((start + count) > ende) :
      drawTo(sqee * radius * cos(start + count) + bx,
      radius * sin(start + count) + by);
      count += inkr;



def bogenGZS( bx,  by,  radius,  start,  ende,  sqee) :
    inkr = 0.05;
    count = 0;

    while ((start + count) <= ende):
        drawTo(sqee * radius * cos(start + count) + bx,
        radius * sin(start + count) + by);
        count += inkr;



def drawTo( lx , ly,pX,  pY) :      
    dx = pX - lx;
    dy = pY - ly;
    
    c = floor(10 * sqrt(dx * dx + dy * dy));#linear insert by 10

    if (c < 1) :
       c = 1;

    for  i in range(0,c) :

        set_XY(lx + (i * dx / c), ly + (i * dy / c));
    
    return pX,pY

def return_angle( a,  b,  c) :
  return acos((a * a + c * c - b * b) / (2 * a * c));

def return_angle_radius(ang):
    return (ang/180)*M_PI
    
def check_XY(lduty,rduty):
    a1=return_angle_radius(servo_angle(rduty))
    Arx=L1*cos(a1)+O2X
    Ary=L1*sin(a1)+O2Y
    a2=return_angle_radius(servo_angle(lduty))
    Alx=L1*cos(a2)+O1X
    Aly=L1*sin(a2)+O1Y
    dx=Arx-Alx
    dy=Ary-Aly
    c=sqrt(dx * dx + dy * dy); 
    a3 = return_angle(L4, L4, c);
    a4 = atan2(dy, dx); 
    x=L4*cos(a3+a4)+Alx
    y=L4*sin(a3+a4)+Aly
    print("x,y:",x,y)
    a5=return_angle(L2, L3, L4);
    #print("a5:",a5)
    Tx=L2*cos(a3+a4+a5)+Alx
    Ty=L2*sin(a3+a4+a5)+Aly
    print("Tx,Ty:",Tx,Ty)
def servo_angle(duty):
    return ((duty-500)*180)/2000;
    
AngL234=return_angle(L2, L4, L3)
print("ANG_L243:",AngL234)

def set_XY( Tx,  Ty, log=0): 
    global servo_left,servo_right
   
    dx = Tx - O1X;
    dy = Ty - O1Y;

    c = sqrt(dx * dx + dy * dy); 
    a1 = atan2(dy, dx); 
    a2 = return_angle(L1, L2, c);
    left_duty=floor(((a2 + a1 - M_PI) * SERVOFAKTORLEFT) + SERVOLEFTNULL)
    u=a2 + a1 - M_PI
    #print("left_duty:",left_duty,servo_angle(left_duty))
    
  

    a2 = return_angle(L2, L1, c);
    Hx = Tx + L3 * cos((a1 - a2 + AngL234) + M_PI);
    Hy = Ty + L3 * sin((a1 - a2 + AngL234) + M_PI);
    

    dx = Hx - O2X;
    dy = Hy - O2Y;
    
    c = sqrt(dx * dx + dy * dy);
    a1 = atan2(dy, dx);
    a2 = return_angle(L1, L4, c);
    right_duty=floor(((a1 - a2) * SERVOFAKTORRIGHT) + SERVORIGHTNULL);
    v=a1-a2
    #print("right_duty:",right_duty,servo_angle(right_duty))
    servo_left.duty(left_duty);
    servo_right.duty(right_duty);
    #check_XY(left_duty,right_duty)
    time.sleep_ms(DRAW_SPEED);
    if log != 0 :
      print("u v:",u,v,left_duty,right_duty)
    return  degrees(u),degrees(v)























