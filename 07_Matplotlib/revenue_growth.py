from matplotlib import pyplot as plt

months  = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [5.2, 7.8, 6.5, 9.1, 12.4, 11.5]

plt.figure(figsize=(9, 5))

plt.plot(
    months, revenue,
    linestyle='--',
    marker='o',
    color='red',
    linewidth=2,
    markersize=8,
    markerfacecolor='white',
    markeredgewidth=2,
    label='Monthly Revenue'
)

plt.title("Start-up Revenue Growth - H1 2026", fontsize=14, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue in Lakhs (INR)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()