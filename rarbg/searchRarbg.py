# -*- coding: utf-8 -*-

import rarbgapi

from .rss import getRSS

client = rarbgapi.RarbgAPI()

categories = {
    'ADULT': rarbgapi.RarbgAPI.CATEGORY_ADULT,
    'MOVIE_XVID': rarbgapi.RarbgAPI.CATEGORY_MOVIE_XVID,
    'MOVIE_XVID_720P': rarbgapi.RarbgAPI.CATEGORY_MOVIE_XVID_720P,
    'MOVIE_H264': rarbgapi.RarbgAPI.CATEGORY_MOVIE_H264,
    'MOVIE_H264_1080P': rarbgapi.RarbgAPI.CATEGORY_MOVIE_H264_1080P,
    'MOVIE_H264_720P': rarbgapi.RarbgAPI.CATEGORY_MOVIE_H264_720P,
    'MOVIE_H264_3D': rarbgapi.RarbgAPI.CATEGORY_MOVIE_H264_3D,
    'MOVIE_H264_4K': rarbgapi.RarbgAPI.CATEGORY_MOVIE_H264_4K,
    'MOVIE_H265_4K': rarbgapi.RarbgAPI.CATEGORY_MOVIE_H265_4K,
    'MOVIE_H265_4K_HDR': rarbgapi.RarbgAPI.CATEGORY_MOVIE_H265_4K_HDR,
    'MOVIE_FULL_BD': rarbgapi.RarbgAPI.CATEGORY_MOVIE_FULL_BD,
    'MOVIE_BD_REMUX': rarbgapi.RarbgAPI.CATEGORY_MOVIE_BD_REMUX,
    'TV_EPISODES': rarbgapi.RarbgAPI.CATEGORY_TV_EPISODES,
    'TV_EPISODES_HD': rarbgapi.RarbgAPI.CATEGORY_TV_EPISODES_HD,
    'TV_EPISODES_UHD': rarbgapi.RarbgAPI.CATEGORY_TV_EPISODES_UHD,
    'MUSIC_MP3': rarbgapi.RarbgAPI.CATEGORY_MUSIC_MP3,
    'MUSIC_FLAC': rarbgapi.RarbgAPI.CATEGORY_MUSIC_FLAC,
    'GAMES_PC_ISO': rarbgapi.RarbgAPI.CATEGORY_GAMES_PC_ISO,
    'GAMES_PC_RIP': rarbgapi.RarbgAPI.CATEGORY_GAMES_PC_RIP,
    'GAMES_PS3': rarbgapi.RarbgAPI.CATEGORY_GAMES_PS3,
    'GAMES_PS4': rarbgapi.RarbgAPI.CATEGORY_GAMES_PS4,
    'GAMES_XBOX': rarbgapi.RarbgAPI.CATEGORY_GAMES_XBOX,
    'SOFTWARE': rarbgapi.RarbgAPI.CATEGORY_SOFTWARE,
    'EBOOK': rarbgapi.RarbgAPI.CATEGORY_EBOOK
}

def getResult(mode, search_obj=None, category_obj=None):
    try:
        if mode == 'title':
            if category_obj:
                category_valid = set(categories.keys()) & category_obj

                if category_valid:
                    result = client.search(search_string=search_obj, \
                        categories=[categories[c] for c in category_valid])
                    return True, getRSS(result)
                
                return False, 'No Valid Categories!'

            result = client.search(search_string=search_obj)
            return True, getRSS(result)

        elif mode == 'imdb':
            if category_obj:
                category_valid = set(categories.keys()) & category_obj

                if category_valid:
                    result = client.search(search_imdb=search_obj, \
                        categories=[categories[c] for c in category_valid])
                    return True, getRSS(result)

                return False, 'No Valid Categories!'

            result = client.search(search_imdb=search_obj)
            return True, getRSS(result)

        elif mode == 'tvdb':
            if category_obj:
                category_valid = set(categories.keys()) & category_obj

                if category_valid:
                    result = client.search(search_tvdb=search_obj, \
                        categories=[categories[c] for c in category_valid])
                    return True, getRSS(result)

                return False, 'No Valid Categories!'

            result = client.search(search_tvdb=search_obj)
            return True, getRSS(result)

        elif mode == 'tmdb':
            if category_obj:
                category_valid = set(categories.keys()) & category_obj

                if category_valid:
                    result = client.search(search_themoviedb=search_obj, \
                        categories=[categories[c] for c in category_valid])
                    return True, getRSS(result)

                return False, 'No Valid Categories!'

            result = client.search(search_themoviedb=search_obj)
            return True, getRSS(result)

        result = client.list(limit=50)
        return True, getRSS(result)

    except Exception as e:
        return False, e

if __name__ == '__main__':
    print('rarbg.to')
