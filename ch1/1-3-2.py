from vpython import *
th = 30/180 * pi # 발사각 ##rad
direction = vec(cos(th), sin(th), 0) # 각도를 이용해 벡터 지정
speed = 5 # 속력
velocity = speed * direction # 속도 벡터

# 벡터 direction, velocity 표현
arrow(axis = vec(direction), shaftwidth = 0.2)
arrow(axis = vec(velocity), shaftwidth = 0.1, color = color.cyan)

# 출력
print(direction, mag(direction))
print(velocity, mag(velocity))