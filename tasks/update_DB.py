import json
from django.db import models
from app01 import models



def UUID_DB_update_branch(version_prefix,branch):
    from app01.tasks.get_uuid import get_version_list
    print("HOUSSSSSSSSSSSSSSSSSS")
    version_list=get_version_list(branch)
    for (uuid,cl,version) in version_list:
        print(uuid,cl,version)
        if int(cl) < 31864035:
            continue
        version = version_prefix + str(version)
        if models.UUID.objects.filter(UUID=uuid).exists():
            print("UUID exist")
            continue
        models.UUID.objects.create(UUID=uuid, CL=cl, version=version)
    print("DDDDone")

def UUID_DB_update():
    UUID_DB_update_branch("8.7.0.","cudnn_rc_hopper_cuda_11.8")
    UUID_DB_update_branch("8.8.0.", "cudnn_dev_next")
def update():
    UUID_DB_update()


if __name__ == '__main__':
    update()