import os

data_root_path = '../../dataset/scenenet/val'
protobuf = '../../dataset/scenenet/scenenet_rgbd_val.pb'
is_exist0 = os.path.exists(data_root_path)
print(is_exist0)
is_exist1 = os.path.exists(protobuf)
print(is_exist1)
print(os.getcwd())

