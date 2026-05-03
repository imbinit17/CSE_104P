import matplotlib.pyplot as plt


years = [
    1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977,
    1978, 1979, 1980, 1981, 1982, 1983, 1984, 1986, 1987, 1988,
    1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
    1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
    2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
    2019, 2020, 2021, 2022, 2023, 2024
]

usd_to_inr = [
    7.5, 7.5, 7.5, 7.49, 7.59, 7.74, 8.1, 8.38, 8.96, 8.74,
    8.19, 8.13, 7.86, 8.66, 9.46, 10.1, 11.36, 12.61, 12.96, 13.92,
    16.23, 17.5, 22.74, 25.92, 30.49, 31.37, 32.43, 35.43, 36.31, 41.26,
    43.06, 44.94, 47.19, 48.61, 46.58, 45.32, 44.1, 45.31, 41.35, 43.51,
    48.41, 45.73, 46.67, 53.44, 56.57, 62.33, 62.97, 66.46, 67.79, 70.09,
    70.39, 76.38, 74.57, 81.35, 81.94, 83.47
]

gold_price = [
    38.69, 41.09, 35.94, 40.8, 58.16, 97.32, 159.26, 161.02, 124.84, 147.71,
    193.22, 306.68, 612.56, 460.03, 375.67, 424.35, 360.48, 317.26, 367.66, 446.46,
    436.94, 381.44, 383.51, 362.11, 343.82, 359.77, 384, 384.17, 387.77, 330.98,
    294.24, 278.88, 279.11, 271.04, 309.73, 363.38, 409.72, 444.74, 603.46, 695.39,
    871.96, 972.35, 1_224.53, 1_571.52, 1_668.98, 1_411.23, 1_266.40, 1_160.06, 1_250.74, 1_257.12,
    1_268.49, 1_392.60, 1_769.64, 1_798.61, 1_800.09, 1_943.08
]
     


fig, ax1 = plt.subplots()


ax1.set_xlabel('Year')
ax1.set_ylabel('1 USD to INR', color='tab:blue')
ax1.plot(years, usd_to_inr, color='tab:blue', label='1 USD to INR')
ax1.tick_params(axis='y', labelcolor='tab:blue')


ax2 = ax1.twinx()
ax2.set_ylabel('Gold Price (USD per troy ounce)', color='tab:orange')
ax2.plot(years, gold_price, color='tab:orange', label='Gold Price (USD)', linestyle='--')
ax2.tick_params(axis='y', labelcolor='tab:orange')


plt.title('USD to INR Exchange Rate and Gold Price Over the Years')
ax1.grid()

plt.figtext(0.5, -0.1,
            "Sources: https://www.bankbazaar.com/currency-exchange/historical-value-of-1-usd-in-inr.html\n"
            "         https://www.statista.com/statistics/268027/change-in-gold-price-since-1990/",
            wrap=True, horizontalalignment='center', fontsize=10)


plt.show()