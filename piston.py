import maya.cmds as cmds

def makePiston(myLookAxis, myLookUpAxis, myCon1, myCon2):
    # myLookAxis = 'Z'
    # myLookUpAxis = 'Y'
    # myCon1 = 'FingerUpA4'
    # myCon2 = 'FingerUpB'

    myNul1 = cmds.group(n=myCon1+'_look_nul', em=True)
    cmds.matchTransform(myNul1, myCon1)

    myLocList = cmds.spaceLocator(n=myCon1+'_look_loc')
    myLoc1 = myLocList[0]
    cmds.matchTransform(myLoc1,myCon1)
    cmds.parent(myLoc1, myNul1)

    myNul2 = cmds.group(n=myCon2+'_look_nul', em=True)
    cmds.matchTransform(myNul2, myCon2)

    myLocList = cmds.spaceLocator(n=myCon2+'_look_loc')
    myLoc2 = myLocList[0]
    cmds.matchTransform(myLoc2,myCon2)
    cmds.parent(myLoc2, myNul2)

    myUpList = cmds.duplicate(myLoc1)
    myUp1 = myUpList[0]
    myUp1 = cmds.rename(myUp1, myCon1+'_look_up')
    # cmds.setAttr(myUp1+'.translate'+myLookUpAxis, 5)

    myUpList = cmds.duplicate(myLoc2)
    myUp2 = myUpList[0]
    myUp2 = cmds.rename(myUp2, myCon2+'_look_up')
    # cmds.setAttr(myUp2+'.translate'+myLookUpAxis, 5)

    cmds.aimConstraint(myLoc2, myLoc1, aim=(0,0,1), wut='object', wuo=myUp1, mo=True)
    cmds.aimConstraint(myLoc1, myLoc2, aim=(0,0,1), wut='object', wuo=myUp2, mo=True)

    myCon1Parent = cmds.listRelatives(myCon1, p=True)
    myCon2Parent = cmds.listRelatives(myCon2, p=True)

    cmds.parentConstraint(myCon1Parent, myNul1, mo=True)
    cmds.parentConstraint(myCon2Parent, myNul2, mo=True)

    cmds.orientConstraint(myLoc1, myCon1, mo=True)
    cmds.orientConstraint(myLoc2, myCon2, mo=True)

def makeLookAt_makeLookAtPos(myLookAxis, myLookUpAxis, myDriver, myDriven, myLookAtPos):
    # myLookAxis = 'Z'
    # myLookUpAxis = 'Y'
    # myDriver = 'FKHatchCoverClipLook_L'
    # myDriven = 'FKHatchCoverClipB_L'

    myNul = cmds.group(n=myDriven+'_look_nul', em=True)
    cmds.matchTransform(myNul, myLookAtPos)

    myLocList = cmds.spaceLocator(n=myDriven+'_look_loc')
    myLoc = myLocList[0]
    cmds.matchTransform(myLoc,myLookAtPos)
    cmds.parent(myLoc, myNul)

    myUpList = cmds.duplicate(myLoc)
    myUp = myUpList[0]
    myUp = cmds.rename(myUp, myDriven+'_look_up')

    cmds.aimConstraint(myLoc, myDriven, aim=(0,0,1), wut='object', wuo=myUp, mo=True)

    cmds.parentConstraint(myDriver, myNul, mo=True)

# makePiston('Z', 'Y', 'FKFingerUpA4_R', 'FKFingerUpB_R')
