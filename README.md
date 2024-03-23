# PythonOffice_v2

安裝 git 和 vscode 和 python

# 安裝好 git 後，於指定資料夾內，點滑鼠右鍵，再點選"Open Git Bash here"
1. git init (最開始啟用git)
2. git status (目前狀態)
3. git add . (新增檔案於目前git的環境下，以便之後設定版本)
4. git commit -m "versionName" (儲存目前版本，versionName可任意輸入以設定目前版本名稱)
5. git config --global user.email "ctho64571@gmail.com" (設定使用者信箱)
6. git config --global user.name "Jason" (設定使用者名字)
7. git log (git版本列表)
8. git restore --staged fileName.副檔名 (將本次add進來的檔案，還原成add前的狀態)  
9. gitk (另開視窗詳細列出每個版本更改的檔案及其內容)
10. git reset --hard xxxx (切換至指定版本xxxx)
11. git reflog (切換至之前的某個版本後，想看那之後的全部版本)
12. git clone https://github.com/stephane/libmodbus.git (從特定網址複製全部檔案下來)

13. git remote add origin https://github.com/yuhtian23ok/PythonOffice.git (連接至指定git位置)
14. git push -u origin main (於指定git 位置上傳目前資料夾內全部檔案)
15. git pull origin main (於指定git 位置下載全部檔案)
16. git checkout main (git 切換到main，平常有main或master可切換，也可視情況自行增加)

# github token
點右上角大頭貼 -> 點 "Settings" -> 出現新頁面，點左邊 "Developer Settings" -> 出現選單，點 "Personal access tokens" -> 點 "Tokens (classic)" -> 點頁面中間右上方 "Generate Token" -> 出現下拉選單，點 "Token (classic)" -> 出現新頁面，輸入Note中說明、選擇token使用期限、勾選下方全部格子，最後點選最下方按鈕已產生token -> 出現token，複製token並記錄
