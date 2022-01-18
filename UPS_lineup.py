import os


trami = ('TRAMI')
cicmi = ('CICMI')
oakwi = ('OAKWI')
casmi = ('CASMI')
lchky = ('LCHKY')
burmd = ('BURMD')
wnton = ('WNTON')


print ('This tool will create a lineup for you\n')
input("Pres ENTER to continue...")


#(CHOOSE BELT)

print('################   PD-2  ##################')



def init():
    global defaultLineup
    global initLineup


    defaultLineup = ['wnton', 'lchky', 'cicmi', 'cicmi', 'oakwi', 'burmd', 'casmi', 'trami', 'trami', 'trami']

    

print('Enter which trailers are up on which doors\nIf there is no trailer currently up, press ENTER to skip that door')


init113 = input ('[113]:')

init114 = input ('[114]:')

init115 = input ('[115]:')

init116 = input ('[116]:')

init117 = input ('[117]:')

init118 = input ('[118]:')

init119 = input ('[119]:')

init120 = input ('[120]:')

init121 = input ('[121]:')

init122 = input ('[122]:')

print('Initial lineup is:\n [113]: '+init113 + '\n [114]: '+init114 + '\n [115]: '+init115 + '\n [116]: '+init116 + '\n [117]: '+init117 + '\n [118]: '+init118 + '\n [119]: '+init119 + '\n [120]: '+init120 + '\n [121]: '+init121 + '\n [122]: '+init122)


initcorrect = input ('Is this correct? [y/n]')
if initcorrect == 'y':
    print('************')
    initLineup = [init113, init114, init115, init116, init117, init118, init119, init120, init121, init122]
    #print (initLineup)
    

if initcorrect == 'n':
    init()




    

init()

print ("Default lineup is: ")
print (defaultLineup)
print ("Inital lineup is: ")
print (initLineup)


#COPY INITLINEUP TO DEFAULTLINEUP
for x in range(0,9):

    if initLineup[x] == defaultLineup[x]:
        pass
        
    else:
        defaultLineup.pop(x)
        defaultLineup.insert(x, initLineup[x])

 
lineup = defaultLineup
print ("Lineup is NOW: ")
print (lineup)





