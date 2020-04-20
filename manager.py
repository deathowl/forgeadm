import glob
import os


class Manager:
    def __init__(self, forgedir):
        self.forgedir = forgedir

    def get_installed_mods(self):
        result = {}
        for mod in glob.glob("%s/mods/*.jar" % self.forgedir):
            raw = mod.split("/")[-1].rstrip(".jar")
            try:
                modname = raw.split("-")[0]
                modv = "-".join(raw.split("-")[1:])
            except:
                modname = raw
                modv = "Unknown"
            result[modname] = modv
        return result

    def read_server_properties(self):
        with open("%s/server.properties") as sp:
            return sp.read()

    def remove_mod(self, modname):
        for f in glob.glob("%s/mods/%s*.jar" % (self.forgedir, modname)):
            os.remove(f)

    def overwrite_server_properties(self, new_contents):
        with open("%s/server.properties", "w") as sp:
            sp.truncate()
            sp.write(new_contents)
