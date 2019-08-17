# 一键部署
## 1：构建镜像
docker build -t ldd/v2ex:1.0 .
## 2: 启动
docker run -dit --name spider1 ldd/v2ex:1.0
