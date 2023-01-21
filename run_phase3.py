import os
import common as c
import json


def list_files(path):
    l = []
    for root, dirs, files in os.walk(path):
        for file in files:
            l.append(os.path.join(root, file))
    return l


def get_text(filename):
    try:
        txt = c.convert(filename)
        if txt is not None:
            txt = txt.strip().lower().replace('\n', ' ').replace('  ',' ')
        return txt
    except:
        return None


def get_files(dir='/home/ubuntu/Resolution2/'):
    # dir="/Users/User/Desktop/resolution2/"
    files = []

    for n in ["files", "files1", "files2", "files_"]:
        files.extend(list_files(dir+n))

    return files


def process(fs, files):
    # for each file
    contents = {}
    for filename in files:
        # base, extension = os.path.splitext(filename)
        print("   "+filename)
        base = os.path.basename(filename)
        key, extension = os.path.splitext(base)
        dir = os.path.dirname(filename)
        txt = get_text(filename)
        dict = {}
        dict["filename"] = filename
        dict["key"] = key
        dict["extension"] = extension
        dict["dir"] = dir
        dict["txt"] = txt
        dict["parent"] = c.get_title(fs, key)

        contents[filename] = dict
    return contents


def init():
    f_file = open("files.json", "r")
    fs = json.load(f_file)
    return fs


def get_res(c):
    res = {}
    for f in c:
        v = c[f]
        if v is not None:
            if v["txt"] is not None:
                if "resolution" in v["txt"]:
                    res[f] = v
    return res


def run():
    files = get_files()
    # files=files[:10]
    fs = init()
    c = process(fs, files)
    r = get_res(c)
    contents_file = open("resolution_"+f+".json", "w")
    json.dump(r, contents_file)
    return c, r
