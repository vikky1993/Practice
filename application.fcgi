#!/home/mitibhat/djang/bin/python

# Set up the virtual environment:
import os, sys
os.environ.setdefault('PATH', '/bin:/usr/bin')
os.environ['PATH'] = '/home/mitibhat/djang/bin:' + os.environ['PATH']
os.environ['VIRTUAL_ENV'] = '/home/mitibhat/djang/bin'
os.environ['PYTHON_EGG_CACHE'] = '/home/mitibhat/djang/bin'
os.chdir('/home/mitibhat/navaneethaedu.com/mysite')

# Add a custom Python path.
sys.path.insert(0, "/home/mitibhat/navaneethaedu.com/mysite")

# Set the DJANGO_SETTINGS_MODULE environment variable to the file in the
# application directory with the db settings etc.
os.environ['DJANGO_SETTINGS_MODULE'] = "mysite.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
