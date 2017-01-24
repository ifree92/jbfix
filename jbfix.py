import os

JAYATANA_FIX = "-javaagent:/usr/share/java/jayatanaag.jar"


def get_vmoptions_files(path_name):
    vmoptfiles = []
    for d, dirs, files in os.walk(os.path.expanduser(path_name)):
        for file in files:
            fname, fext = os.path.splitext(file)
            if ".vmoptions" in fext:
                vmoptfiles.append(os.path.join(d, file))
    return vmoptfiles


def add_jayatana_option(file):
    vmoption_file = open(file, "r+")
    vmoption_file_text = vmoption_file.read()
    if (JAYATANA_FIX not in vmoption_file_text):
        vmoption_file_text += "\n" + JAYATANA_FIX
        vmoption_file.seek(0)
        vmoption_file.truncate()
        vmoption_file.write(vmoption_file_text)
        vmoption_file.close()
        print("fixed:", file)
    else:
        print("already:", file)


for file in get_vmoptions_files("~"):
    add_jayatana_option(file)
