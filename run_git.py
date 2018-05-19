from log.log_yaml import *
# log.info("aaaaaaaaaaa")
# log.debug("debug debug .....")

def execCmd(cmd):
    r = os.system(cmd)
    return r

if __name__ == '__main__':
    os.chdir(r'C:\Users\Administrator\Desktop\Tube_Recognize_Software')
    cmd ="git log --stat   "
    result = execCmd(cmd)
