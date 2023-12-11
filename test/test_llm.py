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
    res = llm.ask_stream('你好', incremental=True)
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
    api_key = os.getenv("ERNIEBOT_API_KEY")
    secret_key = os.getenv("ERNIEBOT_SECRET_KEY")
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export ERNIEBOT_API_KEY=xxx`")
    if secret_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export ERNIEBOT_SECRET_KEY=xxx`")
    llm = LLM.from_llm_type('erniebot', api_key=api_key, secret_key=secret_key)
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
    

def test_erniebot4():
    api_key = os.getenv("ERNIEBOT_API_KEY")
    secret_key = os.getenv("ERNIEBOT_SECRET_KEY")
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export ERNIEBOT_API_KEY=xxx`")
    if secret_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export ERNIEBOT_SECRET_KEY=xxx`")
    llm = LLM.from_llm_type('erniebot4', api_key=api_key, secret_key=secret_key)
    res = llm.ask('你好')
    logger.info(res)


def main():
    # test_chatglm()
    # test_qwen()
    # test_erniebot()
    test_erniebot4()



if __name__ == "__main__":
    main()
