# -*- coding: utf-8 -*-

from feedgen.feed import FeedGenerator

feed = FeedGenerator()

feed.title('Customed RARBG Torrent Feed')
feed.link(href='https://github.com/Apocalypsor/Rarbg')
feed.description('Make RARBG Greater Again! by Apocalypsor')
feed.language('en')

def getRSS(result):
    for r in result:
        fg = feed.add_entry()
        fg.title(r.filename)
        fg.link(href=r.download)
        fg.guid(r.download)

    response = feed.rss_str(pretty=True)

    return response

if __name__ == '__main__':
    print('rarbg.to')
    