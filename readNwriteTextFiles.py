import os

ls = os.linesep    # why?

choice = raw_input("enter \'c\' for create OR \'r\' for read")
# get filename
while True:
    if not choice == 'c' and choice != 'r':
        choice = raw_input("enter \'c\' for create OR \'r\' for read")
    else:
        break
    
    
# for create
if choice == 'c':

    while True: 
        fname = raw_input("enter name: ")
        try: 
            fobj = open(fname, 'w')
        
        except IOError ,e:
              continue
        else:
              break
# get file content (text) lines
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)

# write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()

    print 'DONE FILE CREATED'
    #end create
# for read
elif choice == 'r':

    fname = raw_input('Enter filename: ')


    # attempt to open file for reading
    try: 
        fobj = open(fname, 'r')
    
        if os.path.exists(fname):  
   
            for eachLine in fobj:
                print eachLine.strip('.')
        
            fobj.close()
    except IOError, e:
         print "*** file open error: " ,e
                    #end read
                    # display contents to the screen
                    #  fobj = open(fname, 'r')

