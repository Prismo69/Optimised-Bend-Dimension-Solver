import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def circleGradPoint(radius, angle, OD, S1):
    grad = m.tan(angle)
    x = grad*(radius+OD/2)/m.sqrt(1+grad**2)+radius**2
    y = m.sqrt((radius+OD/2)**2-(x-radius)**2)+S1
    return x, y


plt.rcParams["figure.figsize"] = (10,4)

k = 10000

angle_array = np.arange(0,k)*m.pi/(2*k)
Area_array = []
side1_array = []
side2_array = []

c1_array = []
c2_array = []
c3_array = []
c4_array = []
P1x_array = []
P2x_array = []
P3x_array = []
P4x_array = []
P1y_array = []
P2y_array = []
P3y_array = []
P4y_array = []
xarc_array = []
yarc_array = []

F1 = 510
F2 = 505
OD = 414
R = 300
T1=750
T2=860
a=85
a=a*m.pi/180
M = m.tan(a)
Rmin = OD/2+5
Rmax = min(T1,T2)/m.tan(a/2)-5
R = Rmax

S1 = T1 - R*m.tan(a/2)
S2 = T2 - R*m.tan(a/2)

for i in range(0,k):

    #a1_box = 80
    a1_box = angle_array[i]
    M1 = m.tan(a1_box)
    if M1 == 0:
        M2 = 10**10
    else:
        M2 = -1/M1

 
    xp = T2*m.cos(a)
    yp = T1 + T2*m.sin(a)

    x1, y1 = -F1/2, 0
    x2, y2 = F1/2, 0
    
    x3, y3 = T2*m.sin(a)-F2/2*m.cos(a), T1+T2*m.cos(a)+F2/2*m.sin(a)
    x4, y4 = T2*m.sin(a) + F2/2*m.cos(a), T1+T2*m.cos(a)-F2/2*m.sin(a)

    m1_crit = (y4-y2)/(x4-x2)
    a1_crit = m.atan(m1_crit)
    
    arcM1 = m.tan(-a1_box)
    if arcM1 == 0:
        arcM2 = 10**10
    else:
        arcM2 = -1/arcM1

    xarc = arcM1*(R+OD/2)/m.sqrt(1+arcM1**2)+R
    yarc = arcM2*(R+OD/2)/m.sqrt(1+arcM2**2)+S1
    xarc_array += [xarc]
    yarc_array += [yarc]
    carc = yarc - M1*xarc
    #yarc = m.sqrt((R+OD/2)**2-(xarc-R)**2)+S1
  
    if a1_box < a1_crit:
        c1 = y2-M1*x2
        if M1 > 1/m.tan(a):
            c3 = max(carc,y3-M1*x3, y1-M1*x1)
        else: 
            c3 = y3-M1*x3
        
    else:
        c1 = y4-M1*x4
        c3 = max(y3-M1*x3, carc, y1-M1*x1)
    
    if m.pi/2-a1_box < a:
        c2 = y3-M2*x3
        c4 = y1-M2*x1
    else:
        c2 = y4-M2*x4
        c4 = y1-M2*x1

    c1_array += [c1]
    c2_array += [c2]
    c3_array += [c3]
    c4_array += [c4]
    
    P1x, P1y = (c2-c1)/(M1-M2), M1*(c2-c1)/(M1-M2)+c1
    P2x, P2y = (c3-c2)/(M2-M1), M2*(c3-c2)/(M2-M1)+c2
    P3x, P3y = (c4-c3)/(M1-M2), M1*(c4-c3)/(M1-M2)+c3
    P4x, P4y = (c1-c4)/(M2-M1), M2*(c1-c4)/(M2-M1)+c4

    P1x_array += [P1x]
    P1y_array += [P1y]
    P2x_array += [P2x]
    P2y_array += [P2y]
    P3x_array += [P3x]
    P3y_array += [P3y]
    P4x_array += [P4x]
    P4y_array += [P4y]
    
    side1 = m.sqrt((P2x-P1x)**2 + (P2y-P1y)**2)
    side2 = m.sqrt((P3x-P2x)**2 + (P3y-P2y)**2)
    side1_array += [side1]
    side2_array += [side2]
    Area_array +=[side1/1000*side2/1000]
    

Area_arraylist = Area_array
Area_array = np.array(Area_array)
o_index = Area_arraylist.index(min(Area_array))

fig, (ax1, ax2) = plt.subplots(1, 2)

x1min = -OD/2
x1max = x1min + (R+OD/2)*(1-m.cos(a))
x2min = OD/2
x2max = x2min + (R-OD/2)*(1-m.cos(a))

xCircle1 = np.arange(x1min,x1max,1)
xCircle2 = np.arange(x2min,x2max,1)
yCircle1 = xCircle1*0
yCircle2 = xCircle2*0
for i in range(0,len(xCircle1)):
    yCircle1[i] =  m.sqrt((R+OD/2)**2-(xCircle1[i]-R)**2)+S1
    
for i in range(0, len(xCircle2)):
    yCircle2[i] =  m.sqrt((R-OD/2)**2-(xCircle2[i]-R)**2)+S1

S2_1x = [x1max, x1max+S2*m.sin(a)]
S2_1y = [max(yCircle1), max(yCircle1)+S2*m.cos(a)]

S2_2x = [x2max, x2max+S2*m.sin(a)]
S2_2y = [max(yCircle2), max(yCircle2)+S2*m.cos(a)]



plt.xlim(-400, 1.1*max(max(P1y_array),max(P2y_array),max(P3y_array),max(P4y_array)))
plt.ylim(-400, 1.1*max(max(P1y_array),max(P2y_array),max(P3y_array),max(P4y_array)))

ax1.plot(angle_array*180/m.pi, Area_array)

h1 = ax2.plot([x1]+[x2], [y1]+[y2])
#h2 = ax2.plot([0,0], [0]+[T1])
#h3 = ax2.plot([0,T2*m.sin(a)], [T1]+[T1+T2*m.cos(a)])
h4 = ax2.plot([x3]+[x4], [y3]+[y4])
h5 = ax2.plot([-OD/2, -OD/2], [0, S1])
h6 = ax2.plot([OD/2, OD/2], [0, S1])
h7 = ax2.plot(xCircle1, yCircle1)
h8 = ax2.plot(xCircle2, yCircle2)
h9 = ax2.plot(S2_1x, S2_1y)
h9 = ax2.plot(S2_2x, S2_2y)
#h10 = ax2.plot(xarc_array, yarc_array)

p1 = ax2.plot([P1x_array[o_index]]+[P2x_array[o_index]],[P1y_array[o_index]]+[P2y_array[o_index]])
p2 = ax2.plot([P2x_array[o_index]]+[P3x_array[o_index]],[P2y_array[o_index]]+[P3y_array[o_index]])
p3 = ax2.plot([P3x_array[o_index]]+[P4x_array[o_index]],[P3y_array[o_index]]+[P4y_array[o_index]])
p4 = ax2.plot([P4x_array[o_index]]+[P1x_array[o_index]],[P4y_array[o_index]]+[P1y_array[o_index]])

print("\nWidth: " + str(round(side1_array[o_index],1)))
print("Length: " + str(round(side2_array[o_index],1)))
print("Area: " + str(round(min(Area_array),2)))
print("Relative Angle: "+ str(round(180/m.pi*angle_array[o_index],1)))
print("Critical Angle: " + str(round(180/m.pi*a1_crit)))
print("")

fig, (ax1, ax2) = plt.subplots(1, 2)

Areaplot = ax1.plot(angle_array*180/m.pi, Area_array)
areaDot, = ax1.plot([0],[Area_array[0]], 'ro')

hr1 = ax2.plot([x1]+[x2], [y1]+[y2],'k-')
hr4 = ax2.plot([x3]+[x4], [y3]+[y4],'k-')
hr5 = ax2.plot([-OD/2, -OD/2], [0, S1],'k-')
hr6 = ax2.plot([OD/2, OD/2], [0, S1],'k-')
hr7 = ax2.plot(xCircle1, yCircle1,'k-')
hr8 = ax2.plot(xCircle2, yCircle2,'k-')
hr9 = ax2.plot(S2_1x, S2_1y,'k-')
hr9 = ax2.plot(S2_2x, S2_2y,'k-')

box1, = ax2.plot([P1x_array[0]]+[P2x_array[0]],[P1y_array[0]]+[P2y_array[0]], 'y-')
box2, = ax2.plot([P2x_array[0]]+[P3x_array[0]],[P2y_array[0]]+[P3y_array[0]], 'y-')
box3, = ax2.plot([P3x_array[0]]+[P4x_array[0]],[P3y_array[0]]+[P4y_array[0]], 'y-')
box4, = ax2.plot([P4x_array[0]]+[P1x_array[0]],[P4y_array[0]]+[P1y_array[0]], 'y-')

plt.xlim(-400, 1.1*max(max(P1y_array),max(P2y_array),max(P3y_array),max(P4y_array)))
plt.ylim(-400, 1.1*max(max(P1y_array),max(P2y_array),max(P3y_array),max(P4y_array)))

def animate(i):
    box1.set_data([P1x_array[i]]+[P2x_array[i]],[P1y_array[i]]+[P2y_array[i]])
    box2.set_data([P2x_array[i]]+[P3x_array[i]],[P2y_array[i]]+[P3y_array[i]])
    box3.set_data([P3x_array[i]]+[P4x_array[i]],[P3y_array[i]]+[P4y_array[i]])
    box4.set_data([P4x_array[i]]+[P1x_array[i]],[P4y_array[i]]+[P1y_array[i]])
    areaDot.set_data([angle_array[i]*180/m.pi],[Area_array[i]])
    return box1, box2, box3, box4, areaDot

# create animation using the animate() function
myAnimation = ani.FuncAnimation(fig, animate, frames=np.arange(0, k, 1)[::int(2*k/1000)], \
                                      interval=10, blit=True, repeat=True)

plt.show()