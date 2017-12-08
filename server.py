from errbot import BotPlugin, botcmd
import subprocess, tempfile, re, time

class AutoSysServer(BotPlugin):
    """AutoSys server plugin for Errbot"""

    @botcmd
    def server_target(self, msg, args):
        """Target server for jobs"""
        target_server = ""
        with open('/var/errbot/target_server', 'w') as file:
            proc = subprocess.Popen(['echo',args], stdout=file)
            proc.wait()
            file.seek(0)
            target_server = str(target_server) + str(file.read())
        return target_server + " is now the targeted server."
    
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
