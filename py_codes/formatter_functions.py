def FARcalctor(totarea, bldarea, resarea):
  try:
    if (bldarea >= resarea):
        FAR = bldarea/totarea
    elif (resarea > bldarea):
        FAR = resarea/totarea
    else:
        FAR = -.9999
    return FAR
  except:
    print "Something went wrong inside the FARcalculator function but passed!"
    pass
def fixImperv(imperv, bldrooftop):
  if (imperv == None or imperv == 0) and bldrooftop > 0:
    return bldrooftop
  else:
    return imperv
def sqmPavedCalctor(imperarea, bldrooftop):
  if (bldrooftop == None) or (imperarea == None):
    propPavd = 0
  elif bldrooftop ==None:
    propPavd = imperarea
  else:
    propPavd = (imperarea - bldrooftop)
  return float(propPavd)
def PropImprvCalctor(imperarea, totarea):
  if imperarea == None:
      propimp = 0
  else:
      propimp = 100*imperarea/(totarea*0.092903)
  return float(propimp)
def PropBldRFTpCalctor(bldrftparea, totarea):
  if bldrftparea == None:
      propbldrftp = 0
  else:
      propbldrftp = 100*float(bldrftparea)/float((totarea*0.092903))
  return float(propbldrftp)
def PropPavdCalctor(imperarea, bldrftparea, totarea):
  if bldrftparea ==None or imperarea == None:
      propPavd = 0
  elif bldrftparea ==None:
      propPavd = 100*imperarea/(totarea*0.092903)
  else:
      propPavd = 100*(imperarea - bldrftparea)/(totarea*0.092903)
  return float(propPavd)
def LU_UnitsCalctor(lucadjust, unitnum, locidcnt):
  if unitnum == None:
      units = 0
  else:
      units = int(max(unitnum, locidcnt))
  if lucadjust == "101" and units < 1:
      unitsadjust = 1
  elif lucadjust == "104" and units < 2:
      unitsadjust = 2
  elif lucadjust =="105" and units < 3:
      unitsadjust = 3
  elif lucadjust =="109" and units < 2:
      unitsadjust = 2
  elif lucadjust == "111" and units < 4:
      unitsadjust = 6
  elif lucadjust == "112" and units < 9:
      unitsadjust = 9
  elif lucadjust == "113" and units < 31:
      unitsadjust = 31
  elif lucadjust == "114" and units < 100:
      unitsadjust = 100
  else:
      unitsadjust = units
  return int(unitsadjust)
def Units_SourceFindr(unitsadjust, unitsnum, locidcnt):
  if unitsadjust == unitsnum:
      return "units_nu"
  elif unitsadjust == locidcnt:
      return "loc_idcn"
  elif unitsnum == locidcnt:
      return "units_nu"
  else:
      return "luc_adju"
def muni_idCalctor(parmuniid, assessmuniid, muniDic):
  if assessmuniid > 0:
      muniid = assessmuniid
  else:
      muniid = parmuniid
  return muniid
def MuniLookup(townid, muniDic):
  townName = muniDic[townid]
  return str(townName)
def autoIncrement(inrec):
  if inrec != 0:
    rec = inrec
  else:
    rec = 0
  global rec
  pStart = 1 #adjust start value, if req'd 
  pInterval = 1 #adjust interval value, if req'd
  if (rec == 0): 
      rec = pStart 
  else:
      rec = rec + pInterval 
  return rec
def fixluc(townid, luc):
  if luc == None:
    luc = 0
  townidss = str(townid)
  townids = "'"+ str(townid) +"'"
  lucs = "'" + str(luc) + "'"
  try:
    lucadj = ludict[(townidss, luc)]
    return lucadj
  except:
    if len(str(luc)) ==2:
      return "0"+str(luc)
    elif len(str(luc)) ==3:
      return str(luc)
    elif (len(str(luc)) ==1) and (str(luc)[0]=="0"):
      return str(luc)[1:4]
    else:
      return str(luc)[0:3]
def calcLandValPerAcre(landval, lotareaft):
  if (landval == 0 or landval == None):
    valperacre = 0
  else:
    valperacre = landval / (lotareaft / 43560)
  return valperacre
def calcBldgValPerSqft(bldgval, far, totalareasqft):
  if (bldgval == 0 or bldgval == None) and (far > 0):
    valpersqft = 0
  elif (bldgval > 0) and (far > 0 ):
    valpersqft = bldgval / (far * totalareasqft)
  else:
    valpersqft = -0.9999
  return valpersqft
def calcILratio(bldval, otherval,landval):
  if (landval == None) or (landval == -0.9999) or (landval == 0):
    ilratio = -0.9999
  elif (bldval == None) and (otherval > 0):
    ilratio = otherval/landval
  elif (otherval == None) and (bldval > 0):
    ilratio = bldval/landval
  else:
    ilratio = (bldval + otherval)/landval
  return float(ilratio)
def stringNullChecker(value):
  if value == None:
    return ""
  else:
    return value
def numNullChecker(value):
  if value == None:
    return -0.9999
  else:
    return value
