print("Starting the HyperSH REPL.")
import sys
import os

ver = "1.0.0"

def set_title(title):
    sys.stdout.write(f"\x1b]2;{title}\x07")
    sys.stdout.flush()

set_title(f"HyperSH {ver}")

runninghypersh = True
directory = "~"

def cmd_say(args):
    print(" ".join(args))

hypershcmds = {
    "say": cmd_say
}


while runninghypersh:
    hypershgetinput = input(f"hypersh>{directory}> ").strip().split()

    command = hypershgetinput[0].lower()
    args = hypershgetinput[1:]
    
    if command in hypershcmds:
        hypershcmds[command](args)
    else:
        print(f"Unknown command: {command}")


    
