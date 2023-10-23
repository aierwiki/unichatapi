import os
import sys
from loguru import logger
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unichatapi.llm import LLM


def main():
    api_key = os.getenv("ZHIPU_API_KEY")
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export API_KEY=xxx` or `code: zhipuai.api_key=xxx`")
    llm = LLM.from_llm_type('chatglm', api_key=api_key)
    response = llm.ask('你好')
    logger.info(response)


if __name__ == "__main__":
    main()