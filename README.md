# Description

2種類のテキストに対する一対比較試験を支援するためのシステム。  
事前に比較対象用データをファイルとして作成しておき、質問項目に対して2種類のデータをランダムに表示して、被験者が比較判定していく。

一対比較試験は、多肢選択試験や評定尺度試験と比較して、被験者にとって「実験作業が容易」であり、時間をおいても「再現性の高いデータ取得」が可能であるという長所を持つ。  
本システムでは、一対比較試験の長所である「再現性の高いデータ取得」を更に容易にすべく、一対比較試験における比較判定作業をマウスレスで高速に実施できるように工夫している。  



# Install

This system is used cgi script in Python.  

(1) Activate cgi script on your webserver
* Apache Tutorial: CGI による動的コンテンツ - Apache HTTP サーバ バージョン 2.4
  https://httpd.apache.org/docs/2.4/ja/howto/cgi.html


(2) Get and Relocate Script

```
$ cd <your cgi script directory>
$ git clone paircomparison
$ mv start_paircomparison.html <your html directory>
$ mv end_paircomparison.html <your html directory>
```

Example. Directory Tree

```
/var/www
|-- cgi-bin
|-- paircomparison
|       |-- README.md
|       |-- comparison.py
|       |-- comparison_fname.py
|       |-- end_paircomparison.html
|       |-- start_paircomparison.html
|       |-- text
|           |-- 1.txt
|           |-- 2.txt
|           |-- 3.txt
|-- html
    |-- paircomparison
        |-- end_paircomparison.html
        |-- start_paircomparison.html
```


# Usage

1. Start paircomparison (access start_paircomparison.html)



2. select project



3. check text



4. Done paircomparison (access end_paircomparison.html)



# TODO

* 評定尺度に対応
* 試験時間の計測
* プロジェクトの完了条件を指定し、一対比較試験を繰り返せるように修正
* プロジェクト単位のデータ管理
* ユーザー単位のデータ管理
* 完了ページにプロジェクトの途中経過を表示

