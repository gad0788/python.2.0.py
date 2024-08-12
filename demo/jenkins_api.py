import jenkins

url = 'http://54.197.80.173:8080'
username= 'devops'
password= 'devops'
server = jenkins.Jenkins(url, username, password)
number_jobs=server.jobs_count()
#print(number_jobs)
user = server.get_whoami()
#print(user['fullName'])
jobs = server.get_jobs()
print(jobs)
for job in jobs:
    #print("*******************************************************")
    print(job['name'])
    print(job['url'])
    print(job['color'])
