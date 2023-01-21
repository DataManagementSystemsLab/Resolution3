import common as c
import gdrive as g

from queue import SimpleQueue
txts=[]
g.files={}


folderid='0B0Rlpx3MRZ1SLVFXRFctd0t1cDA'
g.q=SimpleQueue()
g.q.put(folderid)

gauth = g.GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = g.GoogleDrive(gauth)


g.bfs(drive)

txts=c.get_content_files()
#get_contents(txts)

for s in range(0, len(txts),100):
    g.download(txts,500,100)
a_file = open("files.json", "w")
json.dump(files, a_file)
a_file.close()


 
