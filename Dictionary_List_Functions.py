#Dictionary
di = {'Raj':'Pvg','Avi':'Sinhgad','Shreemay':'Pccoe'}
print di
#Updation of Dictionary (Enter value of s in quotes)
s = input("Enter new entry for Raj:")
di['Raj'] = s
#Updated Dictionary
print di
#Lists
print "List created"
li = ['raj','avi','shree','karan']
print li
print "extend function on list"
print "new list is"
li.extend(['john','car'])
print li
#function
n = input("Enter the value of n:")
def mmm(n) :
    print 'n=', n
    if n>2 :
           print 'a'
    else :
         print'b'
mmm(n)
