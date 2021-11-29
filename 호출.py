# 프로그램을 실행하기 전 matplotlib를 설치해 주세요
# cmd 창에서 명령어 'pip install matplotlib' 를 실행해주세요.(파이썬이 가장 최신 버전(3.10.0)이어야 정상 작동됩니다.)

select=(input("1. 대포게임(cannon 입력)\n2. 포물선 추적 프로그램(parabola 입력)\n실행할 프로그램의 이름을 입력해주세요 :"))


import turtle
import random

    # 목표 타겟을 설정하고 그립니다.
target = random.randint(50,150)     #target을 50~150 사이에 있는 임의의 수로 지정합니다.


def up():                       #Up키를 눌렀을 때 호출되는 함수입니다.
    turtle.left(2)   

def down():                     #Down키를 눌렀을 때 호출되는 함수입니다.
    turtle.right(2)            

def space():		            #SpaceBar를 누르면 turtle 대포를 발사합니다.
    angle = turtle.heading()	         #현재 turtle이 바라보는 각도를 저장합니다.
    while turtle.ycor() > 0:                     #turtle이 y좌표가 0이상일 경우에 있는동안 반복합니다.
        turtle.forward(15)                       
        turtle.right(5)	                         #turtle이 이 정도의 세기로 발사됩니다.	

    d = turtle.distance(target, 0)	    #turtle과 목표 지점과의 거리를 구합니다.
    turtle.sety(random.randint(10, 100)) #성공 또는 실패 지점을 지정합니다.

    if d < 25:			    #거리 차이가 25보다 작으면 명중 했다는 것입니다.
        turtle.color("blue")
        turtle.write("Good!",False,"center",("",15))
        turtle.color("black")
        turtle.goto(-200,10)             #위치를 원 위치로 되돌립니다.
        turtle.setheading(angle)
        turtle.ontimer(turtle.bye,0)
    else:
        
        turtle.color("red")
        turtle.write("Bad!",True,"center",("",15))
        turtle.color("black")
        turtle.goto(-200,10)             #위치를 원 위치로 되돌립니다.
        turtle.setheading(angle)           #각도도 처음 기억해 둔 각도로 되돌립니다.

def play_cannon():

    #땅을 그립니다.
    turtle.speed(0)                        #땅을 그리는 시간을 빠르게 합니다.
    turtle.goto(-300,0)
    turtle.down()
    turtle.goto(300,0)

    turtle.pensize(3)
    turtle.color("green")
    turtle.penup()
    turtle.goto(target-25,2)
    turtle.pendown()			
    turtle.goto(target+25,2)                 #target의 x좌표 -25 ~ 25 까지 선을 그립니다.

    turtle.color("black")
    turtle.shape("arrow")                    #turtle 모양이 잘 보이지 않아 화살 모양으로 모양을 변경하였습니다.
    turtle.up()				    
    turtle.goto(-200, 10)
    turtle.setheading(20)

    turtle.onkeypress(up, "Up")                     #Up키를 누르면 up 함수를 실행합니다.
    turtle.onkeypress(down, "Down")                 #Down키를 누르면 down 함수를 실행합니다.
    turtle.onkeypress(space, "space")               #SpaceBar를 누르면 spcae 함수를 실행합니다.
    turtle.listen()		                        #거북이 그래픽 창이 키보드 입력을 받도록 합니다. (Up키와 Down키와 Space Bar)
    

'''
포물선 공식을 이용한 물체의 궤적, 비행시간 및 거리 구하기
'''
#math 모듈을 사용함
import math
#math 모듈 중 제곱 값을 구하는 pow와 자신보다 큰 값 중 가장 근접한 정수를 구하는 ceil을 사용한다.
from math import pow, ceil
#포물선 궤적을 그리기 위해 외부 모듈인 matplotlib 모듈 이용.(그래프를 그리는 역할)
import matplotlib.pyplot as plt

#중력가속도=GA, 그래프 표시 주기=INTERVAL
GA=9.81
INTERVAL=0.001

#그래프에 포물선을 표시하기 위한 배열을 만드는 함수 선언
#시작시간 start, 끝나는 시간 end, 시간주기 step을 입력 받아 배열 선언
def timeArray(start, end, step):
   times=[]
   while start < end:
      times.append(start)
      start += step
   return times

#포물선 그리는 함수 선언
'''
비행시간= 낙하시간t에 관해
F=ma=m(delta_v/t), t=delta_v/a(==중력가속도)
비행시간T는 낙하시간*2
따라서 2 * (Y벡터 속도/중력가속도)

비행 거리는 x축의 변위
위치 S는 속도 x와 비행시간의 곱(S=v_x * t)
'''
def draw_graph(xVelocity, yVelocity):
   flyTime = 2 * yVelocity / GA
   flyDistance = xVelocity * flyTime
   intervals = timeArray(0, flyTime, INTERVAL)
   x=[]
   y=[]
   for t in intervals:
      x.append(xVelocity * t)
      y.append(yVelocity * t - 0.5 * GA * math.pow(t, 2))
   plt.plot(x, y)
   plt.xlabel('X-Vector velocity is '+str(xVelocity)+'m/s')
   plt.ylabel('Y-Vector velocity is '+str(yVelocity)+'m/s')
   plt.title('Fly-time is '+str(math.ceil(flyTime))+'s, Fly-distance is '+str(math.ceil(flyDistance))+'m')

if select=='parabola':
   try:
      xVelocity = float(input('x벡터의 속도를 입력하세요(m/s) : '))
      yVelocity = float(input('y벡터의 속도를 입력하세요(m/s) : '))
   except ValueError:
      print("올바르지 않은 값을 입력했습니다.")
   else:
      draw_graph(xVelocity, yVelocity)
      plt.show()
elif select=='cannon':
    play_cannon()

else:
    print("정해진 프로그램의 이름을 입력해주세요.")
