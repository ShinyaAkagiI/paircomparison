# -*- coding: utf-8 -*-
import sys
import os
import itertools    # 組み合わせ用
import random       # シャッフル用


###################################################
# get_namelist関数
# -------------------------------------------------
# 指定したパス名に一致するファイル一覧を取得する
#
###################################################
def get_namelist(regex="*.json"):
    import glob
    namelist = glob.glob(regex)
    
    return namelist


###################################################
# get_text関数
# -------------------------------------------------
# textファイルのデータ読み込み
#
###################################################
def get_text(filename):    
    fname = filename
    try:
        fin = open(fname, "r")
        textdata = fin.read()
        if textdata[0:3] == "\xef\xbb\xbf": # BOMの削除
            textdata = textdata[3:]
        fin.close()
    except IOError as (errno, strerror):
        print "I/O Error {0}: {1}".format(errno, strerror)
    except ValueError:
        print "Value Error: Counld not convert data to an integer"

    return textdata


###################################################
# cmp_fnameクラス
# -------------------------------------------------
# 比較ファイル名リストを作成・取得する
#
###################################################
class CmpList:
    # 初期化
    def __init__(self):
        self._dirpath = ""  # 探索ディレクトリパス名
        self._filelist = [] # ファイルの名前リスト
        self._datalist = [] # ファイルのデータリスト
        self._cmpnum = []   # 比較番号リスト

    # 探索ディレクトリの指定
    def readDir(self, dname, filetype="*.txt"):
        if os.path.isdir(dname) and len(dname): # ディレクトリの確認
            while dname[-1] == "\\":
                dname = dname[:-1]
            self._dirpath = dname
        else:
            sys.exit(u"適切な探索対象ディレクトリを指定してください．")

        # ファイル名リストの取得
        self._filelist = get_namelist(regex=os.path.join(self._dirpath,filetype))   # ファイル名リスト

        # ファイルデータリストの取得
        for i in self._filelist:
            data = get_text(i)            
            self._datalist.append(data)

        # 比較番号リストの作成        
        self._cmpnum = list(itertools.combinations(range(0,len(self._filelist)), 2))
        random.shuffle(self._cmpnum)
        for i in range(len(self._cmpnum)):
            if random.randint(0,1): # 1/2の確率
                self._cmpnum[i] = (self._cmpnum[i][1], self._cmpnum[i][0])

    # ファイル名リストを取得
    def getFnameList(self):
        return self._filelist
        #import os
        #return [os.path.basename(i) for i in self._filelist]

    # ファイルデータリストを取得
    def getDataList(self):
        return self._datalist

    # 比較番号リストを取得
    def getCmpNum(self):
        return self._cmpnum


###################################################
# Main
###################################################
if __name__ == "__main__":
    cmpf = CmpList()            # インスタンス化
    cmpf.readDir("text")        # 探索ディレクトリの指定

    print cmpf.getFnameList()   # ファイル名リストを表示
    print cmpf.getDataList()    # ファイルデータリストを表示
    print cmpf.getCmpNum()      # 比較番号リストを表示
    

