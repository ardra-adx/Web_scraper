import requests
from bs4 import BeautifulSoup

def scrape_remoteok_jobs():
    url = "https://remoteok.com/remote-dev-jobs"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for tr in soup.find_all("tr", class_="job"):
        title_tag = tr.find("h2")
        company_tag = tr.find("h3")
        location_tag = tr.find("div", class_="location")

        if title_tag and company_tag:
            jobs.append({
                "title": title_tag.text.strip(),
                "company": company_tag.text.strip(),
                "location": location_tag.text.strip() if location_tag else "Remote"
            })

    return jobs
