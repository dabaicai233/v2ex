# 一鍵部署說明
## 1：構建鏡像
docker build -t ldd/v2ex:1.0 .
## 2: 啟動
docker run -dit --name spider1 ldd/v2ex:1.0
