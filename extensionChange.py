# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import os

directName = './jpg/'
fileList = os.listdir(directName)

for fileName in fileList:
    root, ext = os.path.splitext(directName + fileName)
    if ext==".jpg":
        os.rename(directName + fileName, root + '.JPG')