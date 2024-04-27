# Automating Job Applications with BeautifulSoup and Playwright

## Introduction

This project is to show case my skills with Python where I:

- Choose a job board
- Identify a list of job titles I'm interested in applying for
- Scrape job title, pay range, and job link for all returned search results
- Automate the application process for the list of jobs
- Create a very simple graph of the pay data

## Choosing Job Board and Job Titles

- You can see all steps laid out in this [Jupyter Notebook](https://github.com/christianhansonn/PortfolioWebScrape/blob/main/web_scrape.ipynb)

## Scraping Job Board

- I wrote this [Python script](https://github.com/christianhansonn/PortfolioWebScrape/blob/main/job_scraper.py) to call as a function to scrape the desired job board for chosen job titles
- Results were then returned and stored in a Pandas DataFrame

## Application Automation

- I wrote this [Python script](https://github.com/christianhansonn/PortfolioWebScrape/blob/main/apply_function.py) to call as a function to automate the application process, passing the job links as a variable
