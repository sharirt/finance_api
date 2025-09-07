from fdata import get_SP500
from indicators import get_garman_klass_vol, get_dollar_volume, get_rsi

def main():
    sp500 = get_SP500()
    sp500['garman_klass_vol'] = get_garman_klass_vol(sp500)
    sp500['dollar_volume'] = get_dollar_volume(sp500)
    sp500['rsi'] = get_rsi(sp500)
    print("***************************")
    print(sp500)

if __name__ == "__main__":
    main()
