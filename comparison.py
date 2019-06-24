#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import os
import sys
import time

from comparison_fname import CmpList

# REQUEST_METHODのチェック
if os.environ['REQUEST_METHOD'] != 'POST':
    print "Content-Type: text/html; charset=utf-8"
    print ""
    sys.exit("Not Post")

print "Content-Type: text/html; charset=utf-8"
print ""


# POSTデータの確認
form = cgi.FieldStorage()
question = ""
judge = ""
if form.has_key("project"):
    question =  form["project"].value


# HTMLの先頭部分
html_start ="""<html>
<head>
  <title>一対比較システム</title>
  <meta http-equiv="Content-Type" content="text/html: charset=utf-8">
  <meta http-equiv="Content-Style-Type" content="text/css">
  <meta http-equiv="Content-Script-Type" content="text/javascript">
  <meta name="author" content="Shinya Akagi">
  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
  <script>
  $(function(){
     // css
     $( "textarea" ).css({'width':'95%', 'resize':'none', 'overflow':'auto'});
     $( "[type='radio']" ).buttonset();
     $( "[type='radio']").css({ 'opacity': '0' });
     $( "[type='radio'] + label").css({ 'opacity': '1' });
     $( ".checkbox" ).css({
         'font-size': '24px',
         'width':'94%',
         'margin': '0 3% 0 3%',
     });

     // tab一覧の作成
     $( "#tablist" ).tabs({
        activate: function(event, ui){
           var newtabid = ui.newTab.index()+1; // 新規アクティビティのタブID
           var oldtabid = ui.oldTab.index()+1; // 前のアクティビティのタブID

           // 新規アクティビティのタブがチェック済みの場合
           if ( $( "#Q" + newtabid ).data('check') ){
              // 新規タブの背景色を水色
              $( "#Q" + newtabid + " a" ).css('background-color', '#00FFFF');  
           } else {
              // 新規タブの背景色を白色
              $( "#Q" + oldtabid + " a" ).css('background-color', '#FFFFFF');
           }

           // 前のアクティビティのタブがチェック済みの場合
           if ( $( "#Q" + oldtabid ).data('check') ){
              // 前のタブの背景色を緑色
              $( "#Q" + oldtabid + " a" ).css('background-color', '#5FFB17');  
           } else {
              // 前のタブの背景色をクリア
              $( "#Q" + oldtabid + " a" ).css('background-color', '');
           }

           $( "input" ).focus(); // ラジオボタンを選択
        }
     });

     var tabsize = $("#tablist >ul >li").size(); // タブの数

     $( "input" ).focus(); // 1つ目のタブのラジオボタンを選択

     // 次へボタンのクリック時
     $( ".next" ).click(function(){
       // タブの切り替え
       var tabid = $(this).data('tabid');
       $( "#tablist" ).tabs('option', 'active', tabid);
     });

     // 次へボタンのキーボード操作時
     $( ".next" ).keydown(function(e){
       var code = e.which;
       if(code == 8){ // Backspace入力時
         return false;
       }
       else if (code == 13){ // Enter入力時
         var tabid = $(this).data('tabid');
         if (tabid == tabsize){
           end();
         }
         else{
            $( "#tablist" ).tabs('option', 'active', tabid);
         }
         return false;
       }
       else if(code == 37){ // ←入力時
         var tabid = $(this).data('tabid')*2-2;
         $( "[type='radio']" )[tabid].click();
         return false;
       }
       else if(code == 38){ // ↑入力時
         $( "input" ).focus();
         return false;
       }
       else if(code == 39){ // →入力時
         var tabid = $(this).data('tabid')*2-1;
         $( "[type='radio']" )[tabid].click();
         return false;
       }
       else if(code == 40){ // ↓入力時
         return false;
       }
     });

     // 終了処理
     function end(){
       var flag = true;
       for (var tabid=1; tabid<=tabsize; tabid++){ // 入力確認
         if ($( "#Q" + tabid ).data('check') !== 'ok'){
           $( "#tablist" ).tabs('option', 'active', tabid-1);
           flag = false;
           break;
         }
       }
       if(flag){
         $("form input").submit(); // フォームの送信
         //alert("終了");
       }
       else{
         alert("Q" + tabid + "が未記入です");
       }
     };

     // 終了ボタンのクリック時
     $( ".end" ).click(function(){
       end();
     });

     // 終了ボタンのキーボード操作時
     $( ".end" ).keydown(function(e){
       var code = e.which;
       if(code == 8){ // Backspace入力時
         return false;
       }
       else if (code == 13){ // Enter入力時
         end();
         return false;
       }
       else if(code == 37){ // ←入力時
         var tabid = $(this).data('tabid')*2-2;
         $( "[type='radio']" )[tabid].click();
         return false;
       }
       else if(code == 38){ // ↑入力時
         $( "input" ).focus();
         return false;
       }
       else if(code == 39){ // →入力時
         var tabid = $(this).data('tabid')*2-1;
         $( "[type='radio']" )[tabid].click();
         return false;
       }
       else if(code == 40){ // ↓入力時
         return false;
       }
     });

     // ラジオボタンのクリック時
     $( "[type='radio']" ).click(function(){
       var tabid = $(this).data('tabid');
       // タブの背景色を水色
       $( "#Q" + tabid + " a" ).css('background-color', '#00FFFF');
       // タブにcheckデータを追加
       $( "#Q" + tabid ).data('check', 'ok');

       // ?ラベルの背景色を水色
       $( "[type='radio'] +label" ).text("□ Check");
       $( "[type='radio']:checked +label" ).text("■ Check");
       $( "[type='radio'] +label" ).parent().css({'background-color': '#FFFFFF'});
       $( "[type='radio']:checked" ).parent().css({'background-color': '#00FFFF'});
     });

     // ラジオボタンのキーボード操作時
     $( "[type='radio']").keydown(function(e){
       var code = e.which;
       if (code == 13){ // Enter入力時
         var tabid = $(this).data('tabid');
         if (tabid == tabsize){
           end();
         }
         else{
           $( "#tablist" ).tabs('option', 'active', tabid);
         }
         return false;
       }
       else if(code == 8){ // Backspace入力時
         var tabid = $(this).data('tabid') - 2;
         $( "#tablist" ).tabs('option', 'active', tabid);
         return false;
       }
       else if(code == 37){ // ←入力時
         var tabid = $(this).data('tabid')*2-2;
         $( "[type='radio']" )[tabid].click();
         return false;
       }
       else if(code == 38){ // ↑入力時
         return false;
       }
       else if(code == 39){ // →入力時
         var tabid = $(this).data('tabid')*2-1;
         $( "[type='radio']" )[tabid].click();
         return false;
       }
       else if(code == 40){ // ↓入力時
         $( ".next" ).focus();
         $( ".end" ).focus();
         return false;
       }
     });
  });
  </script>
</head>
<body>"""
print html_start


# HTMLの本体部分
cmpl = CmpList()
cmpl.readDir('text')
flist = cmpl.getFnameList() # ファイル名一覧
dlist = cmpl.getDataList()  # データ一覧
nlist = cmpl.getCmpNum()    # 比較番号リスト

# tabの記述（jQuery）
tabdata = "<div id=\"tablist\">\n"
tabdata += "   <ul>\n"
content = "    <p style=\"text-align: center; font-size: 2em;\">{0}</p>\n".format(question)
for i in range(len(nlist)):
    tabid = i+1
    
    # tab一覧の作成
    tabdata += "      <li id=\"Q{0}\"><a href=\"#t{0}\">Q{0}</a></li>\n".format(tabid)

    # content一覧の作成
    if isinstance(nlist[i], tuple) and len(nlist[i]) == 2:
        content += "    <div id=\"t{0}\">\n".format(tabid)

        # 比較テキスト
        content += "      <div style=\"float: left; width:50%; text-align: center;\">\n"
        content += "        <textarea rows=\"15\" readonly>{}</textarea><br/>\n".format(cgi.escape(dlist[nlist[i][0]], True))
        content += "        <div class=\"checkbox\"><input id=\"left{0}\" type=\"radio\" name=\"radio{0}\" data-tabid=\"{0}\">".format(tabid)
        content += "        <label for=\"left{0}\">□ Check</label></div>\n".format(tabid)
        content += "      </div>"

        content += "      <div style=\"float: left; width:50%; text-align: center;\">\n"
        content += "        <textarea rows=\"15\" readonly>{}</textarea><br/>\n".format(cgi.escape(dlist[nlist[i][1]], True))
        content += "        <div class=\"checkbox\"><input id=\"right{0}\" type=\"radio\" name=\"radio{0}\" data-tabid=\"{0}\">\n".format(tabid)
        content += "        <label for=\"right{0}\">□ Check</label></div>\n".format(tabid)
        content += "      </div>"

        # 切り替えボタン
        content += "      <div style=\"text-align: center;\">\n"
        if tabid == len(nlist):
            content += "      <button class=\"end\" data-tabid=\"{}\">終了</button>\n".format(tabid)
        else:
            content += "      <button class=\"next\" data-tabid=\"{}\">次へ</button>\n".format(tabid)
        content += "      </div>\n"
        content += "    </div>\n"

tabdata += "   </ul>\n"
tabdata += "<form action=\"/paircomparison/end_paircomparison.html\" method=\"post\">\n"
tabdata += content
tabdata += "</form>\n"
tabdata += "</div>\n"
print tabdata


# HTMLの末尾部分
html_end = """</body>
</html>"""
print html_end

