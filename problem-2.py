import subprocess

def main():

    command = 'egrep'
    regex = '([a-z])\\1[a-z]*([a-z])\\2'
    f = '/usr/share/dict/words'
    #f = 'problem-2.txt'
    cmd_list = [command, regex, f]
    #print(cmd_list)
    subprocess.call(cmd_list)

main()
