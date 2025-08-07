from enum import Enum
from os import path


class Files(Enum):
    DEBT_CONVERSATION = path.join("..", "munoz-bot-agent", "conversation.log")
    DEBT_ANALYSIS_RESULT = "debt_analysis_result.log"
