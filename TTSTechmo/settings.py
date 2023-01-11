class setup:
    def __init__(self):
        # "An IP address and port (address:port) of a service the client connects to."
        self.service=""
        # "A session ID to be passed to the service. If not specified, the service generates a default session ID."
        self.session_id=""
        # "A timeout in milliseconds used to set gRPC deadline - how long the client is willing to wait for a reply from the server (optional)."
        self.grpc_timeout=0
        # "Lists all available voices."
        self.list_voices=False
        # "streaming or single, calls the streaming (default) or non-streaming version of Synthesize."
        self.response="streaming"
        # "A text to be synthesized."
        self.text=""
        # "A text to be translated."
        self.text_to_translate=''
        # "A file with text to be synthesized."
        self.input_file=""
        # "A path to the output wave file with synthesized audio content."
        self.out_path="TTSTechmo/synthesis_records/synthesis.wav"
        # "A sample rate in Hz of synthesized audio. Set to 0 (default) to use voice's original sample rate."
        self.sample_rate=44100
        # "An encoding of the output audio, pcm16 (default) or ogg-vorbis."
        self.audio_encoding="pcm16"
        # "Allows adjusting the default pitch of the synthesized speech (optional, can be overriden by SSML)."
        self.speech_pitch=1.0
        # "Allows adjusting the default range of the synthesized speech (optional, can be overriden by SSML)."
        self.speech_range=1.0
        # "Allows adjusting the default rate of the synthesized speech (optional, can be overriden by SSML)."
        self.speech_rate=1.0
        # "Allows adjusting the default volume of the synthesized speech (optional, can be overriden by SSML)."
        self.speech_volume=1.0
        # "A name od the voice used to synthesize the phrase (optional, can be overriden by SSML)."
        self.voice_name=""
        # "A gender of the voice - female or male (optional, can be overriden by SSML)."
        self.voice_gender="male"
        # "An age of the voice - adult, child, or senile (optional, can be overriden by SSML)."
        self.voice_age='child'
        # "ISO 639-1 language code of the phrase to synthesize (optional, can be overriden by SSML)."
        self.language="en"
        # "Source language from which we translating (en, pl or es)."
        self.language_source='pl'
        # "Setting of TTS language service version (tts-en or tts-pl)."
        self.tts_lang='tts-en'
        # "Play synthesized audio. Works only with pcm16 (default) encoding."
        self.play=False
        # If set to a path with SSL/TLS credential files (client.crt, client.key, ca.crt), use SSL/TLS authentication. Otherwise use insecure channel (default)."
        self.tls_directory=""