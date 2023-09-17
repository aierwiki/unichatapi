<div align="center">
   <img src="assets/uni.jpeg" width=256></img>
   <p><strong>通过统一的接口调用不同的大语言模型API</strong></p>

[English](README.md) | 简体中文

</div>


## 功能

基于大型语言模型（LLMs）的 AI 机器人非常神奇。然而，它们的行为可能是随机的，不同的机器人在不同的任务上表现也有差异。如果你想获得最佳体验，不要一个一个尝试。ChatALL（中文名：齐叨）可以把一条指令同时发给多个 AI，帮助您发现最好的回答。你需要做的只是[下载、安装](https://github.com/sunner/ChatALL/releases)和提问。

### 这是你吗？

ChatALL 的典型用户是：

- 🤠**大模型重度玩家**，希望从大模型找到最好的答案，或者最好的创作
- 🤓**大模型研究者**，直观比较各种大模型在不同领域的优劣
- 😎**大模型应用开发者**，快速调试 prompt，寻找表现最佳的基础模型

### 支持的 AI

| AI 机器人                                                    | 网页访问 | API      | 说明                                     |
| ------------------------------------------------------------ | -------- | -------- | ---------------------------------------- |
| [ChatGPT](https://chat.openai.com)                           | 支持     | 支持     | 包含 Web Browsing、Azure OpenAI service  |
| [Bing Chat](https://www.bing.com/new)                        | 支持     | 无 API   | 不需要帐号                               |
| [文心一言](https://yiyan.baidu.com/)                         | 否       | 支持     |                                          |
| [Bard](https://bard.google.com/)                             | 支持     | 即将推出 |                                          |
| [Poe](https://poe.com/)                                      | 支持     | 即将推出 |                                          |
| [MOSS](https://moss.fastnlp.top/)                            | 支持     | 无 API   |                                          |
| [通义千问](http://tongyi.aliyun.com/)                        | 支持     | 即将推出 |                                          |
| [得到学习助手](https://ai.dedao.cn/)                         | 即将推出 | 无 API   |                                          |
| [讯飞星火](http://xinghuo.xfyun.cn/)                         | 支持     | 即将推出 |                                          |
| [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html)   | 支持     | 无 API   | 不需要帐号                               |
| [Vicuna](https://lmsys.org/blog/2023-03-30-vicuna/)          | 支持     | 无 API   | 不需要帐号                               |
| [ChatGLM](https://chatglm.cn/blog)                           | 支持     | 无 API   | 不需要帐号                               |
| [Claude](https://www.anthropic.com/index/introducing-claude) | 支持     | 无 API   | 不需要帐号                               |
| [Gradio](httpps://gradio.app/)                               | 支持     | 无 API   | 用于 Hugging Face space 或自己部署的模型 |
| [HuggingChat](https://huggingface.co/chat/)                  | 支持     | 无 API   |
| [天工](https://neice.tiangong.cn/)                           | 支持     | 即将推出 |                                          |
| [You](https://you.com/)                                      | 支持     | 无 API   |                                          |
| [Pi](https://pi.ai)                                          | 支持     | 无 API   |                                          |
| [360 智脑](https://ai.360.cn/)                               | 支持     | 无       |                                          |
| [YouChat](https://you.com/)                                  | 支持     | 无       |                                          |
| [Open Assistant](https://open-assistant.io/)                 | 支持     | 无       |                                          |
| [Claude](https://claude.ai/)                                 | 支持     | 无       |                                          |
| [Character.AI](https://character.ai/)                        | 支持     | 无       |                                          |

还会有更多。[到这里](https://github.com/sunner/ChatALL/labels/more%20LLMs)为你喜欢的 AI 投票吧。

### 其他功能

- 快问模式：不需要等待前面的请求完成，就可以发下一条指令
- 对话历史保存在本地，保护你的隐私
- 高亮喜欢的答案，删除不需要的答案
- 随时启用/禁用任何机器人
- 在一列、两列或三列视图之间切换
- 自动更新到最新版
- 夜间模式（由 @tanchekwei 贡献）
- 快捷键。按 `Ctrl + /` 可以看到所有快捷键（由 @tanchekwei 贡献）
- 多对话窗口（由 @tanchekwei 贡献）
- 支持设置代理（由 @msaong 贡献）
- 提示词管理（由 @tanchekwei 贡献）
- 支持多语言（中文、英语、德语、法语、俄语、越南语、韩语、日语、西班牙语、意大利语）
- 支持 Windows，macOS 和 Linux

计划中：

欢迎参与这些功能的开发。

- [ ] 把前端部署到 GitHub Pages

## 预先需要

ChatALL 是一个客户端，而不是代理。因此，您必须：

1. 拥有可以访问这些 AI 的帐号，或 API token。
2. 与 AI 网站有可靠的网络连接。

## 下载 / 安装
```bash
brew install --cask chatall
```

## 致谢

### 贡献者

<a href="https://github.com/sunner/ChatALL/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sunner/ChatALL" />
</a>

## 赞助

如果您喜欢这个项目，可以通过以下方式支持：

<img src="assets/weixin.jpeg" width="200" />
<img src="assets/zhifubao.jpeg" width="200" />
