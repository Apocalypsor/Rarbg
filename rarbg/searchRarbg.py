# -*- coding: utf-8 -*-

import rarbgapi

from .rss import getRSS

client = rarbgapi.RarbgAPI()

modes = {
    'search_string',
    'search_imdb',
    'search_tvdb',
    'search_themoviedb'
}

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

def getResult(mode, searchObj=None, categoryObj=None):
    try:
        if mode in modes:
            categoryError = None

            if categoryObj:
                categoryValid = set(categories.keys()) & categoryObj

                if categoryValid:
                    searchKw = {
                        mode: searchObj,
                        'categories': [categories[c] for c in categoryValid]
                }
                else:
                    categoryError = 'No Valid Categories!'

            else:
                searchKw = {mode: searchObj}

            if categoryError:
                status, output = False, categoryError
            else:
                result = client.search(**searchKw)
                status, output = True, getRSS(result)

        else:
            result = client.list(limit=50)
            status, output = True, getRSS(result)

        return status, output

    except Exception as e:
        return False, e

if __name__ == '__main__':
    print('rarbg.to')
