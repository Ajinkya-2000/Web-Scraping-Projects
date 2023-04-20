from bs4 import BeautifulSoup as bs
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

# print(html_text)

soup = bs(html_text , 'lxml')
# jobs = soup.find_all('li' , class_ = 'clearfix job-bx wht-shd-bx')
# print(jobs)


def Find_jobs():

    jobs = soup.find_all('li' , class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span' , class_ = 'sim-posted').text.replace(' ','')
        if 'few' in published_date:
            company_name = job.find('h3' , class_ = 'joblist-comp-name').text.replace(' ','')
            skills = soup.find('span' , class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            with open('Information.txt' , 'a') as f:
                f.write(f"Company Name : {company_name.strip()}\n")
                f.write(f"Skills : {skills.strip()}\n")
                f.write(f"More Info : {more_info}\n")
                f.write(f"---------------------------------------------------------------------------------------------------\n")
    with open('Information.txt' , 'a') as f1:
        f1.write("\n")
        f1.write("****************************************New Info***********************************************************************************")
        f1.write("\n")
    print("Information Saved in file Information.txt")
                



# Function Call
Find_jobs()
       
