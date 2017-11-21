import os.path

save_path = 'C:/Users/' + str(os.getlogin()) + '/Desktop'

name = 'Pop'
name_file = str(name) + '\'s file' + '.txt'

completeName = os.path.join(save_path, name_file)
file1 = open(completeName, "w")
file1.write('test\n')
file1.close
