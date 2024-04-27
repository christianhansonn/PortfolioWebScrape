import asyncio
from playwright.async_api import async_playwright

async def apply_to_job(link, applicant):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(link)
        await page.wait_for_selector("button[name='APPLY NOW']")
        await page.click("button[name='APPLY NOW']")
        await page.fill("input[name='First Name']", applicant.name.split(' ')[0])
        await page.fill("input[name='Last Name']", applicant.name.split(' ')[1])
        await page.fill("input[name='Email']", applicant.email)
        await page.fill("input[name='Telephone']", applicant.phone)
        await page.set_input_files("input[name='Resume']", "/path/to/resume.pdf")
        await page.select_option("select[name='Specialisms']", "Technology")
        await page.select_option("select[name='Locations']", "United States")
        await page.select_option("select[name='Permanent/Contract']", "Permanent but open to Contract")
        await page.check("input[name='I confirm that I am legally allowed to work in this country']")
        await page.click("button[type='submit']")
        await context.close()
        await browser.close()
