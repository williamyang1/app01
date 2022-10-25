import os
import json
import requests
import sys

from bs4 import BeautifulSoup
def get_config(config_f):
    print(config_f)
    f = open(config_f)
    config_json = json.load(f)
    #print(f.readlines())
    #print(config_json)
    #print(config_json["Branch"])
    sys.stdout.flush()
    return config_json

def get_files(config_json,version):
    result=[]
    root=config_json["rootpath"]
    for branch in config_json["Branch"]:
        #print(config_json[branch].keys())
        for path in config_json[branch].keys():
            folder=root +branch+ "/"+str(version)+"/"+path
            requires=config_json[branch][path]
            text = get_page_content(folder)
            builds = get_builds(text)
            result.extend((compare_builds(builds, requires,version)))
    return result



def compare_builds(builds, requireds,version):
    result=[]
    #print(requireds)
    for required in requireds:
        mark=0
        name_prefix=required.split("*")[0].strip()
        if required.split("*")[-1].strip().find("bug")!=-1:
            name_suffix = required.split("*")[-1].split("-->")[0].strip()
        else:
            name_suffix=required.split("*")[-1].strip()
        #print("name_prefix:",name_prefix,"name_suffix:",name_suffix)
        for build in builds:
            if build.find(name_prefix)!=-1 and build.find(name_suffix)!=-1 and build.find(version)!=-1:
                print("Build passed %s " %required)
                result.append("Build passed %s" %required)
                sys.stdout.flush()
                mark=1
        if mark ==0 :
            print("***Build %s *NOT* exist***" %required)
            result.append("***Build %s *NOT* exist***" % required)
    return result



def get_page_content(url):
    try:
        res=requests.get(url=url)
        return res.text
    except Exception:
        print("***The page %s can't be opened***"%url)

def get_builds(page_text):
    builds=[]
    #print("Get Builds")
    #print(page_text)
    soup = BeautifulSoup(page_text, 'html.parser')
    for link in soup.find_all('a'):
        #print("LLLLLLLLLL",link.get('href'))
        #print(link.get_text())
        if link.get_text().find("cudnn")!=-1:
            builds.append(link.get_text())
    return builds
def get_files_urm(config_json,version):
    result=[]
    root=config_json["rootpath"]
    for branch in config_json["Branch"]:
        #print(config_json[branch].keys())
        for path in config_json[branch].keys():
            folder=root +branch+ "/"+path+"/"+str(version)
            requires=config_json[branch][path]
            text = get_page_content(folder)
            builds = get_builds(text)
            result.extend(compare_builds(builds, requires,version))
    return result
def kitbunds_test(version):
    global config_file
    global config_urm_file
    if __name__ == "__main__":
        if version.find("8.7.0")!=-1:
            config_f= "./config/kitmaker.txt"
            config_urm_file="./config/urm.txt"
        else:
            config_f = "./config/kitmaker_dev.txt"
            config_urm_file = "./config/urm_dev.txt"
    else:
        if version.find("8.7.0") != -1:
            config_f=os.path.join(os.getcwd(), "app01", "tasks", "config", "kitmaker.txt")
            config_urm_file=os.path.join(os.getcwd(), "app01", "tasks", "config", "urm.txt")
        else:
            config_f = os.path.join(os.getcwd(), "app01", "tasks", "config", "kitmaker_dev.txt")
            config_urm_file = os.path.join(os.getcwd(), "app01", "tasks", "config", "urm_dev.txt")
    result=[]
    config_kitbundls=get_config(config_f)
    result1=get_files(config_kitbundls,version)
    config_urm = get_config(config_urm_file)
    result2=get_files_urm(config_urm,version)
    result.extend(result1)
    result.extend(result2)

    return result
if __name__ == "__main__":
    kitbunds_test("8.7.0.55")


