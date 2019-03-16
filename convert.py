# -*- coding: utf-8 -*-
import os
import sys
import webpage2html

reload(sys)
sys.setdefaultencoding( "utf-8" )

def convert_path_to_utf8(path):
    return unicode(path, 'utf-8')

for root, dirs, files in os.walk("geektime", topdown=False):
    print "processing " + root.decode('gbk').encode('utf-8')
    print "================================================="
    for name in files:
        print "converting " + os.path.join(root, name).decode('gbk').encode('utf-8')
        webpage2html.local_use(convert_path_to_utf8(os.path.join(root, name).decode('gbk').encode('utf-8'))
                               ,convert_path_to_utf8(os.path.join(root, name).decode('gbk').encode('utf-8')))



