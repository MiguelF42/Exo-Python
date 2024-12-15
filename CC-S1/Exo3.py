import platform, psutil

print(platform.system())
print(platform.machine())
print(platform.platform())
print(platform.processor())
print(str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")