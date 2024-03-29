import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unichatapi.llm import LLM
from loguru import logger


def test_chatglm():
    api_key = os.getenv("API_KEY")
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export API_KEY=xxx` or `code: zhipuai.api_key=xxx`")
    llm = LLM.from_llm_type('chatglm', api_key=api_key)
    res = llm.ask('你好')
    logger.info(res)
    logger.info("-------------")
    res = llm.ask_stream('你好', incremental=True, disable_search=True)
    for r in res:
        logger.info(r)
    
    logger.info("-------------")

    res = llm.ask_stream('你好', incremental=False)
    for r in res:
        logger.info(r)


def test_qwen():
    api_key = os.getenv("QWEN_API_KEY")
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export QWEN_API_KEY=xxx` or `code: zhipuai.api_key=xxx`")
    llm = LLM.from_llm_type('qwen', api_key=api_key)
    res = llm.ask('你好')
    logger.info(res)
    logger.info("-------------")
    res = llm.ask_stream('你好', incremental=True)
    for r in res:
        logger.info(r)
    logger.info("-------------")
    res = llm.ask_stream('你好', incremental=False)
    for r in res:
        logger.info(r)


def test_erniebot():
    api_type = "aistudio"
    access_token = os.getenv("ERNIEBOT_ACCESS_TOKEN")
    if access_token is None:
        raise Exception("access_token not provided, you could provide it with `shell: export ERNIEBOT_ACCESS_TOKEN=xxx`")
    llm = LLM.from_llm_type('erniebot', api_type=api_type, access_token=access_token)
    res = llm.ask('你好')
    logger.info(res)
    logger.info("-------------")
    # res = llm.ask_stream('你好', incremental=True)
    # for r in res:
    #     logger.info(r)
    # logger.info("-------------")
    # res = llm.ask_stream('你好', incremental=False)
    # for r in res:
    #     logger.info(r)

def test_baichuan():
    api_key = os.getenv("BAICHUAN_API_KEY", None)
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export BAICHUAN_API_KEY=xxx`")
    llm = LLM.from_llm_type('baichuan', api_key=api_key)
    res = llm.ask('你好')
    logger.info(res)
    logger.info("-------------")

def test_skywork():
    api_key = os.getenv("SKYWORK_API_KEY")
    secret_key = os.getenv("SKYWORK_SECRET_KEY")
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export SKYWORK_API_KEY=xxx`")
    if secret_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export SKYWORK_SECRET_KEY=xxx`")
    llm = LLM.from_llm_type('skywork', api_key=api_key, secret_key=secret_key)
    res = llm.ask('你好')
    logger.info(res)
    logger.info("-------------")


def main():
    # test_chatglm()
    # test_qwen()
    # test_erniebot()
    # test_skywork()
    test_baichuan()


if __name__ == "__main__":
    main()
