# separate by industry
#display(tickers_file_original)

# create dictionary to store tickers in each industry
industry_groups = {}

for i in range(len(tickers_file_original)):
    try: 
        name = tickers_file_original.loc[i, "Ticker"]
        stock = yf.Ticker(name)
        industry = stock.info['industry']
        if industry not in industry_groups:
            industry_groups[industry] = []

        industry_groups[industry].append(name)
    except:
        pass

# chat gpt
max_length = max(len(stocks) for stocks in industry_groups.values())
df = pd.DataFrame({industry: stocks + ['-'] * (max_length - len(stocks))
                   for industry, stocks in industry_groups.items()})

display(df)
