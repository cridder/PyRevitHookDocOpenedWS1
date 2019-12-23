
"""
SET WORKSET1 CURRENT ON DOC OPEN
https://github.com/cridder/PyRevitHookDocOpenedWS1

Place this file in the Hooks folder under your PyRevit extension.
Workset1 is set current, if it exists, on open of a .rvt file

Thanks Ehsan Iran-Nejad !

https://www.patreon.com/pyrevit
https://www.notion.so/Support-on-Patreon-cdf92ba547154f7a85d32b526dc5e59b

https://ein.sh/
https://eirannejad.github.io/pyRevit/
https://www.notion.so/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0
https://www.notion.so/Create-Your-First-Command-2509b43e28bd498fba937f5c1be7f485
https://www.notion.so/Create-Your-First-Hook-0214eee855fc43cead1e6f30f586a04e
https://github.com/eirannejad/pyRevit

tested on latest versions or Revit 2016, 2017, 2018, 2019, 2020 with pyRevit v4.7.4 as of 2020-12-23

"""

from Autodesk.Revit.DB import FilteredWorksetCollector, WorksetKind
from pyrevit import revit, DB, UI
from pyrevit import script
from pyrevit import forms
from pyrevit import EXEC_PARAMS

# document instance
doc = __eventargs__.Document

# if workshared do this stuff
if doc.IsWorkshared:

	# get a workset list object
	worksetList = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset).ToWorksets()

	# set var to Workset1
	worksetOneSTR = "Workset1"

	# create a empty list for worksets
	listOfWorksets = []

	# loop to create a list of workset names
	for ws in worksetList:
		#append workset name to list
		listOfWorksets.append(ws.Name)
		# if workset1 exists get workset1 id
		if ws.Name == "Workset1":
			worksetOneId = ws.Id

	# get worksettable
	worksetTable = doc.GetWorksetTable()
	# get active workset id
	activeWsId = worksetTable.GetActiveWorksetId()
	# get active workset object
	activeWsOBJ = worksetTable.GetWorkset(activeWsId)
	# get active workset name
	nameActiveWsName = activeWsOBJ.Name
	
	#if active workset name is workset1
	if nameActiveWsName == worksetOneSTR:
		# then quit
		#quit()  # changed to false for 2016 
		False
	# does workset1 exist in list
	elif worksetOneSTR in listOfWorksets:
		# if workset1 exists set current
		DB.WorksetTable.SetActiveWorksetId(worksetTable, worksetOneId)
	# display a message because workset1 was renamed
	else:
		forms.alert(" Workset1 was renamed !")

# else
else:
	False
