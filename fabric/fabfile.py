from fabric.api import local
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm


def hello(name="world"):
    print("Hello %s!" % name)
    local("ls -lsa")

def test():
    with settings(warn_only=True):
        result = local('ls-lsa', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")