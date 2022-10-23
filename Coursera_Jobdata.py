# Importing beautifulsoup and urllib libraries
import urllib.request
import bs4 as bs

# Opening and reading the URL, then passing the html parser
URL = "https://boards.greenhouse.io/embed/job_board?for=coursera"
source = urllib.request.urlopen(URL).read()
soup = bs.BeautifulSoup(source, 'html5lib')

# Using an API to get all the required urls
url_list = []
for url in soup.find_all('a'):
    url_list.append(url.get('href'))

# Finding all the job tokens which are located at the end of the link
job_tokens = []
for i in range(len(url_list)):
    job_tokens.append(url_list[i][47:])

# Creating a list to store all the job data
job_data = []
# Going through every url in url_list and extracting the data
for i in range(len(url_list)):
    link = "https://boards.greenhouse.io/embed/job_app?for=coursera&token="+job_tokens[i]
    _source = urllib.request.urlopen(link).read()
    _soup = bs.BeautifulSoup(_source, 'html5lib')
    # Findng the intro and the job data using find and findall functions
    content_intro = (_soup.find('span',  attrs = {'style':'font-weight: 400;'}))
    content_data = (_soup.findAll('li',  attrs = {'style':'font-weight: 400;'}))
    string_1 = str(i+1)
    # This string gives the title of the webpage
    string_2 = _soup.title.get_text()
    string_3 = content_intro.get_text()
    # Combining all the strings to append them to the job_data list
    list = string_1 +") "+string_2+"\n\nDescription:\n"+string_3+"\n\nResponsibilities & Qualifications:\n"
    # Traversing through the content_data list and updating our string list
    for i in content_data:
        list = list + i.get_text()+"\n"
    job_data.append(list)
print(job_data)
