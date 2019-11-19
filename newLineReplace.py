# -*- coding: utf-8 -*-

txtPath = "./txt/test.txt"
outPath = "./txt/Otest.txt"

with open(txtPath, "rb") as f:
    txt = f.read()

txt = txt.replace(b"\r\n", b"HOGE")
txt = txt.replace(b'\n', b'')
txt = txt.replace(b'HOGE', b'\r\n')

with open(outPath, "wb") as f:
    f.write(txt)
     
     
