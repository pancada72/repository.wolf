import xbmc
import sys
import xbmcaddon
import xbmcgui
import os
import time
import skinSwitch

AddonID = xbmcaddon.Addon().getAddonInfo('id')
ADDON = xbmcaddon.Addon(id=AddonID) 
ADDONPATH = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID))
AddonTitle = ADDON.getAddonInfo('name')
HOME =  xbmc.translatePath('special://home/')
KODIVERSION = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
dialog = xbmcgui.Dialog()    
PATH = xbmcaddon.Addon().getAddonInfo('name')
VERSION = xbmcaddon.Addon().getAddonInfo('version')


def SetDefaultSkin():
	skin = xbmc.getSkinDir()
	skinswapped = 0

	##SWITCH SKIN IF THE CURRENT SKIN IS NOT DEFAULT SKIN
	if skin not in ['skin.confluence','skin.estuary']:
            choice = dialog.yesno(AddonTitle, '[COLOR red]Voltar para a skin original.[/COLOR]','Clicar YES, AutoSwitch para a skin original. Espere sem mexer com o rato ou teclado enquanto este processo decorre.', yeslabel='[B][COLOR green]YES[/COLOR][/B]',nolabel='[B][COLOR lightskyblue]NO[/COLOR][/B]')
            if choice == 0:
                sys.exit(1)
            skin = 'skin.estuary' if KODIVERSION >= 17 else 'skin.confluence'
            skinSwitch.swapSkins(skin)
            skinswapped = 1
            time.sleep(1)

	##IF A SKIN SWAP HAS HAPPENED, CHECK IF OK DIALOG (CONFLUENCE INFO SCREEN) IS PRESENT, PRESS OK IF IT'S PRESENT
	if skinswapped == 1:
            if not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin( "Action(Select)" )
	
	##IF THERE'S NO YES/NO DIALOG (SWITCH TO DEFAULT SKIN), THEN SLEEP UNTIL IT APPEARS
	if skinswapped == 1:
            while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		time.sleep(1)
	
	##WHILE YES/NO DIALOG IS PRESENT, AUTOSELECT SKIN CHANGE (PRESS LEFT AND THEN SELECT)
	if skinswapped == 1:
            while xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin( "Action(Left)" )
		xbmc.executebuiltin( "Action(Select)" )
		time.sleep(1)

	skin = xbmc.getSkinDir()

	#CHECK IF THE SKIN IS NOT DEFAULT SKIN
	if skin not in ['skin.confluence','skin.estuary']:
            if skinswapped == 1:
		choice = dialog.yesno(AddonTitle,'ERROR: AutoSwitch sem sucesso','Clicar em  Yes para colocar via manual. Clique em NO para voltar o AutoSwitch habilitar.', yeslabel='[B][COLOR green]YES[/COLOR][/B]',nolabel='[B][COLOR lightskyblue]NO[/COLOR][/B]')
		if choice == 1:
                    xbmc.executebuiltin("ActivateWindow(appearancesettings)")
                    return
		else:
                    sys.exit(1)