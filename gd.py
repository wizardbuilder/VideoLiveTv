import xbmc,xbmcaddon,xbmcplugin,os,mknet

def _getInput(default_text='', heading='', hidden=False):
	keyb = xbmc.Keyboard(default_text, heading, hidden)
	keyb.doModal()
	if (keyb.isConfirmed()):
		result = keyb.getText()
	else:
		result = False


class gd:
	addon_id		= "plugin.video.livetv"
	selfAddon	   = xbmcaddon.Addon(id=addon_id)
	user			= selfAddon.getSetting("hqusername")
	passw		   = selfAddon.getSetting("hqpassword")
	datapath		= xbmc.translatePath(selfAddon.getAddonInfo("profile"))

	# Make any missing dirs
	if not os.path.exists(datapath):
		os.makedirs(datapath)


	epg_file		= os.path.join(os.path.abspath(datapath), "guide.xmltv")
	channels_json   = os.path.join(datapath, "channels.json")
	
	cookie_file	 = os.path.join(datapath, "iptvx9.lwp")
	net			 = mknet.Net()
	BASE_URL		= "http://update.mediaplayerx9.com/x9iptv"
	#BASE_URL		= 'http://192.168.1.25'		   # For testing on local
	user = selfAddon.getSetting("hqusername")
	passw = selfAddon.getSetting("hqpassword")
	auto = selfAddon.getSetting("autologin")

	@classmethod
	def get3Settings(cls):
		cls.user	= cls.selfAddon.getSetting("hqusername")
		cls.passw   = cls.selfAddon.getSetting("hqpassword")
		cls.auto	= cls.selfAddon.getSetting("autologin")
		print ('get3Settings:user:'+cls.user)
		print ('get3Settings:passw:'+cls.passw)

