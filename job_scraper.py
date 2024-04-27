from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def job_scraper(titles, url_link, list):
    for title in titles:
        page_num = 1
        while True:
            url = url_link.format(keyword=title.replace(' ','%20'), num=page_num)
            page = requests.get(url)
            if page.status_code == 200:
                print(f'Extracting data for {title} page {page_num}')
                
                soup = BeautifulSoup(page.text, 'html.parser')

                jobs = [title.text.strip() for title in soup.find_all(class_='pp-content-grid-post-title job_search_title')]
                pay_ranges = [pay_range.text.strip() for pay_range in soup.find_all(class_='job_search_salary_category')]
                links = [link.find('a')['href'] for link in soup.find_all(class_='job_seacrh_dual_buttons_row')]

                if not jobs:
                    break

                for job, pay_range, link in zip(jobs, pay_ranges, links):
                    list.append((job, pay_range, link))
                page_num += 1
            else:
                break
            time.sleep(2)