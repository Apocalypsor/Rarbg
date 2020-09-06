# -*- coding: utf-8 -*-

from feedgen.feed import FeedGenerator

feed = FeedGenerator()

feed.title('Customed RARBG Torrent Feed')
feed.link(href='https://github.com/Apocalypsor/Rarbg')
feed.description('Make RARBG Greater Again! by Apocalypsor')
feed.language('en')

def getRSS(entries):
    for entry in entries:
        feedEntry = feed.add_entry()
        feedEntry.title(entry.filename)
        feedEntry.link(href=entry.download)
        feedEntry.guid(entry.download)

    response = feed.rss_str(pretty=True)

    return response

if __name__ == '__main__':
    print('rarbg.to')
    