from market_data import MarketData
from chart import Chart
from community import Community
from watchlist import Watchlist
from sentiment_analysis import SentimentAnalysis
from portfolio import Portfolio
from news import News
from alert import Alert
from security import Security

def main():
    # Initialize objects
    market_data = MarketData()
    chart = Chart()
    community = Community()
    watchlist = Watchlist()
    sentiment_analysis = SentimentAnalysis()
    portfolio = Portfolio()
    news = News()
    alert = Alert()
    security = Security()

    # Update market data
    market_data.update()

    # Generate chart
    chart.generate()

    # Submit insight
    community.submit_insight()

    # Create watchlist
    watchlist.create()

    # Analyze sentiment
    sentiment_analysis.analyze()

    # Track portfolio
    portfolio.track()

    # Curate news
    news.curate()

    # Generate alert
    alert.generate()

    # Ensure security
    security.ensure()

if __name__ == "__main__":
    main()
