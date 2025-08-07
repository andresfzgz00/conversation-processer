import aiofiles


class FileRepository:
    @classmethod
    async def read_file_async(cls, file_name: str):  
        async with aiofiles.open(file_name, 'r', encoding='utf-8') as f:  
            content = await f.read()  
            return content

        
    @classmethod
    async def write_file_async(cls, file_name: str, content: str):  
        async with aiofiles.open(file_name, 'w', encoding='utf-8') as f:  
            await f.write(content)

        