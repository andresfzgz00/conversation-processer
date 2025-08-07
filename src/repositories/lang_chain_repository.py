from src.core import settings
from typing import TypeVar, Type, List, Dict, Any, Optional
from pydantic import BaseModel

from langchain_openai import ChatOpenAI

T = TypeVar("T", bound=BaseModel)


class LangChainRepository:
    def __init__(self):
        self.llm: ChatOpenAI = ChatOpenAI(
            model="gpt-4o-mini", temperature=0, api_key=settings.OPENAI_API_KEY
        )

    async def invoke_llm(
        self,
        messages: List[Dict[str, Any]],
        structured_output_class: Optional[Type[T]] = None,
    ):
        llm: ChatOpenAI = self.llm
        if structured_output_class:
            llm = self.llm.with_structured_output(structured_output_class)

        return await llm.ainvoke(messages)


lang_chain_repository = LangChainRepository()
