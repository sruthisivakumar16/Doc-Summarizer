from sec_edgar_downloader import Downloader

def download_10k_filings(ticker, limit=5):
    """
    Downloads a specified number of 10-K filings for the given ticker symbol.
    Filings will be saved in the 'data/raw' folder.
    """
    dl = Downloader("Personal Project","sec-filings@yopmail.com","data/raw")

    dl.get("10-K", ticker, limit=limit)
    print(f"Downloaded {limit} 10-K filings for {ticker}")

if __name__ == "__main__":
    download_10k_filings("AAPL",limit=5)