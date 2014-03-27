import lxml.etree as LE

NSMAP = {'ns3': 'http://lcs.lbs.maps.nokia.com/1.0/places',
         'ns2': 'http://lbs.maps.nokia.com/1.0/common',
         'n': 'http://lcs.lbs.maps.nokia.com/1.0/common'}
tree = LE.parse('sample.xml')

def counterOfUnicWords(word, myDic):
    if word in myDic:
        myDic[word] += 1
    else:
        myDic[word] = 1
    return myDic

col = 0 # Counter all converted tags

fstrT = open('csv\StreetType.csv','w+')
fstrN = open('csv\StreetName.csv','w+')
fstrT.write("id; attached; before;")
fstrN.write("id; BaseName; Prefix; Suffix; StreetType; Id-StreetType;")
strname = tree.findall('//n:StreetName', namespaces=NSMAP)
i = 0
d={}
for k in strname:
    i+=1
    fstrN.write("\n%s; " %(i))
    d2={}
    for n in k:
        if n.tag == "{http://lcs.lbs.maps.nokia.com/1.0/common}StreetType":
            fstrT.write("\n%s; %s; %s; " %(i, n.get('attached'), n.get('before')))
            col += 1  
        d={'%s' %(n.tag) : '%s' %(n.text)}
        d2.update(d)
        col += 1
    fstrN.write("%s; %s; %s; " %(d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}BaseName'),
                               d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}Prefix'),
                               d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}Suffix'),
                              ))
    if d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}StreetType') != None:
        fstrN.write("%s; %s;" %(d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}StreetType'),
                                i))
        col += 1
    else:
        fstrN.write("%s; None;" %(d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}StreetType')))
fstrT.close()
fstrN.close()

fadm = open('csv\Admin.csv','w+')
fadm.write("id; Level2; Level3; Level4; Level5; Order ; Order2; Order5; Builtup;")
strname = tree.xpath('//n:Admin', namespaces=NSMAP)
i = 0
for k in strname:
    entry = strname[i]
    i += 1    
    fadm.write("\n%s; " %(i))
    if entry.xpath('./n:AdminLevel/n:Level2/text()', namespaces=NSMAP)!= []:
           z = entry.xpath('./n:AdminLevel/n:Level2/text()', namespaces=NSMAP)
           fadm.write("%s; " %(z[0]))
           col += 1
    else:
           fadm.write("None; ")
    if entry.xpath('./n:AdminLevel/n:Level3/text()', namespaces=NSMAP) != []:
            z = entry.xpath('./n:AdminLevel/n:Level3/text()', namespaces=NSMAP)
            fadm.write("%s; " %(z[0]))
            col += 1
    else:
            fadm.write("None; ")
    if entry.xpath('./n:AdminLevel/n:Level4/text()', namespaces=NSMAP) != []:
            z = entry.xpath('./n:AdminLevel/n:Level4/text()', namespaces=NSMAP)
            fadm.write("%s; " %(z[0]))
            col += 1
    else:
            fadm.write("None; ")
            
    if entry.xpath('./n:AdminLevel/n:Level5/text()', namespaces=NSMAP)!= []:
            z = entry.xpath('./n:AdminLevel/n:Level5/text()', namespaces=NSMAP)
            fadm.write("%s; " %(z[0]))
            col += 1
    else:
            fadm.write("None; ")
    if entry.xpath('./n:OrderLevel/n:Order1/text()', namespaces=NSMAP) != []:
            z = entry.xpath('./n:OrderLevel/n:Order1/text()', namespaces=NSMAP)
            fadm.write("%s; " %(z[0]))
            col += 1
    else:
            fadm.write("None; ")
    if entry.xpath('./n:OrderLevel/n:Order2/text()', namespaces=NSMAP) != []:
            z = entry.xpath('./n:OrderLevel/n:Order2/text()', namespaces=NSMAP)
            fadm.write("%s; " %(z[0]))
            col += 1
    else:
            fadm.write("None; ")
    if entry.xpath('./n:OrderLevel/n:Order8/text()', namespaces=NSMAP) != []:
            z = entry.xpath('./n:OrderLevel/n:Order8/text()', namespaces=NSMAP)
            fadm.write("%s; " %(z[0]))
            col += 1
    else:
            fadm.write("None; ")
    if entry.xpath('./n:OrderLevel/n:Builtup/text()', namespaces=NSMAP) != []:
            z = entry.xpath('./n:OrderLevel/n:Builtup/text()', namespaces=NSMAP)
            fadm.write("%s; " %(z[0]))
            col += 1
    else:
            fadm.write("None; ")
fadm.close()

fadr = open('csv\Address.csv','w+')
fadr.write("id; languageCode; defaultLanguage; id-StreetName; HouseNumber; CountryCode; PostalCode; id-Admin;")
strname = tree.findall('//n:Parsed', namespaces=NSMAP)
i = 1
d={}
for k in strname:
    
    fadr.write("\n%s; %s; %s; %s; " %(i, k.get('languageCode'), k.get('defaultLanguage'), i))   
    col += 2
    d2={}
    for n in k:
        d={'%s' %(n.tag) : '%s' %(n.text)}
        d2.update(d)
    fadr.write("%s; %s; %s; " %(d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}HouseNumber'),
                               d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}CountryCode'),
                               d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}PostalCode'),
                              ))
    if d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}HouseNumber') != None:
        col += 1
        
    if d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}CountryCode') != None:
        col += 1
   
    if d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}PostalCode') != None:
        col += 1
    
    fadr.write(" %s;" %(i))
    i+=1
fadr.close()

fgeop = open('csv\GeoPosition.csv','w+')
fgeop.write("id; type; Latitude; Longitude; Altitude;")
strname = tree.findall('//n:GeoPosition', namespaces=NSMAP)
i = 1
d={}
for k in strname:
    fgeop.write("\n%s; %s; " %(i, k.get('type')))
    col += 1   
    d2={}
    for n in k:
        d={'%s' %(n.tag) : '%s' %(n.text)}
        d2.update(d)
    fgeop.write("%s; %s; %s; " %(d2.get('{http://lbs.maps.nokia.com/1.0/common}Latitude'),
                               d2.get('{http://lbs.maps.nokia.com/1.0/common}Longitude'),
                               d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}Altitude'),
                              ))
    if d2.get('{http://lbs.maps.nokia.com/1.0/common}Latitude') != None:
        col += 1
        
    if d2.get('{http://lbs.maps.nokia.com/1.0/common}Longitude') != None:
        col += 1
   
    if d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}Altitude') != None:
        col += 1

    i+=1
fgeop.close()

fiden = open('csv\Identity.csv','w+')
fiden.write("id; lastUpdatedTimeStamp; isDeleted; PlaceId; QualityLevel")
strname = tree.findall('//ns3:Identity', namespaces=NSMAP)
i = 1
d={}
for k in strname:
    fiden.write("\n%s; %s; %s; " %(i, k.get('lastUpdatedTimeStamp'), k.get('isDeleted')))
    col += 2   
    d2={}
    for n in k:
        d={'%s' %(n.tag) : '%s' %(n.text)}
        d2.update(d)
    fiden.write("%s; %s;" %(d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}PlaceId'),
                            d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}QualityLevel'),
                                ))
    if d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}PlaceId') != None:
        col += 1
   
    if d2.get('{http://lcs.lbs.maps.nokia.com/1.0/common}QualityLevel') != None:
        col += 1
    i+=1
fiden.close()

ftnaml = open('csv\Text-NameList.csv','w+')
ftnaml.write("id; type; languageCode; default; Text")
strname = tree.findall('//n:TextList/n:Text', namespaces=NSMAP)
i = 1
a = {}
for k in strname:
    for n in k:
        ftnaml.write("\n%s; %s; %s; %s; %s;" %(i, n.get('type'), n.get('languageCode'), n.get('default'), n.text))   
        a = counterOfUnicWords(n.get('languageCode'), a)
        if n.get('type') != None: col += 1
        if n.get('languageCode') != None: col += 1
        if n.get('default') != None: col += 1
        if n.text != None: col += 1
    i+=1

ftnaml.close()

fnam = open('csv\Name.csv','w+')
fnam.write("id; primaryFlag; categoryReference; id-Namelist")
strname = tree.findall('//n:NameList/n:Name', namespaces=NSMAP)
i = 1
for k in strname:
    fnam.write("\n%s; %s; %s; %s; " %(i, k.get('primaryFlag'), k.get('categoryReference'), i))
    if k.get('primaryFlag') != None: col += 1
    if k.get('categoryReference') != None: col += 1
    i+=1
fnam.close()

fcat = open('csv\Category.csv','w+')
fcat.write("id; categorySystem; primaryFlag; CategoryId; id-TextCategoryName;")
strname = tree.findall('//n:CategoryList/n:Category', namespaces=NSMAP)
i = 0
l = 1
b = {}
for k in strname:
    i+=1
    fcat.write("\n%s; %s; %s; " %(i, k.get('categorySystem'), k.get('primaryFlag')))
    if k.get('categorySystem') != None: col += 1
    if k.get('primaryFlag') != None: col += 1
    for n in k:
        if n.tag == '{http://lcs.lbs.maps.nokia.com/1.0/common}CategoryId':
            fcat.write("%s; " %(n.text))
            b = counterOfUnicWords(n.text, b)
            if n.text != None: col += 1
        if n.tag == '{http://lcs.lbs.maps.nokia.com/1.0/common}CategoryName':
            fcat.write(" %s;" %(l))
            l += 1
        
fcat.close()            

ftcatn = open('csv\Text-CategoryName.csv','w+')
ftcatn.write("id; languageCode; type; default; Text")
strname = tree.findall('//n:Category/n:CategoryName', namespaces=NSMAP)
i = 1
for k in strname:
    ftcatn.write("\n%s; " %(i))
    for n in k:
        ftcatn.write("%s; %s; %s; %s;" %(n.get('languageCode'), n.get('type'),
                                         n.get('default'), n.text))
        if n.get('languageCode') != None: col += 1
        if n.get('type') != None: col += 1
        if n.get('default') != None: col += 1
        if n.text != None: col += 1
    i+=1        
ftcatn.close()

strname = tree.findall('//n:Contact/n:AdditionalContactInfo', namespaces=NSMAP)
i=0
d=[]
for k in strname:
    for n in k:
        str2 = strname[i].find('{http://lcs.lbs.maps.nokia.com/1.0/common}StandardNumber')
        d.append(str2.text)
        i += 1


fcont = open('csv\Contact.csv','w+')
fcont.write("id; type; preferred; categoryReference; ContactString; AdditionalContactInfo")
strname = tree.findall('//n:Contact', namespaces=NSMAP)
i=1
l=0
for k in strname:
    fcont.write("\n%s; %s; %s; %s; " %(i, k.get('type'), k.get('preferred'), k.get('categoryReference')))
    if k.get('type') != None: col += 1
    if k.get('preferred') != None: col += 1
    if k.get('categoryReference') != None: col += 1
    for n in k:
        if n.tag == '{http://lcs.lbs.maps.nokia.com/1.0/common}ContactString': 
            fcont.write("%s; " %(n.text))
            if n.text != None: col += 1
        if n.tag == '{http://lcs.lbs.maps.nokia.com/1.0/common}AdditionalContactInfo': 
            fcont.write("%s;" %(d[l]))
            if d[l] != None: col += 1
            l+=1
    i+=1
fcont.close()              

fstat = open('csv\Stat.csv','w+')
fstat.write("Item; Value : RecordsCount;")
fstat.write("\nstat1; AllConvertedTags : %s" %(col))
for key,val in b.items():
    fstat.write("\nstat2; %s : %s;" %(key, val))
for key,val in a.items():
    fstat.write("\nstat3; %s:%s; " %(key, val))
fstat.close()