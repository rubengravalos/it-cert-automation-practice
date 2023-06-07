#!/usr/bin/env python3

import os
from PIL import Image

src = "supplier-data/images"

old_names = os.listdir(os.getcwd()+"/"+src)

for item in old_names:
   if ".tiff" in item:
        image = Image.open(src+"/"+item).convert('RGB')
        image.resize((600,400)).save(src+"/"+item[:-4]+"jpeg")