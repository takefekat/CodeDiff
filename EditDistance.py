
import sys
import os
import FileOperation
import EditDistanceBetweenFiles



if __name__ == '__main__':

    args = sys.argv
    if len(args) != 4 :
        print(" NOTE: python3 EditDistance.py \"bace_folder_path\" \"new_folder_path\" \"res_folder_path\" ")
        sys.exit()

    bace_folder_path = args[1]
    new_folder_path = args[2]
    res_folder_path = args[3]
    print("base folder：" + bace_folder_path)
    print("new folder ：" + new_folder_path)
    print("res folder ：" + res_folder_path)

    # 出力フォルダ作成
    FileOperation.MakeResultFolder(bace_folder_path, new_folder_path, res_folder_path)



    sys.exit()