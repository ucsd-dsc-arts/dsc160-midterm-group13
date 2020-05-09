from bs4 import BeautifulSoup
import os
import requests

DATA_DIR = 'data'
toy_story_4_base = 'https://i0.wp.com/caps.pictures/201/9-toystory4/full/toystory4-animationscreencaps.com-{num}.jpg?strip=all'

scenes = [x*100+10 for x in range(10)]

def scrape(movie_base, movie_name):
    movie_dir = os.path.join(DATA_DIR, movie_name)
    if os.path.isdir(movie_dir) == False:
        os.mkdir(movie_dir)
    for start in scenes:
        for i in range(start, start + 10):
                img_path = movie_base.format(num = i)
                out_file = os.path.join(movie_dir, '{x}.jpg'.format(x=i))
                temp = requests.get(img_path, out_file)
                print(out_file)
                if not os.path.exists(out_file):
                    with open(out_file, 'wb') as f:
                        f.write(temp.content)

scrape(toy_story_4_base, 'toy_story_4')
