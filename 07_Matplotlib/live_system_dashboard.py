import psutil
from matplotlib import pyplot as plt
from matplotlib import animation as anm
from collections import deque
from datetime import datetime

MAX_POINTS = 60

cpu_data  = deque([0] * MAX_POINTS, maxlen=MAX_POINTS)
mem_data  = deque([0] * MAX_POINTS, maxlen=MAX_POINTS)
time_data = deque([''] * MAX_POINTS, maxlen=MAX_POINTS)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 6))
fig.suptitle("Live System Telemetry Dashboard", fontsize=14, fontweight='bold')

def update(frame):
    cpu_data.append(psutil.cpu_percent(interval=None))
    mem_data.append(100 - psutil.virtual_memory().percent)
    time_data.append(datetime.now().strftime("%H:%M:%S"))
    
    ax1.clear()
    ax2.clear()

    x = list(range(MAX_POINTS))
    
    ax1.plot(x, list(cpu_data), color='red', linewidth=1.8, label='CPU Usage %')
    ax1.fill_between(x, list(cpu_data), alpha=0.2, color='red')
    ax1.set_ylim(0, 100)
    ax1.set_xlim(0, MAX_POINTS)
    ax1.set_ylabel("CPU %", fontsize=11)
    ax1.set_title("CPU Usage", fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=10)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.set_xticks([])
    
    ax2.plot(x, list(mem_data), color='blue', linewidth=1.8, label='Available Memory %')
    ax2.fill_between(x, list(mem_data), alpha=0.2, color='blue')
    ax2.set_ylim(0, 100)
    ax2.set_xlim(0, MAX_POINTS)
    ax2.set_ylabel("Available Memory %", fontsize=11)
    ax2.set_title("Available Memory", fontsize=12, fontweight='bold')
    ax2.legend(loc='upper left', fontsize=10)
    ax2.grid(True, linestyle='--', alpha=0.5)
    
    tick_positions = list(range(0, MAX_POINTS, 10))
    tick_labels    = [list(time_data)[i] if list(time_data)[i] else '' for i in tick_positions]
    
    ax2.set_xticks(tick_positions)
    ax2.set_xticklabels(tick_labels, fontsize=8, rotation=15)
    
    ax2.set_xlabel("Time (sliding window)", fontsize=10)
    plt.tight_layout()

ani = anm.FuncAnimation(fig, update, interval=100, cache_frame_data=False)
plt.show()