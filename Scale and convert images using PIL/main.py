#! /usr/bin/env python3

import os
from PIL import Image

src = "images/"
dst = "/opt/icons/"

old_names = os.listdir(os.getcwd()+"/"+src)

for item in old_names:
   if not item[0]==".":
      image = Image.open(src+item).convert('RGB')
      image.rotate(90).resize((128,128)).save(dst+item, "JPEG")