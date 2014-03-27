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


t = '//n:Category/n:CategoryId'
w = '600-6900-0000'

#Testing:
if testCounterOfUnicWords(t, w) == countValueOfTag(t, w): 
    print 'Test Passed'
else: 
    print 'Test Failed' 