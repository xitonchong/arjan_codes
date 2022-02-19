from typing import Protocol 

class StreamingService(Protocol):
    def start_streaming(self) -> str: 
        ... 


    def fill_buffer(self, stream_reference: str):
        ... 


    def stop_streaming(self, stream_reference: str): 
        ...