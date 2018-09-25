
import urllib
from bs4 import BeautifulSoup
import pandas as pd

def nameMatching(testName, dbName, threshold=0.7):
    testName = testName.lower()
    dbName = dbName.strip().lower()
    testList = testName.split(' ')
    dbNameList = dbName.split(' ')
    count = 0
    for name in testList:
        if name in dbNameList:
            count+= 1
    count = count/len(testList)
    if count > threshold:
        return True
    return False

def getPepResults(name, folder):
    country_list = ["AF.html","AL.html","AG.html","AN.html","AO.html","AC.html","AR.html","AM.html","AA.html","AS.html","AU.html","AJ.html","BF.html","BA.html","BG.html","BB.html","BO.html","BE.html","BH.html","BN.html","BD.html","BT.html","BL.html","BK.html","BC.html","BR.html","BX.html","BU.html","UV.html","BM.html","BY.html","CV.html","CB.html","CM.html","CA.html","CT.html","CD.html","CI.html","CH.html","CO.html","CN.html","CG.html","CF.html","CW.html","CS.html","IV.html","HR.html","CU.html","CY.html","EZ.html","DA.html","DJ.html","DO.html","DR.html","EC.html","EG.html","ES.html","EK.html","ER.html","EN.html","WZ.html","ET.html","FJ.html","FI.html","FR.html","GB.html","GA.html","GG.html","GM.html","GH.html","GR.html","GJ.html","GT.html","GV.html","PU.html","GY.html","HA.html","VT.html","HO.html","HU.html","IC.html","IN.html","ID.html","IR.html","IZ.html","EI.html","IS.html","IT.html","JM.html","JA.html","JO.html","KZ.html","KE.html","KR.html","KN.html","KS.html","KV.html","KU.html","KG.html","LA.html","LG.html","LE.html","LT.html","LI.html","LY.html","LS.html","LH.html","LU.html","MK.html","MA.html","MI.html","MY.html","MV.html","ML.html","MT.html","RM.html","MR.html","MP.html","MX.html","FM.html","MD.html","MN.html","MG.html","MJ.html","MO.html","MZ.html","WA.html","NR.html","NP.html","NL.html","NZ.html","NU.html","NG.html","NI.html","NO.html","MU.html","PK.html","PS.html","PM.html","PP.html","PA.html","PE.html","RP.html","PL.html","PO.html","QA.html","RO.html","RS.html","RW.html","SC.html","ST.html","VC.html","WS.html","SM.html","TP.html","SA.html","SG.html","RI.html","SE.html","SL.html","SN.html","LO.html","SI.html","BP.html","SO.html","SF.html","OD.html","SP.html","CE.html","SU.html","NS.html","SW.html","SZ.html","SY.html","TW.html","TI.html","TZ.html","TH.html","TT.html","TO.html","TN.html","TD.html","TS.html","TU.html","TX.html","TV.html","UG.html","UP.html","AE.html","UK.html","UY.html","UZ.html","NH.html","VE.html","VM.html","YM.html","ZA.html","ZI.html"]
    names = []
    websites = []
    fileName = folder + '/' + name.replace(' ', '_') + '_PEPResults.csv'
    for country in country_list:

        sites= "https://www.cia.gov/library/publications/world-leaders-1/"+country
        page = urllib.request.urlopen(sites)
        soup = BeautifulSoup(page, 'html.parser')

        item_list = soup.findAll('span', attrs={'class':'cos_name'})

        for item in item_list:
            text = item.text
            if nameMatching(name, text):
                print(name + ' is a PEP' + " " + sites)
                websites.append(sites)
                names.append(text.strip())
    if len(names) == 0:
        print(name + ' NOT FOUND as a PEP')
    else:
        df = pd.DataFrame({'Names':names, 'Websites':websites})
        df.to_csv(fileName, header=True, index=False)


