import common as c
import gdrive as g
import json
from queue import SimpleQueue
txts=[]



folderid='0B0Rlpx3MRZ1SLVFXRFctd0t1cDA'
download=False

gauth = g.GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = g.GoogleDrive(gauth)

c.failed=[]
files=g.bfs(drive,folderid)

txts=c.get_content_files(files)


if download:

    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    for s in range(0, len(txts),100):
        g.download(files,txts,s,100)
    f_file = open("failed.json", "w")
    json.dump(c.failed, f_file)
    f_file.close()
    if not os.path.exists("files"):
        os.makedirs("files")
    c.flatten_dir("tmp","files") 
    

a_file = open("files.json", "w")
json.dump(files, a_file)
a_file.close()




