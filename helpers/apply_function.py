from helpers.applicant_class import Applicant
from playwright.async_api import async_playwright

async def apply_to_job(link: str, applicant: Applicant) -> None:
    """
    Automates the process of applying to a job using the given link and applicant details.

    This asynchronous function uses the Playwright library to automate the process of filling out
    a job application form on a webpage. The function navigates to the job application page,
    fills out the form fields with the provided applicant's details, and submits the application.

    Args:
        link (str): The URL of the job application page.
        applicant (Applicant): An object containing the applicant's details. The object should have the
                            following attributes: name (str), email (str), phone (str).

    Returns:
        None

    Example:
        class Applicant:
            def __init__(self, name, email, phone):
                self.name = name
                self.email = email
                self.phone = phone

        applicant = Applicant(name="John Doe", email="john.doe@example.com", phone="1234567890")
        await apply_to_job("https://example.com/apply", applicant)
    """
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
