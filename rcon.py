from mcrcon import MCRcon
gmodes = {
    0: "survival",
    1: "creative",
    2: "adventure"
}

class RCon():
    def __init__(self, host, port, passw):
        self.host = host
        self.port = port
        self.passw = passw

    def op_player(self, pname):
        self.__exec_cmd("/say Opping '%s' via MyForge" % pname)
        self.__exec_cmd("/op %s" % pname)
    def deop_player(self,pname):
        self.__exec_cmd("/say De-Oping '%s' via MyForge" % pname)
        self.__exec_cmd("/deop %s" % pname)

    def set_gamemode_for_player(self,pname, mode):
        self.__exec_cmd("/say Setting gamemode to '%s' for player: %s via MyForge" % (gmodes[mode], pname))
        self.__exec_cmd("/gamemode %s %s" % (mode, pname))
    
    def trigger_save(self):
        self.__exec_cmd("/say MyForge triggered a world save")
        self.__exec_cmd("/save-all flush")

    
    def say(self, what):
        self.__exec_cmd("/say %s", what)
        self.__exec_cmd("/save-all flush")



    def __exec_cmd(self, cmd):
        with MCRcon(self.host, self.passw, port=self.port) as mcr:
            mcr.command(cmd)