from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def job_scraper(titles: list, url_link: str) -> list[list[str]]:
    """
    Scrapes job postings from a specified URL and appends them to a given list.

    This function takes a list of job titles, formats a URL with each title, and scrapes job postings,
    including job titles, pay ranges, and links to job details from the webpage. The results are appended
    to the provided list.

    Args:
        titles (list): A list of job titles to search for.
        url_link (str): The URL template containing placeholders for the job title and page number.
                        Example: 'https://example.com/jobs?keyword={keyword}&page={num}'
        list (list): The list to which the scraped job details will be appended. Each element in the list
                     will be a tuple containing the job title, pay range, and link to the job details.

    Returns:
        list[list[str]]: List of job titles, pay range, and application link

    Example:
        >>> titles = ["Data Scientist", "Software Engineer"]
        >>> url_link = 'https://example.com/jobs?keyword={keyword}&page={num}'
        >>> job_list = []
        >>> job_scraper(titles, url_link, job_list)
        >>> print(job_list)
        [
            ["Software Engineer", "$100,000-$120,000","https://example.com/software_engineer"],
            ["Sr. Software Engineer", "$140,000-$200,000","https://example.com/sr_software_engineer"]
        ]
    """
    job_data = []

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
                    job_data.append((job, pay_range, link))
                page_num += 1
            else:
                break
            time.sleep(2)
            
    return job_data