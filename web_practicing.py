from bs4 import BeautifulSoup
import requests
import time



def find_job():
    no_skills = []
    have_unfamiliar_skills = False
    while True:
            try:
                num_skills = int(input("Put number of skills that you are unfamiliar with: "))
                if num_skills > 0:
                    break
                else:
                    print('You have to enter a number greater than 0')
            except ValueError:
                print("Invalid input. Please enter a number.")

    for i in range(num_skills):
        unfamiliar_skill = input(f"Put skill {i+1} that you are unfamiliar with: ")
        no_skills.append(unfamiliar_skill.lower())  # Convert to lowercase for case-insensitive comparison
        print(f"Filtering out {unfamiliar_skill}")

    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml' )
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs): 
        published_date = job.find('span',class_ = 'sim-posted').span.text

        if 'few' in published_date:
            
            skills_requirement = job.find('span', class_ = 'srp-skills').text.replace(' ','')

            for skill in no_skills:
                if skill in skills_requirement:
                    have_unfamiliar_skills = True
                    
            with open(f"posts/{index}.txt",'w') as f:        
                if not have_unfamiliar_skills:
                    company_name = job.find('h3',class_ = "joblist-comp-name").text.replace(' ','')
                    more_info = job.h2.a['href']        
                    f.write(f'Company name: {company_name.strip()}')
                    f.write(f"skills required: {skills_requirement.strip()}")
                    f.write(f"More info: {more_info}")
                else:
                    continue

if __name__ == '__main__':
    find_job()
    time_wait = 3
    print(f"Waiting time is {time_wait} minutes")
    time.sleep(time_wait*60)