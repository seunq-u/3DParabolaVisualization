import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import animation

# 매개변수 t 설정 (시간)
t = np.linspace(-1, 9, 500)  # 0부터 2초까지 100개의 점으로 나눔

# 초기 속도, 발사 각도, 초기 높이 설정
v = 55
theta = np.radians((degree := 45))  # 45도
h = 0

# x(t), y(t), z(t) 계산
x = v * np.cos(theta) * t
y = v * np.sin(theta) * t - 0.5 * 9.8 * t**2 + h
z = t

# 3차원 그래프 그리기
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, z, y)

# 그래프 설정
ax.set_xlabel('X')
ax.set_ylabel('T')
ax.set_zlabel('Y')

def animate(frame):
    print(f"ANIMATE [frame {frame}]", end="\r")
    ax.view_init(elev=270, azim=frame)
    return fig,

# 애니메이션(GIF) 생성 및 저장
ani = animation.FuncAnimation(fig, animate, frames=360, interval=10)
ani.save(f'./[v={v} d={degree} h={h}].gif', fps=20)