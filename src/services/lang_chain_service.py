from typing import List, Dict, Any
import json
from langchain_core.messages import SystemMessage

from ..repositories import lang_chain_repository, FileRepository
from ..enums import Files
from ..models import DebtAnalysisResult
from ..prompts import SystemPrompts


class LangChainService:
    @classmethod
    async def get_debt_analysis_result(cls) -> None:
        try:
            conversation_messages_str: str = await FileRepository.read_file_async(
                Files.DEBT_CONVERSATION.value
            )
            conversation_messages_str_list: List[str] = (
                conversation_messages_str.splitlines()
            )

            conversation_messages: List[Dict[str, Any]] = [
                json.loads(message) for message in conversation_messages_str_list
            ]

            messages: List[Dict[str, Any]] = [
                SystemMessage(SystemPrompts.DEBT_ANALYSIS_PROMPT),
                *conversation_messages
            ]

            result = await lang_chain_repository.invoke_llm(
                messages, DebtAnalysisResult
            )
            
            return result

        except Exception as e:
            print("Exception: ", e)
