from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from queue import SimpleQueue
import common as c
import os


def getList(drive, folderid):
	#folderid='0B0Rlpx3MRZ1SLVFXRFctd0t1cDA'
	value="'%s' in parents and trashed=false" % (folderid )
	obj={'q':value}
	fileList = drive.ListFile(obj).GetList()
	return fileList






def bfs(drive, root):
	q=SimpleQueue()
	q.put(root)
	files={}
	while not q.empty():
		id=q.get()
		lst=getList(drive,id)
		for x in lst:
			files[x['id']]=x
			if c.isFolder(x):
				q.put(x['id'])
	return files

def download_file(f,dir):
	id=f['id']
	ext=c.get_ext(f["mimeType"])
	try:
		if ext==".gdoc":
			filename=dir+"/"+id+ext+".txt"
			f.GetContentFile(filename,mimetype="text/plain")
		else:
			filename=dir+"/"+id+ext
			f.GetContentFile(filename)
	except:
		print(" could not download "+str(id))
		c.failed.append(id)


def download(files,lst, start=0, len=100):
	print( "Download start:"+str(start))
	for id in lst[start: start+len]:
		path="tmp/"+str((int)(start/100))
		isExist = os.path.exists(path)
		if not isExist:
			os.mkdir(path)
		o=files[id]
		download_file(o,path)




