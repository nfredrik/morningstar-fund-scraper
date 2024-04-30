# Morningstar Fund Scraper

The Morningstar Fund Scraper is a Python package for retrieving fund data from the Morningstar website.

## Installation

You can install the package using pip:

pip install morningstar-fund-scraper

## Usage

```python
from morningstar_fund_scraper import Fund

# Initialize the Fund object with an optional perfid parameter (default is '0P0000IWH7')
fund = Fund()

# Get the latest Net Asset Value (NAV) data for the fund
nav_data = fund.get_nav()

print(nav_data)
```


Example Output
The get_nav() method returns a dictionary containing the fund name, NAV, currency, and date:

```python
{
    'fund': 'Morningstar Global Fund',
    'nav': 123.45,
    'currency': 'USD',
    'the_date': '2022-04-21'
}
```


