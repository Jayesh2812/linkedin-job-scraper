from bs4 import BeautifulSoup as bs
import requests
output = open('output.txt','w',encoding='utf-8')

base_url = "https://www.linkedin.com/jobs/"

keywords = "%2C".join(['django'])
location = "%2C".join(['Mumbai'])
pageNum = '0'

url = f"{base_url}search?keywords={keywords}&location={location}&pageNum={pageNum}&redirect=false&position=1"

classname = 'jobs-search__results-list'
response = requests.get(url)

content = bs(response.content, "html.parser")

jobs_list_container = content.find(class_=classname)
jobs_list = jobs_list_container.find_all('li')

for job in jobs_list:
    output.write("JOB TITLE: "+ job.div.h3.text+"\n")
    output.write("COMPANY: "+ job.div.h4.text+"\n")
    output.write("JOB POSTER'S NAME: ")

    second_response = requests.get(job.a['href'])
    job_poster_content = bs(second_response.content, "html.parser").find(class_="base-main-card")


    if job_poster_content:
        output.write(job_poster_content.div.h3.text)
    else:
        output.write('NULL')

    output.write('\n')
    output.write("JOB POSTER'S LINKEDIN URL: ")
    if job_poster_content:
        output.write('https://in.linkedin.com/in/')
        raw_link = job_poster_content.a['href']
        user_name = raw_link[89 : raw_link.find('&')]
        output.write(user_name)
    else:
        output.write('NULL')
    
    output.write('\n\n')
print('Status Code:',response.status_code)


