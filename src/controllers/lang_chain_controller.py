from ..services import LangChainService
from ..repositories import FileRepository
from ..enums import Files

class LangChainController:
  @classmethod
  async def get_debt_analysis_result(cls) -> None:
      result = await LangChainService.get_debt_analysis_result()
      
      await FileRepository.write_file_async(Files.DEBT_ANALYSIS_RESULT.value, result.model_dump_json())