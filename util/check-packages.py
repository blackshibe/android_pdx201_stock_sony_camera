from aapt2 import aapt

locations = [
    "/run/media/blackshibe/_",
    "/run/media/blackshibe/product",
    "/run/media/blackshibe/vendor",
]

# find every .apk file in locations
def find_apk_files():
    import os
    apk_files = []
    for location in locations:
        for root, dirs, files in os.walk(location):
            for file in files:
                if file.endswith(".apk"):
                    apk_files.append(os.path.join(root, file))
    return apk_files

# print apk files
apk_files = find_apk_files()

for file in apk_files:
    print("APK found: ", file)
    try:
        apk_info = aapt.get_apk_info(file)
        print(apk_info["package_name"])
    except:
        print("Couldn't find package signature") 
