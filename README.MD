
---

# Nigeria Universities Web Scraping and Data Transformation Project

## Overview

This project focuses on web scraping university data from a website that contains information about federal, state, uniform, and private universities in Nigeria. The scraped data is then processed and transformed using BeautifulSoup, pandas, and other Python libraries.

## Project Steps

### 1. Web Scraping

I utilized BeautifulSoup to scrape data from the following tables on the website:

- Federal Universities
- State Universities
- Uniform Universities
- Private Universities

### 2. Data Concatenation

The scraped data from the four tables was concatenated into a single DataFrame, combining information from different types of universities.

### 3. Data Cleaning

To prepare the data for further analysis, I performed the following cleaning steps:

- Removed blank rows
- Extracted numeric values from a string using regular expressions

### 4. DataFrame Manipulation

I kept essential columns and removed unnecessary ones to streamline the dataset for analysis.

### 5. Fee Generation

I applied a lambda function to generate fees for the universities based on their type (Federal, State, Private, Uniform).

### 6. Data Storage

The final transformed dataset was saved as a CSV file locally for further analysis. Additionally, the data was sent to a PostgreSQL database for storage.

## Usage

### Prerequisites

- Python
- BeautifulSoup
- pandas
- PostgreSQL

### Installation

```bash
pip install beautifulsoup4 pandas psycopg2
```

### Execution

```bash
python web_scraper.py
```

## File Structure

- `web_scraper.py`: Python script for web scraping and data transformation.
- `transformed_data.csv`: Final dataset after cleaning and manipulation.
- `README.md`: Project documentation.

## Acknowledgments

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

