import os, xbmc, xbmcaddon
import binascii
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[B][COLOR yellow]Wolf Wizard[/COLOR][/B]'
BUILDERNAME    = 'Wolf Wizard'
#########################Make sure to change the repo to yours!!!!
EXCLUDES       = [ADDON_ID, 'My_Builds', 'backupdir']
BUILDFILE      = 'https://cld.pt/dl/download/ef99d18e-1522-4f76-98cd-ef48f543fb35/autobuilds.txt?download=true'
UPDATECHECK    = 0
APKFILE        = 'https://cld.pt/dl/download/2b1a4170-9ae8-4961-aab4-7402c779c971/apk.txt?download=true'
YOUTUBETITLE   = 'http://'
YOUTUBEFILE    = 'https://cld.pt/dl/download/e73d1806-c06d-4fb0-8747-2abe29dfee38/youtubetheone.txt?download=true'
ADDONFILE      = 'https://cld.pt/dl/download/408b1486-de55-492b-a973-d639e45a41d5/addons.txt?download=true'
ADVANCEDFILE   = 'https://cld.pt/dl/download/3ef2b38f-830c-4134-8fc8-b0de22786b95/krypton%20advanced.txt?download=true'
ROMPACK        = 'http://'
EMUAPKS        = 'http://'
ADDONPACK      = 'http://'
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################

##Alway test to see the color combo!!

#### NEW GUI THEME ###################################
# Choose from the following 
# Only these colors avalable
# white , blue , orange , yellow , red , purple , pink , lime , cyan, green
#Button focus color
FOCUS_BUTTON_COLOR = 'yellow'
EXIT_BUTTON_COLOR = 'white'
#Highlight outline for lists
HIGHLIGHT_LIST = 'white'
##No TXT file Banner
NO_TXT_FILE = 'red'

############################################
############################################
### The full list of colors for below can found @ https://forum.kodi.tv/showthread.php?tid=210837

#Top Main buttons
MAIN_BUTTONS_TEXT = 'white'
#All other buttons
OTHER_BUTTONS_TEXT = 'yellow'
#all list text color
##FYI any color placed in the txt file will overide this
LIST_TEXT = 'yellow'


#Description text title color
DES_T_COLOR = 'yellow'
#Description color
DESCOLOR = 'white'

#Wizard title name and verion color
WIZTITLE = 'Wolf Wizard'
WIZTITLE_COLOR = 'yellow'
VERTITLE_COLOR = 'white'
VER_NUMBER_COLOR = 'yellow'
############################################################

## The colors and theme below is still used for the pop up dialogs
##Alway test to see the color combo
# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'gold'
COLOR2         = 'red'
COLOR3         = 'red'
COLOR4         = 'snow'
COLOR5         = 'lime'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR2+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR2+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'



#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://i.imgur.com/7CIT93Q.png'
ICONMAINT      = 'https://i.imgur.com/YFw2062.png'
ICONAPK        = 'https://i.imgur.com/cGG1z5S.png'
ICONADDONS     = 'https://i.imgur.com/HlvkAYR.png'
ICONYOUTUBE    = 'https://i.imgur.com/vXDhnji.png'
ICONSAVE       = 'https://i.imgur.com/9HVIKLi.png'
ICONTRAKT      = 'https://i.imgur.com/uqCUoDB.png'
ICONREAL       = 'https://i.imgur.com/Eby6mRW.png'
ICONLOGIN      = 'https://i.imgur.com/xRVbX5r.png'
ICONCONTACT    = 'https://i.imgur.com/Pn7Ctja.png'
ICONSETTINGS   = 'https://i.imgur.com/kOVekP3.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '~'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Obrigado por usar o instalador Wolf.'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'icon.png')
CONTACTFANART  = 'https://cld.pt/dl/download/398f18f6-aa12-4922-b173-d954cb6c12e4/fanart.jpg?download=true'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'https://cld.pt/dl/download/3781985e-491c-447d-bb66-1e8aeed402a1/autobuilds.txt?download=true'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://'
# Url to folder zip is located in
REPOZIPURL     =  'http://'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = 'https://cld.pt/dl/download/c822dc56-0c68-408f-84d8-0ee2b9a474c3/notify.txt?download=true'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font25'
HEADERMESSAGE  = 'Wolf Builds Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = 'https://cld.pt/dl/download/bb146926-bf4f-4ad7-9d54-1d766f8051b8/spiral-wolf-dreams-i10931.jpg?download=true'
# Font for Notification Window
FONTSETTINGS   = 'Font12'
# Background for Notification Window
BACKGROUND     = 'https://cld.pt/dl/download/398f18f6-aa12-4922-b173-d954cb6c12e4/fanart.jpg?download=true'
############################    #############################