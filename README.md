![Jumia Logo](https://1.bp.blogspot.com/-3yr6lXiWQ_k/VfAwsiQ6hFI/AAAAAAAAAi8/rlOfxY02MIU/s1600/Jumia%2BLogo.png)

# Jumia Appliances Web Scraping Project

## Introduction & Objectives
Jumia is one of Africa’s leading e-commerce platforms, offering a wide range of products including household appliances. Gaining insights into the pricing and product details listed on Jumia can be invaluable for market analysis, competitive benchmarking, and consumer decision-making.

This project demonstrates a simple scraping of appliance names and prices from the Jumia Appliances page and saving as a csv file using Python. By analysing the extracted data, we can identify pricing trends, understand product availability, and evaluate the competitive positioning of various appliances on the platform.

### Key Objectives:
- Extract product names and prices for appliances on the Jumia platform.
- Present the scraped data in a structured and easy-to-read format.
- Save the scraped data to a CSV file for further analysis and storage.
- Demonstrate foundational web scraping techniques using `requests` and `BeautifulSoup`.

## Data Collection Process
The dataset was collected using web scraping methods:

### Data Source:
- [Jumia Appliances Page](https://www.jumia.com.ng/mlp-appliances/)

### Tools Used:
- `requests` for fetching webpage content.
- `BeautifulSoup` for parsing and extracting HTML elements.

### Approach:
- Scraped appliance names and prices using HTML class attributes for specific elements ("name" and "prc").
- Displayed the data in a readable format directly in the console.

## Questions and Results
This project addresses the following questions:

1. **What appliances and their prices are listed on the Jumia appliances page?**
   - Scraped and displayed the product names alongside their respective prices.

2. **How can we extract and display the data in a readable format?**
   - Utilised Python’s `zip` function to pair product names with prices and format the output for readability.

## Code Workflow

### 1. Fetch Webpage Content
- The script sends an HTTP GET request to the Jumia Appliances page and retrieves the raw HTML content.

### 2. Parse HTML with BeautifulSoup
- BeautifulSoup parses the HTML to extract elements with specific class attributes ("name" for products, "prc" for prices).

### 3. Format and Display Data
- The script pairs appliance names and prices using the `zip` function and prints them in the format:

```plaintext
Appliance Name - Price
```

## Key Insight
- Demonstrated how web scraping techniques can simplify market research and data collection.

## Limitations
- **Static HTML Dependency**: The script relies on the static structure of the webpage. Any changes to the HTML may require code adjustments.
- **Single Page Scraping**: Currently, the script scrapes only the first page of results.

## Acknowledgements
- **Jumia Nigeria**: For providing the platform used for web scraping.
- **BeautifulSoup Documentation**: [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- **Requests Documentation**: [https://docs.python-requests.org/](https://docs.python-requests.org/)

