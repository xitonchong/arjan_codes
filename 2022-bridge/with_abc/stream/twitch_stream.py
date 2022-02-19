import logging 

from stream.data import generate_id 
from stream.service import StreamingService 


class TwitchStreamingService(StreamingService):
    def start_stream(self):
        stream_reference = generate_id() 
        logging.info(f"Starting Twitch Stream swith reference {stream_reference}")
        return stream_reference

    def fill_buffer(self, stream_reference: str) -> None: 
        buffer_data = self.retrieve_buffer_data() 
        logging.info(
            f"Received buffer data: {buffer_data}."
            f" Sending to Twitch Srea: {stream_reference}."
        )

    def stop_stream(self, stream_reference: str):
        logging.info(f"Closing Twitch Stream with reference {stream_reference} ")