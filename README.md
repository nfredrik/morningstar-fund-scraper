[![pypi](https://img.shields.io/pypi/v/midsummer.svg)](https://pypi.python.org/pypi/morningstar-fund-scraper)
[![Downloads](https://static.pepy.tech/badge/midsummer)](https://pepy.tech/project/morningstar-fund-scraper) 
[![Downloads](https://static.pepy.tech/badge/midsummer/month)](https://pepy.tech/project/morningstar-fund-scraper)
[![versions](https://img.shields.io/pypi/pyversions/pydantic.svg)](https://github.com/morningstar-fund-scraper/morningstar-fund-scraper)

# Morningstar Fund Scraper

**Morningstar Fund Scraper** is a versatile Python package designed to extract financial fund data directly from the
Morningstar website. It simplifies the process of accessing up-to-date fund information for financial analysis and
research.

## Installation

Install the package effortlessly using pip:

```bash
pip install morningstar-fund-scraper
```

## Usage

To begin, locate your desired fund on the Morningstar website. For instance, navigate to Morningstar Fund Snapshot and
note the fund ID.

In this example, the fund ID is F00000PYZ6. This ID will be used to fetch data for the specified fund.

```python
from morningstar_fund_scraper import Fund

# Initialize the Fund object with an optional perfid parameter
fund = Fund(perfid="F00000PYZ6")

# Get the latest Net Asset Value (NAV) data for the fund
nav_data = fund.get_nav()

print(nav_data)
```

## Example Output

The get_nav() method returns a dictionary containing the fund name, NAV, currency, and date:

```python
{'fund': 'Länsförsäkringar Global Index', 'nav': '452,35', 'currency': 'SEK', 'date': '2024-04-29'}

```


