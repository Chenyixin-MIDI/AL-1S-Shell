def set_file_version(filename, version):
    from win32api import BeginUpdateResource, UpdateResource, EndUpdateResource
    h = BeginUpdateResource(filename, 0)
    UpdateResource(h, 16, 1, version)
    EndUpdateResource(h, 0)
    version = (1, 0, 0, 0)
set_file_version("dist/hello.exe", 3.1)
