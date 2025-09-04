from fdata import get_SP500

def main():
    sp500 = get_SP500(end_date='2025-09-04',start_date='2024-09-03',interval='1m')
    print(sp500)

if __name__ == "__main__":
    main()
