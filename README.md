# sales-forecasting

## Project Overview
This project is to build an end-to-end sales prediction model that automates and enhances the forecasting process for Rossmann's stores. The model will ultimately deliver a tool that provides accurate predictions to the finance team. It will consider various external and internal factors affecting sales, ensuring a reliable forecasting system.

## project scope
1. Analyze key factors influencing sales, including promotions, holidays, seasonality, and locality.
2.	Build a predictive model that incorporates historical data and external variables.
3.	Provide accurate and actionable forecasts to the finance team, enabling better decision-making and resource allocation across stores.

## Dataset Overview
The dataset is from kaggle <https://www.kaggle.com/competitions/rossmann-store-sales/data>, consists of historical sales data from Rossmann stores, covering a range of features that influence sales performance. Below is a breakdown of the key variables:
* Id: A unique identifier representing each combination of store and date in the test set.
* Store: A unique ID for each store in the dataset.
* Sales: The daily turnover (target variable) for each store on a given date.
* Customers: The number of customers visiting a store on a specific day.
* Open: Indicator for whether a store was open on a given day (1 = open, 0 = closed).
* StateHoliday: A categorical variable indicating if the store was affected by a state holiday (a = public holiday, b = Easter holiday, c = Christmas, 0 = None).
* SchoolHoliday: Indicates whether the store was affected by public school closures on a specific date.
* StoreType: Categorizes stores into four types (a, b, c, d).
* Assortment: Describes the product assortment levels in the store (a = basic, b = extra, c = extended).
* CompetitionDistance: The distance to the nearest competitor store in meters.
* CompetitionOpenSince[Month/Year]: The month and year when the nearest competitor store opened.
* Promo: Indicates whether the store was running a promotion on a specific day.
* Promo2: A binary variable showing whether a store was running an extended promotion (0 = no, 1 = yes).
* Promo2Since[Year/Week]: The year and week when the store started participating in Promo2.
* PromoInterval: Specifies the months during which a store's Promo2 promotion is active (e.g., "Feb, May, Aug, Nov").

## Prerequisites
* Python 3.x: Ensure Python is installed on your system.
* Virtual Environment: Recommended for managing project dependencies.
* Required Libraries:
- pandas: Data manipulation and analysis. 
- numpy: Numerical operations. 
- matplotlib: Data visualization. 
- seaborn: Statistical visualizations.
- scikit-learn

**Installation**

1. Create a virtual environment:
On macOS/Linux:

```python -m venv venv```
```source venv/bin/activate```

on windows:
```python -m venv venv ```
```venv\Scripts\activate ```

2. Install dependencies:
``` pip install -r requirements.txt```


**Contributing**

Contributions are welcome!

**License**

This project is licensed under the Apache License. See the LICENSE file for more details.