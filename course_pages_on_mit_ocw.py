import re
from bs4 import BeautifulSoup
import os
import httplib2
def make_soup(s):
    http=httplib2.Http()
    status,response=http.request(s)
    page=BeautifulSoup(response)
    return page
def parse(s):
    flag=1
    lum1=''
    lum2=''
    soup1=make_soup(s)
    match=re.compile('download-course-materials')
    for link in soup1.findAll('a'):
        href=link['href']
        if re.search(match,href):
            lum='http://ocw.mit.edu'+href
            match2=re.compile('.zip')
            soup2=make_soup(lum)
            for link in soup2.findAll('a'):
                href1=link['href']
                if re.search(match2,href1):
                    lum2='http://ocw.mit.edu'+href1
                    print(lum2)
                    return lum2
    return ''
def course_pages_on_mit_ocw():
    f=open('mit.txt','w')
    s='http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/'
    soup1=make_soup(s)
    b=''
    match=re.compile('/courses/electrical-engineering-and-computer-science/')
    for link in soup1.findAll('a'):
        href=link['href']
        if re.search(match,href):
            a='http://ocw.mit.edu'+href
            if(a!=b):
                x=parse(a)
                b=a
                if(x!=''):
                    f.write(x)
                    f.write('\n')
    f.close()
course_pages_on_mit_ocw()
