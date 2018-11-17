# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
import generator
from BeautifulSoup import BeautifulStoneSoup , BeautifulSoup , BeautifulSOAP
try :
 from xml . sax . saxutils import escape
except : traceback . print_exc ( )
try :
 import json
except :
 import simplejson as json
import SimpleDownloader as downloader
import time
if 64 - 64: i11iIiiIii
OO0o = [ '180upload.com' , 'allmyvideos.net' , 'bestreams.net' , 'clicknupload.com' , 'cloudzilla.to' , 'movshare.net' , 'novamov.com' , 'nowvideo.sx' , 'videoweed.es' , 'daclips.in' , 'datemule.com' , 'fastvideo.in' , 'faststream.in' , 'filehoot.com' , 'filenuke.com' , 'sharesix.com' , 'docs.google.com' , 'plus.google.com' , 'picasaweb.google.com' , 'gorillavid.com' , 'gorillavid.in' , 'grifthost.com' , 'hugefiles.net' , 'ipithos.to' , 'ishared.eu' , 'kingfiles.net' , 'mail.ru' , 'my.mail.ru' , 'videoapi.my.mail.ru' , 'mightyupload.com' , 'mooshare.biz' , 'movdivx.com' , 'movpod.net' , 'movpod.in' , 'movreel.com' , 'mrfile.me' , 'nosvideo.com' , 'openload.io' , 'played.to' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'uploaded.net' , 'primeshare.tv' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'uploaded.net' , 'sharerepo.com' , 'stagevu.com' , 'streamcloud.eu' , 'streamin.to' , 'thefile.me' , 'thevideo.me' , 'tusfiles.net' , 'uploadc.com' , 'zalaa.com' , 'uploadrocket.net' , 'uptobox.com' , 'v-vids.com' , 'veehd.com' , 'vidbull.com' , 'videomega.tv' , 'vidplay.net' , 'vidspot.net' , 'vidto.me' , 'vidzi.tv' , 'vimeo.com' , 'vk.com' , 'vodlocker.com' , 'xfileload.com' , 'xvidstage.com' , 'zettahost.tv' ]
Oo0Ooo = [ 'plugin.video.dramasonline' , 'plugin.video.f4mTester' , 'plugin.video.shahidmbcnet' , 'plugin.video.SportsDevil' , 'plugin.stream.vaughnlive.tv' , 'plugin.video.ZemTV-shani' ]
if 85 - 85: OOO0O0O0ooooo % IIii1I . II1 - O00ooooo00
class I1IiiI ( urllib2 . HTTPErrorProcessor ) :
 def http_response ( self , request , response ) :
  return response
 https_response = http_response
 if 27 - 27: iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o
I1IiI = False ;
if I1IiI :
 if 73 - 73: OOooOOo / ii11ii1ii
 if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
 try :
  import pysrc . pydevd as pydevd
  if 97 - 97: oO0o0ooO0 - IIII / O0oO - o0oO0
  pydevd . settrace ( 'localhost' , stdoutToServer = True , stderrToServer = True )
 except ImportError :
  sys . stderr . write ( "Error: " +
 "You must add org.python.pydev.debug.pysrc to your PYTHONPATH." )
  sys . exit ( 1 )
  if 100 - 100: i11Ii11I1Ii1i
Ooo = generator . addon
o0oOoO00o = generator . addon_version
i1 = generator . profile
oOOoo00O0O = generator . home
i1111 = os . path . join ( i1 , 'history' )
i11 = os . path . join ( i1 , 'list_revision' )
I11 = os . path . join ( oOOoo00O0O , 'icon.png' )
Oo0o0000o0o0 = os . path . join ( oOOoo00O0O , 'fanart.jpg' )
oOo0oooo00o = i1
oO0o0o0ooO0oO = os . path . join ( i1 , 'LivewebTV' )
oo0o0O00 = os . path . join ( i1 , 'source_file' )
downloader = downloader . SimpleDownloader ( )
oO = generator . debug
if os . path . exists ( oo0o0O00 ) == True :
 i1iiIIiiI111 = open ( oo0o0O00 ) . read ( )
else : i1iiIIiiI111 = [ ]
if 62 - 62: i11iIiiIii - iIiiiI1IiI1I1
def IIIiI11ii ( url , headers = None ) :
 try :
  if headers is None :
   headers = { 'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0' }
  O000oo = urllib2 . Request ( url , None , headers )
  i1iIIi1 = urllib2 . urlopen ( O000oo )
  ii11iIi1I = i1iIIi1 . read ( )
  i1iIIi1 . close ( )
  return ii11iIi1I
 except urllib2 . URLError , iI111I11I1I1 :
  generator . addon_log ( 'URL: ' + url )
  if hasattr ( iI111I11I1I1 , 'code' ) :
   generator . addon_log ( 'We failed with error code - %s.' % iI111I11I1I1 . code )
   xbmc . executebuiltin ( "XBMC.Notification(TV Direto,We failed with error code - " + str ( iI111I11I1I1 . code ) + ",10000," + I11 + ")" )
  elif hasattr ( iI111I11I1I1 , 'reason' ) :
   generator . addon_log ( 'We failed to reach a server.' )
   generator . addon_log ( 'Reason: %s' % iI111I11I1I1 . reason )
   xbmc . executebuiltin ( "XBMC.Notification(TV Direto,We failed to reach a server. - " + str ( iI111I11I1I1 . reason ) + ",10000," + I11 + ")" )
   if 55 - 55: OOooOOo % O00ooooo00 / oO0o0ooO0 - OoOO0ooOOoo0O - OOO0O0O0ooooo / iIiiiI1IiI1I1
def iii11iII ( ) :
 try :
  if Ooo . getSetting ( "source_file" ) == "true" :
   i1I111I ( '[COLOR white][I][B][COLOR lime]»» [/COLOR]SOURCE FILE[/I][/B][/COLOR]' , 'url' , 5 , I11 , Oo0o0000o0o0 , '' , '' , '' , '' )
  if Ooo . getSetting ( "browse_xml_database" ) == "true" :
   i1I111I ( 'XML Database' , 'http://xbmcplus.xb.funpic.de/www-data/filesystem/' , 15 , I11 , Oo0o0000o0o0 , '' , '' , '' , '' )
  if Ooo . getSetting ( "browse_community" ) == "true" :
   i1I111I ( 'Community Files' , 'community_files' , 16 , I11 , Oo0o0000o0o0 , '' , '' , '' , '' )
  if Ooo . getSetting ( "searchotherplugins" ) == "true" :
   i1I111I ( 'Search Other Plugins' , 'Search Plugins' , 25 , I11 , Oo0o0000o0o0 , '' , '' , '' , '' )
 except : traceback . print_exc ( )
 if 1 - 1: O0oO % Ooo00oOo00o * o00O0oo
def OoOo ( ) :
 IiIiIi = json . loads ( open ( oo0o0O00 ) . read ( ) )
 if len ( IiIiIi ) > 1 :
  for II in IiIiIi :
   if isinstance ( II , list ) :
    i1I111I ( II [ 0 ] . encode ( 'utf-8' ) , II [ 1 ] . encode ( 'utf-8' ) , 1 , I11 , Oo0o0000o0o0 , '' , '' , '' , '' , 'source' )
   else :
    iI = I11
    iI11iiiI1II = Oo0o0000o0o0
    O0oooo0Oo00 = ''
    Ii11iii11I = ''
    credits = ''
    oOo00Oo00O = ''
    if II . has_key ( 'thumbnail' ) :
     iI = II [ 'thumbnail' ]
    if II . has_key ( 'fanart' ) :
     iI11iiiI1II = II [ 'fanart' ]
    if II . has_key ( 'description' ) :
     O0oooo0Oo00 = II [ 'description' ]
    if II . has_key ( 'date' ) :
     Ii11iii11I = II [ 'date' ]
    if II . has_key ( 'genre' ) :
     oOo00Oo00O = II [ 'genre' ]
    if II . has_key ( 'credits' ) :
     credits = II [ 'credits' ]
    i1I111I ( II [ 'title' ] . encode ( 'utf-8' ) , II [ 'url' ] . encode ( 'utf-8' ) , 1 , iI , iI11iiiI1II , O0oooo0Oo00 , oOo00Oo00O , Ii11iii11I , credits , 'source' )
    if 43 - 43: IIiIiII11i - IIII * IIii1I
 else :
  if len ( IiIiIi ) == 1 :
   if isinstance ( IiIiIi [ 0 ] , list ) :
    O0O00o0OOO0 ( IiIiIi [ 0 ] [ 1 ] . encode ( 'utf-8' ) , Oo0o0000o0o0 )
   else :
    O0O00o0OOO0 ( IiIiIi [ 0 ] [ 'url' ] , IiIiIi [ 0 ] [ 'fanart' ] )
    if 27 - 27: OOO0O0O0ooooo % O00ooooo00 * OoOO0ooOOoo0O + i11iIiiIii + II1 * O00ooooo00
def o0oo0o0O00OO ( url = None ) :
 if url is None :
  if not Ooo . getSetting ( "new_file_source" ) == "" :
   o0oO = Ooo . getSetting ( 'new_file_source' ) . decode ( 'utf-8' )
  elif not Ooo . getSetting ( "new_url_source" ) == "" :
   o0oO = Ooo . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  o0oO = url
 if o0oO == '' or o0oO is None :
  return
 generator . addon_log ( 'Adding New Source: ' + o0oO . encode ( 'utf-8' ) )
 if 48 - 48: o00O0oo + o00O0oo / iIiiiI1IiI1I1 / IIii1I
 i1iiI11I = None
 if 29 - 29: II1
 ii11iIi1I = iII1i1I1II ( o0oO )
 print 'source_url' , o0oO
 if isinstance ( ii11iIi1I , BeautifulSOAP ) :
  if ii11iIi1I . find ( 'channels_info' ) :
   i1iiI11I = ii11iIi1I . channels_info
  elif ii11iIi1I . find ( 'items_info' ) :
   i1iiI11I = ii11iIi1I . items_info
 if i1iiI11I :
  i1IiIiiI = { }
  i1IiIiiI [ 'url' ] = o0oO
  try : i1IiIiiI [ 'title' ] = i1iiI11I . title . string
  except : pass
  try : i1IiIiiI [ 'thumbnail' ] = i1iiI11I . thumbnail . string
  except : pass
  try : i1IiIiiI [ 'fanart' ] = i1iiI11I . fanart . string
  except : pass
  try : i1IiIiiI [ 'genre' ] = i1iiI11I . genre . string
  except : pass
  try : i1IiIiiI [ 'description' ] = i1iiI11I . description . string
  except : pass
  try : i1IiIiiI [ 'date' ] = i1iiI11I . date . string
  except : pass
  try : i1IiIiiI [ 'credits' ] = i1iiI11I . credits . string
  except : pass
 else :
  if '/' in o0oO :
   I1I = o0oO . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in o0oO :
   I1I = o0oO . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in I1I :
   I1I = urllib . unquote_plus ( I1I )
  oOO00oOO = xbmc . Keyboard ( I1I , 'Displayed Name, Rename?' )
  oOO00oOO . doModal ( )
  if ( oOO00oOO . isConfirmed ( ) == False ) :
   return
  OoOoiI = oOO00oOO . getText ( )
  if len ( OoOoiI ) == 0 :
   return
  i1IiIiiI = { }
  i1IiIiiI [ 'title' ] = OoOoiI
  i1IiIiiI [ 'url' ] = o0oO
  i1IiIiiI [ 'fanart' ] = iI11iiiI1II
  if 60 - 60: o00O0oo / o00O0oo
 if os . path . exists ( oo0o0O00 ) == False :
  I1II1III11iii = [ ]
  I1II1III11iii . append ( i1IiIiiI )
  Oo000 = open ( oo0o0O00 , "w" )
  Oo000 . write ( json . dumps ( I1II1III11iii ) )
  Oo000 . close ( )
 else :
  IiIiIi = json . loads ( open ( oo0o0O00 , "r" ) . read ( ) )
  IiIiIi . append ( i1IiIiiI )
  Oo000 = open ( oo0o0O00 , "w" )
  Oo000 . write ( json . dumps ( IiIiIi ) )
  Oo000 . close ( )
 Ooo . setSetting ( 'new_url_source' , "" )
 Ooo . setSetting ( 'new_file_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(Wolf,New source added.,5000," + I11 + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : Ooo . openSettings ( )
 if 51 - 51: i11iIiiIii . IIiIiII11i + iIiiiI1IiI1I1
def II111ii1II1i ( name ) :
 IiIiIi = json . loads ( open ( oo0o0O00 , "r" ) . read ( ) )
 for OoOo00o in range ( len ( IiIiIi ) ) :
  if isinstance ( IiIiIi [ OoOo00o ] , list ) :
   if IiIiIi [ OoOo00o ] [ 0 ] == name :
    del IiIiIi [ OoOo00o ]
    Oo000 = open ( oo0o0O00 , "w" )
    Oo000 . write ( json . dumps ( IiIiIi ) )
    Oo000 . close ( )
    break
  else :
   if IiIiIi [ OoOo00o ] [ 'title' ] == name :
    del IiIiIi [ OoOo00o ]
    Oo000 = open ( oo0o0O00 , "w" )
    Oo000 . write ( json . dumps ( IiIiIi ) )
    Oo000 . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 70 - 70: IIII * OoOO
def i1II1 ( url , browse = False ) :
 if url is None :
  url = 'http://xbmcplus.xb.funpic.de/www-data/filesystem/'
 OoO0O0 = BeautifulSoup ( IIIiI11ii ( url ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 for II in OoO0O0 ( 'a' ) :
  II1i1IiiIIi11 = II [ 'href' ]
  if not II1i1IiiIIi11 . startswith ( '?' ) :
   iI1Ii11iII1 = II . string
   if iI1Ii11iII1 not in [ 'Parent Directory' , 'recycle_bin/' ] :
    if II1i1IiiIIi11 . endswith ( '/' ) :
     if browse :
      i1I111I ( iI1Ii11iII1 , url + II1i1IiiIIi11 , 15 , I11 , iI11iiiI1II , '' , '' , '' )
     else :
      i1I111I ( iI1Ii11iII1 , url + II1i1IiiIIi11 , 14 , I11 , iI11iiiI1II , '' , '' , '' )
    elif II1i1IiiIIi11 . endswith ( '.xml' ) :
     if browse :
      i1I111I ( iI1Ii11iII1 , url + II1i1IiiIIi11 , 1 , I11 , iI11iiiI1II , '' , '' , '' , '' , 'download' )
     else :
      if os . path . exists ( oo0o0O00 ) == True :
       if iI1Ii11iII1 in i1iiIIiiI111 :
        i1I111I ( iI1Ii11iII1 + ' (in use)' , url + II1i1IiiIIi11 , 11 , I11 , iI11iiiI1II , '' , '' , '' , '' , 'download' )
       else :
        i1I111I ( iI1Ii11iII1 , url + II1i1IiiIIi11 , 11 , I11 , iI11iiiI1II , '' , '' , '' , '' , 'download' )
      else :
       i1I111I ( iI1Ii11iII1 , url + II1i1IiiIIi11 , 11 , I11 , iI11iiiI1II , '' , '' , '' , '' , 'download' )
       if 51 - 51: iIiiiI1IiI1I1 * Ooo00oOo00o % ii11ii1ii * iIiiiI1IiI1I1 % OoOO / i11Ii11I1Ii1i
       if 49 - 49: ii11ii1ii
def IIii1Ii1 ( browse = False ) :
 I1II11IiII = 'http://community-links.googlecode.com/svn/trunk/'
 OoO0O0 = BeautifulSoup ( IIIiI11ii ( I1II11IiII ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 OOO0OOo = OoO0O0 ( 'ul' ) [ 0 ] ( 'li' ) [ 1 : ]
 for II in OOO0OOo :
  iI1Ii11iII1 = II ( 'a' ) [ 0 ] [ 'href' ]
  if browse :
   i1I111I ( iI1Ii11iII1 , I1II11IiII + iI1Ii11iII1 , 1 , I11 , iI11iiiI1II , '' , '' , '' , '' , 'download' )
  else :
   i1I111I ( iI1Ii11iII1 , I1II11IiII + iI1Ii11iII1 , 11 , I11 , iI11iiiI1II , '' , '' , '' , '' , 'download' )
   if 47 - 47: o0000oOoOoO0o + O0oO - O0oO * IIiIiII11i + oO0o0ooO0 % O0oO
def iII1i1I1II ( url , data = None ) :
 if url . startswith ( 'http://' ) or url . startswith ( 'https://' ) :
  data = IIIiI11ii ( url )
  if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
   print 'found m3u data'
   return data
 elif data == None :
  if not '/' in url or not '\\' in url :
   print 'No directory found. Lets make the url to cache dir'
   url = os . path . join ( oO0o0o0ooO0oO , url )
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    i111IiI1I = xbmcvfs . copy ( url , os . path . join ( i1 , 'temp' , 'sorce_temp.txt' ) )
    if i111IiI1I :
     data = open ( os . path . join ( i1 , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( i1 , 'temp' , 'sorce_temp.txt' ) )
    else :
     generator . addon_log ( "failed to copy from smb:" )
   else :
    data = open ( url , 'r' ) . read ( )
    if re . match ( "#EXTM3U" , data ) or 'm3u' in url :
     print 'found m3u data'
     return data
  else :
   generator . addon_log ( "Soup Data not found!" )
   return
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 70 - 70: oO0o0ooO0 . IiIIi1I1Iiii / ii11ii1ii . oO0o0ooO0 - OOO0O0O0ooooo / O0oO
 if 62 - 62: IIii1I * OOooOOo
def O0O00o0OOO0 ( url , fanart , data = None ) :
 OoO0O0 = iII1i1I1II ( url , data )
 if 26 - 26: IIII . o0oO0
 if isinstance ( OoO0O0 , BeautifulSOAP ) :
  if 68 - 68: Ooo00oOo00o
  if len ( OoO0O0 ( 'channels' ) ) > 0 and Ooo . getSetting ( 'donotshowbychannels' ) == 'false' :
   IIi1iIIiI = OoO0O0 ( 'channel' )
   for O0OoO in IIi1iIIiI :
    if 69 - 69: OoOO0ooOOoo0O . o0oO0 + oO0o0ooO0 / IiIIi1I1Iiii - OoOO0ooOOoo0O
    if 63 - 63: o0000oOoOoO0o % OoOO0ooOOoo0O * OoOO0ooOOoo0O * Ooo00oOo00o / OoOO
    o0ooO = ''
    O0o0O00Oo0o0 = 0
    try :
     o0ooO = O0OoO ( 'externallink' ) [ 0 ] . string
     O0o0O00Oo0o0 = len ( O0OoO ( 'externallink' ) )
    except : pass
    if 87 - 87: i11Ii11I1Ii1i * IiIIi1I1Iiii % i11iIiiIii % OOooOOo - o0000oOoOoO0o
    if O0o0O00Oo0o0 > 1 : o0ooO = ''
    if 68 - 68: o0oO0 % O00ooooo00 . O0oO . OoOO
    iI1Ii11iII1 = O0OoO ( 'name' ) [ 0 ] . string
    o0 = O0OoO ( 'thumbnail' ) [ 0 ] . string
    if o0 == None :
     o0 = ''
     if 91 - 91: IIii1I + o0oO0
    try :
     if not O0OoO ( 'fanart' ) :
      if Ooo . getSetting ( 'use_thumb' ) == "true" :
       i1i = o0
      else :
       i1i = fanart
     else :
      i1i = O0OoO ( 'fanart' ) [ 0 ] . string
     if i1i == None :
      raise
    except :
     i1i = fanart
     if 46 - 46: o0oO0 % o00O0oo + Ooo00oOo00o . OOooOOo . Ooo00oOo00o
    try :
     O0oooo0Oo00 = O0OoO ( 'info' ) [ 0 ] . string
     if O0oooo0Oo00 == None :
      raise
    except :
     O0oooo0Oo00 = ''
     if 96 - 96: IiIIi1I1Iiii
    try :
     oOo00Oo00O = O0OoO ( 'genre' ) [ 0 ] . string
     if oOo00Oo00O == None :
      raise
    except :
     oOo00Oo00O = ''
     if 45 - 45: OOO0O0O0ooooo * ii11ii1ii % IiIIi1I1Iiii * II1 + IIII . OOooOOo
    try :
     Ii11iii11I = O0OoO ( 'date' ) [ 0 ] . string
     if Ii11iii11I == None :
      raise
    except :
     Ii11iii11I = ''
     if 67 - 67: i11iIiiIii - O00ooooo00 % OoOO . OOO0O0O0ooooo
    try :
     credits = O0OoO ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 77 - 77: O0oO / IIiIiII11i
    try :
     if o0ooO == '' :
      i1I111I ( iI1Ii11iII1 . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , o0 , i1i , O0oooo0Oo00 , oOo00Oo00O , Ii11iii11I , credits , True )
     else :
      if 15 - 15: O0oO . IIii1I . II1 / i11iIiiIii - oO0o0ooO0 . O00ooooo00
      i1I111I ( iI1Ii11iII1 . encode ( 'utf-8' ) , o0ooO . encode ( 'utf-8' ) , 1 , o0 , i1i , O0oooo0Oo00 , oOo00Oo00O , Ii11iii11I , None , 'source' )
    except :
     generator . addon_log ( 'There was a problem adding directory from getData(): ' + iI1Ii11iII1 . encode ( 'utf-8' , 'ignore' ) )
  else :
   generator . addon_log ( 'No Channels: getItems' )
   i1O0OoO0o ( OoO0O0 ( 'item' ) , fanart )
 else :
  OO0oOO0O ( OoO0O0 )
  if 91 - 91: OOO0O0O0ooooo
  if 61 - 61: iIiiiI1IiI1I1
def OO0oOO0O ( data ) :
 O0OOO = data . rstrip ( )
 II11iIiIIIiI = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\r\n]+)' ) . findall ( O0OOO )
 o0o = len ( II11iIiIIIiI )
 print 'total m3u links' , o0o
 for o00 , OooOO000 , OOoOoo in II11iIiIIIiI :
  if 'tvg-logo' in o00 :
   o0 = oO0000OOo00 ( o00 , 'tvg-logo=[\'"](.*?)[\'"]' )
   if o0 :
    if o0 . startswith ( 'http' ) :
     o0 = o0
     if 27 - 27: IIiIiII11i % IIiIiII11i
    elif not Ooo . getSetting ( 'logo-folderPath' ) == "" :
     IIiIi1iI = Ooo . getSetting ( 'logo-folderPath' )
     o0 = IIiIi1iI + o0
     if 35 - 35: oO0o0ooO0 % OOO0O0O0ooooo - OOO0O0O0ooooo
    else :
     o0 = o0
     if 16 - 16: iIiiiI1IiI1I1 % OOooOOo - iIiiiI1IiI1I1 + oO0o0ooO0
     if 12 - 12: o0000oOoOoO0o / o0000oOoOoO0o + i11iIiiIii
  else :
   o0 = ''
  if 'type' in o00 :
   Ii = oO0000OOo00 ( o00 , 'type=[\'"](.*?)[\'"]' )
   if Ii == 'yt-dl' :
    OOoOoo = OOoOoo + "&mode=18"
   elif Ii == 'regex' :
    I1II11IiII = OOoOoo . split ( '&regexs=' )
    if 22 - 22: iIiiiI1IiI1I1
    iiI1I11i1i = III1Iiii1I11 ( iII1i1I1II ( '' , data = I1II11IiII [ 1 ] ) )
    if 9 - 9: OoOO / IiIIi1I1Iiii - IIiIiII11i / II1 / IIii1I - ii11ii1ii
    o00oooO0Oo ( I1II11IiII [ 0 ] , OooOO000 , o0 , '' , '' , '' , '' , '' , None , iiI1I11i1i , o0o )
    continue
   elif Ii == 'ftv' :
    OOoOoo = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( OooOO000 ) + '&url=' + OOoOoo + '&mode=125&ch_fanart=na'
  o00oooO0Oo ( OOoOoo , OooOO000 , o0 , '' , '' , '' , '' , '' , None , '' , o0o )
def o0O0OOO0Ooo ( name , url , fanart ) :
 OoO0O0 = iII1i1I1II ( url )
 iiIiI = OoO0O0 . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 I1 = iiIiI ( 'item' )
 try :
  i1i = iiIiI ( 'fanart' ) [ 0 ] . string
  if i1i == None :
   raise
 except :
  i1i = fanart
 for O0OoO in iiIiI ( 'subchannel' ) :
  name = O0OoO ( 'name' ) [ 0 ] . string
  try :
   o0 = O0OoO ( 'thumbnail' ) [ 0 ] . string
   if o0 == None :
    raise
  except :
   o0 = ''
  try :
   if not O0OoO ( 'fanart' ) :
    if Ooo . getSetting ( 'use_thumb' ) == "true" :
     i1i = o0
   else :
    i1i = O0OoO ( 'fanart' ) [ 0 ] . string
   if i1i == None :
    raise
  except :
   pass
  try :
   O0oooo0Oo00 = O0OoO ( 'info' ) [ 0 ] . string
   if O0oooo0Oo00 == None :
    raise
  except :
   O0oooo0Oo00 = ''
   if 86 - 86: OOooOOo - oO0o0ooO0 - Ooo00oOo00o * IIII
  try :
   oOo00Oo00O = O0OoO ( 'genre' ) [ 0 ] . string
   if oOo00Oo00O == None :
    raise
  except :
   oOo00Oo00O = ''
   if 66 - 66: II1 + OOO0O0O0ooooo
  try :
   Ii11iii11I = O0OoO ( 'date' ) [ 0 ] . string
   if Ii11iii11I == None :
    raise
  except :
   Ii11iii11I = ''
   if 11 - 11: o00O0oo + II1 - Ooo00oOo00o / ii11ii1ii + IiIIi1I1Iiii . iIiiiI1IiI1I1
  try :
   credits = O0OoO ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 41 - 41: oO0o0ooO0 - OOO0O0O0ooooo - OOO0O0O0ooooo
  try :
   i1I111I ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , o0 , i1i , O0oooo0Oo00 , oOo00Oo00O , credits , Ii11iii11I )
  except :
   generator . addon_log ( 'There was a problem adding directory - ' + name . encode ( 'utf-8' , 'ignore' ) )
 i1O0OoO0o ( I1 , i1i )
 if 68 - 68: o0000oOoOoO0o % o0oO0
 if 88 - 88: IIii1I - i11Ii11I1Ii1i + o0000oOoOoO0o
def IiI111111IIII ( name , url , fanart ) :
 OoO0O0 = iII1i1I1II ( url )
 iiIiI = OoO0O0 . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 I1 = iiIiI ( 'subitem' )
 i1O0OoO0o ( I1 , fanart )
 if 37 - 37: o0oO0 / OOooOOo
def i1O0OoO0o ( items , fanart ) :
 o0o = len ( items )
 generator . addon_log ( 'Total Items: %s' % o0o )
 i1I1iI1iIi111i = Ooo . getSetting ( 'add_playlist' )
 iiIi1IIi1I = Ooo . getSetting ( 'ask_playlist_items' )
 o0OoOO000ooO0 = Ooo . getSetting ( 'use_thumb' )
 o0o0o0oO0oOO = Ooo . getSetting ( 'parentalblocked' )
 o0o0o0oO0oOO = o0o0o0oO0oOO == "true"
 ii1Ii11I = Ooo . getSetting ( 'premiumpin' )
 ii1Ii11I = ii1Ii11I == "NatalManiac"
 for o00o0 in items :
  ii = False
  OOooooO0Oo = False
  if 91 - 91: ii11ii1ii . IIii1I / OoOO0ooOOoo0O + O00ooooo00
  I1i = 'false'
  try :
   I1i = o00o0 ( 'premium' ) [ 0 ] . string
  except :
   generator . addon_log ( I1i )
   I1i = ''
  if I1i == 'true' :
   if not ii1Ii11I : continue
   if 53 - 53: OoOO * OOooOOo + i11Ii11I1Ii1i - iIiiiI1IiI1I1
   if 2 - 2: o00O0oo + oO0o0ooO0 - IIiIiII11i % ii11ii1ii . IIII
  I1I1i1I = 'false'
  try :
   I1I1i1I = o00o0 ( 'parentalblock' ) [ 0 ] . string
  except :
   generator . addon_log ( 'parentalblock Error' )
   I1I1i1I = ''
  if I1I1i1I == 'true' and o0o0o0oO0oOO : continue
  if 30 - 30: II1
  if 5 - 5: i11Ii11I1Ii1i - iIiiiI1IiI1I1 - II1 % oO0o0ooO0 + IIiIiII11i * IIii1I
  if 37 - 37: O0oO % i11Ii11I1Ii1i + OOooOOo + ii11ii1ii * o00O0oo % OOO0O0O0ooooo
  if 61 - 61: IIiIiII11i - o0000oOoOoO0o . OoOO0ooOOoo0O / o0000oOoOoO0o + IiIIi1I1Iiii
  if 5 - 5: i11Ii11I1Ii1i + i11Ii11I1Ii1i / OOO0O0O0ooooo * IiIIi1I1Iiii - o0000oOoOoO0o % i11Ii11I1Ii1i
  if 15 - 15: i11iIiiIii % oO0o0ooO0 . IiIIi1I1Iiii + OoOO
  if 61 - 61: IiIIi1I1Iiii * OoOO % IiIIi1I1Iiii - O00ooooo00 - IIii1I
  try :
   iI1Ii11iII1 = o00o0 ( 'title' ) [ 0 ] . string
   if iI1Ii11iII1 is None :
    iI1Ii11iII1 = 'unknown?'
  except :
   generator . addon_log ( 'Name Error' )
   iI1Ii11iII1 = ''
   if 74 - 74: OoOO + iIiiiI1IiI1I1 / Ooo00oOo00o
   if 100 - 100: OOooOOo * IIii1I
   if 86 - 86: Ooo00oOo00o * o0000oOoOoO0o . IIII
  try :
   if o00o0 ( 'epg' ) :
    if o00o0 . epg_url :
     generator . addon_log ( 'Get EPG Regex' )
     iIO0O0Oooo0o = o00o0 . epg_url . string
     oOOoo00O00o = o00o0 . epg_regex . string
     O0O00Oo = oooooo0O000o ( iIO0O0Oooo0o , oOOoo00O00o )
     if O0O00Oo :
      iI1Ii11iII1 += ' - ' + O0O00Oo
    elif o00o0 ( 'epg' ) [ 0 ] . string > 1 :
     iI1Ii11iII1 += OoO ( o00o0 ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   generator . addon_log ( 'EPG Error' )
  try :
   I1II11IiII = [ ]
   if len ( o00o0 ( 'link' ) ) > 0 :
    if 51 - 51: II1 * o0000oOoOoO0o
    if 73 - 73: OoOO * i11iIiiIii % OoOO0ooOOoo0O . OoOO
    for II in o00o0 ( 'link' ) :
     if not II . string == None :
      I1II11IiII . append ( II . string )
   elif len ( o00o0 ( 'lonk' ) ) > 0 :
    if 66 - 66: OoOO0ooOOoo0O + OoOO0ooOOoo0O + i11Ii11I1Ii1i / IIII + o0000oOoOoO0o
    if 30 - 30: OOO0O0O0ooooo
    for II in o00o0 ( 'lonk' ) :
     if not II . string == None :
      I1II11IiII . append ( II . string )
      if 44 - 44: OoOO0ooOOoo0O / o00O0oo / o00O0oo
   elif len ( o00o0 ( 'sportsdevil' ) ) > 0 :
    for II in o00o0 ( 'sportsdevil' ) :
     if not II . string == None :
      OOO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + II . string
      iiiiI = o00o0 ( 'referer' ) [ 0 ] . string
      if iiiiI :
       if 62 - 62: II1 * IIiIiII11i
       OOO = OOO + '%26referer=' + iiiiI
      I1II11IiII . append ( OOO )
   elif len ( o00o0 ( 'p2p' ) ) > 0 :
    for II in o00o0 ( 'p2p' ) :
     if not II . string == None :
      if 'sop://' in II . string :
       oOOOoo0O0oO = 'plugin://plugin.video.p2p-streams/?mode=2url=' + II . string + '&' + 'name=' + iI1Ii11iII1
       I1II11IiII . append ( oOOOoo0O0oO )
      else :
       iIII1I111III = 'plugin://plugin.video.p2p-streams/?mode=1&url=' + II . string + '&' + 'name=' + iI1Ii11iII1
       I1II11IiII . append ( iIII1I111III )
   elif len ( o00o0 ( 'vaughn' ) ) > 0 :
    for II in o00o0 ( 'vaughn' ) :
     if not II . string == None :
      IIo0o0O0O00oOOo = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=' + II . string
      I1II11IiII . append ( IIo0o0O0O00oOOo )
   elif len ( o00o0 ( 'ilive' ) ) > 0 :
    for II in o00o0 ( 'ilive' ) :
     if not II . string == None :
      if not 'http' in II . string :
       iIIIiIi = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/' + II . string + '&amp;link=99&amp;mode=iLivePlay'
      else :
       iIIIiIi = 'plugin://plugin.video.tbh.ilive/?url=' + II . string + '&amp;link=99&amp;mode=iLivePlay'
   elif len ( o00o0 ( 'yt-dl' ) ) > 0 :
    for II in o00o0 ( 'yt-dl' ) :
     if not II . string == None :
      OO0O0 = II . string + '&mode=18'
      I1II11IiII . append ( OO0O0 )
   elif len ( o00o0 ( 'dm' ) ) > 0 :
    for II in o00o0 ( 'dm' ) :
     if not II . string == None :
      I11I11 = "plugin://plugin.video.dailymotion_com/?mode=playVideo&url=" + II . string
      I1II11IiII . append ( I11I11 )
   elif len ( o00o0 ( 'dmlive' ) ) > 0 :
    for II in o00o0 ( 'dmlive' ) :
     if not II . string == None :
      I11I11 = "plugin://plugin.video.dailymotion_com/?mode=playLiveVideo&url=" + II . string
      I1II11IiII . append ( I11I11 )
   elif len ( o00o0 ( 'utube' ) ) > 0 :
    for II in o00o0 ( 'utube' ) :
     if not II . string == None :
      if ' ' in II . string :
       o000O0O = 'plugin://plugin.video.youtube/search/?q=' + urllib . quote_plus ( II . string )
       OOooooO0Oo = o000O0O
      elif len ( II . string ) == 11 :
       o000O0O = 'plugin://plugin.video.youtube/play/?video_id=' + II . string
      elif ( II . string . startswith ( 'PL' ) and not '&order=' in II . string ) or II . string . startswith ( 'UU' ) :
       o000O0O = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + II . string
      elif II . string . startswith ( 'PL' ) or II . string . startswith ( 'UU' ) :
       o000O0O = 'plugin://plugin.video.youtube/play/?playlist_id=' + II . string
      elif II . string . startswith ( 'UC' ) and len ( II . string ) > 12 :
       o000O0O = 'plugin://plugin.video.youtube/channel/' + II . string + '/'
       OOooooO0Oo = o000O0O
      elif not II . string . startswith ( 'UC' ) and not ( II . string . startswith ( 'PL' ) ) :
       o000O0O = 'plugin://plugin.video.youtube/user/' + II . string + '/'
       OOooooO0Oo = o000O0O
     I1II11IiII . append ( o000O0O )
   elif len ( o00o0 ( 'imdb' ) ) > 0 :
    for II in o00o0 ( 'imdb' ) :
     if not II . string == None :
      if Ooo . getSetting ( 'genesisorpulsar' ) == '0' :
       I1i1i1iii = 'plugin://plugin.video.genesis/?action=play&imdb=' + II . string
      else :
       I1i1i1iii = 'plugin://plugin.video.pulsar/movie/tt' + II . string + '/play'
      I1II11IiII . append ( I1i1i1iii )
   elif len ( o00o0 ( 'f4m' ) ) > 0 :
    for II in o00o0 ( 'f4m' ) :
     if not II . string == None :
      if '.f4m' in II . string :
       I1111i = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( II . string )
      elif '.m3u8' in II . string :
       I1111i = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( II . string ) + '&amp;streamtype=HLS'
       if 14 - 14: o0000oOoOoO0o / ii11ii1ii
      else :
       I1111i = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( II . string ) + '&amp;streamtype=SIMPLE'
     I1II11IiII . append ( I1111i )
   elif len ( o00o0 ( 'ftv' ) ) > 0 :
    for II in o00o0 ( 'ftv' ) :
     if not II . string == None :
      iII11I1IiiIi = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( iI1Ii11iII1 ) + '&url=' + II . string + '&mode=125&ch_fanart=na'
     I1II11IiII . append ( iII11I1IiiIi )
   elif len ( o00o0 ( 'urlsolve' ) ) > 0 :
    for II in o00o0 ( 'urlsolve' ) :
     if not II . string == None :
      oo0oO = II . string + '&mode=19'
      I1II11IiII . append ( oo0oO )
   if len ( I1II11IiII ) < 1 :
    raise
  except :
   generator . addon_log ( 'Error <link> element, Passing:' + iI1Ii11iII1 . encode ( 'utf-8' , 'ignore' ) )
   continue
  try :
   ii = o00o0 ( 'externallink' ) [ 0 ] . string
  except : pass
  if 94 - 94: IIii1I / IiIIi1I1Iiii % IIII * IIII * iIiiiI1IiI1I1
  if ii :
   IIiIiI = [ ii ]
   ii = True
  else :
   ii = False
  try :
   OOooooO0Oo = o00o0 ( 'jsonrpc' ) [ 0 ] . string
  except : pass
  if OOooooO0Oo :
   if 94 - 94: OoOO0ooOOoo0O . O00ooooo00 - ii11ii1ii % OOO0O0O0ooooo - Ooo00oOo00o
   IIiIiI = [ OOooooO0Oo ]
   if 72 - 72: oO0o0ooO0
   OOooooO0Oo = True
  else :
   OOooooO0Oo = False
  try :
   o0 = o00o0 ( 'thumbnail' ) [ 0 ] . string
   if o0 == None :
    raise
  except :
   o0 = ''
  try :
   if not o00o0 ( 'fanart' ) :
    if Ooo . getSetting ( 'use_thumb' ) == "true" :
     i1i = o0
    else :
     i1i = fanart
   else :
    i1i = o00o0 ( 'fanart' ) [ 0 ] . string
   if i1i == None :
    raise
  except :
   i1i = fanart
  try :
   O0oooo0Oo00 = o00o0 ( 'info' ) [ 0 ] . string
   if O0oooo0Oo00 == None :
    raise
  except :
   O0oooo0Oo00 = ''
   if 1 - 1: Ooo00oOo00o * O0oO * II1 + i11Ii11I1Ii1i
  try :
   oOo00Oo00O = o00o0 ( 'genre' ) [ 0 ] . string
   if oOo00Oo00O == None :
    raise
  except :
   oOo00Oo00O = ''
   if 33 - 33: OOO0O0O0ooooo * ii11ii1ii - o0oO0 % o0oO0
  try :
   Ii11iii11I = o00o0 ( 'date' ) [ 0 ] . string
   if Ii11iii11I == None :
    raise
  except :
   Ii11iii11I = ''
   if 18 - 18: o0oO0 / IiIIi1I1Iiii * o0oO0 + o0oO0 * i11iIiiIii * OoOO
  iiI1I11i1i = None
  if o00o0 ( 'regex' ) :
   try :
    I1II1 = o00o0 ( 'regex' )
    iiI1I11i1i = III1Iiii1I11 ( I1II1 )
   except :
    pass
  try :
   if len ( I1II11IiII ) > 1 :
    oooO = 0
    i1I1i111Ii = [ ]
    for II in I1II11IiII :
     if i1I1iI1iIi111i == "false" :
      oooO += 1
      o00oooO0Oo ( II , '%s) %s' % ( oooO , iI1Ii11iII1 . encode ( 'utf-8' , 'ignore' ) ) , o0 , i1i , O0oooo0Oo00 , oOo00Oo00O , Ii11iii11I , True , i1I1i111Ii , iiI1I11i1i , o0o )
     elif i1I1iI1iIi111i == "true" and iiIi1IIi1I == 'true' :
      if iiI1I11i1i :
       i1I1i111Ii . append ( II + '&regexs=' + iiI1I11i1i )
      elif any ( x in II for x in OO0o ) and II . startswith ( 'http' ) :
       i1I1i111Ii . append ( II + '&mode=19' )
      else :
       i1I1i111Ii . append ( II )
     else :
      i1I1i111Ii . append ( II )
    if len ( i1I1i111Ii ) > 1 :
     o00oooO0Oo ( '' , iI1Ii11iII1 , o0 , i1i , O0oooo0Oo00 , oOo00Oo00O , Ii11iii11I , True , i1I1i111Ii , iiI1I11i1i , o0o )
   else :
    if ii :
     if not iiI1I11i1i == None :
      i1I111I ( iI1Ii11iII1 . encode ( 'utf-8' ) , IIiIiI [ 0 ] . encode ( 'utf-8' ) , 1 , o0 , fanart , O0oooo0Oo00 , oOo00Oo00O , Ii11iii11I , None , '!!update' , iiI1I11i1i , I1II11IiII [ 0 ] . encode ( 'utf-8' ) )
      if 67 - 67: IIiIiII11i . O00ooooo00
     else :
      i1I111I ( iI1Ii11iII1 . encode ( 'utf-8' ) , IIiIiI [ 0 ] . encode ( 'utf-8' ) , 1 , o0 , fanart , O0oooo0Oo00 , oOo00Oo00O , Ii11iii11I , None , 'source' , None , None )
      if 27 - 27: i11Ii11I1Ii1i % IIiIiII11i
    elif OOooooO0Oo :
     i1I111I ( iI1Ii11iII1 . encode ( 'utf-8' ) , IIiIiI [ 0 ] , 53 , o0 , fanart , O0oooo0Oo00 , oOo00Oo00O , Ii11iii11I , None , 'source' )
     if 73 - 73: o0000oOoOoO0o
    else :
     o00oooO0Oo ( I1II11IiII [ 0 ] , iI1Ii11iII1 . encode ( 'utf-8' , 'ignore' ) , o0 , i1i , O0oooo0Oo00 , oOo00Oo00O , Ii11iii11I , True , None , iiI1I11i1i , o0o )
     if 70 - 70: IIii1I
  except :
   generator . addon_log ( 'There was a problem adding item - ' + iI1Ii11iII1 . encode ( 'utf-8' , 'ignore' ) )
   if 31 - 31: O0oO - IIiIiII11i % IIii1I
def III1Iiii1I11 ( reg_item ) :
 try :
  iiI1I11i1i = { }
  for II in reg_item :
   iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] = { }
   iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'name' ] = II ( 'name' ) [ 0 ] . string
   if 92 - 92: O00ooooo00 - IIii1I
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'expres' ] = II ( 'expres' ) [ 0 ] . string
    if not iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'expres' ] :
     iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'expres' ] = ''
   except :
    generator . addon_log ( "Regex: -- No Referer --" )
   iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'page' ] = II ( 'page' ) [ 0 ] . string
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'referer' ] = II ( 'referer' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No Referer --" )
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'connection' ] = II ( 'connection' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No connection --" )
    if 16 - 16: Ooo00oOo00o - OOooOOo - o0000oOoOoO0o - O00ooooo00 / oO0o0ooO0
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'notplayable' ] = II ( 'notplayable' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No notplayable --" )
    if 88 - 88: Ooo00oOo00o
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'noredirect' ] = II ( 'noredirect' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No noredirect --" )
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'origin' ] = II ( 'origin' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No origin --" )
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'accept' ] = II ( 'accept' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No accept --" )
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'includeheaders' ] = II ( 'includeheaders' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No includeheaders --" )
    if 71 - 71: OoOO
    if 7 - 7: OoOO - IIiIiII11i . IIii1I - O00ooooo00
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'listrepeat' ] = II ( 'listrepeat' ) [ 0 ] . string
    print 'listrepeat' , iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'listrepeat' ] , II ( 'listrepeat' ) [ 0 ] . string , II
   except :
    generator . addon_log ( "Regex: -- No listrepeat --" )
    if 59 - 59: ii11ii1ii
    if 81 - 81: OOooOOo - OOooOOo . IIII
    if 73 - 73: o00O0oo % i11iIiiIii - IIiIiII11i
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'proxy' ] = II ( 'proxy' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No proxy --" )
    if 7 - 7: OOO0O0O0ooooo * i11iIiiIii * oO0o0ooO0 + i11Ii11I1Ii1i % Ooo00oOo00o - i11Ii11I1Ii1i
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'x-req' ] = II ( 'x-req' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No x-req --" )
    if 39 - 39: IiIIi1I1Iiii * o0000oOoOoO0o % o0000oOoOoO0o - II1 + ii11ii1ii - o00O0oo
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'x-addr' ] = II ( 'x-addr' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No x-addr --" )
    if 23 - 23: i11iIiiIii
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'x-forward' ] = II ( 'x-forward' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No x-forward --" )
    if 30 - 30: ii11ii1ii - O00ooooo00 % iIiiiI1IiI1I1 + o00O0oo * IIii1I
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'agent' ] = II ( 'agent' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- No User Agent --" )
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'post' ] = II ( 'post' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- Not a post" )
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'rawpost' ] = II ( 'rawpost' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- Not a rawpost" )
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'htmlunescape' ] = II ( 'htmlunescape' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- Not a htmlunescape" )
    if 81 - 81: O0oO % O00ooooo00 . IIii1I
    if 4 - 4: i11iIiiIii % Ooo00oOo00o % O00ooooo00 / O0oO
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'readcookieonly' ] = II ( 'readcookieonly' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- Not a readCookieOnly" )
    if 6 - 6: IIII / IIiIiII11i % o0000oOoOoO0o - IIiIiII11i
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = II ( 'cookiejar' ) [ 0 ] . string
    if not iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] :
     iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = ''
   except :
    generator . addon_log ( "Regex: -- Not a cookieJar" )
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'setcookie' ] = II ( 'setcookie' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- Not a setcookie" )
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'appendcookie' ] = II ( 'appendcookie' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- Not a appendcookie" )
    if 31 - 31: o0000oOoOoO0o
   try :
    iiI1I11i1i [ II ( 'name' ) [ 0 ] . string ] [ 'ignorecache' ] = II ( 'ignorecache' ) [ 0 ] . string
   except :
    generator . addon_log ( "Regex: -- no ignorecache" )
    if 23 - 23: o0oO0 . O0oO
    if 92 - 92: OOooOOo + o0oO0 * oO0o0ooO0 % IIiIiII11i
    if 42 - 42: IiIIi1I1Iiii
    if 76 - 76: IIiIiII11i * IIII % o0oO0
    if 57 - 57: IIii1I - O00ooooo00 / o0oO0 - OOO0O0O0ooooo * II1 % iIiiiI1IiI1I1
  iiI1I11i1i = urllib . quote ( repr ( iiI1I11i1i ) )
  return iiI1I11i1i
  if 68 - 68: II1 * o00O0oo % OOooOOo - O0oO
 except :
  iiI1I11i1i = None
  generator . addon_log ( 'regex Error: ' + iI1Ii11iII1 . encode ( 'utf-8' , 'ignore' ) )
  if 34 - 34: o0oO0 . IIii1I * OOooOOo * OoOO0ooOOoo0O / o0oO0 / OoOO
def oOoOOo0O ( url ) :
 try :
  for II in range ( 1 , 51 ) :
   OOOooo = OooO0OO ( url )
   if "EXT-X-STREAM-INF" in OOOooo : return url
   if not "EXTM3U" in OOOooo : return
   xbmc . sleep ( 2000 )
  return
 except :
  return
  if 69 - 69: i11Ii11I1Ii1i % OoOO0ooOOoo0O
def ii1I1IIii11 ( regexs , url , cookieJar = None , forCookieJarOnly = False , recursiveCall = False , cachedPages = { } , rawPost = False , cookie_jar_file = None ) :
 if not recursiveCall :
  regexs = eval ( urllib . unquote ( regexs ) )
  if 67 - 67: IIII + o00O0oo / ii11ii1ii . OoOO0ooOOoo0O + o0000oOoOoO0o
  if 62 - 62: i11iIiiIii + i11iIiiIii - ii11ii1ii
 I1OooooO0oOOOO = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 if 100 - 100: IIII % o0000oOoOoO0o
 OOOiII1 = True
 for OOo in I1OooooO0oOOOO :
  if OOo in regexs :
   if 22 - 22: OOooOOo * OOO0O0O0ooooo . O0oO * i11iIiiIii - IIiIiII11i * i11Ii11I1Ii1i
   OOooo0O0o0 = regexs [ OOo ]
   if 14 - 14: ii11ii1ii % OOO0O0O0ooooo * IIII + oO0o0ooO0 + IiIIi1I1Iiii * oO0o0ooO0
   iII1I1IiI11ii = False
   if 'cookiejar' in OOooo0O0o0 :
    if 72 - 72: IIiIiII11i % i11iIiiIii . IiIIi1I1Iiii / iIiiiI1IiI1I1
    iII1I1IiI11ii = OOooo0O0o0 [ 'cookiejar' ]
    if '$doregex' in iII1I1IiI11ii :
     cookieJar = ii1I1IIii11 ( regexs , OOooo0O0o0 [ 'cookiejar' ] , cookieJar , True , True , cachedPages )
     iII1I1IiI11ii = True
    else :
     iII1I1IiI11ii = True
     if 14 - 14: OoOO + Ooo00oOo00o
   if iII1I1IiI11ii :
    if cookieJar == None :
     if 3 - 3: OoOO . IiIIi1I1Iiii / iIiiiI1IiI1I1
     cookie_jar_file = None
     if 'open[' in OOooo0O0o0 [ 'cookiejar' ] :
      cookie_jar_file = OOooo0O0o0 [ 'cookiejar' ] . split ( 'open[' ) [ 1 ] . split ( ']' ) [ 0 ]
      if 39 - 39: o0oO0
     cookieJar = OoOooOoO ( cookie_jar_file )
     if cookie_jar_file :
      iiIiii1iI1i ( cookieJar , cookie_jar_file )
      if 34 - 34: i11Ii11I1Ii1i * IIiIiII11i . O00ooooo00 * i11Ii11I1Ii1i / i11Ii11I1Ii1i
      if 30 - 30: OoOO + IiIIi1I1Iiii / IiIIi1I1Iiii % OoOO . OoOO
      if 55 - 55: i11Ii11I1Ii1i - o00O0oo + iIiiiI1IiI1I1 + IIII % oO0o0ooO0
    elif 'save[' in OOooo0O0o0 [ 'cookiejar' ] :
     cookie_jar_file = OOooo0O0o0 [ 'cookiejar' ] . split ( 'save[' ) [ 1 ] . split ( ']' ) [ 0 ]
     iiI11i1II = os . path . join ( i1 , cookie_jar_file )
     print 'complete_path' , iiI11i1II
     iiIiii1iI1i ( cookieJar , cookie_jar_file )
   if OOooo0O0o0 [ 'page' ] and '$doregex' in OOooo0O0o0 [ 'page' ] :
    OOooo0O0o0 [ 'page' ] = ii1I1IIii11 ( regexs , OOooo0O0o0 [ 'page' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 51 - 51: ii11ii1ii % IiIIi1I1Iiii % ii11ii1ii * OOO0O0O0ooooo - o0000oOoOoO0o % IiIIi1I1Iiii
   if 'setcookie' in OOooo0O0o0 and OOooo0O0o0 [ 'setcookie' ] and '$doregex' in OOooo0O0o0 [ 'setcookie' ] :
    OOooo0O0o0 [ 'setcookie' ] = ii1I1IIii11 ( regexs , OOooo0O0o0 [ 'setcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if 'appendcookie' in OOooo0O0o0 and OOooo0O0o0 [ 'appendcookie' ] and '$doregex' in OOooo0O0o0 [ 'appendcookie' ] :
    OOooo0O0o0 [ 'appendcookie' ] = ii1I1IIii11 ( regexs , OOooo0O0o0 [ 'appendcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 65 - 65: i11Ii11I1Ii1i
    if 68 - 68: i11Ii11I1Ii1i % i11iIiiIii + iIiiiI1IiI1I1
   if 'post' in OOooo0O0o0 and '$doregex' in OOooo0O0o0 [ 'post' ] :
    OOooo0O0o0 [ 'post' ] = ii1I1IIii11 ( regexs , OOooo0O0o0 [ 'post' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    print 'post is now' , OOooo0O0o0 [ 'post' ]
    if 52 - 52: OoOO - IiIIi1I1Iiii + OoOO % ii11ii1ii
   if 'rawpost' in OOooo0O0o0 and '$doregex' in OOooo0O0o0 [ 'rawpost' ] :
    OOooo0O0o0 [ 'rawpost' ] = ii1I1IIii11 ( regexs , OOooo0O0o0 [ 'rawpost' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages , rawPost = True )
    if 35 - 35: IIii1I
    if 42 - 42: o0oO0 . IIiIiII11i . O00ooooo00 + OOooOOo + o0000oOoOoO0o + IIiIiII11i
   if 'rawpost' in OOooo0O0o0 and '$epoctime$' in OOooo0O0o0 [ 'rawpost' ] :
    OOooo0O0o0 [ 'rawpost' ] = OOooo0O0o0 [ 'rawpost' ] . replace ( '$epoctime$' , I1IooooO0oOoOOoO ( ) )
    if 20 - 20: o00O0oo + oO0o0ooO0 / OOO0O0O0ooooo % IIii1I
   if 'rawpost' in OOooo0O0o0 and '$epoctime2$' in OOooo0O0o0 [ 'rawpost' ] :
    OOooo0O0o0 [ 'rawpost' ] = OOooo0O0o0 [ 'rawpost' ] . replace ( '$epoctime2$' , oOo0O ( ) )
    if 64 - 64: OoOO - IIII + IIII - o00O0oo
    if 30 - 30: IIii1I . IIiIiII11i . o0000oOoOoO0o / ii11ii1ii
   iiI1I1 = ''
   if OOooo0O0o0 [ 'page' ] and OOooo0O0o0 [ 'page' ] in cachedPages and not 'ignorecache' in OOooo0O0o0 and forCookieJarOnly == False :
    iiI1I1 = cachedPages [ OOooo0O0o0 [ 'page' ] ]
   else :
    if OOooo0O0o0 [ 'page' ] and not OOooo0O0o0 [ 'page' ] == '' and OOooo0O0o0 [ 'page' ] . startswith ( 'http' ) :
     if '$epoctime$' in OOooo0O0o0 [ 'page' ] :
      OOooo0O0o0 [ 'page' ] = OOooo0O0o0 [ 'page' ] . replace ( '$epoctime$' , I1IooooO0oOoOOoO ( ) )
     if '$epoctime2$' in OOooo0O0o0 [ 'page' ] :
      OOooo0O0o0 [ 'page' ] = OOooo0O0o0 [ 'page' ] . replace ( '$epoctime2$' , oOo0O ( ) )
      if 56 - 56: IIiIiII11i . OOO0O0O0ooooo + IiIIi1I1Iiii
      if 1 - 1: IIII
     O0O0Ooo = OOooo0O0o0 [ 'page' ] . split ( '|' )
     oOoO0 = O0O0Ooo [ 0 ]
     Oo0 = None
     if len ( O0O0Ooo ) > 1 :
      Oo0 = O0O0Ooo [ 1 ]
      if 83 - 83: i11iIiiIii % ii11ii1ii % i11Ii11I1Ii1i
      if 11 - 11: iIiiiI1IiI1I1 % Ooo00oOo00o * IIII + i11Ii11I1Ii1i + oO0o0ooO0
      if 24 - 24: IiIIi1I1Iiii - OoOO0ooOOoo0O % IIii1I . O00ooooo00 / OOO0O0O0ooooo
      if 36 - 36: IIiIiII11i - o00O0oo
      if 29 - 29: i11Ii11I1Ii1i * o0000oOoOoO0o
      if 10 - 10: o0oO0 % O0oO * O0oO . o00O0oo / oO0o0ooO0 % o0000oOoOoO0o
      if 49 - 49: Ooo00oOo00o / OoOO0ooOOoo0O + OOO0O0O0ooooo * ii11ii1ii
      if 28 - 28: i11Ii11I1Ii1i + i11iIiiIii / o00O0oo % OOooOOo % IiIIi1I1Iiii - OOO0O0O0ooooo
      if 54 - 54: O00ooooo00 + iIiiiI1IiI1I1
      if 83 - 83: OoOO - IIiIiII11i + o0000oOoOoO0o
     iIi1Ii1i1iI = urllib2 . ProxyHandler ( urllib2 . getproxies ( ) )
     if 16 - 16: o0000oOoOoO0o / IiIIi1I1Iiii / II1 * IIiIiII11i + O00ooooo00 % o0000oOoOoO0o
     if 71 - 71: OOooOOo
     if 14 - 14: i11iIiiIii % o0000oOoOoO0o
     O000oo = urllib2 . Request ( oOoO0 )
     if 'proxy' in OOooo0O0o0 :
      OooO0oo = OOooo0O0o0 [ 'proxy' ]
      print 'proxytouse' , OooO0oo
      if 89 - 89: oO0o0ooO0
      if oOoO0 [ : 5 ] == "https" :
       ooOoOO0OoO00o = urllib2 . ProxyHandler ( { 'https' : OooO0oo } )
       if 11 - 11: IiIIi1I1Iiii - IIiIiII11i * iIiiiI1IiI1I1 . OoOO . OoOO0ooOOoo0O
      else :
       ooOoOO0OoO00o = urllib2 . ProxyHandler ( { 'http' : OooO0oo } )
       if 61 - 61: IIII % IIiIiII11i - ii11ii1ii - iIiiiI1IiI1I1 % OOO0O0O0ooooo
      OoOOO00 = urllib2 . build_opener ( ooOoOO0OoO00o )
      urllib2 . install_opener ( OoOOO00 )
      if 94 - 94: O0oO
      if 57 - 57: oO0o0ooO0 % oO0o0ooO0 * i11iIiiIii
     O000oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
     OooO0oo = None
     if 7 - 7: OOO0O0O0ooooo . oO0o0ooO0
     if 'referer' in OOooo0O0o0 :
      O000oo . add_header ( 'Referer' , OOooo0O0o0 [ 'referer' ] )
     if 'accept' in OOooo0O0o0 :
      O000oo . add_header ( 'Accept' , OOooo0O0o0 [ 'accept' ] )
     if 'agent' in OOooo0O0o0 :
      O000oo . add_header ( 'User-agent' , OOooo0O0o0 [ 'agent' ] )
     if 'x-req' in OOooo0O0o0 :
      O000oo . add_header ( 'X-Requested-With' , OOooo0O0o0 [ 'x-req' ] )
     if 'x-addr' in OOooo0O0o0 :
      O000oo . add_header ( 'x-addr' , OOooo0O0o0 [ 'x-addr' ] )
     if 'x-forward' in OOooo0O0o0 :
      O000oo . add_header ( 'X-Forwarded-For' , OOooo0O0o0 [ 'x-forward' ] )
     if 'setcookie' in OOooo0O0o0 :
      print 'adding cookie' , OOooo0O0o0 [ 'setcookie' ]
      O000oo . add_header ( 'Cookie' , OOooo0O0o0 [ 'setcookie' ] )
     if 'appendcookie' in OOooo0O0o0 :
      print 'appending cookie to cookiejar' , OOooo0O0o0 [ 'appendcookie' ]
      OO0oOOoo = OOooo0O0o0 [ 'appendcookie' ]
      OO0oOOoo = OO0oOOoo . split ( ';' )
      for oOOO00o000o in OO0oOOoo :
       iIi11i1 , oO00oo0o00o0o = oOOO00o000o . split ( '=' )
       IiIIIIIi , iIi11i1 = iIi11i1 . split ( ':' )
       IiIi1iIIi1 = cookielib . Cookie ( version = 0 , name = iIi11i1 , value = oO00oo0o00o0o , port = None , port_specified = False , domain = IiIIIIIi , domain_specified = False , domain_initial_dot = False , path = '/' , path_specified = True , secure = False , expires = None , discard = True , comment = None , comment_url = None , rest = { 'HttpOnly' : None } , rfc2109 = False )
       cookieJar . set_cookie ( IiIi1iIIi1 )
     if 'origin' in OOooo0O0o0 :
      O000oo . add_header ( 'Origin' , OOooo0O0o0 [ 'origin' ] )
     if Oo0 :
      Oo0 = Oo0 . split ( '&' )
      for oOOO00o000o in Oo0 :
       iIi11i1 , oO00oo0o00o0o = oOOO00o000o . split ( '=' )
       O000oo . add_header ( iIi11i1 , oO00oo0o00o0o )
     if not cookieJar == None :
      if 86 - 86: o00O0oo * IIiIiII11i + o00O0oo + iIiiiI1IiI1I1
      i1i111iI = urllib2 . HTTPCookieProcessor ( cookieJar )
      OoOOO00 = urllib2 . build_opener ( i1i111iI , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      OoOOO00 = urllib2 . install_opener ( OoOOO00 )
      print 'noredirect' , 'noredirect' in OOooo0O0o0
      if 29 - 29: OoOO / O00ooooo00 . IIiIiII11i - OOooOOo - OOooOOo - oO0o0ooO0
      if 'noredirect' in OOooo0O0o0 :
       IiiIiI111iI = urllib2 . build_opener ( I1IiiI )
       OoOOO00 = urllib2 . install_opener ( IiiIiI111iI )
       if 85 - 85: ii11ii1ii . OOooOOo / i11Ii11I1Ii1i . OOO0O0O0ooooo % o0oO0
     if 'connection' in OOooo0O0o0 :
      print '..........................connection//////.' , OOooo0O0o0 [ 'connection' ]
      from keepalive import HTTPHandler
      OO0ooo0oOO = HTTPHandler ( )
      OoOOO00 = urllib2 . build_opener ( OO0ooo0oOO )
      urllib2 . install_opener ( OoOOO00 )
      if 97 - 97: IIiIiII11i / IIII
      if 71 - 71: iIiiiI1IiI1I1 / O00ooooo00 . OoOO % II1 . OOooOOo
      if 41 - 41: O00ooooo00 * iIiiiI1IiI1I1 / II1 . o0000oOoOoO0o
     O0 = None
     if 33 - 33: O00ooooo00
     if 'post' in OOooo0O0o0 :
      Ii1iII1iI1 = OOooo0O0o0 [ 'post' ]
      if '$LiveStreamRecaptcha' in Ii1iII1iI1 :
       ( i1i1IIIIi1i , Ii11iiI ) = IIi1iiii1iI ( OOooo0O0o0 [ 'page' ] )
       if i1i1IIIIi1i :
        Ii1iII1iI1 += 'recaptcha_challenge_field:' + i1i1IIIIi1i + ',recaptcha_response_field:' + Ii11iiI
      iIiiii = Ii1iII1iI1 . split ( ',' ) ;
      O0 = { }
      for O0000OOO0 in iIiiii :
       iIi11i1 = O0000OOO0 . split ( ':' ) [ 0 ] ;
       oO00oo0o00o0o = O0000OOO0 . split ( ':' ) [ 1 ] ;
       O0 [ iIi11i1 ] = oO00oo0o00o0o
      O0 = urllib . urlencode ( O0 )
      if 51 - 51: IIiIiII11i / O0oO / oO0o0ooO0
     if 'rawpost' in OOooo0O0o0 :
      O0 = OOooo0O0o0 [ 'rawpost' ]
      if '$LiveStreamRecaptcha' in O0 :
       ( i1i1IIIIi1i , Ii11iiI ) = IIi1iiii1iI ( OOooo0O0o0 [ 'page' ] )
       if i1i1IIIIi1i :
        O0 += '&recaptcha_challenge_field=' + i1i1IIIIi1i + '&recaptcha_response_field=' + Ii11iiI
     if O0 :
      i1iIIi1 = urllib2 . urlopen ( O000oo , O0 )
     else :
      i1iIIi1 = urllib2 . urlopen ( O000oo )
      if 6 - 6: oO0o0ooO0 - i11Ii11I1Ii1i * o0000oOoOoO0o . IIII / OOO0O0O0ooooo * i11Ii11I1Ii1i
     iiI1I1 = i1iIIi1 . read ( )
     if 22 - 22: IiIIi1I1Iiii % IIII * OoOO / o0000oOoOoO0o % i11iIiiIii * o00O0oo
     if 'proxy' in OOooo0O0o0 and not iIi1Ii1i1iI is None :
      urllib2 . install_opener ( urllib2 . build_opener ( iIi1Ii1i1iI ) )
      if 95 - 95: II1 - O0oO * IIiIiII11i + OOooOOo
     iiI1I1 = iIi1 ( iiI1I1 )
     if 21 - 21: o00O0oo
     if 'includeheaders' in OOooo0O0o0 :
      if 92 - 92: i11iIiiIii / o0oO0 - IIII % i11Ii11I1Ii1i * o0oO0 + IiIIi1I1Iiii
      iiI1I1 += '$$HEADERS_START$$:'
      for Oo000 in i1iIIi1 . headers :
       iiI1I1 += Oo000 + ':' + i1iIIi1 . headers . get ( Oo000 ) + '\n'
      iiI1I1 += '$$HEADERS_END$$:'
      if 11 - 11: II1 . o0oO0
     generator . addon_log ( iiI1I1 )
     generator . addon_log ( cookieJar )
     if 80 - 80: II1 - o0000oOoOoO0o * oO0o0ooO0 * OoOO / IIiIiII11i / o0000oOoOoO0o
     i1iIIi1 . close ( )
     cachedPages [ OOooo0O0o0 [ 'page' ] ] = iiI1I1
     if 13 - 13: o0oO0 * i11Ii11I1Ii1i + i11iIiiIii * o0oO0 - i11Ii11I1Ii1i
     if 23 - 23: IIii1I * O00ooooo00 % II1 * O0oO
     if 9 - 9: O0oO - iIiiiI1IiI1I1 + OOO0O0O0ooooo / IIii1I / i11iIiiIii
     if forCookieJarOnly :
      return cookieJar
    elif OOooo0O0o0 [ 'page' ] and not OOooo0O0o0 [ 'page' ] . startswith ( 'http' ) :
     if OOooo0O0o0 [ 'page' ] . startswith ( '$pyFunction:' ) :
      I1IIIiI1I1ii1 = iiiI1I1iIIIi1 ( OOooo0O0o0 [ 'page' ] . split ( '$pyFunction:' ) [ 1 ] , '' , cookieJar , OOooo0O0o0 )
      if forCookieJarOnly :
       return cookieJar
      iiI1I1 = I1IIIiI1I1ii1
     else :
      iiI1I1 = OOooo0O0o0 [ 'page' ]
   if '$pyFunction:playmedia(' in OOooo0O0o0 [ 'expres' ] or 'ActivateWindow' in OOooo0O0o0 [ 'expres' ] or '$PLAYERPROXY$=' in url or any ( x in url for x in Oo0Ooo ) :
    OOOiII1 = False
   if '$doregex' in OOooo0O0o0 [ 'expres' ] :
    OOooo0O0o0 [ 'expres' ] = ii1I1IIii11 ( regexs , OOooo0O0o0 [ 'expres' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if not OOooo0O0o0 [ 'expres' ] == '' :
    print 'doing it ' , OOooo0O0o0 [ 'expres' ]
    if '$LiveStreamCaptcha' in OOooo0O0o0 [ 'expres' ] :
     I1IIIiI1I1ii1 = Iii ( OOooo0O0o0 , iiI1I1 , cookieJar )
     if 19 - 19: o00O0oo % iIiiiI1IiI1I1 / i11iIiiIii / IIII - II1
     url = url . replace ( "$doregex[" + OOo + "]" , I1IIIiI1I1ii1 )
    elif OOooo0O0o0 [ 'expres' ] . startswith ( '$pyFunction:' ) or '#$pyFunction' in OOooo0O0o0 [ 'expres' ] :
     if 37 - 37: o0000oOoOoO0o / II1 - i11iIiiIii
     if OOooo0O0o0 [ 'expres' ] . startswith ( '$pyFunction:' ) :
      I1IIIiI1I1ii1 = iiiI1I1iIIIi1 ( OOooo0O0o0 [ 'expres' ] . split ( '$pyFunction:' ) [ 1 ] , iiI1I1 , cookieJar , OOooo0O0o0 )
     else :
      I1IIIiI1I1ii1 = i1iIiIi1I ( OOooo0O0o0 [ 'expres' ] , iiI1I1 , cookieJar , OOooo0O0o0 )
     if 'ActivateWindow' in OOooo0O0o0 [ 'expres' ] : return
     print 'url k val' , url , OOo , I1IIIiI1I1ii1
     if 45 - 45: O00ooooo00 + iIiiiI1IiI1I1
     url = url . replace ( "$doregex[" + OOo + "]" , I1IIIiI1I1ii1 )
    else :
     if 'listrepeat' in OOooo0O0o0 :
      IiII1II11I = OOooo0O0o0 [ 'listrepeat' ]
      O0Oo00O = re . findall ( OOooo0O0o0 [ 'expres' ] , iiI1I1 )
      return IiII1II11I , O0Oo00O , OOooo0O0o0 , regexs
      if 91 - 91: OoOO0ooOOoo0O % oO0o0ooO0 . i11Ii11I1Ii1i / IIII * IIii1I
     if not iiI1I1 == '' :
      if 43 - 43: i11Ii11I1Ii1i + IIII - o0oO0 / OOO0O0O0ooooo * IiIIi1I1Iiii + IIiIiII11i
      i1IIIIiI111I = re . compile ( OOooo0O0o0 [ 'expres' ] ) . search ( iiI1I1 )
      I1IIIiI1I1ii1 = ''
      try :
       I1IIIiI1I1ii1 = i1IIIIiI111I . group ( 1 ) . strip ( )
      except : traceback . print_exc ( )
     else :
      I1IIIiI1I1ii1 = OOooo0O0o0 [ 'expres' ]
      if 11 - 11: IIiIiII11i - Ooo00oOo00o
     if rawPost :
      print 'rawpost'
      I1IIIiI1I1ii1 = urllib . quote_plus ( I1IIIiI1I1ii1 )
     if 'htmlunescape' in OOooo0O0o0 :
      if 39 - 39: i11iIiiIii - IIii1I / OoOO0ooOOoo0O
      import HTMLParser
      I1IIIiI1I1ii1 = HTMLParser . HTMLParser ( ) . unescape ( I1IIIiI1I1ii1 )
     url = url . replace ( "$doregex[" + OOo + "]" , I1IIIiI1I1ii1 )
     if 70 - 70: O0oO
   else :
    url = url . replace ( "$doregex[" + OOo + "]" , '' )
 if '$epoctime$' in url :
  url = url . replace ( '$epoctime$' , I1IooooO0oOoOOoO ( ) )
 if '$epoctime2$' in url :
  url = url . replace ( '$epoctime2$' , oOo0O ( ) )
  if 34 - 34: o0oO0 % O0oO
 if '$GUID$' in url :
  import uuid
  url = url . replace ( '$GUID$' , str ( uuid . uuid1 ( ) ) . upper ( ) )
 if '$get_cookies$' in url :
  url = url . replace ( '$get_cookies$' , IiI1i ( cookieJar ) )
  if 87 - 87: i11Ii11I1Ii1i
 if recursiveCall : return url
 print 'final url' , url
 if url == "" :
  return
 else :
  return url , OOOiII1
  if 45 - 45: Ooo00oOo00o / II1 - IIII / oO0o0ooO0 % O0oO
def OoOIii11iI11i1I ( ) :
 import binascii
 generator . addon_log ( "Request" )
 O0O00o0OOO0 ( generator . url + generator . base , '' )
 if 64 - 64: i11iIiiIii
def I1II ( t ) :
 import hashlib
 oOOO00o000o = hashlib . md5 ( )
 oOOO00o000o . update ( t )
 return oOOO00o000o . hexdigest ( )
 if 17 - 17: o0000oOoOoO0o % IiIIi1I1Iiii / OoOO . O0oO * o0000oOoOoO0o - iIiiiI1IiI1I1
def i1i1IIii1i1 ( encrypted ) :
 oOoO00 = ""
 print 'enc' , encrypted
 if 40 - 40: ii11ii1ii
 if 67 - 67: OoOO0ooOOoo0O + iIiiiI1IiI1I1 - OOO0O0O0ooooo . OoOO0ooOOoo0O * iIiiiI1IiI1I1 * o00O0oo
 if 90 - 90: oO0o0ooO0 . O0oO
 if 81 - 81: o0000oOoOoO0o - o00O0oo % i11Ii11I1Ii1i - Ooo00oOo00o / IiIIi1I1Iiii
def Ii1iI111 ( media_url ) :
 try :
  import CustomPlayer
  O0oooo00o0Oo = CustomPlayer . MyXBMCPlayer ( )
  I1iii = xbmcgui . ListItem ( label = str ( iI1Ii11iII1 ) , iconImage = "DefaultVideo.png" , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  O0oooo00o0Oo . play ( media_url , I1iii )
  xbmc . sleep ( 1000 )
  while O0oooo00o0Oo . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 return ''
 if 86 - 86: OoOO * OOO0O0O0ooooo * O0oO
def Ooo0oo ( params ) :
 ii11iIi1I = json . dumps ( params )
 IIi11IIiIii1 = xbmc . executeJSONRPC ( ii11iIi1I )
 if 17 - 17: oO0o0ooO0 + OoOO0ooOOoo0O . Ooo00oOo00o - IiIIi1I1Iiii * i11iIiiIii
 try :
  i1iIIi1 = json . loads ( IIi11IIiIii1 )
 except UnicodeDecodeError :
  i1iIIi1 = json . loads ( IIi11IIiIii1 . decode ( 'utf-8' , 'ignore' ) )
  if 20 - 20: IIiIiII11i . II1 % o0000oOoOoO0o
 try :
  if 'result' in i1iIIi1 :
   return i1iIIi1 [ 'result' ]
  return None
 except KeyError :
  logger . warn ( "[%s] %s" % ( params [ 'method' ] , i1iIIi1 [ 'error' ] [ 'message' ] ) )
  return None
  if 63 - 63: IIiIiII11i % IIii1I
  if 39 - 39: IIII / iIiiiI1IiI1I1 / OoOO % IIiIiII11i
def O0Oo00 ( proxysettings = None ) :
 if 41 - 41: IIii1I % o00O0oo
 if proxysettings == None :
  print 'proxy set to nothing'
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":false}, "id":1}' )
 else :
  if 59 - 59: o0000oOoOoO0o + i11iIiiIii
  oo0OOo0O = proxysettings . split ( ':' )
  Ii1IiII = oo0OOo0O [ 0 ]
  I1iooo = oo0OOo0O [ 1 ]
  ii1iiIi1 = oo0OOo0O [ 2 ]
  i111iiI1ii = None
  IIiii = None
  if 30 - 30: o00O0oo / oO0o0ooO0 . O0oO . II1 - IiIIi1I1Iiii
  if len ( oo0OOo0O ) > 3 and '@' in proxysettings :
   i111iiI1ii = oo0OOo0O [ 3 ]
   IIiii = proxysettings . split ( '@' ) [ - 1 ]
   if 44 - 44: OOO0O0O0ooooo * II1 % i11Ii11I1Ii1i + iIiiiI1IiI1I1
  print 'proxy set to' , ii1iiIi1 , Ii1IiII , I1iooo
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":true}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxytype", "value":' + str ( ii1iiIi1 ) + '}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyserver", "value":"' + str ( Ii1IiII ) + '"}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyport", "value":' + str ( I1iooo ) + '}, "id":1}' )
  if 39 - 39: OoOO0ooOOoo0O % IIii1I % OOO0O0O0ooooo % II1 * OoOO + IIII
  if 68 - 68: IiIIi1I1Iiii + i11iIiiIii
  if not i111iiI1ii == None :
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyusername", "value":"' + str ( i111iiI1ii ) + '"}, "id":1}' )
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxypassword", "value":"' + str ( IIiii ) + '"}, "id":1}' )
   if 69 - 69: IIii1I * IIii1I * i11iIiiIii + IIiIiII11i / o0000oOoOoO0o % oO0o0ooO0
   if 58 - 58: o0000oOoOoO0o * ii11ii1ii + OOO0O0O0ooooo % o0000oOoOoO0o
def iI1I1iIi11 ( ) :
 oo0ooOO = Ooo0oo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.usehttpproxy" } , 'id' : 1 } ) [ 'value' ]
 print 'proxyActive' , oo0ooOO
 ii1iiIi1 = Ooo0oo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxytype" } , 'id' : 1 } ) [ 'value' ]
 if 24 - 24: Ooo00oOo00o % Ooo00oOo00o * IIii1I
 if oo0ooOO :
  Ii1IiII = Ooo0oo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyserver" } , 'id' : 1 } ) [ 'value' ]
  I1iooo = unicode ( Ooo0oo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyport" } , 'id' : 1 } ) [ 'value' ] )
  i111iiI1ii = Ooo0oo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyusername" } , 'id' : 1 } ) [ 'value' ]
  IIiii = Ooo0oo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxypassword" } , 'id' : 1 } ) [ 'value' ]
  if 50 - 50: Ooo00oOo00o . i11iIiiIii - OoOO0ooOOoo0O . OoOO0ooOOoo0O
  if i111iiI1ii and IIiii and Ii1IiII and I1iooo :
   return Ii1IiII + ':' + str ( I1iooo ) + ':' + str ( ii1iiIi1 ) + ':' + i111iiI1ii + '@' + IIiii
  elif Ii1IiII and I1iooo :
   return Ii1IiII + ':' + str ( I1iooo ) + ':' + str ( ii1iiIi1 )
 else :
  return None
  if 31 - 31: o0000oOoOoO0o / IiIIi1I1Iiii * O00ooooo00 . OOooOOo
def OO0o0oO ( media_url , name , iconImage , proxyip , port ) :
 if 83 - 83: ii11ii1ii / i11iIiiIii % IIii1I . o00O0oo % OoOO0ooOOoo0O . II1
 o00oO00 = xbmcgui . DialogProgress ( )
 o00oO00 . create ( 'Progress' , 'Playing with custom proxy' )
 o00oO00 . update ( 10 , "" , "setting proxy.." , "" )
 OO0oOOo = False
 OO0oO0o = ''
 try :
  if 39 - 39: ii11ii1ii * i11Ii11I1Ii1i + oO0o0ooO0 * iIiiiI1IiI1I1
  OO0oO0o = iI1I1iIi11 ( )
  print 'existing_proxy' , OO0oO0o
  if 97 - 97: IIii1I + o00O0oo + iIiiiI1IiI1I1 % O0oO % o0oO0 % OoOO0ooOOoo0O
  O0Oo00 ( proxyip + ':' + port + ':0' )
  if 21 - 21: IIiIiII11i / i11Ii11I1Ii1i % i11Ii11I1Ii1i - ii11ii1ii
  print 'proxy setting complete' , iI1I1iIi11 ( )
  OO0oOOo = True
  o00oO00 . update ( 80 , "" , "setting proxy complete, now playing" , "" )
  o00oO00 . close ( )
  o00oO00 = None
  import CustomPlayer
  O0oooo00o0Oo = CustomPlayer . MyXBMCPlayer ( )
  I1iii = xbmcgui . ListItem ( label = str ( name ) , iconImage = iconImage , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  O0oooo00o0Oo . play ( media_url , I1iii )
  xbmc . sleep ( 1000 )
  while O0oooo00o0Oo . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 if o00oO00 :
  o00oO00 . close ( )
 if OO0oOOo :
  print 'now resetting the proxy back'
  O0Oo00 ( OO0oO0o )
  print 'reset here'
 return ''
 if 70 - 70: IiIIi1I1Iiii . OOooOOo
 if 58 - 58: o00O0oo + iIiiiI1IiI1I1 * IIII * i11iIiiIii - IIii1I
def oooo00o0o0o ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  O0Oo00oO0O00 = page_value
  page_value = OooO0OO ( page_value , headers = referer )
  if 32 - 32: iIiiiI1IiI1I1 . oO0o0ooO0 - IIII * o0oO0
 OOO00oo0ooO = "(eval\(function\(p,a,c,k,e,(?:r|d).*)"
 if 38 - 38: IIii1I - iIiiiI1IiI1I1 - IIiIiII11i
 ooo = re . compile ( OOO00oo0ooO ) . findall ( page_value )
 OOOO0oooo = ""
 if ooo and len ( ooo ) > 0 :
  for oO00oo0o00o0o in ooo :
   oooooOo0 = O0o0O0OO00o ( oO00oo0o00o0o )
   OOo00O = oO0000OOo00 ( oooooOo0 , '\'(.*?)\'' )
   if 'unescape' in oooooOo0 :
    oooooOo0 = urllib . unquote ( OOo00O )
   OOOO0oooo += oooooOo0 + '\n'
  print 'final value is ' , OOOO0oooo
  if 81 - 81: O0oO . ii11ii1ii / o0oO0
  O0Oo00oO0O00 = oO0000OOo00 ( OOOO0oooo , 'src="(.*?)"' )
  if 17 - 17: i11iIiiIii - o0000oOoOoO0o . O0oO % IIii1I + o00O0oo - i11Ii11I1Ii1i
  page_value = OooO0OO ( O0Oo00oO0O00 , headers = referer )
  if 78 - 78: o00O0oo * OOooOOo . OOO0O0O0ooooo / OOO0O0O0ooooo
  if 80 - 80: O00ooooo00 - IiIIi1I1Iiii / Ooo00oOo00o - i11iIiiIii
  if 68 - 68: OoOO0ooOOoo0O - OoOO % OOO0O0O0ooooo % o0oO0
 Ii1II = oO0000OOo00 ( page_value , 'streamer\'.*?\'(.*?)\'\)' )
 ooO0O0o0 = oO0000OOo00 ( page_value , 'file\',\s\'(.*?)\'' )
 if 92 - 92: IiIIi1I1Iiii % OoOO * IIii1I - OoOO . ii11ii1ii
 if 95 - 95: o0oO0 % IIiIiII11i
 return Ii1II + ' playpath=' + ooO0O0o0 + ' pageUrl=' + O0Oo00oO0O00
 if 42 - 42: II1 - IIII / II1 / oO0o0ooO0
def O0OOooo0OooOo ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  page_value = OooO0OO ( page_value , headers = referer )
 OOO00oo0ooO = "var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
 ooo = re . compile ( OOO00oo0ooO ) . findall ( page_value ) [ 0 ]
 if 62 - 62: OOooOOo / IIiIiII11i - OoOO - IIiIiII11i + i11iIiiIii + O00ooooo00
 I1i11II , Oo000 , II11 , I1iiioOO0OO0O , o00o , oO00oo0o00o0o = ( ooo )
 o00o = int ( o00o )
 I1i11II = int ( I1i11II ) / o00o
 Oo000 = int ( Oo000 ) / o00o
 II11 = int ( II11 ) / o00o
 I1iiioOO0OO0O = int ( I1iiioOO0OO0O ) / o00o
 if 47 - 47: ii11ii1ii + IIII - OoOO0ooOOoo0O % II1
 O0Oo00O = 'rtmp://' + str ( I1i11II ) + '.' + str ( Oo000 ) + '.' + str ( II11 ) + '.' + str ( I1iiioOO0OO0O ) + oO00oo0o00o0o ;
 return O0Oo00O
 if 52 - 52: o0oO0 / i11Ii11I1Ii1i - o00O0oo
def iIiI ( url , useragent = None ) :
 str = '#EXTM3U'
 str += '\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=361816'
 str += '\n' + url + '&bytes=0-200000'
 oo0o0O00 = os . path . join ( i1 , 'testfile.m3u' )
 str += '\n'
 iIIIi1i1I11i ( oo0o0O00 , str )
 if 55 - 55: IiIIi1I1Iiii - o0000oOoOoO0o
 return oo0o0O00
 if 84 - 84: o0oO0 + IiIIi1I1Iiii - OOooOOo * OOooOOo
def iIIIi1i1I11i ( file_name , page_data , append = False ) :
 if append :
  o00o = open ( file_name , 'a' )
  o00o . write ( page_data )
  o00o . close ( )
 else :
  o00o = open ( file_name , 'wb' )
  o00o . write ( page_data )
  o00o . close ( )
  return ''
  if 61 - 61: II1 . OoOO0ooOOoo0O . II1 / IiIIi1I1Iiii
def o00O ( file_name ) :
 o00o = open ( file_name , 'rb' )
 I1iiioOO0OO0O = o00o . read ( )
 o00o . close ( )
 return I1iiioOO0OO0O
 if 48 - 48: IIII . i11iIiiIii
def IIi ( page_data ) :
 import re , base64 , urllib ;
 oo0OO = page_data
 while 'geh(' in oo0OO :
  if oo0OO . startswith ( 'lol(' ) : oo0OO = oo0OO [ 5 : - 1 ]
  if 2 - 2: iIiiiI1IiI1I1 - Ooo00oOo00o . O0oO * IIII / OoOO0ooOOoo0O
  oo0OO = re . compile ( '"(.*?)"' ) . findall ( oo0OO ) [ 0 ] ;
  oo0OO = base64 . b64decode ( oo0OO ) ;
  oo0OO = urllib . unquote ( oo0OO ) ;
 print oo0OO
 return oo0OO
 if 80 - 80: o0000oOoOoO0o / o00O0oo / OOooOOo + O00ooooo00 - IiIIi1I1Iiii
def iIIiiIIi1IiI ( page_data ) :
 print 'get_dag_url2' , page_data
 I11IIIiIi11 = OooO0OO ( page_data ) ;
 I11iiIi1i1 = '(http.*)'
 import uuid
 i1IiiI1iIi = str ( uuid . uuid1 ( ) ) . upper ( )
 oOOo00O0OOOo = re . compile ( I11iiIi1i1 ) . findall ( I11IIIiIi11 )
 i11I1I1iiI = [ ( 'X-Playback-Session-Id' , i1IiiI1iIi ) ]
 for I1i1iii1Ii in oOOo00O0OOOo :
  try :
   iIO0O00OOo = OooO0OO ( I1i1iii1Ii , headers = i11I1I1iiI ) ;
   if 66 - 66: i11iIiiIii / ii11ii1ii - II1 / O00ooooo00 . i11iIiiIii
  except : pass
  if 16 - 16: IiIIi1I1Iiii % OoOO + o00O0oo - OOO0O0O0ooooo . IIII / o0oO0
 return page_data + '|&X-Playback-Session-Id=' + i1IiiI1iIi
 if 35 - 35: OoOO0ooOOoo0O / o0oO0 / iIiiiI1IiI1I1 - IIii1I + iIiiiI1IiI1I1 . o0oO0
 if 81 - 81: IIII * o0000oOoOoO0o - OoOO * oO0o0ooO0 % OOooOOo * OOooOOo
def ooO ( page_data ) :
 print 'get_dag_url' , page_data
 if page_data . startswith ( 'http://dag.total-stream.net' ) :
  i11I1I1iiI = [ ( 'User-Agent' , 'Verismo-BlackUI_(2.4.7.5.8.0.34)' ) ]
  page_data = OooO0OO ( page_data , headers = i11I1I1iiI ) ;
  if 100 - 100: IIiIiII11i / ii11ii1ii * IIII . OOO0O0O0ooooo / o0000oOoOoO0o
 if '127.0.0.1' in page_data :
  return oOO0o000Oo00o ( page_data )
 elif oO0000OOo00 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  iii11II1I = oO0000OOo00 ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + oO0000OOo00 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + oO0000OOo00 ( page_data , '\\?y=([^&]+)&' )
 else :
  iii11II1I = oO0000OOo00 ( page_data , 'href="([^"]+)"[^"]+$' )
  if len ( iii11II1I ) == 0 :
   iii11II1I = page_data
 iii11II1I = iii11II1I . replace ( ' ' , '%20' )
 return iii11II1I
 if 5 - 5: OOooOOo - O0oO * O0oO
def oO0000OOo00 ( data , re_patten ) :
 II11iIiIIIiI = ''
 OOooo0O0o0 = re . search ( re_patten , data )
 if OOooo0O0o0 != None :
  II11iIiIIIiI = OOooo0O0o0 . group ( 1 )
 else :
  II11iIiIIIiI = ''
 return II11iIiIIIiI
 if 50 - 50: iIiiiI1IiI1I1 * OoOO / oO0o0ooO0 . ii11ii1ii + IiIIi1I1Iiii - o0000oOoOoO0o
def oOO0o000Oo00o ( page_data ) :
 iii11II1I = ''
 if '127.0.0.1' in page_data :
  iii11II1I = oO0000OOo00 ( page_data , '&ver_t=([^&]+)&' ) + ' live=true timeout=15 playpath=' + oO0000OOo00 ( page_data , '\\?y=([a-zA-Z0-9-_\\.@]+)' )
  if 18 - 18: OOooOOo % i11iIiiIii % OoOO / OoOO0ooOOoo0O / ii11ii1ii / O00ooooo00
 if oO0000OOo00 ( page_data , 'token=([^&]+)&' ) != '' :
  iii11II1I = iii11II1I + '?token=' + oO0000OOo00 ( page_data , 'token=([^&]+)&' )
 elif oO0000OOo00 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  iii11II1I = oO0000OOo00 ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + oO0000OOo00 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + oO0000OOo00 ( page_data , '\\?y=([^&]+)&' )
 else :
  iii11II1I = oO0000OOo00 ( page_data , 'HREF="([^"]+)"' )
  if 48 - 48: OOooOOo + o00O0oo / O0oO + iIiiiI1IiI1I1
 if 'dag1.asx' in iii11II1I :
  return ooO ( iii11II1I )
  if 18 - 18: OoOO
 if 'devinlivefs.fplive.net' not in iii11II1I :
  iii11II1I = iii11II1I . replace ( 'devinlive' , 'flive' )
 if 'permlivefs.fplive.net' not in iii11II1I :
  iii11II1I = iii11II1I . replace ( 'permlive' , 'flive' )
 return iii11II1I
 if 23 - 23: iIiiiI1IiI1I1
 if 24 - 24: IIii1I + IIii1I * IIII
def i1I11iIII1i1I ( str_eval ) :
 oOO0oo = ""
 try :
  IiIIi1I1I11Ii = "w,i,s,e=(" + str_eval + ')'
  exec ( IiIIi1I1I11Ii )
  oOO0oo = o0OO ( w , II , s , e )
 except : traceback . print_exc ( file = sys . stdout )
 if 58 - 58: II1 . IIiIiII11i / iIiiiI1IiI1I1 / iIiiiI1IiI1I1 - O0oO + IiIIi1I1Iiii
 return oOO0oo
 if 59 - 59: II1 + o00O0oo . o0oO0 - OOO0O0O0ooooo % IIii1I / OOO0O0O0ooooo
def o0OO ( w , i , s , e ) :
 OO = 0 ;
 ooO0o = 0 ;
 ii1iI1iI1 = 0 ;
 o00oOOO = [ ] ;
 OoOO0OOoo = [ ] ;
 while True :
  if ( OO < 5 ) :
   OoOO0OOoo . append ( w [ OO ] )
  elif ( OO < len ( w ) ) :
   o00oOOO . append ( w [ OO ] ) ;
  OO += 1 ;
  if ( ooO0o < 5 ) :
   OoOO0OOoo . append ( i [ ooO0o ] )
  elif ( ooO0o < len ( i ) ) :
   o00oOOO . append ( i [ ooO0o ] )
  ooO0o += 1 ;
  if ( ii1iI1iI1 < 5 ) :
   OoOO0OOoo . append ( s [ ii1iI1iI1 ] )
  elif ( ii1iI1iI1 < len ( s ) ) :
   o00oOOO . append ( s [ ii1iI1iI1 ] ) ;
  ii1iI1iI1 += 1 ;
  if ( len ( w ) + len ( i ) + len ( s ) + len ( e ) == len ( o00oOOO ) + len ( OoOO0OOoo ) + len ( e ) ) :
   break ;
   if 1 - 1: IIiIiII11i * i11iIiiIii + o0oO0 * i11iIiiIii + Ooo00oOo00o
 iIIi1IIi = '' . join ( o00oOOO )
 i111i11I1ii = '' . join ( OoOO0OOoo )
 ooO0o = 0 ;
 OOooo = [ ] ;
 for OO in range ( 0 , len ( o00oOOO ) , 2 ) :
  if 54 - 54: iIiiiI1IiI1I1 . o00O0oo
  oOO = - 1 ;
  if ( ord ( i111i11I1ii [ ooO0o ] ) % 2 ) :
   oOO = 1 ;
   if 32 - 32: OOooOOo * IIiIiII11i % i11Ii11I1Ii1i * oO0o0ooO0 . OOO0O0O0ooooo
  OOooo . append ( chr ( int ( iIIi1IIi [ OO : OO + 2 ] , 36 ) - oOO ) ) ;
  ooO0o += 1 ;
  if ( ooO0o >= len ( OoOO0OOoo ) ) :
   ooO0o = 0 ;
 O0Oo00O = '' . join ( OOooo )
 if 'eval(function(w,i,s,e)' in O0Oo00O :
  print 'STILL GOing'
  O0Oo00O = re . compile ( 'eval\(function\(w,i,s,e\).*}\((.*?)\)' ) . findall ( O0Oo00O ) [ 0 ]
  return i1I11iIII1i1I ( O0Oo00O )
 else :
  print 'FINISHED'
  return O0Oo00O
  if 48 - 48: IIII * IIII
def O0o0O0OO00o ( page_value , regex_for_text = '' , iterations = 1 , total_iteration = 1 ) :
 try :
  I1I1 = None
  if page_value . startswith ( "http" ) :
   page_value = OooO0OO ( page_value )
  print 'page_value' , page_value
  if regex_for_text and len ( regex_for_text ) > 0 :
   page_value = re . compile ( regex_for_text ) . findall ( page_value ) [ 0 ]
   if 4 - 4: ii11ii1ii % OOooOOo * o0000oOoOoO0o
  page_value = ii1IiIi11 ( page_value , iterations , total_iteration )
 except : traceback . print_exc ( file = sys . stdout )
 print 'unpacked' , page_value
 if 'sav1live.tv' in page_value :
  page_value = page_value . replace ( 'sav1live.tv' , 'sawlive.tv' )
  print 'sav1 unpacked' , page_value
 return page_value
 if 22 - 22: OoOO0ooOOoo0O
def ii1IiIi11 ( sJavascript , iteration = 1 , totaliterations = 2 ) :
 print 'iteration' , iteration
 if sJavascript . startswith ( 'var _0xcb8a=' ) :
  ii1ii = sJavascript . split ( 'var _0xcb8a=' )
  IiIIi1I1I11Ii = "myarray=" + ii1ii [ 1 ] . split ( "eval(" ) [ 0 ]
  exec ( IiIIi1I1I11Ii )
  oOoooO00O = 62
  I1ii1111Ii = int ( ii1ii [ 1 ] . split ( ",62," ) [ 1 ] . split ( ',' ) [ 0 ] )
  o0O = myarray [ 0 ]
  iiiI1i11Ii = myarray [ 3 ]
  with open ( 'temp file' + str ( iteration ) + '.js' , "wb" ) as iIiII :
   iIiII . write ( str ( iiiI1i11Ii ) )
   if 19 - 19: O0oO
 else :
  if 78 - 78: o0000oOoOoO0o % ii11ii1ii
  if "rn p}('" in sJavascript :
   ii1ii = sJavascript . split ( "rn p}('" )
  else :
   ii1ii = sJavascript . split ( "rn A}('" )
  print ii1ii
  if 39 - 39: OoOO + IIiIiII11i - IIii1I - ii11ii1ii
  o0O , oOoooO00O , I1ii1111Ii , iiiI1i11Ii = ( '' , '0' , '0' , '' )
  if 7 - 7: O0oO . OOooOOo / OoOO . o0000oOoOoO0o * o00O0oo - iIiiiI1IiI1I1
  IiIIi1I1I11Ii = "p1,a1,c1,k1=('" + ii1ii [ 1 ] . split ( ".spli" ) [ 0 ] + ')'
  exec ( IiIIi1I1I11Ii )
 iiiI1i11Ii = iiiI1i11Ii . split ( '|' )
 ii1ii = ii1ii [ 1 ] . split ( "))'" )
 if 37 - 37: o0oO0 . OOooOOo / OOO0O0O0ooooo * IIII
 if 7 - 7: Ooo00oOo00o * o00O0oo + iIiiiI1IiI1I1 % i11iIiiIii
 if 8 - 8: i11Ii11I1Ii1i * OOO0O0O0ooooo
 if 73 - 73: ii11ii1ii / OoOO0ooOOoo0O / o00O0oo / Ooo00oOo00o
 if 11 - 11: OOooOOo + O0oO - II1 / Ooo00oOo00o
 if 34 - 34: i11Ii11I1Ii1i
 if 45 - 45: i11Ii11I1Ii1i / IiIIi1I1Iiii / oO0o0ooO0
 if 44 - 44: OoOO - oO0o0ooO0 / iIiiiI1IiI1I1 * Ooo00oOo00o * IiIIi1I1Iiii
 if 73 - 73: ii11ii1ii - IIiIiII11i * O00ooooo00 / i11iIiiIii * o0000oOoOoO0o % iIiiiI1IiI1I1
 if 56 - 56: II1 * IiIIi1I1Iiii . IiIIi1I1Iiii . OoOO
 if 24 - 24: IiIIi1I1Iiii . o00O0oo * oO0o0ooO0 % IIII / o0000oOoOoO0o
 if 58 - 58: IIiIiII11i - OoOO % OOO0O0O0ooooo . IIiIiII11i % Ooo00oOo00o % O0oO
 if 87 - 87: OoOO0ooOOoo0O - i11iIiiIii
 if 78 - 78: i11iIiiIii / IIii1I - ii11ii1ii
 if 23 - 23: o00O0oo
 if 40 - 40: ii11ii1ii - iIiiiI1IiI1I1 / IiIIi1I1Iiii
 if 14 - 14: OoOO
 if 5 - 5: ii11ii1ii . IIii1I % IIii1I
 if 56 - 56: II1 - o00O0oo - O00ooooo00
 if 8 - 8: o0oO0 / o0000oOoOoO0o . IIiIiII11i + OoOO / i11iIiiIii
 if 31 - 31: i11Ii11I1Ii1i - IIii1I + IIII . IiIIi1I1Iiii / O0oO % IIii1I
 if 6 - 6: O0oO * i11iIiiIii % IIii1I % i11iIiiIii + ii11ii1ii / O00ooooo00
 iI111I11I1I1 = ''
 I1iiioOO0OO0O = ''
 if 53 - 53: o00O0oo + IIii1I
 if 70 - 70: OoOO
 oo0O = str ( III1i1IiI1i ( o0O , oOoooO00O , I1ii1111Ii , iiiI1i11Ii , iI111I11I1I1 , I1iiioOO0OO0O , iteration ) )
 if 32 - 32: II1 - OOooOOo - i11iIiiIii * ii11ii1ii / IiIIi1I1Iiii + II1
 if 35 - 35: O00ooooo00 - ii11ii1ii * IIII
 if 63 - 63: IIII * OoOO . II1 / o0000oOoOoO0o * IiIIi1I1Iiii . i11Ii11I1Ii1i
 if 62 - 62: O00ooooo00 / i11Ii11I1Ii1i . IIiIiII11i * ii11ii1ii
 if 21 - 21: ii11ii1ii
 if iteration >= totaliterations :
  if 81 - 81: o00O0oo / IIii1I - i11Ii11I1Ii1i * o0oO0 . IIiIiII11i * OoOO
  return oo0O
 else :
  if 95 - 95: IIiIiII11i
  return ii1IiIi11 ( oo0O , iteration + 1 )
  if 88 - 88: O0oO % Ooo00oOo00o + o0oO0 + o0oO0 * iIiiiI1IiI1I1
def III1i1IiI1i ( p , a , c , k , e , d , iteration , v = 1 ) :
 if 78 - 78: II1
 if 77 - 77: OoOO / O00ooooo00 / IiIIi1I1Iiii % o0000oOoOoO0o
 if 48 - 48: o00O0oo - O0oO + IIii1I + II1
 while ( c >= 1 ) :
  c = c - 1
  if ( k [ c ] ) :
   IiI1i111IiIiIi1 = str ( i1II11II1 ( c , a ) )
   if v == 1 :
    p = re . sub ( '\\b' + IiI1i111IiIiIi1 + '\\b' , k [ c ] , p )
   else :
    p = II1IIIii ( p , IiI1i111IiIiIi1 , k [ c ] )
    if 40 - 40: OOooOOo % Ooo00oOo00o
    if 62 - 62: ii11ii1ii
    if 15 - 15: o00O0oo + oO0o0ooO0 . o0000oOoOoO0o * Ooo00oOo00o . OOooOOo
    if 18 - 18: O00ooooo00 % iIiiiI1IiI1I1 + o0oO0 % oO0o0ooO0
    if 72 - 72: IIii1I
    if 45 - 45: IiIIi1I1Iiii - ii11ii1ii % o0oO0
 return p
 if 38 - 38: o0oO0 % o0000oOoOoO0o - II1
 if 87 - 87: Ooo00oOo00o % IIiIiII11i
 if 77 - 77: IIii1I - O00ooooo00 . OoOO0ooOOoo0O
def II1IIIii ( source_str , word_to_find , replace_with ) :
 iIi1iIIIiIiI = None
 iIi1iIIIiIiI = source_str . split ( word_to_find )
 if len ( iIi1iIIIiIiI ) > 1 :
  OooOo000o0o = [ ]
  iI1I1iII1i = 0
  for iiIIii in iIi1iIIIiIiI :
   if 70 - 70: ii11ii1ii - o0000oOoOoO0o
   OooOo000o0o . append ( iiIIii )
   I1IIIiI1I1ii1 = word_to_find
   if 62 - 62: o00O0oo
   if 63 - 63: o0000oOoOoO0o + i11Ii11I1Ii1i * OoOO0ooOOoo0O / ii11ii1ii / IiIIi1I1Iiii * IIii1I
   if iI1I1iII1i == len ( iIi1iIIIiIiI ) - 1 :
    I1IIIiI1I1ii1 = ''
   else :
    if len ( iiIIii ) == 0 :
     if ( len ( iIi1iIIIiIiI [ iI1I1iII1i + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( iIi1iIIIiIiI [ iI1I1iII1i + 1 ] ) > 0 and iIi1iIIIiIiI [ iI1I1iII1i + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) :
      I1IIIiI1I1ii1 = replace_with
      if 57 - 57: OOooOOo - OoOO0ooOOoo0O / i11Ii11I1Ii1i % i11iIiiIii
    else :
     if ( iIi1iIIIiIiI [ iI1I1iII1i ] [ - 1 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) and ( ( len ( iIi1iIIIiIiI [ iI1I1iII1i + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( iIi1iIIIiIiI [ iI1I1iII1i + 1 ] ) > 0 and iIi1iIIIiIiI [ iI1I1iII1i + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) ) :
      I1IIIiI1I1ii1 = replace_with
      if 3 - 3: IIII . i11Ii11I1Ii1i % IIiIiII11i + OoOO
   OooOo000o0o . append ( I1IIIiI1I1ii1 )
   iI1I1iII1i += 1
   if 64 - 64: O00ooooo00
  source_str = '' . join ( OooOo000o0o )
 return source_str
 if 29 - 29: ii11ii1ii / i11iIiiIii / IIiIiII11i % OoOO0ooOOoo0O % i11iIiiIii
def i111II ( num , radix ) :
 if 63 - 63: IIiIiII11i - Ooo00oOo00o % IIII % o00O0oo / ii11ii1ii / O00ooooo00
 OOOooo = ""
 if num == 0 : return '0'
 while num > 0 :
  OOOooo = "0123456789abcdefghijklmnopqrstuvwxyz" [ num % radix ] + OOOooo
  num /= radix
 return OOOooo
 if 69 - 69: IiIIi1I1Iiii * iIiiiI1IiI1I1 * i11Ii11I1Ii1i . IIII - OoOO
def i1II11II1 ( cc , a ) :
 IiI1i111IiIiIi1 = "" if cc < a else i1II11II1 ( int ( cc / a ) , a )
 cc = ( cc % a )
 I11iiIIiI1ii = chr ( cc + 29 ) if cc > 35 else str ( i111II ( cc , 36 ) )
 return IiI1i111IiIiIi1 + I11iiIIiI1ii
 if 12 - 12: o0oO0 % i11iIiiIii + ii11ii1ii + o0oO0 / o00O0oo
 if 53 - 53: O0oO . o0oO0 % IIii1I % OOooOOo % o00O0oo
def IiI1i ( cookieJar ) :
 try :
  o0OoOoOOoOo0o = ""
  for OoOo00o , iIiii in enumerate ( cookieJar ) :
   o0OoOoOOoOo0o += iIiii . name + "=" + iIiii . value + ";"
 except : pass
 if 2 - 2: O00ooooo00 - IIiIiII11i + o00O0oo . iIiiiI1IiI1I1
 return o0OoOoOOoOo0o
 if 25 - 25: OoOO0ooOOoo0O
 if 34 - 34: OOooOOo . IIii1I % OOO0O0O0ooooo
def iiIiii1iI1i ( cookieJar , COOKIEFILE ) :
 try :
  iiI11i1II = os . path . join ( i1 , COOKIEFILE )
  cookieJar . save ( iiI11i1II , ignore_discard = True )
 except : pass
 if 43 - 43: OoOO - IIII
def OoOooOoO ( COOKIEFILE ) :
 if 70 - 70: IIII / o0000oOoOoO0o % i11Ii11I1Ii1i - oO0o0ooO0
 i1II11Iii1I = None
 if COOKIEFILE :
  try :
   iiI11i1II = os . path . join ( i1 , COOKIEFILE )
   i1II11Iii1I = cookielib . LWPCookieJar ( )
   i1II11Iii1I . load ( iiI11i1II , ignore_discard = True )
  except :
   i1II11Iii1I = None
   if 92 - 92: o0000oOoOoO0o % O0oO % OOooOOo
 if not i1II11Iii1I :
  i1II11Iii1I = cookielib . LWPCookieJar ( )
  if 4 - 4: OOooOOo + oO0o0ooO0 / OoOO0ooOOoo0O
 return i1II11Iii1I
 if 13 - 13: IIII
def iiiI1I1iIIIi1 ( fun_call , page_data , Cookie_Jar , m ) :
 o0OOOOO0O = ''
 if oOo0oooo00o not in sys . path :
  sys . path . append ( oOo0oooo00o )
  if 35 - 35: oO0o0ooO0 - oO0o0ooO0 + O00ooooo00 - OOO0O0O0ooooo - o0oO0
 print fun_call
 try :
  oOO0o0oo0 = 'import ' + fun_call . split ( '.' ) [ 0 ]
  print oOO0o0oo0 , sys . path
  exec ( oOO0o0oo0 )
  print 'done'
 except :
  print 'error in import'
  traceback . print_exc ( file = sys . stdout )
 print 'ret_val=' + fun_call
 exec ( 'ret_val=' + fun_call )
 print o0OOOOO0O
 if 78 - 78: o0000oOoOoO0o + IIII . O0oO
 return str ( o0OOOOO0O )
 if 91 - 91: IIii1I . ii11ii1ii . OoOO + II1
def i1iIiIi1I ( fun_call , page_data , Cookie_Jar , m ) :
 print 'doEvalFunction'
 o0OOOOO0O = ''
 if oOo0oooo00o not in sys . path :
  sys . path . append ( oOo0oooo00o )
 o00o = open ( oOo0oooo00o + "/LSProdynamicCode.py" , "w" )
 o00o . write ( fun_call ) ;
 o00o . close ( )
 import LSProdynamicCode
 o0OOOOO0O = LSProdynamicCode . GetLSProData ( page_data , Cookie_Jar , m )
 return str ( o0OOOOO0O )
 if 69 - 69: o0oO0 - IIiIiII11i
 if 95 - 95: IIiIiII11i * i11iIiiIii . i11Ii11I1Ii1i
def IIi1iiii1iI ( url ) :
 iIIi1 = OooO0OO ( url )
 o0o0OoOOOOOo = ""
 Ii11iii1II1i = ""
 o0OOoOO = "<script.*?src=\"(.*?recap.*?)\""
 II11iIiIIIiI = re . findall ( o0OOoOO , iIIi1 )
 iII1 = False
 III1I1 = None
 Ii11iii1II1i = None
 if 12 - 12: IIii1I % i11Ii11I1Ii1i % i11Ii11I1Ii1i
 if II11iIiIIIiI and len ( II11iIiIIIiI ) > 0 :
  o0i1iI1iiI1I = II11iIiIIIiI [ 0 ]
  iII1 = True
  if 52 - 52: Ooo00oOo00o % oO0o0ooO0 * iIiiiI1IiI1I1
  I1IiIii11I = 'challenge.*?\'(.*?)\''
  i1iii1ii = '\'(.*?)\''
  II1I11Iii1 = OooO0OO ( o0i1iI1iiI1I )
  o0o0OoOOOOOo = re . findall ( I1IiIii11I , II1I11Iii1 ) [ 0 ]
  i1iIIi1II1iiI = 'http://www.google.com/recaptcha/api/reload?c=' ;
  III1Ii1i1I1 = o0i1iI1iiI1I . split ( 'k=' ) [ 1 ]
  i1iIIi1II1iiI += o0o0OoOOOOOo + '&k=' + III1Ii1i1I1 + '&captcha_k=1&type=image&lang=en-GB'
  O0O00OooO = OooO0OO ( i1iIIi1II1iiI )
  III1I1 = re . findall ( i1iii1ii , O0O00OooO ) [ 0 ]
  I1IiI1iI11 = 'http://www.google.com/recaptcha/api/image?c=' + III1I1
  if not I1IiI1iI11 . startswith ( "http" ) :
   I1IiI1iI11 = 'http://www.google.com/recaptcha/api/' + I1IiI1iI11
  import random
  iIi11i1 = random . randrange ( 100 , 1000 , 5 )
  iIi = os . path . join ( i1 , str ( iIi11i1 ) + "captcha.img" )
  iiO0O0o0oO0O00 = open ( iIi , "wb" )
  iiO0O0o0oO0O00 . write ( OooO0OO ( I1IiI1iI11 ) )
  iiO0O0o0oO0O00 . close ( )
  o0O0oO0 = oo0 ( captcha = iIi )
  Ii11iii1II1i = o0O0oO0 . get ( )
  os . remove ( iIi )
 return III1I1 , Ii11iii1II1i
 if 39 - 39: i11Ii11I1Ii1i . iIiiiI1IiI1I1
def OooO0OO ( url , cookieJar = None , post = None , timeout = 20 , headers = None ) :
 if 45 - 45: OoOO0ooOOoo0O * OOooOOo / IIii1I
 if 77 - 77: o0oO0 - o00O0oo
 i1i111iI = urllib2 . HTTPCookieProcessor ( cookieJar )
 OoOOO00 = urllib2 . build_opener ( i1i111iI , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 if 11 - 11: OoOO
 O000oo = urllib2 . Request ( url )
 O000oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lWolf Gecko) Chrome/33.0.1750.154 Safari/537.36' )
 if headers :
  for oOOO00o000o , iiI1Ii11II1I in headers :
   O000oo . add_header ( oOOO00o000o , iiI1Ii11II1I )
   if 44 - 44: oO0o0ooO0 % i11iIiiIii - IIII * OoOO + IiIIi1I1Iiii * o0000oOoOoO0o
 i1iIIi1 = OoOOO00 . open ( O000oo , post , timeout = timeout )
 iiI1I1 = i1iIIi1 . read ( )
 i1iIIi1 . close ( )
 return iiI1I1 ;
 if 41 - 41: OOO0O0O0ooooo * i11Ii11I1Ii1i - OOooOOo . oO0o0ooO0
def oOIIIiI1ii1IIi ( str , reg = None ) :
 if reg :
  str = re . findall ( reg , str ) [ 0 ]
 o0O0oo0o = urllib . unquote ( str [ 0 : len ( str ) - 1 ] ) ;
 II11iI1iiI = '' ;
 for II in range ( len ( o0O0oo0o ) ) :
  II11iI1iiI += chr ( ord ( o0O0oo0o [ II ] ) - o0O0oo0o [ len ( o0O0oo0o ) - 1 ] ) ;
 II11iI1iiI = urllib . unquote ( II11iI1iiI )
 print II11iI1iiI
 return II11iI1iiI
 if 48 - 48: o00O0oo . II1 . IIiIiII11i . OOooOOo % OoOO / IIII
def iIi1 ( str ) :
 ii1I111i1Ii = re . findall ( 'unescape\(\'(.*?)\'' , str )
 print 'js' , ii1I111i1Ii
 if ( not ii1I111i1Ii == None ) and len ( ii1I111i1Ii ) > 0 :
  for OOOooO0OO0o in ii1I111i1Ii :
   if 10 - 10: oO0o0ooO0 - OOooOOo . II1 . o0000oOoOoO0o . Ooo00oOo00o * IIII
   str = str . replace ( OOOooO0OO0o , urllib . unquote ( OOOooO0OO0o ) )
 return str
 if 78 - 78: OoOO0ooOOoo0O / Ooo00oOo00o - OoOO0ooOOoo0O * II1 . OOooOOo
OOoooOoO0Oo = 0
def Iii ( m , html_page , cookieJar ) :
 global OOoooOoO0Oo
 OOoooOoO0Oo += 1
 Oo000iiIiII11i1 = m [ 'expres' ]
 O0Oo00oO0O00 = m [ 'page' ]
 oOo00Ooo0o0 = re . compile ( '\$LiveStreamCaptcha\[([^\]]*)\]' ) . findall ( Oo000iiIiII11i1 ) [ 0 ]
 if 33 - 33: o00O0oo
 o0i1iI1iiI1I = re . compile ( oOo00Ooo0o0 ) . findall ( html_page ) [ 0 ]
 print Oo000iiIiII11i1 , oOo00Ooo0o0 , o0i1iI1iiI1I
 if not o0i1iI1iiI1I . startswith ( "http" ) :
  oOO0 = 'http://' + "" . join ( O0Oo00oO0O00 . split ( '/' ) [ 2 : 3 ] )
  if o0i1iI1iiI1I . startswith ( "/" ) :
   o0i1iI1iiI1I = oOO0 + o0i1iI1iiI1I
  else :
   o0i1iI1iiI1I = oOO0 + '/' + o0i1iI1iiI1I
   if 15 - 15: IiIIi1I1Iiii + o00O0oo . i11Ii11I1Ii1i - IIii1I / OOO0O0O0ooooo % IIii1I
 iIi = os . path . join ( i1 , str ( OOoooOoO0Oo ) + "captcha.jpg" )
 iiO0O0o0oO0O00 = open ( iIi , "wb" )
 print ' c capurl' , o0i1iI1iiI1I
 O000oo = urllib2 . Request ( o0i1iI1iiI1I )
 O000oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  O000oo . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  O000oo . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'setcookie' in m :
  print 'adding cookie' , m [ 'setcookie' ]
  O000oo . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 86 - 86: IIiIiII11i / OoOO0ooOOoo0O * oO0o0ooO0
  if 64 - 64: i11Ii11I1Ii1i / OOO0O0O0ooooo * OOooOOo * i11Ii11I1Ii1i
  if 60 - 60: o00O0oo / O00ooooo00 % OoOO / OoOO * OoOO . i11iIiiIii
  if 99 - 99: OOooOOo
 urllib2 . urlopen ( O000oo )
 i1iIIi1 = urllib2 . urlopen ( O000oo )
 if 77 - 77: ii11ii1ii
 iiO0O0o0oO0O00 . write ( i1iIIi1 . read ( ) )
 i1iIIi1 . close ( )
 iiO0O0o0oO0O00 . close ( )
 o0O0oO0 = oo0 ( captcha = iIi )
 Ii11iii1II1i = o0O0oO0 . get ( )
 return Ii11iii1II1i
 if 48 - 48: OOooOOo % OoOO / o00O0oo . IIii1I * iIiiiI1IiI1I1
def oo000oO ( imageregex , html_page , cookieJar , m ) :
 global OOoooOoO0Oo
 OOoooOoO0Oo += 1
 if 78 - 78: oO0o0ooO0 + OOooOOo + O0oO - O0oO . i11iIiiIii / Ooo00oOo00o
 if 27 - 27: oO0o0ooO0 - OOO0O0O0ooooo % o00O0oo * o0oO0 . O0oO % IIii1I
 if not imageregex == '' :
  if html_page . startswith ( "http" ) :
   oOO0 = OooO0OO ( html_page , cookieJar = cookieJar )
  else :
   oOO0 = html_page
  o0i1iI1iiI1I = re . compile ( imageregex ) . findall ( html_page ) [ 0 ]
 else :
  o0i1iI1iiI1I = html_page
  if 'oneplay.tv/embed' in html_page :
   import oneplay
   oOO0 = OooO0OO ( html_page , cookieJar = cookieJar )
   o0i1iI1iiI1I = oneplay . getCaptchaUrl ( oOO0 )
   if 37 - 37: II1 + OOO0O0O0ooooo - O00ooooo00 % i11Ii11I1Ii1i
 iIi = os . path . join ( i1 , str ( OOoooOoO0Oo ) + "captcha.jpg" )
 iiO0O0o0oO0O00 = open ( iIi , "wb" )
 print ' c capurl' , o0i1iI1iiI1I
 O000oo = urllib2 . Request ( o0i1iI1iiI1I )
 O000oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  O000oo . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  O000oo . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'accept' in m :
  O000oo . add_header ( 'Accept' , m [ 'accept' ] )
 if 'setcookie' in m :
  print 'adding cookie' , m [ 'setcookie' ]
  O000oo . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 24 - 24: OOooOOo
  if 94 - 94: O00ooooo00 * O00ooooo00 % iIiiiI1IiI1I1 + o0000oOoOoO0o
  if 28 - 28: IIiIiII11i
  if 49 - 49: o00O0oo . ii11ii1ii % OoOO0ooOOoo0O / oO0o0ooO0
  if 95 - 95: OOO0O0O0ooooo * OOooOOo * O0oO . i11Ii11I1Ii1i / IIii1I
 i1iIIi1 = urllib2 . urlopen ( O000oo )
 if 28 - 28: O0oO + OoOO0ooOOoo0O - i11Ii11I1Ii1i / IIii1I - IIiIiII11i
 iiO0O0o0oO0O00 . write ( i1iIIi1 . read ( ) )
 i1iIIi1 . close ( )
 iiO0O0o0oO0O00 . close ( )
 o0O0oO0 = oo0 ( captcha = iIi )
 Ii11iii1II1i = o0O0oO0 . get ( )
 return Ii11iii1II1i
 if 45 - 45: OOO0O0O0ooooo / O00ooooo00 * OoOO0ooOOoo0O * Ooo00oOo00o
 if 35 - 35: OoOO / IIII % IIiIiII11i + IIii1I
 if 79 - 79: OOooOOo / i11Ii11I1Ii1i
 if 77 - 77: IiIIi1I1Iiii
 if 46 - 46: o0oO0
 if 72 - 72: IIII * o0000oOoOoO0o
 if 67 - 67: O00ooooo00
 if 5 - 5: iIiiiI1IiI1I1 . II1
 if 57 - 57: IIiIiII11i
 if 35 - 35: II1 - o0oO0 / Ooo00oOo00o
 if 50 - 50: OOooOOo
 if 33 - 33: o00O0oo
 if 98 - 98: OOooOOo % iIiiiI1IiI1I1
def OoO0O000 ( name , headname ) :
 if 14 - 14: Ooo00oOo00o / Ooo00oOo00o * OOO0O0O0ooooo . OoOO0ooOOoo0O
 if 59 - 59: iIiiiI1IiI1I1 * i11iIiiIii
 ooOooO00Oo = xbmc . Keyboard ( 'default' , 'heading' , True )
 ooOooO00Oo . setDefault ( name )
 ooOooO00Oo . setHeading ( headname )
 ooOooO00Oo . setHiddenInput ( False )
 return ooOooO00Oo . getText ( )
 if 86 - 86: iIiiiI1IiI1I1 + i11Ii11I1Ii1i + O0oO
 if 9 - 9: i11Ii11I1Ii1i + iIiiiI1IiI1I1 % i11Ii11I1Ii1i % O0oO + IIii1I
 if 59 - 59: O00ooooo00
 if 48 - 48: OOO0O0O0ooooo * oO0o0ooO0 * Ooo00oOo00o . Ooo00oOo00o * o00O0oo - oO0o0ooO0
class oo0 ( xbmcgui . WindowDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . cptloc = kwargs . get ( 'captcha' )
  self . img = xbmcgui . ControlImage ( 335 , 30 , 624 , 60 , self . cptloc )
  self . addControl ( self . img )
  self . kbd = xbmc . Keyboard ( )
  if 14 - 14: OoOO + i11iIiiIii
 def get ( self ) :
  self . show ( )
  time . sleep ( 2 )
  self . kbd . doModal ( )
  if ( self . kbd . isConfirmed ( ) ) :
   OOOoo = self . kbd . getText ( )
   self . close ( )
   return OOOoo
  self . close ( )
  return False
  if 27 - 27: OOooOOo * O0oO - OOooOOo + O00ooooo00 % iIiiiI1IiI1I1 . i11Ii11I1Ii1i
def I1IooooO0oOoOOoO ( ) :
 import time
 return str ( int ( time . time ( ) * 1000 ) )
 if 7 - 7: OoOO - OoOO0ooOOoo0O * o0000oOoOoO0o + ii11ii1ii . OoOO
def oOo0O ( ) :
 import time
 return str ( int ( time . time ( ) ) )
 if 85 - 85: OOO0O0O0ooooo
def IiiIiI1I1 ( ) :
 iI111i11iI1 = [ ]
 III1ii = sys . argv [ 2 ]
 if len ( III1ii ) >= 2 :
  iI1III1iIi11 = sys . argv [ 2 ]
  i11I1I = iI1III1iIi11 . replace ( '?' , '' )
  if ( iI1III1iIi11 [ len ( iI1III1iIi11 ) - 1 ] == '/' ) :
   iI1III1iIi11 = iI1III1iIi11 [ 0 : len ( iI1III1iIi11 ) - 2 ]
  oo0ooooo00o = i11I1I . split ( '&' )
  iI111i11iI1 = { }
  for II in range ( len ( oo0ooooo00o ) ) :
   Oo = { }
   Oo = oo0ooooo00o [ II ] . split ( '=' )
   if ( len ( Oo ) ) == 2 :
    iI111i11iI1 [ Oo [ 0 ] ] = Oo [ 1 ]
 return iI111i11iI1
 if 80 - 80: IIii1I . OOO0O0O0ooooo / oO0o0ooO0 % oO0o0ooO0
def ooOo000OoO0o ( url ) :
 import urlresolver
 ooooo0O0 = urlresolver . HostedMediaFile ( url )
 if ooooo0O0 :
  oo0oO = urlresolver . resolve ( url )
  i1III1iI = oo0oO
  if isinstance ( i1III1iI , list ) :
   for OOo in i1III1iI :
    ii1i = Ooo . getSetting ( 'quality' )
    if OOo [ 'quality' ] == 'HD' :
     oo0oO = OOo [ 'url' ]
     break
    elif OOo [ 'quality' ] == 'SD' :
     oo0oO = OOo [ 'url' ]
    elif OOo [ 'quality' ] == '1080p' and Ooo . getSetting ( '1080pquality' ) == 'true' :
     oo0oO = OOo [ 'url' ]
     break
  else :
   oo0oO = i1III1iI
 else :
  xbmc . executebuiltin ( "XBMC.Notification(Wolf,Urlresolver donot support this domain. - ,5000)" )
 return oo0oO
def i1IiiiiIi1I ( name , mu_playlist , queueVideo = None ) :
 i1I1i111Ii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 if 56 - 56: II1 * OOO0O0O0ooooo
 if Ooo . getSetting ( 'ask_playlist_items' ) == 'true' and not queueVideo :
  import urlparse
  oo0OoOOooO = [ ]
  for II in mu_playlist :
   o0o0OO0o00o0O = urlparse . urlparse ( II ) . netloc
   if o0o0OO0o00o0O == '' :
    oo0OoOOooO . append ( name )
   else :
    oo0OoOOooO . append ( o0o0OO0o00o0O )
  IIIIIIi1i = xbmcgui . Dialog ( )
  OoOo00o = IIIIIIi1i . select ( 'Choose a video source' , oo0OoOOooO )
  if OoOo00o >= 0 :
   if "&mode=19" in mu_playlist [ OoOo00o ] :
    if 26 - 26: IIii1I - OOO0O0O0ooooo . OOO0O0O0ooooo
    xbmc . Player ( ) . play ( ooOo000OoO0o ( mu_playlist [ OoOo00o ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) ) )
   elif "$doregex" in mu_playlist [ OoOo00o ] :
    print mu_playlist [ OoOo00o ]
    O0oOoo = mu_playlist [ OoOo00o ] . split ( '&regexs=' )
    print O0oOoo
    I1II11IiII , OOOiII1 = ii1I1IIii11 ( O0oOoo [ 1 ] , O0oOoo [ 0 ] )
    OoOOoO0O0oO = I1II11IiII . replace ( ';' , '' )
    xbmc . Player ( ) . play ( OoOOoO0O0oO )
    if 92 - 92: IiIIi1I1Iiii / i11iIiiIii + OoOO
   else :
    I1II11IiII = mu_playlist [ OoOo00o ]
    xbmc . Player ( ) . play ( I1II11IiII )
 elif not queueVideo :
  if 87 - 87: OOooOOo % IIii1I
  i1I1i111Ii . clear ( )
  o00o0 = 0
  for II in mu_playlist :
   o00o0 += 1
   o0OO0OOO0O = xbmcgui . ListItem ( '%s) %s' % ( str ( o00o0 ) , name ) )
   if 36 - 36: i11iIiiIii / IIII . o00O0oo + O0oO . OOO0O0O0ooooo + IIiIiII11i
   try :
    if "$doregex" in II :
     O0oOoo = II . split ( '&regexs=' )
     print O0oOoo
     I1II11IiII , OOOiII1 = ii1I1IIii11 ( O0oOoo [ 1 ] , O0oOoo [ 0 ] )
    elif "&mode=19" in II :
     I1II11IiII = ooOo000OoO0o ( II . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    if I1II11IiII :
     i1I1i111Ii . add ( I1II11IiII , o0OO0OOO0O )
    else :
     raise
   except Exception :
    i1I1i111Ii . add ( II , o0OO0OOO0O )
    pass
    if 36 - 36: O00ooooo00 - OoOO - o0oO0
  xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
 else :
  if 7 - 7: i11iIiiIii + IIiIiII11i
  I1iii = xbmcgui . ListItem ( name )
  i1I1i111Ii . add ( mu_playlist , I1iii )
  if 47 - 47: o0oO0 - o0000oOoOoO0o / i11Ii11I1Ii1i - IiIIi1I1Iiii + IIII - IIii1I
  if 68 - 68: oO0o0ooO0 - OoOO0ooOOoo0O + IiIIi1I1Iiii
def i11Iii1Ii1i1 ( name , url ) :
 if Ooo . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('Wolf','Choose a location to save files.',15000," + I11 + ")" )
  Ooo . openSettings ( )
 iI1III1iIi11 = { 'url' : url , 'download_path' : Ooo . getSetting ( 'save_location' ) }
 downloader . download ( name , iI1III1iIi11 )
 IIIIIIi1i = xbmcgui . Dialog ( )
 O0Oo00O = IIIIIIi1i . yesno ( 'Wolf' , 'Do you want to add this file as a source?' )
 if O0Oo00O :
  o0oo0o0O00OO ( os . path . join ( Ooo . getSetting ( 'save_location' ) , name ) )
  if 10 - 10: IIII . O00ooooo00 + oO0o0ooO0
def oOOoOOO0oo0 ( url , name ) :
 if 87 - 87: i11Ii11I1Ii1i / OOooOOo % ii11ii1ii * OoOO0ooOOoo0O
 oOOOoo0o = [ 'plugin.video.PsycoTV' , 'plugin://plugin.video.phstreams' , 'plugin://plugin.video.SportsDevil' , 'plugin://plugin.video.CanTVLive' , 'plugin://plugin.video.ccloudtv' , 'plugin://plugin.video.prosport' , 'plugin://plugin.video.p2psport' , ]
 if 44 - 44: OOO0O0O0ooooo % O00ooooo00
 if 42 - 42: iIiiiI1IiI1I1 - Ooo00oOo00o - II1 . IIII / OOooOOo
 if 56 - 56: i11iIiiIii - IIii1I . iIiiiI1IiI1I1
 if 81 - 81: O0oO / OOooOOo * O0oO . OOO0O0O0ooooo
 if 61 - 61: Ooo00oOo00o * o0000oOoOoO0o + o0oO0 . IIii1I % o00O0oo . o0oO0
 if 53 - 53: o0oO0 * O0oO / IIii1I / IIiIiII11i % OoOO
 if 39 - 39: Ooo00oOo00o / II1 . Ooo00oOo00o * OoOO / OOooOOo
 oo0OoOOooO = [ 'Psycho TV' , 'Phoenix' , 'SportsDevil' , 'CanTVLive' , 'Ccloudtv' , 'Prosport' , 'P2psport' ]
 if 38 - 38: Ooo00oOo00o / i11Ii11I1Ii1i % o0oO0 * o00O0oo + i11iIiiIii % i11Ii11I1Ii1i
 IIIIIIi1i = xbmcgui . Dialog ( )
 OoOo00o = IIIIIIi1i . select ( 'Choose a video source' , oo0OoOOooO )
 if 61 - 61: o0oO0 - oO0o0ooO0 % OoOO / i11Ii11I1Ii1i / IIII + IIii1I
 if OoOo00o >= 0 :
  url = oOOOoo0o [ OoOo00o ]
  print 'url' , url
  O0O0oo ( url )
  if 83 - 83: O0oO / o0oO0
def i1I111I ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False , regexs = None , reg_url = None , allinfo = { } ) :
 if 64 - 64: Ooo00oOo00o % O0oO . o0oO0 % Ooo00oOo00o + o00O0oo * O0oO
 OOOO00OooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOOiI1 = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if len ( allinfo ) < 1 :
  O00oO0o000oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 else :
  O00oO0o000oO . setInfo ( type = "Video" , infoLabels = allinfo )
 O00oO0o000oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II11i1iI = [ ]
  o0o0o0oO0oOO = Ooo . getSetting ( 'parentalblocked' )
  o0o0o0oO0oOO = o0o0o0oO0oOO == "true"
  iI1 = Ooo . getSetting ( 'parentalblockedpin' )
  if 12 - 12: o0oO0 + o0000oOoOoO0o + o00O0oo . O0oO / oO0o0ooO0
  if len ( iI1 ) > 0 :
   if o0o0o0oO0oOO :
    I1i11II11i1iI . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   else :
    I1i11II11i1iI . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 29 - 29: O0oO . i11Ii11I1Ii1i - iIiiiI1IiI1I1
  if showcontext == 'source' :
   if 68 - 68: IIii1I + iIiiiI1IiI1I1 / OoOO0ooOOoo0O
   if name in str ( i1iiIIiiI111 ) :
    I1i11II11i1iI . append ( ( 'Remove from Sources' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 91 - 91: OOooOOo % IIii1I . IIiIiII11i
    if 70 - 70: o00O0oo % iIiiiI1IiI1I1 % OOO0O0O0ooooo . O00ooooo00 / o0oO0
  elif showcontext == 'download' :
   I1i11II11i1iI . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
   if 100 - 100: OoOO * i11iIiiIii % OoOO0ooOOoo0O / IiIIi1I1Iiii / i11Ii11I1Ii1i + OoOO
  if showcontext == '!!update' :
   o00ooOoo = (
 '%s?url=%s&mode=17&regexs=%s'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( reg_url ) , regexs )
 )
   I1i11II11i1iI . append ( ( '[COLOR yellow]!!update[/COLOR]' , 'XBMC.RunPlugin(%s)' % o00ooOoo ) )
  O00oO0o000oO . addContextMenuItems ( I1i11II11i1iI )
 OOOiI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOO00OooO , listitem = O00oO0o000oO , isFolder = True )
 return OOOiI1
def i111i1I1ii1i ( url , title , media_type = 'video' ) :
 if 100 - 100: O0oO . oO0o0ooO0 - IIii1I . i11iIiiIii / iIiiiI1IiI1I1
 if 71 - 71: o0oO0 * IiIIi1I1Iiii . o00O0oo
 import youtubedl
 if not url == '' :
  if media_type == 'audio' :
   youtubedl . single_YD ( url , download = True , audio = True )
  else :
   youtubedl . single_YD ( url , download = True )
 elif xbmc . Player ( ) . isPlaying ( ) == True :
  import YDStreamExtractor
  if YDStreamExtractor . isDownloading ( ) == True :
   if 49 - 49: O0oO * OOO0O0O0ooooo . O0oO
   YDStreamExtractor . manageDownloads ( )
  else :
   ii1II1II = xbmc . Player ( ) . getPlayingFile ( )
   if 42 - 42: oO0o0ooO0
   ii1II1II = ii1II1II . split ( '|User-Agent=' ) [ 0 ]
   o0OO0OOO0O = { 'url' : ii1II1II , 'title' : title , 'media_type' : media_type }
   youtubedl . single_YD ( '' , download = True , dl_info = o0OO0OOO0O )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)" )
  if 68 - 68: o0000oOoOoO0o . IiIIi1I1Iiii % i11Ii11I1Ii1i - II1 * IIII . o0000oOoOoO0o
  if 46 - 46: i11iIiiIii - o0000oOoOoO0o * IIiIiII11i * o00O0oo % OoOO * O00ooooo00
def Iii1I ( string ) :
 if isinstance ( string , basestring ) :
  if isinstance ( string , unicode ) :
   string = string . encode ( 'ascii' , 'ignore' )
 return string
def i1i1i1i1IiII1 ( string , encoding = 'utf-8' ) :
 if isinstance ( string , basestring ) :
  if not isinstance ( string , unicode ) :
   string = unicode ( string , encoding , 'ignore' )
 return string
def II1oOOO00OOOoOO ( s ) : return "" . join ( filter ( lambda III : ord ( III ) < 128 , s ) )
if 53 - 53: o0oO0 + OOooOOo
def i1IiiiiiIiII ( command ) :
 ii11iIi1I = ''
 try :
  ii11iIi1I = xbmc . executeJSONRPC ( i1i1i1i1IiII1 ( command ) )
 except UnicodeEncodeError :
  ii11iIi1I = xbmc . executeJSONRPC ( Iii1I ( command ) )
  if 26 - 26: ii11ii1ii . IIii1I
 return i1i1i1i1IiII1 ( ii11iIi1I )
 if 67 - 67: IiIIi1I1Iiii / OOO0O0O0ooooo
def O0O0oo ( url , give_me_result = None , playlist = False ) :
 if 'audio' in url :
  oO0Oo00oo = i1i1i1i1IiII1 ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params": {"directory":"%s","media":"video", "properties": ["title", "album", "artist", "duration","thumbnail", "year"]}, "id": 1}' ) % url
 else :
  oO0Oo00oo = i1i1i1i1IiII1 ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":[ "plot","playcount","director", "genre","votes","duration","trailer","premiered","thumbnail","title","year","dateadded","fanart","rating","season","episode","studio","mpaa"]},"id":1}' ) % url
 OoOoooO000OO = json . loads ( i1IiiiiiIiII ( oO0Oo00oo ) )
 if 62 - 62: o0000oOoOoO0o + IiIIi1I1Iiii % IIii1I / IIii1I . i11Ii11I1Ii1i . O0oO
 if give_me_result :
  return OoOoooO000OO
 if OoOoooO000OO . has_key ( 'error' ) :
  return
 else :
  if 21 - 21: Ooo00oOo00o - oO0o0ooO0 - IIiIiII11i / OOooOOo
  for II in OoOoooO000OO [ 'result' ] [ 'files' ] :
   ii1 = { }
   url = II [ 'file' ]
   iI1Ii11iII1 = II1oOOO00OOOoOO ( II [ 'label' ] )
   o0 = II1oOOO00OOOoOO ( II [ 'thumbnail' ] )
   iI11iiiI1II = II1oOOO00OOOoOO ( II [ 'fanart' ] )
   ii1 = dict ( ( k , v ) for k , v in II . iteritems ( ) if not v == '0' or not v == - 1 or v == '' )
   ii1 . pop ( "file" , None )
   if II [ 'filetype' ] == 'file' :
    if playlist :
     i1IiiiiIi1I ( iI1Ii11iII1 , url , queueVideo = '1' )
     continue
    else :
     o00oooO0Oo ( url , iI1Ii11iII1 , o0 , iI11iiiI1II , '' , '' , '' , '' , None , '' , total = len ( OoOoooO000OO [ 'result' ] [ 'files' ] ) , allinfo = ii1 )
     if 97 - 97: OoOO * OoOO / IIII
     if II [ 'type' ] and II [ 'type' ] == 'tvshow' :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'tvshows' )
     elif II [ 'episode' ] > 0 :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'episodes' )
      if 6 - 6: OoOO0ooOOoo0O
   else :
    i1I111I ( iI1Ii11iII1 , url , 53 , o0 , iI11iiiI1II , '' , '' , '' , '' , allinfo = ii1 )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if 72 - 72: o00O0oo * OoOO - OOooOOo / OoOO + o0000oOoOoO0o - IIII
def o00oooO0Oo ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total , setCookie = "" , allinfo = { } ) :
 if 49 - 49: Ooo00oOo00o - OOO0O0O0ooooo / Ooo00oOo00o * OOooOOo + o0oO0
 I1i11II11i1iI = [ ]
 o0o0o0oO0oOO = Ooo . getSetting ( 'parentalblocked' )
 o0o0o0oO0oOO = o0o0o0oO0oOO == "true"
 iI1 = Ooo . getSetting ( 'parentalblockedpin' )
 if 35 - 35: iIiiiI1IiI1I1 . IIiIiII11i / O00ooooo00 / IIiIiII11i * OoOO0ooOOoo0O
 if len ( iI1 ) > 0 :
  if o0o0o0oO0oOO :
   I1i11II11i1iI . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  else :
   I1i11II11i1iI . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   if 85 - 85: iIiiiI1IiI1I1 . i11Ii11I1Ii1i % o0000oOoOoO0o % o00O0oo
 try :
  name = name . encode ( 'utf-8' )
 except : pass
 if 80 - 80: OoOO0ooOOoo0O * o00O0oo / IIii1I % OoOO0ooOOoo0O / IIii1I
 if 42 - 42: O00ooooo00 / i11iIiiIii . IiIIi1I1Iiii * IIII . i11iIiiIii * OOO0O0O0ooooo
 if 44 - 44: O00ooooo00 . IIiIiII11i / i11iIiiIii + O0oO
 if 27 - 27: o0000oOoOoO0o
 if 52 - 52: o0oO0 % OOooOOo + IIii1I * OoOO0ooOOoo0O . oO0o0ooO0
 if 95 - 95: IIii1I . O0oO - II1 * Ooo00oOo00o / ii11ii1ii
 OOOiI1 = True
 oOo0OO0o0 = False
 if regexs :
  II1I1I = '17'
  if 'listrepeat' in regexs :
   oOo0OO0o0 = True
   print 'setting as folder in link'
  I1i11II11i1iI . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif ( any ( x in url for x in OO0o ) and url . startswith ( 'http' ) ) or url . endswith ( '&mode=19' ) :
  url = url . replace ( '&mode=19' , '' )
  II1I1I = '19'
  I1i11II11i1iI . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . endswith ( '&mode=18' ) :
  url = url . replace ( '&mode=18' , '' )
  II1I1I = '18'
  I1i11II11i1iI . append ( ( '[COLOR white]!!Download!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  if Ooo . getSetting ( 'dlaudioonly' ) == 'true' :
   I1i11II11i1iI . append ( ( '!!Download [COLOR seablue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . startswith ( 'magnet:?xt=' ) :
  if '&' in url and not '&amp;' in url :
   url = url . replace ( '&' , '&amp;' )
  url = 'plugin://plugin.video.pulsar/play?uri=' + url
  II1I1I = '12'
 else :
  II1I1I = '12'
  I1i11II11i1iI . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 if 'plugin://plugin.video.youtube/play/?video_id=' in url :
  III11I = url . replace ( 'plugin://plugin.video.youtube/play/?video_id=' , 'https://www.youtube.com/watch?v=' )
  I1i11II11i1iI . append ( ( '!!Download [COLOR blue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( III11I ) , urllib . quote_plus ( name ) ) ) )
 OOOO00OooO = sys . argv [ 0 ] + "?"
 i1o0oo0 = False
 if playlist :
  if Ooo . getSetting ( 'add_playlist' ) == "false" :
   OOOO00OooO += "url=" + urllib . quote_plus ( url ) + "&mode=" + II1I1I
  else :
   OOOO00OooO += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) )
   name = name + '[COLOR green][/COLOR]'
   i1o0oo0 = True
 else :
  OOOO00OooO += "url=" + urllib . quote_plus ( url ) + "&mode=" + II1I1I
 if regexs :
  OOOO00OooO += "&regexs=" + regexs
 if not setCookie == '' :
  OOOO00OooO += "&setCookie=" + urllib . quote_plus ( setCookie )
  if 67 - 67: OOO0O0O0ooooo * o00O0oo - ii11ii1ii - iIiiiI1IiI1I1
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 if len ( allinfo ) < 1 :
  O00oO0o000oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
  if 41 - 41: IIiIiII11i - o0oO0 % iIiiiI1IiI1I1 . o0oO0 - o00O0oo
 else :
  O00oO0o000oO . setInfo ( type = "Video" , infoLabels = allinfo )
 O00oO0o000oO . setProperty ( "Fanart_Image" , fanart )
 if 45 - 45: oO0o0ooO0 - o0000oOoOoO0o
 if ( not i1o0oo0 ) and not any ( x in url for x in Oo0Ooo ) and not '$PLAYERPROXY$=' in url :
  if regexs :
   if 70 - 70: Ooo00oOo00o % IIiIiII11i / IIiIiII11i . o00O0oo % i11Ii11I1Ii1i . iIiiiI1IiI1I1
   if '$pyFunction:playmedia(' not in urllib . unquote_plus ( regexs ) and 'notplayable' not in urllib . unquote_plus ( regexs ) and 'listrepeat' not in urllib . unquote_plus ( regexs ) :
    if 10 - 10: oO0o0ooO0 - i11iIiiIii . OoOO % O00ooooo00
    O00oO0o000oO . setProperty ( 'IsPlayable' , 'true' )
  else :
   O00oO0o000oO . setProperty ( 'IsPlayable' , 'true' )
 else :
  generator . addon_log ( 'NOT setting isplayable' + url )
  if 78 - 78: IIii1I * IiIIi1I1Iiii . IiIIi1I1Iiii - o0000oOoOoO0o . IIii1I
 if not playlist is None :
  if Ooo . getSetting ( 'add_playlist' ) == "false" :
   I111I1I = name . split ( ') ' ) [ 1 ]
   Oo0000 = [
 ( 'Play ' + I111I1I + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( I111I1I ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) ) )
 ]
   O00oO0o000oO . addContextMenuItems ( Oo0000 )
   if 52 - 52: OoOO / IIII
 OOOiI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOO00OooO , listitem = O00oO0o000oO , totalItems = total , isFolder = oOo0OO0o0 )
 if 37 - 37: o00O0oo
 if 83 - 83: OOO0O0O0ooooo
 return OOOiI1
 if 89 - 89: IiIIi1I1Iiii + OoOO - ii11ii1ii
 if 40 - 40: Ooo00oOo00o + Ooo00oOo00o
def o0oo0o00ooO00 ( url , name , iconimage , setresolved = True ) :
 if setresolved :
  O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = iconimage )
  O00oO0o000oO . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
  O00oO0o000oO . setProperty ( "IsPlayable" , "true" )
  O00oO0o000oO . setPath ( url )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O00oO0o000oO )
 else :
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  if 37 - 37: Ooo00oOo00o - OoOO . II1 . i11Ii11I1Ii1i + OOooOOo / oO0o0ooO0
  if 15 - 15: O0oO . O00ooooo00 * OOooOOo % IIii1I
  if 35 - 35: OoOO + o0oO0 - OOooOOo % OoOO0ooOOoo0O % ii11ii1ii % OOooOOo
  if 45 - 45: IIiIiII11i * o0000oOoOoO0o % Ooo00oOo00o
def OoO ( link ) :
 I1II11IiII = urllib . urlopen ( link )
 i111I11I = I1II11IiII . read ( )
 I1II11IiII . close ( )
 OoOoOOoO = i111I11I . split ( "Jetzt" )
 ii1ii1i11I1I = OoOoOOoO [ 1 ] . split ( 'programm/detail.php?const_id=' )
 iiII1iiiiiii = ii1ii1i11I1I [ 1 ] . split ( '<br /><a href="/' )
 iiIiii = iiII1iiiiiii [ 0 ] [ 40 : len ( iiII1iiiiiii [ 0 ] ) ]
 iiI1ii = ii1ii1i11I1I [ 2 ] . split ( "</a></p></div>" )
 O0OooOO = iiI1ii [ 0 ] [ 17 : len ( iiI1ii [ 0 ] ) ]
 O0OooOO = O0OooOO . encode ( 'utf-8' )
 return "  - " + O0OooOO + " - " + iiIiii
 if 49 - 49: O0oO / i11Ii11I1Ii1i / o0000oOoOoO0o
 if 25 - 25: IIiIiII11i % OOO0O0O0ooooo + O00ooooo00 - i11Ii11I1Ii1i
def oooooo0O000o ( url , regex ) :
 ii11iIi1I = IIIiI11ii ( url )
 try :
  o00o0 = re . findall ( regex , ii11iIi1I ) [ 0 ]
  return o00o0
 except :
  generator . addon_log ( 'regex failed' )
  generator . addon_log ( regex )
  return
  if 38 - 38: ii11ii1ii % o0oO0 + i11iIiiIii + IIII + i11Ii11I1Ii1i / i11iIiiIii
  if 94 - 94: IIII - IiIIi1I1Iiii + OoOO0ooOOoo0O
  if 59 - 59: o00O0oo . IIiIiII11i - IIii1I + IIii1I
def oO0o0Oo ( d , root = "root" , nested = 0 ) :
 if 76 - 76: i11Ii11I1Ii1i / OOooOOo + OoOO
 IiI11I111 = lambda Ooo000O00 : '<' + Ooo000O00 + '>'
 i1iI1Iiii1I = lambda Ooo000O00 : '</' + Ooo000O00 + '>\n'
 I1iII = lambda oO00oo0o00o0o , Iii1I1IIII : Iii1I1IIII + IiI11I111 ( OooooOoO ) + str ( oO00oo0o00o0o ) + i1iI1Iiii1I ( OooooOoO )
 if 79 - 79: i11Ii11I1Ii1i % o0000oOoOoO0o
 Iii1I1IIII = IiI11I111 ( root ) + '\n' if root else ""
 if 54 - 54: OOooOOo - o0oO0
 for OooooOoO , O0I1II1 in d . iteritems ( ) :
  oOOoo = type ( O0I1II1 )
  if nested == 0 : OooooOoO = 'regex'
  if oOOoo is list :
   for oO00oo0o00o0o in O0I1II1 :
    oO00oo0o00o0o = escape ( oO00oo0o00o0o )
    Iii1I1IIII = I1iII ( oO00oo0o00o0o , Iii1I1IIII )
    if 9 - 9: o00O0oo . Ooo00oOo00o * O00ooooo00 . II1
  if oOOoo is dict :
   Iii1I1IIII = I1iII ( '\n' + oO0o0Oo ( O0I1II1 , None , nested + 1 ) , Iii1I1IIII )
  if oOOoo is not list and oOOoo is not dict :
   if not O0I1II1 is None : O0I1II1 = escape ( O0I1II1 )
   Iii1I1IIII = I1iII ( O0I1II1 , Iii1I1IIII )
   if 32 - 32: OOooOOo . OoOO % IIiIiII11i - iIiiiI1IiI1I1
 Iii1I1IIII += i1iI1Iiii1I ( root ) if root else ""
 if 11 - 11: OOO0O0O0ooooo + IIiIiII11i
 return Iii1I1IIII
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 80 - 80: OoOO0ooOOoo0O % OoOO0ooOOoo0O % OOO0O0O0ooooo - i11iIiiIii . IIII / OOO0O0O0ooooo
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_UNSORTED )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_DATE )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_GENRE )
except :
 pass
 if 13 - 13: IIiIiII11i + OOO0O0O0ooooo - OoOO % IiIIi1I1Iiii / oO0o0ooO0 . O00ooooo00
iI1III1iIi11 = IiiIiI1I1 ( )
if 60 - 60: IiIIi1I1Iiii . O0oO % IIiIiII11i - o0oO0
I1II11IiII = None
iI1Ii11iII1 = None
II1I1I = None
i1I1i111Ii = None
oooOo = None
iI11iiiI1II = Oo0o0000o0o0
i1I1i111Ii = None
oOoO0Oo0 = None
iiI1I11i1i = None
if 7 - 7: i11Ii11I1Ii1i + oO0o0ooO0
try :
 I1II11IiII = urllib . unquote_plus ( iI1III1iIi11 [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 iI1Ii11iII1 = urllib . unquote_plus ( iI1III1iIi11 [ "name" ] )
except :
 pass
try :
 oooOo = urllib . unquote_plus ( iI1III1iIi11 [ "iconimage" ] )
except :
 pass
try :
 iI11iiiI1II = urllib . unquote_plus ( iI1III1iIi11 [ "fanart" ] )
except :
 pass
try :
 II1I1I = int ( iI1III1iIi11 [ "mode" ] )
except :
 pass
try :
 i1I1i111Ii = eval ( urllib . unquote_plus ( iI1III1iIi11 [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 oOoO0Oo0 = int ( iI1III1iIi11 [ "fav_mode" ] )
except :
 pass
try :
 iiI1I11i1i = iI1III1iIi11 [ "regexs" ]
except :
 pass
 if 32 - 32: IIii1I % IIiIiII11i / i11iIiiIii + o0000oOoOoO0o - ii11ii1ii . IIII
generator . addon_log ( "Mode: " + str ( II1I1I ) )
if 86 - 86: O00ooooo00 / oO0o0ooO0 * IIiIiII11i
if 67 - 67: OoOO * OoOO / OoOO0ooOOoo0O * II1 + OOooOOo
if not I1II11IiII is None :
 generator . addon_log ( "URL: " + str ( I1II11IiII . encode ( 'utf-8' ) ) )
generator . addon_log ( "Name: " + str ( iI1Ii11iII1 ) )
if 79 - 79: O00ooooo00
if II1I1I == None :
 OoOIii11iI11i1I ( )
 generator . addon_log ( "getSources" )
 iii11iII ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 1 - 1: OoOO0ooOOoo0O / O00ooooo00
elif II1I1I == 1 :
 generator . addon_log ( "getData" )
 ii11iIi1I = None
 if iiI1I11i1i :
  ii11iIi1I = ii1I1IIii11 ( iiI1I11i1i , I1II11IiII )
  I1II11IiII = ''
  if 74 - 74: o00O0oo / II1 / IiIIi1I1Iiii * i11iIiiIii . iIiiiI1IiI1I1 . II1
 O0O00o0OOO0 ( I1II11IiII , iI11iiiI1II , ii11iIi1I )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 59 - 59: i11iIiiIii . II1 / o00O0oo * OoOO + II1
elif II1I1I == 2 :
 generator . addon_log ( "getChannelItems" )
 o0O0OOO0Ooo ( iI1Ii11iII1 , I1II11IiII , iI11iiiI1II )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 3 - 3: i11iIiiIii * IiIIi1I1Iiii % IIii1I % IIiIiII11i * IIII / o0000oOoOoO0o
elif II1I1I == 3 :
 generator . addon_log ( "getSubChannelItems" )
 IiI111111IIII ( iI1Ii11iII1 , I1II11IiII , iI11iiiI1II )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 95 - 95: O0oO * OOO0O0O0ooooo * o0oO0 . II1 % IiIIi1I1Iiii + OoOO
elif II1I1I == 5 :
 generator . addon_log ( "LinksSources" )
 OoOo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 98 - 98: OoOO0ooOOoo0O . II1
elif II1I1I == 6 :
 generator . addon_log ( "rmFavorite" )
 try :
  iI1Ii11iII1 = iI1Ii11iII1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iI1Ii11iII1 = iI1Ii11iII1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 rmFavorite ( iI1Ii11iII1 )
 if 54 - 54: OOO0O0O0ooooo / O0oO % i11Ii11I1Ii1i * O00ooooo00 * OOO0O0O0ooooo
elif II1I1I == 7 :
 generator . addon_log ( "addSource" )
 o0oo0o0O00OO ( I1II11IiII )
 if 48 - 48: ii11ii1ii . OoOO0ooOOoo0O % OOooOOo - OOooOOo
elif II1I1I == 8 :
 generator . addon_log ( "rmSource" )
 II111ii1II1i ( iI1Ii11iII1 )
 if 33 - 33: o00O0oo % iIiiiI1IiI1I1 + Ooo00oOo00o
elif II1I1I == 9 :
 generator . addon_log ( "download_file" )
 i11Iii1Ii1i1 ( iI1Ii11iII1 , I1II11IiII )
 if 93 - 93: O00ooooo00 . O0oO / IIiIiII11i + O0oO
elif II1I1I == 10 :
 generator . addon_log ( "getCommunitySources" )
 IIii1Ii1 ( )
 if 58 - 58: OoOO + OOO0O0O0ooooo . IiIIi1I1Iiii + OOooOOo - Ooo00oOo00o - OOooOOo
elif II1I1I == 11 :
 generator . addon_log ( "addSource" )
 o0oo0o0O00OO ( I1II11IiII )
 if 41 - 41: IiIIi1I1Iiii / O00ooooo00 / IiIIi1I1Iiii - IIII . ii11ii1ii
elif II1I1I == 12 :
 generator . addon_log ( "setResolvedUrl" )
 if not I1II11IiII . startswith ( "plugin://plugin" ) or not any ( x in I1II11IiII for x in Oo0Ooo ) :
  o00o0 = xbmcgui . ListItem ( path = I1II11IiII )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o00o0 )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + I1II11IiII + ')' )
  if 65 - 65: OOO0O0O0ooooo * i11iIiiIii . II1 / IIiIiII11i / IIII
  if 69 - 69: i11Ii11I1Ii1i % i11Ii11I1Ii1i
elif II1I1I == 13 :
 generator . addon_log ( "play_playlist" )
 i1IiiiiIi1I ( iI1Ii11iII1 , i1I1i111Ii )
 if 76 - 76: i11iIiiIii * IIII / Ooo00oOo00o % OoOO + o0000oOoOoO0o
elif II1I1I == 14 :
 generator . addon_log ( "get_xml_database" )
 i1II1 ( I1II11IiII )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 48 - 48: IIii1I % O00ooooo00 + OOooOOo % ii11ii1ii
elif II1I1I == 15 :
 generator . addon_log ( "browse_xml_database" )
 i1II1 ( I1II11IiII , True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 79 - 79: OOooOOo % IIiIiII11i % oO0o0ooO0 / O00ooooo00 % Ooo00oOo00o
elif II1I1I == 16 :
 generator . addon_log ( "browse_community" )
 IIii1Ii1 ( I1II11IiII , browse = True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 56 - 56: IIii1I - i11iIiiIii * IIII
elif II1I1I == 17 :
 generator . addon_log ( "getRegexParsed" )
 if 84 - 84: o0000oOoOoO0o + oO0o0ooO0 + ii11ii1ii
 ii11iIi1I = None
 if iiI1I11i1i and 'listrepeat' in urllib . unquote_plus ( iiI1I11i1i ) :
  IiII1II11I , O0Oo00O , OOooo0O0o0 , iiI1I11i1i = ii1I1IIii11 ( iiI1I11i1i , I1II11IiII )
  if 33 - 33: oO0o0ooO0
  I1iiioOO0OO0O = ''
  if 93 - 93: i11Ii11I1Ii1i
  if 34 - 34: OoOO0ooOOoo0O - i11Ii11I1Ii1i * IiIIi1I1Iiii / ii11ii1ii
  iI1iiIi1 = OOooo0O0o0 [ 'name' ]
  i1iiiIi1Iii = iiI1I11i1i . pop ( iI1iiIi1 )
  if 54 - 54: i11Ii11I1Ii1i . IIii1I * O00ooooo00
  I1II11IiII = ''
  import copy
  II1II1i = ''
  for iIO0OO0o0O00oO in O0Oo00O :
   try :
    o00OoO0o0oOo = copy . deepcopy ( iiI1I11i1i )
    if 92 - 92: O00ooooo00 % i11Ii11I1Ii1i + i11Ii11I1Ii1i - IIii1I . oO0o0ooO0
    iIIi1o0Ooo0o0Oo = IiII1II11I
    II = 0
    for II in range ( len ( iIO0OO0o0O00oO ) ) :
     if 55 - 55: IIii1I * IIII
     if len ( o00OoO0o0oOo ) > 0 :
      for oo , Ii11iI in o00OoO0o0oOo . iteritems ( ) :
       if Ii11iI is not None :
        for ii111I11Ii , i11IiiI1Ii1 in Ii11iI . iteritems ( ) :
         if i11IiiI1Ii1 is not None :
          if 23 - 23: IIII % II1 / IIii1I + OoOO / O00ooooo00 / ii11ii1ii
          if 94 - 94: O00ooooo00
          if 36 - 36: IIiIiII11i + IiIIi1I1Iiii
          if 46 - 46: IIII
          if type ( i11IiiI1Ii1 ) is dict :
           for ooIiI11i1I11111 , Ii1IIIIIIiI1 in i11IiiI1Ii1 . iteritems ( ) :
            if Ii1IIIIIIiI1 is not None :
             i11IiiI1Ii1 [ ooIiI11i1I11111 ] = Ii1IIIIIIiI1 . replace ( '[' + iI1iiIi1 + '.param' + str ( II + 1 ) + ']' , iIO0OO0o0O00oO [ II ] . decode ( 'utf-8' ) )
          else :
           Ii11iI [ ii111I11Ii ] = i11IiiI1Ii1 . replace ( '[' + iI1iiIi1 + '.param' + str ( II + 1 ) + ']' , iIO0OO0o0O00oO [ II ] . decode ( 'utf-8' ) )
     iIIi1o0Ooo0o0Oo = iIIi1o0Ooo0o0Oo . replace ( '[' + iI1iiIi1 + '.param' + str ( II + 1 ) + ']' , iIO0OO0o0O00oO [ II ] . decode ( 'utf-8' ) )
     if 24 - 24: IIiIiII11i * oO0o0ooO0 % OOO0O0O0ooooo - IiIIi1I1Iiii
     if 30 - 30: O00ooooo00
     if 4 - 4: o0oO0 - IIiIiII11i % OoOO0ooOOoo0O / ii11ii1ii % OoOO0ooOOoo0O * iIiiiI1IiI1I1
    IiI1I = ''
    if len ( o00OoO0o0oOo ) > 0 :
     IiI1I = oO0o0Oo ( o00OoO0o0oOo , 'lsproroot' )
     IiI1I = IiI1I . split ( '<lsproroot>' ) [ 1 ] . split ( '</lsproroot' ) [ 0 ]
     if 25 - 25: OoOO0ooOOoo0O % IIiIiII11i + i11iIiiIii + OOO0O0O0ooooo * II1
    II1II1i += '\n<item>%s\n%s</item>' % ( iIIi1o0Ooo0o0Oo , IiI1I )
   except : traceback . print_exc ( file = sys . stdout )
   if 64 - 64: O00ooooo00
   if 10 - 10: o0oO0 % OOO0O0O0ooooo / IIiIiII11i % o00O0oo
   if 25 - 25: iIiiiI1IiI1I1 / Ooo00oOo00o
   if 64 - 64: OOO0O0O0ooooo % i11Ii11I1Ii1i
   if 40 - 40: ii11ii1ii + o00O0oo
  O0O00o0OOO0 ( '' , '' , II1II1i )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 else :
  I1II11IiII , OOOiII1 = ii1I1IIii11 ( iiI1I11i1i , I1II11IiII )
  if I1II11IiII :
   if '$PLAYERPROXY$=' in I1II11IiII :
    I1II11IiII , ooOoOO0OoO00o = I1II11IiII . split ( '$PLAYERPROXY$=' )
    print 'proxy' , ooOoOO0OoO00o
    OoO000Oo0oO , iiiIiiiI1 = ooOoOO0OoO00o . split ( ':' )
    OO0o0oO ( I1II11IiII , iI1Ii11iII1 , oooOo , OoO000Oo0oO , iiiIiiiI1 )
   else :
    o0oo0o00ooO00 ( I1II11IiII , iI1Ii11iII1 , oooOo , OOOiII1 )
  else :
   xbmc . executebuiltin ( "XBMC.Notification(Wolf,Failed to extract regex. - " + "this" + ",4000," + I11 + ")" )
elif II1I1I == 18 :
 generator . addon_log ( "youtubedl" )
 try :
  import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(Wolf,Please [COLOR yellow]install Youtube-dl[/COLOR] module ,10000," ")" )
 OOoOoo = youtubedl . single_YD ( I1II11IiII )
 o0oo0o00ooO00 ( OOoOoo , iI1Ii11iII1 , oooOo )
elif II1I1I == 19 :
 generator . addon_log ( "Genesiscommonresolvers" )
 o0oo0o00ooO00 ( ooOo000OoO0o ( I1II11IiII ) , iI1Ii11iII1 , oooOo , True )
 if 50 - 50: i11Ii11I1Ii1i * OOooOOo + OoOO - i11iIiiIii + IiIIi1I1Iiii * OoOO
elif II1I1I == 21 :
 generator . addon_log ( "download current file using youtube-dl service" )
 i111i1I1ii1i ( '' , iI1Ii11iII1 , 'video' )
elif II1I1I == 23 :
 generator . addon_log ( "get info then download" )
 i111i1I1ii1i ( I1II11IiII , iI1Ii11iII1 , 'video' )
elif II1I1I == 24 :
 generator . addon_log ( "Audio only youtube download" )
 i111i1I1ii1i ( I1II11IiII , iI1Ii11iII1 , 'audio' )
elif II1I1I == 25 :
 generator . addon_log ( "Searchin Other plugins" )
 oOOoOOO0oo0 ( I1II11IiII , iI1Ii11iII1 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif II1I1I == 55 :
 generator . addon_log ( "enabled lock" )
 iI1 = Ooo . getSetting ( 'parentalblockedpin' )
 oOO00oOO = xbmc . Keyboard ( '' , 'Enter Pin' )
 oOO00oOO . doModal ( )
 if not ( oOO00oOO . isConfirmed ( ) == False ) :
  OoOoiI = oOO00oOO . getText ( )
  if OoOoiI == iI1 :
   Ooo . setSetting ( 'parentalblocked' , "false" )
   xbmc . executebuiltin ( "XBMC.Notification(Wolf,Parental Block Disabled,5000," + I11 + ")" )
  else :
   xbmc . executebuiltin ( "XBMC.Notification(Wolf,Wrong Pin??,5000," + I11 + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif II1I1I == 56 :
 generator . addon_log ( "disable lock" )
 Ooo . setSetting ( 'parentalblocked' , "true" )
 xbmc . executebuiltin ( "XBMC.Notification(Wolf,Parental block enabled,5000," + I11 + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 20 - 20: o0oO0 / ii11ii1ii % OOooOOo
elif II1I1I == 53 :
 generator . addon_log ( "Requesting JSON-RPC Items" )
 O0O0oo ( I1II11IiII )
 if 69 - 69: o0oO0 - O00ooooo00 % IIII . o0000oOoOoO0o - o0000oOoOoO0o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
