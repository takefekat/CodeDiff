# Project Name    : CodeDiff
# File Name       : EditDistanceBetweenStrings.py
# Encoding        : UTF-8
# Creation Date   : 2019.10.4
# Last Update     : 2019.10.4
# Copyright © 2019 Fumito Takeuchi All rights reserved.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import
import os
import sys
import FileOperation

# Compute Edit Distance and Edit Operations between Files.
# in : bace file
# In : new file
# Out: edit distance
# Out: edit operation array[][] 
#      {{changetype, baceline, newline}, ...} (changetype -> 0:no change, 1:change, 2:add, 3:delete)
def EditDistanceBetweenFiles(base_file, new_file):

    # fileオープン
    with open(base_file) as f:
        bace_lines = f.readlines()
    with open(new_file) as f:
        new_lines = f.readlines()

    # 問題サイズ
    N = len(bace_lines)
    M = len(new_lines)
    print(N)
    print(M)

    # DPテーブル
    dp = [[N*M for i in range(M+1)] for j in range(N+1)]
    back_track = [[[0 for i in range(2)] for j in range(M+1)] for k in range(N+1)]

    # DPテーブル初期化
    for i in range(M+1):
        dp[0][i] = i
    for i in range(N+1):
        dp[i][0] = i
    back_track[0][0] = [-1,-1]

    # 編集距離DP
    for i in range(1,N+1):
        for j in range(1,M+1):
            # delete
            if dp[i][j] > dp[i-1][j] + 1 :
                dp[i][j] = dp[i-1][j] + 1
                back_track[i][j] = list([i-1,j])
            # add
            if dp[i][j] > dp[i][j-1] + 1:
                dp[i][j] = dp[i][j-1] + 1
                back_track[i][j] = list([i,j-1])
            # change / nochange
            cost = 0 if isSameLine(bace_lines[i-1], new_lines[j-1] )else 1 
            if dp[i][j] > dp[i-1][j-1] + cost:
                dp[i][j] = dp[i-1][j-1] + cost
                back_track[i][j] = list([i-1,j-1])
    edit_distance = dp[N][M]
    print(edit_distance)

    # 解の復元（バックトラック）
    pre_i = N
    pre_j = M
    trace = back_track[pre_i][pre_j]
    res = []
    while trace[0] != -1 and trace[1] != -1 :
        nxt_i = trace[0]
        nxt_j = trace[1]
        # add
        if pre_i == nxt_i:
            res.append(["a",0,pre_j])
        # delete
        elif pre_j == nxt_j:
            res.append(["d",pre_i,0])
        # no change
        elif isSameLine(bace_lines[pre_i-1], new_lines[pre_j-1] ) :
            res.append(["-",pre_i,pre_j])
        # change
        else:
            res.append(["c",pre_i,pre_j])

        pre_i = nxt_i
        pre_j = nxt_j
        trace = back_track[nxt_i][nxt_j]

    res.reverse()
    print(res)

    return edit_distance, res


# Difference between lines
# in : line1
# in : line2
# Out: True when line1 = line2.
def isSameLine(line1,line2):
    # 行頭、行末の空白は差分なしとする(TODO どうするべきか)
    return line1.strip() == line2.strip()


if __name__ == '__main__':

    args = sys.argv
    if len(args) != 3:
        print("NOTE: python3 EditDistanceBetweenStrings.py \"file_path1\" \"filepath2\"")
        sys.exit()

    bace_file_path = args[1]
    new_file_path = args[2]
    print("base file：" + bace_file_path)
    print("new file ：" + new_file_path)

    # 入力ファイルチェック
    FileOperation.CheckFile(bace_file_path)
    FileOperation.CheckFile(new_file_path)

    # 編集距離計算
    distance, res = EditDistanceBetweenFiles(args[1],args[2])

    # CSVファイル出力
    output_filename = args[1].split(os.sep)[-1]
    "example_out"+ os.path.splitext(output_filename)[0] + ".csv"
    FileOperation.List2CSVFile(res,output_filename)

    print("Done. Output: " + output_filename)

    sys.exit()
