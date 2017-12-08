from errbot import BotPlugin, botcmd
import subprocess, tempfile, re, time

class AutoSysServer(BotPlugin):
    """AutoSys server plugin for Errbot"""
    target_server = ""

    @botcmd
    def server_target(self, msg, args):
        """Target server for jobs"""
        self.target_server = args
        return args + " is now the targeted server."
    
    @botcmd
    def server_active(self, msg, args):
        """Start requested job"""
        return self.target_server + " is now the targeted server."
    
# Used to run commands in terminal and capture the result in string var.
#with tempfile.TemporaryFile() as tempf:
#    proc = subprocess.Popen(['ls','-l'], stdout=tempf)
#    proc.wait()
#    tempf.seek(0)
#    string = str(string) + str(tempf.read())
