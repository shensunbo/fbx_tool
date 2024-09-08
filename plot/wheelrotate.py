import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from matplotlib.widgets import TextBox

# 创建画布和坐标轴
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# 车轮参数
wheel_radius = 9.5
spoke_length = 5
marker_radius = wheel_radius + 1.5  # 单独定义标记的半径

# 初始化五个辐条
spokes = [patches.Polygon([[0, 0], [0, spoke_length]], closed=True, edgecolor='black') for _ in range(5)]

# 初始化五个扇形区域的颜色
colors = ['red', 'green', 'blue', 'orange', 'purple']

# 初始化五个扇形区域
sectors = [patches.Wedge((0, 0), wheel_radius, i * 72, (i + 1) * 72, facecolor=colors[i]) for i in range(5)]

# 添加辐条和扇形区域到坐标轴
for i in range(5):
    ax.add_patch(spokes[i])
    ax.add_patch(sectors[i])

# 添加文本标记
marker_text = ax.text(marker_radius * np.cos(0), marker_radius * np.sin(0), 'Marker', ha='center', va='center')

# 添加文本输入框
speed_textbox_ax = plt.axes([0.1, 0.01, 0.2, 0.04], facecolor='lightgoldenrodyellow')
speed_textbox = TextBox(speed_textbox_ax, 'Speed (KM/H)', initial='10.0')

# 记录起始时间
start_time = None

# 更新函数，用于每一帧的动画
def update(frame):
    global start_time

    if start_time is None:
        start_time = frame / 90.0  # Set the start time when the animation begins

    try:
        speed_kmh = float(speed_textbox.text)
    except ValueError:
        speed_kmh = 10.0  # Default value if parsing fails

    # Convert speed from KM/H to meters per second
    speed_ms = speed_kmh * 1000 / 3600

    # Calculate angular velocity based on the specified radius (0.25 m)
    target_radius = 0.25
    angular_velocity = speed_ms / target_radius

    current_time = frame / 90.0  # Current time in seconds
    elapsed_time = current_time - start_time

    angle = elapsed_time * angular_velocity  # 控制旋转速度，考虑车轮半径
    for i in range(5):
        spokes[i].set_xy([[0, 0], [spoke_length * np.sin(angle + i * 2 * np.pi / 5), spoke_length * np.cos(angle + i * 2 * np.pi / 5)]])
        sectors[i].set_theta1(i * 72 + angle * 180 / np.pi)
        sectors[i].set_theta2((i + 1) * 72 + angle * 180 / np.pi)

    # 更新标记位置
    marker_x = wheel_radius * np.cos(angle)
    marker_y = wheel_radius * np.sin(angle)
    marker_text.set_position((marker_x, marker_y))

    return spokes + sectors + [marker_text]

# 创建动画
ani = animation.FuncAnimation(fig, update, interval=1000 / 90, blit=True)

# 显示动画
plt.show()
