from http.server import BaseHTTPRequestHandler
import requests
from bs4 import BeautifulSoup
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        url = "https://www.athle.fr/asp.net/main.html/html.aspx?htmlid=129"

        # Fetch the HTML content of the website
        response = requests.get(url)
        html_content = response.content

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the <div> with class="titlefr"
        div_titlefr = soup.findAll('div', class_='titlefr')

        # Check if the <div> exists and contains an <a> tag
        ok = False
        if div_titlefr:
            for div in div_titlefr:
                a_tag = div.find('a')
                if a_tag:
                    if "Championnats de France de 10 km" == a_tag.text:
                        print("Available!")
                        url = a_tag['href']
                        ok = True
        if ok:
            self.wfile.write(url.encode())
        else:
            self.wfile.write(("Not yet!").encode())
        return