# -*- coding: utf-8 -*-

import urlparse, sys, urllib, xbmc, xbmcaddon, xbmcgui

dialog = xbmcgui.Dialog()

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?', '')))

mode = params.get('mode')

action = params.get('action')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0", "1") else 0


if action is None:
    from resources.lib.indexers import navigator
    from resources.lib.modules import cache
    cache.cache_version_check()
    navigator.navigator().root()

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)

elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows()

elif action == 'livetvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().livetvNavigator()

elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows(lite=True)

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()

elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().settings()

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()

elif action == 'clearCacheSearch':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheSearch()

elif action == 'clearMetaCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheMeta()

elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')

elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies
    movies.movies().widget()

elif action == 'movieSearch':
    from resources.lib.indexers import movies
    movies.movies().search()

elif action == 'movieSearchnew':
    from resources.lib.indexers import movies
    movies.movies().search_new()

elif action == 'movieSearchterm':
    from resources.lib.indexers import movies
    movies.movies().search_term(name)

elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies
    movies.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies
    movies.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies
    movies.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies
    movies.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies
    movies.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()

elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search()

elif action == 'tvSearchnew':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_new()

elif action == 'tvSearchterm':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_term(name)

elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().userlists()

elif action == 'seasons':
    from resources.lib.indexers import episodes
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    from resources.lib.indexers import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    from resources.lib.indexers import episodes
    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    from resources.lib.indexers import episodes
    episodes.episodes().widget()

elif action == 'calendars':
    from resources.lib.indexers import episodes
    episodes.episodes().calendars()

elif action == 'episodeUserlists':
    from resources.lib.indexers import episodes
    episodes.episodes().userlists()

elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url, windowedtrailer)

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()

elif action == 'changelog':
    from resources.lib.indexers import navigator
    navigator.navigator().changelog()

elif action == 'smuSettings':
    try:
        import resolveurl
    except:
        pass
    resolveurl.display_settings()

elif action == 'urlResolver':
    try:
        import resolveurl
    except:
        pass
    resolveurl.display_settings()

elif action == 'urlResolverRDTorrent':
     from resources.lib.modules import control
     control.openSettings(query, "script.module.resolveurl")

elif action == 'download':
    import json
    from resources.lib.modules import sources
    from resources.lib.modules import downloader
    try:
        downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except:
        pass

elif action == 'play':
    from resources.lib.modules import sources
    sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)

elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.modules import sources
    sources.sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.modules import sources
    sources.sources().clearSources()

elif action == 'random':
    rtype = params.get('rtype')
    if rtype == 'movie':
        from resources.lib.indexers import movies
        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'episode':
        from resources.lib.indexers import episodes
        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'season':
        from resources.lib.indexers import episodes
        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=episode"
    elif rtype == 'show':
        from resources.lib.indexers import tvshows
        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=season"
    from resources.lib.modules import control
    from random import randint
    import json
    try:
        rand = randint(1, len(rlist))-1
        for p in ['title', 'year', 'imdb', 'tvdb', 'season', 'episode', 'tvshowtitle', 'premiered', 'select']:
            if rtype == "show" and p == "tvshowtitle":
                try:
                    r += '&'+p+'='+urllib.quote_plus(rlist[rand]['title'])
                except:
                    pass
            else:
                try:
                    r += '&'+p+'='+urllib.quote_plus(rlist[rand][p])
                except:
                    pass
        try:
            r += '&meta='+urllib.quote_plus(json.dumps(rlist[rand]))
        except:
            r += '&meta='+urllib.quote_plus("{}")
        if rtype == "movie":
            try:
                control.infoDialog(rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except:
                pass
        elif rtype == "episode":
            try:
                control.infoDialog(rlist[rand]['tvshowtitle']+" - Season "+rlist[rand][
                    'season']+" - "+rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except:
                pass
        control.execute('RunPlugin(%s)' % r)
    except:
        control.infoDialog(control.lang(32537).encode('utf-8'), time=8000)

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().add(name, title, year, imdb, tmdb)

elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().range(url)

elif action == 'moviesToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libmovies().silent(url)

elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)

elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().range(url)

elif action == 'tvshowsToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libtvshows().silent(url)

elif action == 'updateLibrary':
    from resources.lib.modules import libtools
    libtools.libepisodes().update(query)

elif action == 'service':
    from resources.lib.modules import libtools
    libtools.libepisodes().service()

elif action == 'ustvgoNavigator':
    from resources.lib.indexers import ustvgo

    ustvgo.ustvgo().root()

elif action == 'ustvgoPlay':
    from resources.lib.indexers import ustvgo

    ustvgo.ustvgo().play(url)

elif action == 'acronaitv_menu':
    from resources.lib.indexers import acronaitv

    acronaitv.acronaitv().list_categories()

elif action == 'arconai_cable':
    from resources.lib.indexers import acronaitv

    acronaitv.acronaitv().list_cable()

elif action == 'arconai_shows':
    from resources.lib.indexers import acronaitv

    acronaitv.acronaitv().list_shows()

elif action == 'arconai_movies':
    from resources.lib.indexers import acronaitv

    acronaitv.acronaitv().list_movies()

elif action == 'arconai_play':
    from resources.lib.indexers import acronaitv

    acronaitv.acronaitv().play_video(params['selection'])

elif action == 'wrestlingNavigator':
    from resources.lib.indexers import watchwrestling

    watchwrestling.WatchWrestling().root()

elif action == 'wrestlingMenuLA':
    from resources.lib.indexers import watchwrestling

    watchwrestling.WatchWrestling().rootLA()

elif action == 'wrestlingMenuCZ':
    from resources.lib.indexers import watchwrestling

    watchwrestling.WatchWrestling().rootCZ()

elif action == 'wrestlingMenu24':
    from resources.lib.indexers import watchwrestling

    watchwrestling.WatchWrestling().root24()

elif action == 'wrestlingMenuAWL':
    from resources.lib.indexers import watchwrestling

    watchwrestling.WatchWrestling().rootAWL()

elif action == 'wrestlingScrape':
    from resources.lib.indexers import watchwrestling

    watchwrestling.WatchWrestling().scrape(url)

elif action == 'wrestlingPlay':
    from resources.lib.indexers import watchwrestling

    watchwrestling.WatchWrestling().play(url)

if action == 'entertainment':
    from resources.lib.indexers import lists

    lists.indexer().entertainment()

if action == 'movies':
    from resources.lib.indexers import lists

    lists.indexer().movies()

if action == 'kids':
    from resources.lib.indexers import lists

    lists.indexer().kids()

if action == 'sports':
    from resources.lib.indexers import lists

    lists.indexer().sports()

if action == 'news':
    from resources.lib.indexers import lists

    lists.indexer().news()

if action == 'music':
    from resources.lib.indexers import lists

    lists.indexer().music()

if action == 'foreign':
    from resources.lib.indexers import lists

    lists.indexer().foreign()

if action == 'pluto':
    from resources.lib.indexers import lists

    lists.indexer().pluto()

if action == 'theaters':
    from resources.lib.indexers import lists

    lists.indexer().theaters()

if action == 'navXXX':
    from resources.lib.indexers import lists

    lists.indexer().rootXXX()

elif 'youtube' in str(action):
    from resources.lib.indexers import lists

    lists.indexer().youtube(url, action)

elif action == 'lists_play':
    from resources.lib.indexers import lists
    lists.player().play(url, content)

if action == 'clicks':
    from resources.lib.indexers import lists
    lists.indexer().clicks()


def toggleAll(setting, query=None, sourceList=None):
    from resources.lib.sources import getAllHosters
    from resources.lib.modules import control
    sourceList = getAllHosters() if not sourceList else sourceList
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, setting)
    control.openSettings(query)


if mode == "toggleAllNormal":
    sourcelist = ['1movietv', '5movies', 'alluc', 'animetoon', 'cartoonhd', 'cmovieshd', 'divxcrawler', 'extramovies',
                  'fmoviesio', 'ganoolrip', 'iwannawatch', 'moviescouch', 'newepisodes', 'projectfreetv',
                  'seriesonline', 'streamdreams', 'streamsnow', 'swatchseries', 'telepisodes', 'timewatch',
                  'watchepisodes4', 'watchfree', 'watchseriessto', 'wsunblock', 'zmovies']
    toggleAll(params['setting'], params['query'], sourcelist)

if mode == "toggleAllDebrid":
    sourcelist = ['0dayreleases', '300mbdownload', '300mbfilms', 'ddlspot', 'directdl', 'maxrls', 'ganool',
                  'moviesleak', 'mvrls', 'rapidmoviez', 'rlsb', 'rlsbb', 'sceneddl', 'scenerls', 'tvdownload', 'ultrahd']
    toggleAll(params['setting'], params['query'], sourcelist)

if mode == "toggleAllDirect":
    sourcelist = ['d1dldrm', 'pz10028', 'pz10093', 's1dlserver', 's2dlserver']
    toggleAll(params['setting'], params['query'], sourcelist)

if mode == "toggleAllTorrent":
    sourcelist = ['1337x', 'btdb', 'btscene', 'doublr', 'eztv', 'glodls', 'idope', 'kickass2', 'limetorr', 'magnetdl',
                  'piratebay', 'skytorrents', 'topnow', 'torrapi', 'torrdown', 'torrentquest', 'yifyddl', 'ytsam',
                  'zoogle']
    toggleAll(params['setting'], params['query'], sourcelist)
