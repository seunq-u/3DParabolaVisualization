import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
from matplotlib import animation

# 2. 발사 각도 및 방향 각도 설정
theta_list = [30, 45, 60]  # 발사 각도 (도)
alpha_list = [30, 45, 60]  # 발사 방향 각도 (도)
alpha_color = {
    30:{30: 'lightcoral', 45: 'r', 60: 'darkred'},
    45:{30: 'lightgreen', 45: 'g', 60: 'darkolivegreen'},
    60:{30: 'lightskyblue', 45: 'b', 60: 'darkblue'}
    }
# 3. 초기 속도, 중력 가속도, 초기 높이 설정
v0 = 35  # 초기 발사 속도 (m/s)
g = 10  # 중력 가속도 (m/s^2)
h = 0    # 초기 높이 (m)

# 4. 시간 범위 설정
t = np.linspace(0, 8.1, 300)  # 0초부터 8.1초까지 300개의 시간 간격

# 5. 3차원 궤적 계산 함수 정의
def calculate_trajectory(v, theta, alpha, t, h):
    theta_rad = math.radians(theta)  # 발사 각도를 라디안으로 변환
    alpha_rad = math.radians(alpha)
    x = v * np.cos(theta_rad) * np.cos(alpha_rad) * t
    y = v * np.cos(theta_rad) * np.sin(alpha_rad) * t
    z = v * np.sin(theta_rad) * t - 0.5 * g * t**2 + h
    return x, y, z

# 6. 궤적 데이터 계산
trajectories = []
for theta in theta_list:
    for alpha in alpha_list:
        x, y, z = calculate_trajectory(v0, theta, alpha, t, h)
        trajectories.append((x, y, z, theta, alpha))

# 7. 3차원 그래프 생성 및 궤적 표시
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for x, y, z, theta, alpha in trajectories:
    ax.plot(x, y, z, label=f'theta: {theta}°, alpha: {alpha}°', color=alpha_color[theta][alpha])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 8. 그래프 설정
ax.set_xlabel('X (LR distance, m)')
ax.set_ylabel('Y (FR distance, m)')
ax.set_zlabel('Z (height, m)')
ax.set_title(f'3D XY-Z {v0}m/s')
ax.legend()

# 9. 그래프 범위 설정 (모든 축 0 이상)
ax.set_xlim(0, np.max(x) * 1.6)
ax.set_ylim(0, np.max(y) * 1.6)
ax.set_zlim(0, np.max(z) * 1.2)


def animate(frame):
    print(f"ANIMATE [frame {frame}]", end="\r")
    if frame >= 360:
        frame = 0
    ax.view_init(elev=15, azim=265+frame)
    return fig,

# 애니메이션(GIF) 생성 및 저장
ani = animation.FuncAnimation(fig, animate, frames=400, interval=10)
ani.save(f'./{theta_list}.gif', fps=40)