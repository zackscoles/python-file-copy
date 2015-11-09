import datetime, shutil, os, os.path, time, calendar
import db_check
global move_date

def db_initialize():

    action_date = calendar.timegm(time.gmtime())
    
    db_check.newEntry(action_date, 'Check')
    db_check.newEntry(action_date, 'Move')
    

def file_check(check_dir, save_dir, file_list):

    action_date = calendar.timegm(time.gmtime())
    modWindow = action_date - 86400

    print 'The current time is: '
    print time.ctime(action_date)

    _dir = check_dir
    _tran = save_dir

    _files = os.listdir(_dir)

    print '\nThe current files in folder ' + _dir + ' are:' 
    
    for f in _files:
        print f

    print '\nThe dates of the files are: '

    for a in _files:
        b = os.path.abspath(_dir + '/' + a)

        modified = time.ctime(os.path.getmtime(b))
        created = time.ctime(os.path.getctime(b))

        print '\n' + b + ' was:'
        print "last modified:    %s" % modified
        print "created:          %s" % created

        c = os.path.getmtime(b)

        g = os.path.getctime(b)

        if (c > modWindow) or (g > modWindow):
            print a + ' will be moved'
            '''
            shutil.move(b, _tran)
            '''
            file_list.append(a)

    print ''

    db_check.newEntry(action_date, 'Check')

    return file_list, action_date
    

def file_move(check_dir, save_dir, file_list):
    global move_date
    
    action_date = calendar.timegm(time.gmtime())
    modWindow = action_date - 86400
    

    print 'The current time is: '
    print time.ctime(action_date)

    move_date = []
    db_check.viewLastMove(move_date)
    print move_date
 
    _dir = check_dir
    _tran = save_dir

    _files = os.listdir(_dir)

    print '\nThe current files in folder ' + _dir + ' are:' 
    
    for f in _files:
        print f

    print '\nThe dates of the files are: '

    for a in _files:
        b = os.path.abspath(_dir + '/' + a)

        modified = time.ctime(os.path.getmtime(b))
        created = time.ctime(os.path.getctime(b))
        
        print '\n' + b + ' was:'
        print "last modified:    %s" % modified
        print "created:          %s" % created

        c = os.path.getmtime(b)

        g = os.path.getctime(b)

        if (c > modWindow) or (g > modWindow) or (c > move_date) or (g > move_date):
            print a + ' will be moved'

            shutil.move(b, _tran)

            file_list.append(a)

    print ''

    db_check.newEntry(action_date, 'Move')

    return file_list, action_date

if __name__ == "__main__": file_check(os.getcwd(), os.getcwd(), 'a')
