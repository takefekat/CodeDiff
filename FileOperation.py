# Project Name    : CodeDiff
# File Name       : FileOperation.py
# Encoding        : UTF-8
# Creation Date   : 
# Last Update     : 
# Copyright © 2019, 2020 Fumito Takeuchi All rights reserved.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import
import sys
import os
import csv
import glob

def CheckFile(file_path):
    # ファイルの存在を確認
    if not os.path.isfile(file_path) :
        print("No such a file: " + file_path)
        sys.exit()
   
    # 拡張子を確認
    target_filetype = os.path.splitext(file_path)[1]
    support_filetype = [".c",".h",".asm"]
    if not target_filetype in support_filetype:
        print("No support filetype: " + target_filetype + " " + file_path)


# Output CSV File for Edit Operations.
# in : edit distance res array[]
# in : output file path
# Out: CSV file 
def List2CSVFile(list_, output_file_path):
    with open(output_file_path, "w", encoding="UTF-8") as f: # 文字コードをUTF-8に指定
        writer = csv.writer(f, lineterminator="\n") # writerオブジェクトの作成 改行記号で行を区切る
        writer.writerows(list_) # csvファイルに書き込み


def MakeResultFolder(base_folder_path, new_folder_path, res_folder_path):

    # 入力ファイル/フォルダ取得    
    base_files = glob.glob(base_folder_path + "**", recursive=True)
    new_files = glob.glob(new_folder_path + "**", recursive=True)

    # フォルダ作成
    res_folder_path
    for folder_path in base_files:
        if os.path.isdir(folder_path) :
            os.mkdir

    print(l)
    
