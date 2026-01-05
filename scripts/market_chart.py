import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def generate_chart():
    # 1. Fetch Data (Bitcoin or SPY)
    data = yf.download("BTC-USD", period="7d", interval="90m")
    
    # 2. Setup "Hacker Dark Mode" Plot
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Matches GitHub Dark Mode Background
    fig.patch.set_facecolor('#0d1117') 
    ax.set_facecolor('#0d1117')

    # 3. Plot the Line (Neon Green)
    ax.plot(data.index, data['Close'], color='#20C20E', linewidth=2)
    ax.fill_between(data.index, data['Close'], color='#20C20E', alpha=0.1)

    # 4. Minimalist Axis
    ax.grid(color='#2d333b', linestyle='--', linewidth=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#8b949e')
    ax.spines['bottom'].set_color('#8b949e')
    ax.tick_params(colors='#8b949e')
    
    plt.title("Live System Metric: BTC-USD", color='white', fontsize=12, fontfamily='monospace')
    plt.tight_layout()

    # 5. Save
    plt.savefig("chart.png", dpi=100, bbox_inches='tight')

if __name__ == "__main__":
    generate_chart()