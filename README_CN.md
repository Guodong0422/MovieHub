# MovieHub：电影内容管理与发现平台

MovieHub 是一个基于 Flask 开发的电影内容管理与发现平台。绝大部分依托AI工具开发，本人只进行了简单修改，意在表现产品设计能力和开发理解，耗时约2小时。

项目支持电影信息增删改查、CSV 数据集导入、搜索筛选、REST API 数据访问、Dashboard 数据看板、Watchlist 待看列表，以及基于规则的相似电影推荐功能。

本项目作为个人作品集项目进行重构和扩展，主要用于展示全栈开发能力、数据库设计能力、API 设计能力、数据管理能力，以及产品思维。

---

## 产品背景

许多电影内容平台或媒体资料库都需要管理大量电影元数据，例如电影标题、类型、评分、上映年份、简介和海报等信息。

MovieHub 被设计为一个轻量级的电影内容管理与发现平台，用户或内容管理者可以通过该系统完成以下操作：

* 管理电影信息
* 从 CSV 文件批量导入电影数据
* 搜索、筛选和排序电影记录
* 通过 Dashboard 查看内容数据分析
* 将感兴趣的电影加入 Watchlist 待看列表
* 根据电影类型和评分发现相似电影

该项目模拟了一个小型内容平台或媒体资料管理系统的核心工作流程。

---

## 核心功能

### 电影信息管理

* 新增电影记录
* 在首页查看所有电影
* 查看电影详情页
* 编辑已有电影信息
* 删除电影记录

### 搜索、筛选与排序

* 根据电影标题进行关键词搜索
* 根据电影类型进行筛选
* 按评分排序
* 按上映年份排序

### CSV 数据集导入

* 从 CSV 文件批量导入电影数据
* 将 CSV 字段映射到数据库字段
* 将年份和评分字段转换为合适的数据类型
* 根据电影标题跳过重复记录

### REST API

* `GET /api/movies`
  以 JSON 格式返回所有电影记录。

* `GET /api/movies/<id>`
  根据电影 ID 返回单部电影记录。

### Dashboard 数据看板

Dashboard 页面提供基础产品指标和数据洞察，包括：

* 电影总数量
* 平均电影评分
* 最高评分电影
* 最常见电影类型
* 不同电影类型的数量分布

### Watchlist 待看列表

* 将电影加入个人待看列表
* 在独立 Watchlist 页面查看已收藏电影
* 从 Watchlist 中移除电影

### 相似电影推荐

* 推荐与当前电影类型相同的电影
* 排除当前正在浏览的电影
* 按评分从高到低排序推荐结果
* 在电影详情页最多展示 3 部相似电影

---

## 技术栈

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* HTML
* CSS
* Bootstrap
* REST API
* CSV 数据导入
* Git / GitHub

---

## 项目结构

```text
moviehub/
├── app.py
├── models.py
├── import_movies.py
├── requirements.txt
├── README.md
├── data/
│   └── movies.csv
├── static/
│   └── style.css
└── templates/
    ├── add_movie.html
    ├── base.html
    ├── dashboard.html
    ├── detail.html
    ├── edit_movie.html
    ├── index.html
    └── watchlist.html
```

---

## 本地运行方式

### 1. 克隆项目

```bash
git clone https://github.com/Guodong0422/MovieHub.git
cd moviehub
```

### 2. 创建虚拟环境

```bash
python -m venv venv
```

### 3. 激活虚拟环境

Windows PowerShell：

```powershell
.\venv\Scripts\Activate.ps1
```

如果无法正常激活虚拟环境，也可以直接使用虚拟环境中的 Python 运行项目：

```powershell
.\venv\Scripts\python.exe app.py
```

### 4. 安装依赖

```bash
pip install -r requirements.txt
```

### 5. 启动 Flask 应用

```bash
python app.py
```

然后在浏览器中打开：

```text
http://127.0.0.1:5000
```

---

## 导入电影数据集

电影数据存放在：

```text
data/movies.csv
```

运行以下命令导入数据：

```bash
python import_movies.py
```

导入脚本会读取 CSV 文件，检查重复电影标题，转换年份和评分字段，并将新的电影记录写入 SQLite 数据库。

---

## API 接口说明

### 获取所有电影

```http
GET /api/movies
```

示例返回：

```json
[
  {
    "id": 1,
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": "Sci-Fi",
    "rating": 8.8,
    "description": "A thief enters people's dreams to steal and plant ideas.",
    "poster_url": "https://example.com/poster.jpg"
  }
]
```

### 根据 ID 获取单部电影

```http
GET /api/movies/1
```

示例返回：

```json
{
  "id": 1,
  "title": "Inception",
  "director": "Christopher Nolan",
  "year": 2010,
  "genre": "Sci-Fi",
  "rating": 8.8,
  "description": "A thief enters people's dreams to steal and plant ideas.",
  "poster_url": "https://example.com/poster.jpg"
}
```

---

## 产品思维

MovieHub 不只是一个普通的 CRUD 技术项目，也被设计成一个小型产品原型。

项目中包含多个偏产品方向的设计考虑：

* 搜索与筛选功能提升内容发现效率
* CSV 导入功能支持内容运营和数据初始化流程
* Dashboard 数据看板帮助内容管理者理解电影库结构
* Watchlist 功能记录基础用户偏好行为
* 相似电影推荐模拟内容平台中的基础推荐场景
* REST API 设计为未来前端扩展或外部客户端调用提供基础

---

## 用户故事

### 用户故事 1：搜索与内容发现

作为电影浏览用户，我希望能够搜索和筛选电影，从而快速找到自己感兴趣的内容。

### 用户故事 2：内容管理

作为内容管理者，我希望能够新增、编辑和删除电影记录，从而高效维护电影资料库。

### 用户故事 3：数据集导入

作为内容运营人员，我希望能够从 CSV 文件批量导入电影数据，从而避免手动逐条创建电影记录。

### 用户故事 4：产品数据分析

作为产品经理，我希望查看 Dashboard 数据指标，从而理解电影资料库的内容结构和质量。

### 用户故事 5：Watchlist 待看列表

作为用户，我希望能够将感兴趣的电影保存到待看列表中，从而之后可以方便地再次查看。

### 用户故事 6：相似电影推荐

作为用户，我希望在电影详情页看到相似电影推荐，从而发现更多相关内容。

---

## 当前限制

当前项目是一个本地运行的 Flask 应用，暂未包含以下功能：

* 用户登录和认证
* 多用户账号管理
* 云数据库部署
* 生产环境级别的安全配置
* 高级机器学习推荐模型

这些限制是为了保持项目作为轻量级作品集原型的清晰度和可维护性。

---

## 未来优化方向

后续可以考虑加入：

* 用户登录与身份认证
* 基于 Watchlist 和评分行为的个性化推荐
* 用户评论和评分系统
* 网页端 CSV 上传功能
* API 文档页面
* 大规模数据下的分页功能
* 部署到 Render、Railway 或 PythonAnywhere
* 使用 GitHub Pages 制作静态项目展示页

---

## 作品集总结

本项目展示了以下能力：

* 使用 Flask 进行全栈 Web 应用开发
* 使用 SQLite 和 SQLAlchemy 进行关系型数据库设计
* 设计 REST API 并返回 JSON 数据
* 处理 CSV 数据并实现批量导入
* 实现搜索、筛选和排序逻辑
* 设计 Dashboard 数据看板与产品指标
* 通过 Watchlist 功能设计用户行为模块
* 实现基于规则的推荐逻辑
* 进行产品需求拆解和功能规划
