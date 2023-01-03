class setup:
    def __init__(self):
        # Service setting in synthesize, because of ap
        self.service=""
        self.session_id=""
        self.grpc_timeout=0
        self.list_voices=False
        self.response="streaming"
        self.text=""
        self.input_file=""
        self.out_path="class_test_object_02.wav"
        self.sample_rate=44100
        self.audio_encoding="pcm16"
        self.speech_pitch=1.0
        self.speech_range=1.0
        self.speech_rate=1.0
        self.speech_volume=1.0
        self.voice_name=""
        self.voice_gender="male"
        self.voice_age='child'
        self.language="pl"
        self.play=False
        self.tls_directory=""