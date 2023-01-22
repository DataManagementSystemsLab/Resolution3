import textract
import json
import os
import traceback
import shutil

def isPdf(f):
        if 'mimeType' in f:
                if f['mimeType']=='application/pdf':
                        return True    
        return False

def isDoc(f):
        if 'mimeType' in f:
                if f['mimeType']=='application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                        return True
                if f['mimeType']=="application/msword":
                        return True        
        return False            

def isFolder(f):
        if 'mimeType' in f:
                if f['mimeType']=='application/vnd.google-apps.folder':
                        return True
        return False

def get_content_files(fs):
        txts=[]
        for key,value in fs.items():
                if not isFolder(value):
                        txts.append(key)  
        return txts             

def convert(filename):
        success=False
        try:
                txt=""
                txt=textract.process(filename)
                txt=txt.decode("utf-8")
                success=True
        except  Exception as e:
                print(e)
                pass
        if not success:
                return None     
        return txt

def get_title(fs, id):
        l=[]
        if id not in fs: 
                return []
        o=fs[id]
        parent_title=[]
        if 'parents' in o:
                if len(o['parents']) >= 1:
                        pid=o['parents'][0]['id']
                        parent_title=get_title(fs,pid)
                l= parent_title
        l.append( o['title'])
        return l         

def   save_txt(filename,txt):
                base, extension = os.path.splitext(filename)
                txtfilename="../txts/"+base+".txt"
                print("File->>>>" +txtfilename)
                with open(txtfilename, 'w') as tmpf:
                        tmpf.write(txt)    



def get_resolutions( files, dir="/Users/User/Desktop/resolution3/files/"):
        resolutions=[]
        failed=[]
        empty=[]
        for filename in os.listdir(dir):
                f = os.path.join(dir, filename)
                # Split the file name into two parts: the base name, and the extension
                base, extension = os.path.splitext(filename)
                # checking if it is a file
                if os.path.isfile(f) and base in files:
                        print(f)
                        try:
                                txt=convert(f)
                                txt=txt.strip()
                                if len(txt)==0:
                                        empty.append(filename)
                                #else:
                                #        save_txt(filename,txt)  
                                #        if 'resolution' in txt:
                                #                print ("found in " +filename)
                                #                print(get_str_title(files,base))
                                #                resolutions.append(filename)
                        except:
                                print("Exception "+base) 
                                failed.append(filename)
                                traceback.print_exc()
                else:
                        print ("skipping "+base) 
        return resolutions,failed,empty

        
def get_pdfs(files):
        pdfs=[]
        for k,v in files.items():
                if isPdf(v):
                        pdfs.append(k)
                
        return pdfs     

def get_docs(files):
        docs=[]
        for k,v in files.items():
                if isDoc(v):
                        docs.append(k)
                
        return docs     

def get_folders(files):
        folders=[]
        for k,v in files.items():
                if isFolder(v):
                        folders.append(k)
                
        return folders  
def get_ext(t):
                        ext=""
                        if t=="application/msword":
                                ext=".doc"
                        elif t=="application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                                ext=".docx"  
                        elif t=="application/pdf":
                                ext=".pdf"
                        elif t=="image/jpeg":
                                ext=".jpg"
                        elif t=="text/html":
                                ext=".html"
                        elif t=="text/plain":
                                ext=".txt"
                        elif t=="text/csv":  
                                ext=".csv"  
                        elif t=="application/vnd.openxmlformats-officedocument.presentationml.presentation":
                                ext=".pptx"
                        elif t=="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                                ext=".xslx"
                        elif t=="video/mp4":
                                ext=".mp4"
                        elif t=="audio/x-m4a":
                                ext=".m4a"  
                        elif t=="application/vnd.google-apps.document":
                                ext=".gdoc"      
                        return ext



def list_files(dir):
    f=[]
    for root, dirs, files in os.walk(dir):
        for file in files:
            f.append(os.path.join(root, file))
    return f            

def flatten_dir(src_dir, target_dir):
    for filename in list_files(src_dir):
       if os.path.isfile(filename):
          shutil.move(filename, target_dir)
