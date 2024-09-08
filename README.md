# Web Scraper

## Project Overview
Web Scraper is an application built using FastAPI and Next.js, designed to retrieve product data from e-commerce websites like BestBuy and Newegg. Users can input a product name and view search results that include the site, item title, and price. This project demonstrates the ability to scrape data from external websites, aggregate it, and present it to users in an organized table.

## Features
- **Product Search:** Users can search for products by entering a product name in the search input field.
- **Data Display:** The results include the name of the e-commerce site, product title, and price, displayed in a table.
- **Scraping Multiple Websites:** Retrieves product information from both BestBuy and Newegg.
- **FastAPI Backend:** The backend is implemented using FastAPI to scrape and provide the product data via an API.
- **Next.js Frontend:** The frontend is built using Next.js, handling user input and displaying search results.
- **Session Storage:** Results are stored in `sessionStorage` to persist between navigation.

## Project Structure
```plaintext
webScraper/
├── pages/
│   ├── index.js               # Main page for product search input
│               # Results page for displaying product data
│
├── .next/                     # Next.js build directory
├── main.py                    # FastAPI backend for scraping
├── package.json               # Project dependencies
├── pyenv.cfg                  # Python virtual environment config
└── README.md                  # Project documentation
```

## Installation & Setup

### Prerequisites
- **Node.js:** Ensure Node.js is installed on your machine.
- **Python:** Ensure Python 3.x is installed.
- **FastAPI & Required Libraries:** You need to install FastAPI, BeautifulSoup, and other required libraries for the backend.

Install the Python dependencies with the following command:
bash
pip install fastapi uvicorn beautifulsoup4 requests

## Step 1: Clone the Repository
Clone this repository using Git:
git clone https://github.com/yairTzach/webScraper.git

## Step 2: Install Dependencies
Navigate to the project directory and install the necessary Node.js and Python dependencies.

For Node.js dependencies:
npm install

## Step 3: Start the FastAPI Backend Server
Start the FastAPI server to handle the scraping API:


uvicorn main:app --reload
## Step 4: Start the Next.js Frontend
In another terminal, run the following command to start the Next.js frontend development server:

npm run dev
## Step 5: Access the Application
Once both the backend and frontend are running, you can access the application in your browser at:

http://localhost:3000

How the Application Works
Product Search: Users input a product name on the main page.
Backend Scraping: The frontend sends an API request to the FastAPI backend, which scrapes product data from e-commerce websites like BestBuy and Newegg.
Data Retrieval: The scraped data is returned to the frontend and displayed in a table format.
Results Display: The results include the site name, product title, and price.

