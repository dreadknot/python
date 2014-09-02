from fabric.api import *
from fabric.contrib.console import confirm


#env.hosts = ['localhost']
#env.host = "localhost"
#env.password = "vagrant"
#env.port = 2212
#env.user = "vagrant"
#env.host_string = "vagrant@127.0.0.1:2212"
#env.no_keys = ['True']

def hello(name="world"):
    print("Hello %s!" % name)
    local("ls -lsa")

def test():
    with settings(warn_only=True):
        result = local('ls-lsa', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def deploy():
    code_dir = '/srv/django/myproject'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")

def list_license():
    run("sudo /opt/splunk/bin/splunk list license")

def apply_splunk_license(license, host_string='127.0.0.1', splunk_dir="/opt/splunk"):
    """Apply a splunk license to a remote host"""

    if license is None:
	   license = prompt('What license to apply?: ')

    with cd(splunk_dir):
 		license_location = put(license)
 		for s in license_location:
 			run("sudo %s/bin/splunk add license %s" % (splunk_dir, s))
