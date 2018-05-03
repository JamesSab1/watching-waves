from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup


def videos(request):
    html = urlopen(
        'https://www.youtube.com/channel/UCSX640dbdNQ62S8Mg77d93A/videos')
    bsobj = BeautifulSoup(html, 'lxml')

    links_list = []

    try:
        for link in bsobj.findAll('a'):
            if '/watch?v=' in link.attrs['href']:
                links_list.append(link.attrs['href'])
    except TypeError:
        print('nowt there')

    video_list = []

    for link in links_list:
        link = link[9:]
        video_list.append(link)

    return render(request, 'watch_videos/videos.html', {'video_list':
                                                        video_list})
