from vpython import *
# 벡터 r 지정
r = vector(3, 4, 5)
# 벡터 r 표현
r_arrow = arrow(pos = vec(0, 0, 0), axis = r, shaftwidth = 0.2)

# 3차원 좌표축 표현
x_axis = arrow(axis = vec(10, 0, 0), color = color.red, shaftwidth = 0.1)
y_axis = arrow(axis = vec(0, 10, 0), color = color.green, shaftwidth = 0.1)
z_axis = arrow(axis = vec(0, 0, 10), color = color.blue, shaftwidth = 0.1)

# 벡터 크기 계산
r_mag = mag(r) #// r_mag = r.mag
# 단위 벡터 계산
r_hat = hat(r) #// r_hat = r.hat // r_hat = norm(r) // r_hat = r.norm()
# 벡터 출력
print("r: ", r)