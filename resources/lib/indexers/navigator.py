import sys
from os import path

import xbmcvfs

from resources.lib import control
from resources.lib.tools import cParser

sysaddon = sys.argv[0]
syshandle = int(sys.argv[1]) if len(sys.argv) > 1 else ''
artPath = control.artPath()
addonFanart = control.addonFanart()

class navigator:
	def root(self):
		self.addDirectoryItem("Szukaj filmów", 'moviesSearch', '01_suche_filme.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem("Szukaj seriali", 'tvshowsSearch', '02_suche_tv_serien.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem("Szukaj osoby / aktora", 'personSearch', '03_darsteller_suche_nach_person.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem("Filmy", 'movieNavigator', '04_filme.png', 'DefaultMovies.png')
		self.addDirectoryItem("Seriale", 'tvNavigator', '05_tv_serien.png', 'DefaultTVShows.png')
		self.addDirectoryItem("LIVE-TV", 'liveTVNavigator', 'DefaultTVShows.png', 'DefaultTVShows.png')
		self.addDirectoryItem("LiveTV lite", 'liveTVLiteNavigator', 'DefaultTVShows.png', 'DefaultTVShows.png')
		self.addDirectoryItem("Odtwórz adres URL streamu", 'playURL', '07_stream_url_abspielen.png', 'DefaultAddonWebSkin.png', isFolder=False)
		self.addDirectoryItem("Narzędzia", 'toolNavigator', '06_werkzeuge.png', 'DefaultAddonProgram.png')
		self._endDirectory(content='', cache=False)

	def movies(self):
		self.addDirectoryItem("[B]Filmy[/B] - Nowe", 'listings&media_type=movie&url=kino', '04_01_filme_neu.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem("[B]Filmy[/B] - Rok", 'movieYears', '04_02_filme_jahr.png', 'DefaultMovies.png')
		self.addDirectoryItem("[B]Filmy[/B] - Gatunki", 'movieGenres', '04_03_filme_genres.png', 'DefaultMovies.png')
		self.addDirectoryItem("[B]Filmy[/B] - Najpopularniejsze", 'listings&media_type=movie&url=production_status=released%26sort_by=popularity.desc', '04_04_filme_am_populaersten.png', 'DefaultMovies.png')
		self.addDirectoryItem("[B]Filmy[/B] - Najwyżej oceniane", 'listings&media_type=movie&url=production_status=released%26sort_by=vote_average.desc', '04_05_filme_am_besten_bewertet.png', 'DefaultMovies.png')
		self.addDirectoryItem("[B]Filmy[/B] - Najczęściej oceniane", 'listings&media_type=movie&url=production_status=released%26sort_by=vote_count.desc', '04_06_filme_meist_bewertet.png', 'DefaultMovies.png')
		self.addDirectoryItem("[B]Filmy[/B] - Największe przychody", 'listings&media_type=movie&url=production_status=released%26sort_by=revenue.desc', '04_07_filme_bestes_einspielergebnis.png', 'DefaultMovies.png')
		if control.getSetting('trakt.watchlist.menu', 'true') == 'true':
			self.addDirectoryItem("[B]Trakt[/B] - Lista obserwowanych filmów", 'traktList&type=watchlist&media_type=movie', '04_filme.png', 'DefaultMovies.png')
		if control.getSetting('trakt.collection.menu', 'true') == 'true':
			self.addDirectoryItem("[B]Trakt[/B] - Kolekcja filmów", 'traktList&type=collection&media_type=movie', '04_filme.png', 'DefaultMovies.png')
		self._endDirectory()

	def tvshows(self):
		self.addDirectoryItem("[B]Seriale[/B] - Gatunki", 'tvGenres', '05_01_serien_genres.png', 'DefaultTVShows.png')
		self.addDirectoryItem("[B]Seriale[/B] - Najpopularniejsze", 'listings&media_type=tv&url=sort_by=popularity.desc', '05_02_serien_am_populaersten.png', 'DefaultTVShows.png')
		self.addDirectoryItem("[B]Seriale[/B] - Najwyżej oceniane", 'listings&media_type=tv&url=sort_by=vote_average.desc', '05_03_serien_am_besten_bewertet.png', 'DefaultTVShows.png')
		self.addDirectoryItem("[B]Seriale[/B] - Najczęściej oceniane", 'listings&media_type=tv&url=sort_by=vote_count.desc', '05_04_serien_meist_bewertet.png', 'DefaultTVShows.png')
		if control.getSetting('trakt.watchlist.menu', 'true') == 'true':
			self.addDirectoryItem("[B]Trakt[/B] - Lista obserwowanych seriali", 'traktList&type=watchlist&media_type=tv', '05_tv_serien.png', 'DefaultTVShows.png')
		if control.getSetting('trakt.collection.menu', 'true') == 'true':
			self.addDirectoryItem("[B]Trakt[/B] - Kolekcja seriali", 'traktList&type=collection&media_type=tv', '05_tv_serien.png', 'DefaultTVShows.png')
		self._endDirectory()

	def tools(self):
		self.addDirectoryItem("[B]Wsparcie[/B]: pokaż informacje", 'pluginInfo', '06_01_support_informationen_anzeigen.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem("[B]Wsparcie[/B]: utwórz i prześlij pakiet", 'supportUpload', '06_01_support_informationen_anzeigen.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(control.addonName +": USTAWIENIA", 'addonSettings', '06_02_xvault_einstellungen.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem("[B]Resolver[/B]: USTAWIENIA", 'resolverSettings', '06_03_resolver_einstellungen.png', 'DefaultAddonProgram.png', isFolder=False)
		self._endDirectory()

	def downloads(self):
		movie_downloads = control.getSetting('download.movie.path')
		tv_downloads = control.getSetting('download.tv.path')
		if len(control.listDir(movie_downloads)[0]) > 0:
			self.addDirectoryItem("Filmy", movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
		if len(control.listDir(tv_downloads)[0]) > 0:
			self.addDirectoryItem("Seriale", tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)
		self._endDirectory()

	def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
		url = '%s?action=%s' % (sysaddon, query) if isAction else query
		thumb = self.getMedia(thumb, icon)
		listitem = control.item(name, offscreen=True)
		listitem.setArt({'poster': thumb, 'icon': icon})
		if context is not None:
			cm = []
			cm.append((context[0], 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
			listitem.addContextMenuItems(cm)

		isMatch, sPlot = cParser.parseSingleResult(query, "plot'.*?'([^']+)")
		if not isMatch: sPlot = '[COLOR blue]{0}[/COLOR]'.format(name)
		if isFolder:
			listitem.setInfo('video', {'overlay': 4, 'plot': control.unquote_plus(sPlot)})
			listitem.setIsFolder(True)
		else:
			listitem.setProperty('IsPlayable', 'false')
		self.addFanart(listitem, query)
		control.addItem(syshandle, url, listitem, isFolder)

	def _endDirectory(self, content='', cache=True):
		control.content(syshandle, content)
		control.plugincategory(syshandle, control.addonName + ' / '+ control.addonVersion)
		control.endofdirectory(syshandle, succeeded=True, cacheToDisc=cache)

	def addFanart(self, listitem, query):
		if control.getSetting('fanart')=='true':
			isMatch, sFanart = cParser.parseSingleResult(query, "fanart'.*?'([^']+)")
			if isMatch:
				sFanart = self.getMedia(sFanart)
				listitem.setProperty('fanart_image', sFanart)
			else:
				listitem.setProperty('fanart_image', addonFanart)

	def getMedia(self,mediaFile=None, icon=None):
		if xbmcvfs.exists(path.join(artPath, mediaFile)): mediaFile = path.join(artPath, mediaFile)
		elif xbmcvfs.exists(path.join(artPath, 'sites', mediaFile)): mediaFile = path.join(artPath, 'sites', mediaFile)
		elif mediaFile.startswith('http'): return mediaFile
		else: mediaFile = icon
		return mediaFile
	

