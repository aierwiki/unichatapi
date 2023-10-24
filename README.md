<div align="center">
   <img src="assets/uni.jpeg" width=256></img>
   <p><strong>通过统一的接口调用不同的大语言模型API</strong></p>

[English](README.md) | 简体中文

</div>


## 功能

在这个百模大战的时代，每家的大模型都开发了自己的SDK，而作为应用方，我们可能会需要接入多个不同的模型去白嫖免费的token额度，或者比较不同大模型的效果，开发接入各家LLM的代码是一件繁琐且无趣的事情。另外一个问题是各家的SDK的使用方式都有点恶心，不够直接了当。在这种背景下我开发了UniChatAPI项目，本项目旨在提供一个简洁的SDK，快速接入不同厂家的LLM。你需要做的只是[下载、安装](https://github.com/aierwiki/unichatapi)和提问。

### 这是你吗？

UniChatAPI 的典型用户是：

- 🤠**羊毛党**，希望白嫖各种大模型，来实现自己的应用。
- 🤓**大模型调研**，快速接入各种大模型，比较各种大模型在不同领域的优劣
- 😎**大模型应用开发者**，快速调试 prompt，快速搭建自己的应用Demo

### 支持的 LLM

| AI 机器人                                                     | 是否支持API      | 说明                                     |
| ------------------------------------------------------------ | -------- | ---------------------------------------- |
| [ChatGPT](https://chat.openai.com)                           |      |                              |
| [智谱清言](https://zhipuai.cn/)                                 | ✅      |                              |
| [文心一言](https://yiyan.baidu.com/)                          | ✅       |                                          |
| [Bard](https://bard.google.com/)                              |     |                                          |
| [通义千问](http://tongyi.aliyun.com/)                         | ✅     |       |
| [讯飞星火](http://xinghuo.xfyun.cn/)                          |      |           |
| [天工](https://neice.tiangong.cn/)                            |      |                    |
| [360 智脑](https://ai.360.cn/)                                |      |                      |
| [Claude](https://claude.ai/)                                 |      |                           |

### 支持的Embedding

| AI 机器人                                                     | 是否支持API      | 说明                                     |
| ------------------------------------------------------------ | -------- | ---------------------------------------- |
| [OpenAI](https://openai.com)                                |   ✅   |                              |
| [智谱清言](https://zhipuai.cn/)                                 |       |                              |
| [文心一言](https://yiyan.baidu.com/)                          |        |                                          |
| [Bard](https://bard.google.com/)                              |     |                                          |
| [通义千问](http://tongyi.aliyun.com/)                         |     |       |
| [讯飞星火](http://xinghuo.xfyun.cn/)                          |      |           |
| [天工](https://neice.tiangong.cn/)                            |      |                    |
| [360 智脑](https://ai.360.cn/)                                |      |                      |
| [Claude](https://claude.ai/)                                 |      |                           |


## 预先需要

UniChatAPI 是一个LLM接入SDK，而不是代理。因此，您必须：

1. 拥有可以访问这些 AI 的帐号，或 API token。
2. 与 AI 网站有可靠的网络连接。

## 下载 / 安装
```bash
pip install unichatpai
```

## 使用

### 对接聊天机器人

```python
import os
from loguru import logger
from unichatapi.llm import LLM


api_key = os.getenv("ZHIPU_API_KEY")
if api_key is None:
    raise Exception("api_key not provided, you could provide it with `shell: export API_KEY=xxx` or `code: zhipuai.api_key=xxx`")
llm = LLM.from_llm_type('chatglm', api_key=api_key)
response = llm.ask('你好')
logger.info(response)
```

### 对接文本向量化模型

```python
import os
from loguru import logger
from unichatapi.llm import LLM


api_key = "123456"
api_base = "http://localhost:3003/v1"
emb_model = Embedding.from_emb_type('openai', api_key=api_key, api_base=api_base)
res = emb_model.encode("你好")
logger.info(res)
res = emb_model.encode(["你好", "你好啊"])
logger.info(res)
```

## 致谢

### 贡献者
<a href="https://github.com/aierwiki/unichatapi/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=aierwiki/unichatapi" />
</a>

## 赞助

如果您喜欢这个项目，可以通过以下方式支持：

<img src="assets/weixin.jpeg" width="200" />
<img src="assets/zhifubao.jpeg" width="200" />
