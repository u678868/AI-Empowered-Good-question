# AI Empowered

> 本目录遵循 `AGENTS.md` 中定义的协作规范与安全边界（只读隔离区 / 读写开发区）。

## 项目简介

竞赛项目脚手架已初始化，**业务逻辑尚未实现**。本文件的状态表与代码实际进度严格同步，未完成项均已如实标注，请勿将未实现项视为已完成。

## 目录结构

```
AI Empowered/
├── AGENTS.md            # 🔒 协作规范（只读，不得修改）
├── screenshots/         # 🔒 运行截图（3-8 张）
├── demo/                # 🔒 Demo 视频 / 链接 / 演示脚本
├── submission/          # 🔒 最终提交文件（由作者手动迁移）
├── src/                 # 🔓 核心业务源码
├── tests/               # 🔓 单元测试与集成测试
├── docs/                # 🔓 技术设计文档
├── temp/                # 🔓 临时文件
├── README.md            # 本文件（主说明文档）
├── AI_USAGE.md          # AI 使用记录
├── requirements.txt     # 运行依赖
├── requirements-dev.txt # 开发依赖
├── pyproject.toml       # 项目与工具配置
└── Makefile             # 常用开发命令
```

## 核心文件清单

| 文件路径 | 职责说明 |
| :--- | :--- |
| `src/__init__.py` | 源码包初始化与版本号 |
| `src/main.py` | 程序入口（脚手架占位，业务逻辑未实现） |
| `tests/test_smoke.py` | 脚手架冒烟测试 |
| `docs/architecture.md` | 项目架构与目录分区说明 |
| `AI_USAGE.md` | AI 使用记录 |
| `requirements.txt` | 运行依赖 |
| `requirements-dev.txt` | 开发/测试依赖 |
| `pyproject.toml` | 项目元数据与工具配置 |
| `Makefile` | 常用开发命令封装 |

## 功能状态表

| 功能模块 | 对应核心文件 | 状态 (已完成/未实现) |
| :--- | :--- | :--- |
| 项目脚手架与目录规范 | `src/__init__.py`、`pyproject.toml` | ✅ 已完成 |
| 冒烟测试 | `tests/test_smoke.py` | ✅ 已完成 |
| 架构文档 | `docs/architecture.md` | ✅ 已完成 |
| 业务主流程 | `src/main.py` | ⏳ 未实现 |
| 核心业务服务 | `src/services/core.py` | ⏳ 未实现 |

## 开发环境

- Python 3.13（虚拟环境：`.venv/`，基于本机 3.13.2 创建）
- 激活：`.\.venv\Scripts\Activate.ps1`
- 安装依赖：`.\.venv\Scripts\python.exe -m pip install -r requirements.txt`