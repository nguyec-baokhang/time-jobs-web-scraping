from bs4 import BeautifulSoup
import requests





no_skills = []
suitable_job = []

print("Put skill that you are unfamiliar with")
unfamiliar_skill = input(">")
no_skills.append(unfamiliar_skill)
print(f"Filterting out {unfamiliar_skill}")

print(no_skills)
def find_job():
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml' )
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span',class_ = 'sim-posted').span.text

        if 'few' in published_date:
            
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')

            if unfamiliar_skill not in skills:
                suitable_job.append(job)
            else:
                continue
    for job in suitable_job:
        company_name = job.find('h3',class_ = "joblist-comp-name").text.replace(' ','')
        more_info = job.h2.a['href']
                    
        print(f'Company name: {company_name.strip()}')
        print(f"skills required: {skills.strip()}")
        print(f"More info: {more_info}")

                
find_job()