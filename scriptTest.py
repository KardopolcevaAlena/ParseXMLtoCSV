import lxml.etree as LE

NSMAP = {'ns3': 'http://lcs.lbs.maps.nokia.com/1.0/places',
         'ns2': 'http://lbs.maps.nokia.com/1.0/common',
         'n': 'http://lcs.lbs.maps.nokia.com/1.0/common'}
tree = LE.parse('sample.xml')

def counterOfUnicWords(word, myDic): # Tested function, that  returns dictionary
                                    # of tag values and counts
    if word in myDic:
        myDic[word] += 1
    else:
        myDic[word] = 1
    return myDic

def countValueOfTag(t, w): # Calculate count of value 'w' in tag 't'
    b = tree.findall(t, namespaces=NSMAP)
    diction = []
    for n in b:
        diction.append(n.text)
    return diction.count(w)

def testCounterOfUnicWords(tag, word): # Test function, that uses tested function 
                                    # and return count of value 'word' in tag 'tag'
 	strname = tree.findall(tag, namespaces=NSMAP)
 	d= {}
 	for k in strname:
 		d2 = counterOfUnicWords(k.text, d)
 	return d2[word]

def getListValues(tag): # Function returns list of values for the set tag 't'
    strname = tree.findall(tag, namespaces=NSMAP)
    lis = []
    i = 0
    for n in strname:
        a = n.text in lis
        if a == False:
            lis.append(n.text)
            i += 1
    return lis        

t = '//n:Category/n:CategoryId'

#Testing:
lis = getListValues(t)
i=0
while i < len(lis)-1:
    if testCounterOfUnicWords(t, lis[i]) == countValueOfTag(t, lis[i]): 
        print 'Test %s Passed' %(i+1)
    else: 
        print 'Test %s Failed' %(i+1)
        print 'Failed object is: %s' %(lis[i])
    i += 1  