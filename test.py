from log.log_yaml import *
# log.info("aaaaaaaaaaa")
# log.debug("debug debug .....")

# execute command, and return the output
def execCmd(cmd):
    r = os.system(cmd)
    return r

if __name__ == '__main__':
    git_path=r'C:\Users\Administrator\Desktop\Tube_Recognize_Software'
    os.chdir(r'C:\Users\Administrator\Desktop\Tube_Recognize_Software')
    # ======================================================
    # cmd ="git log --stat   "
    # result = execCmd(cmd)
    # # print (result)
    # # print(type(result))
    # ======================================================
    import git
    from git import Repo
    repo = git.Repo(git_path)
    r=repo.git.log('--stat') # git commit -m 'this is a test'
    print(r)
    print(type(r))