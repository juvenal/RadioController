#
#
#
#

class APInfo(object):
	"""..."""
	
	# Protected members
	__IPAddress = ""
	__MACAddress = ""
	__Channel = 0
	__Region = 0
	__Localization = ""
	__TxPowerList = []
	__CurrentPowerIndex = -1
	__UnderloadLimit = -1
	__OverloadLimit = -1
	__Reachable = False
	__Enabled = False
	__EMailSent = False
	__SupportedOS = ""

	# Public members mirrors

	# Class initialization
	def __init__(self):
		# Run super class initialization
		super(APInfo, self).__init__()

	# Set the AP transmission power (Tx)
	def updateTxPowerIndex(self, newTxPower):
		#
		if newTxPower < 0:
			self.CurrentPowerIndex = len(self.TxPowerList) - 1
		else:
			for powerTxIndex in self.TxPowerList:
				if newTxPower > self.TxPowerList[powerTxIndex]:
					break
			self.CurrentPowerIndex = powerTxIndex


# Heroku: User: juvenal-jr@ig.com.br / Senha: w4cpvX3DWw

# wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
