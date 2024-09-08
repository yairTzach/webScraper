import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

headers = {
  # changing user agent for not getting blocked by the site.
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
}


app = FastAPI()

origins = [
    "http://localhost:3000",  # Allow frontend address
    "http://127.0.0.1:3000"   # Allow frontend address using a different common hostname
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allow multiple methods
    allow_headers=["*"],  # Allow all headers
)




@app.get("/search/{product_name}")
def search(product_name: str):

        bestbuy_results = search_bestbuy(product_name)
       # walmart_results = search_walmart(product_name)
        newegg_results = search_newegg(product_name)
        combined_results = bestbuy_results + newegg_results #walmart_results + newegg_results
        return combined_results

def search_bestbuy(product_name):
  session = requests.Session()
  results = []

  # url for search in best buy
  URL = "https://www.bestbuy.com/?intl=nosplash"

  session.get(URL, headers=headers)

  URL1 = "https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&st={}".format('-'.join(product_name.split()))

  response = session.get(URL1 , headers=headers)

  # makes sure that of using the appropriate parser for HTML content
  soup = BeautifulSoup(response.content, "html.parser")

  product_list = soup.find_all("li" , class_="sku-item") # Adjust as per page structure
  if product_list:
    first_product = product_list[0]

    # Extract details about the first product
    product_link = first_product.find("a", class_="image-link")  # This class might be more stable
    if product_link:
       product_page_url = "https://www.bestbuy.com" + product_link.get("href")  # Use .get for safer attribute access

    product_price = first_product.find('div', {'class': 'sku-list-item-price'}).find('span').text.strip()
    results.append({"Site": "BestBuy", "Item title name": product_page_url, "Price(USD)": product_price})
    return results
  else:
      results.append({"Site": "BestBuy", "Item title name": f"No results for {product_name} in BestBuy site!",
                      "Price(USD)": ""})

      return results

'''
def search_walmart(product_name):
    results = []

    # Correct search URL for Walmart with query
    URL = "https://www.walmart.com/search?q={}".format('-'.join(product_name.split()))
    page = requests.get(URL, headers=headers)

    # Check if the page content loaded correctly
    if page.status_code != 200:
        print(f"Failed to retrieve Walmart page. Status code: {page.status_code}")
        results.append(
            {"Site": "Walmart", "Item title name": f"No results for {product_name} in Walmart site!", "Price(USD)": ""})
        return results

    soup = BeautifulSoup(page.content, "html.parser")

    # New product list selectors, adjusted for Walmart's current structure
    product_list = soup.find_all("div", class_="search-result-gridview-item-wrapper")

    if product_list:
        first_product = product_list[0]

        # Get the product title and link
        product_link = first_product.find("a", class_="product-title-link")
        if product_link:
            product_page_url = "https://www.walmart.com" + product_link.get("href")
            product_title = product_link.get_text().strip()

        # Get the product price (try multiple possible classes for price)
        product_price = first_product.find("span", class_="price-characteristic")
        if product_price:
            product_price = product_price.get_text().strip()
        else:
            product_price = "N/A"

        # Append the extracted data to the results list
        results.append({"Site": "Walmart", "Item title name": product_title, "Price(USD)": f"${product_price}",
                        "URL": product_page_url})
        return results
    else:
        # No products found, return an empty result
        results.append(
            {"Site": "Walmart", "Item title name": f"No results for {product_name} in Walmart site!", "Price(USD)": ""})
        return results

'''
def search_newegg(product_name):
  results=[]

  URL = "https://www.newegg.com/p/pl?d={}".format('-'.join(product_name.split()))
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, "html.parser")
  product_list3 = soup.find_all("div" , class_="item_cell_9SIA4REJSX0480_2_1")
  product_list2 = soup.find_all("div",class_="item-cell")
  product_list = soup.find_all("div",class_="item-cell is-blackfriday")
  product_list.extend(product_list2)
  product_list.extend(product_list3)

  if product_list:
    first_product = product_list[0]
    product_price = first_product.find("li", class_='price-current').text.strip()
    product_price = product_price[:-2]
    product_page_anchor = first_product.find("a", class_="item-title")  # This class might be more stable
    if product_page_anchor:
      product_page_url = product_page_anchor.get("href")  # Use .get for safer attribute access
      # Visit the product page URL
      product_page = requests.get(product_page_url, headers=headers)
      product_soup = BeautifulSoup(product_page.content, "html.parser")
      results.append({"Site": "Newegg", "Item title name": product_page_url, "Price(USD)": product_price})
      return results
  else:
      results.append({"Site": "Newegg", "Item title name": f"No results for {product_name} in Newegg site!",
                      "Price(USD)": ""})
      return results

