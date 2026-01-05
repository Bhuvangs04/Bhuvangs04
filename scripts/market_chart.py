import yfinance as yf
import matplotlib.pyplot as plt

def generate_chart():
    # 1. Fetch Data (Safer Method)
    # Using .history() prevents MultiIndex errors common in yf.download
    ticker = yf.Ticker("BTC-USD")
    data = ticker.history(period="7d", interval="90m")
    
    if data.empty:
        print("Error: No data fetched for BTC-USD")
        return

    # 2. Setup Dark Mode Plot
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Transparent/Dark Backgrounds
    fig.patch.set_facecolor('#0d1117') 
    ax.set_facecolor('#0d1117')

    # 3. Plot Data
    ax.plot(data.index, data['Close'], color='#20C20E', linewidth=2)
    ax.fill_between(data.index, data['Close'], color='#20C20E', alpha=0.1)

    # 4. Styling
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