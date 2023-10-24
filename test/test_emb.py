import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from loguru import logger
from unichatapi.embedding import Embedding



def test_openai():
    api_key = "123456"
    api_base = "http://localhost:3003/v1"
    emb_model = Embedding.from_emb_type('openai', api_key=api_key, api_base=api_base)
    res = emb_model.encode("你好", is_query=True)
    logger.info(res)
    res = emb_model.encode(["你好", "你好啊"])
    logger.info(res)


def main():
    test_openai()


if __name__ == "__main__":
    main()

