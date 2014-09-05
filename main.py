import csv
import requests
from pyquery import PyQuery as pq

SW_URL = 'http://www.somewhereinblog.net/blog/'
BLOG_ID = 'zobayrasadgit push -u origin master'

BLOG_URL = 'http://www.somewhereinblog.net/blog/getProfilePosts/'

POST_ID_LIST = []
 
MAX_NUMBER = 100

def get_last_post_id():
    if len(POST_ID_LIST)>0:
        return POST_ID_LIST[len(POST_ID_LIST)-1]
    return 0
    
def get_cookies():
    resp = requests.get(SW_URL+BLOG_ID)
    return resp.cookies
    
def get_first_page():
    url = SW_URL+BLOG_ID
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content)
        archive_panel = soup.find('div', {'id':'rightpanel'})
        post_headings = archive_panel.findAll('h1')
        for post in post_headings:
            print post
            
    return

def prepare_post_list(post_links):
    for link in post_links:
        li_a = link.attrib.get('href').strip().split('#')
        if len(li_a) > 1:
            li_len = len(li_a[0].split('/'))
            POST_ID_LIST.append(li_a[0].split('/')[li_len-1])
    return
    
def do_post():
    offset = 14
    headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
            'X-Requested-With':'XMLHttpRequest'}
    
    post_id = get_last_post_id()
    
    BASE = 15
    for i in enumerate(range(0, MAX_NUMBER, 14)):
       if i[0] > 0:
           offset = i[1]+i[0]-1
           postcount = i[1]+i[0]
           resp = requests.post(BLOG_URL, data={'blog':BLOG_ID, 'offset':offset, 'table':'archive_posts',
                   'last_posts_id':post_id, 'current_posts_count':postcount}, headers=headers)

           data = pq(resp.content)

           post_links = data('a')
           prepare_post_list(post_links)


    with open("posts.csv",'wb') as f:
        wr = csv.writer(f)
        wr.writerow(POST_ID_LIST)

    print "DONE!!"

    
def main():
    request_counter = 0
    if request_counter == 0:
        get_first_page()
    return 


if __name__=='__main__':
    # get_first_page()
    do_post()