from google.cloud import texttospeech

def list_voices():
    """Lists the available voices."""
    client = texttospeech.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    for voice in voices.voices:
        # Display the voice's name. Example: tpc-vocoded
        print('Name: {}'.format(voice.name))

        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            print('Supported language: {}'.format(language_code))

        # SSML Voice Gender values from google.cloud.texttospeech.enums
        ssml_voice_genders = ['SSML_VOICE_GENDER_UNSPECIFIED', 'MALE',
                              'FEMALE', 'NEUTRAL']

        # Display the SSML Voice Gender
        print('SSML Voice Gender: {}[{}]'.format(
            ssml_voice_genders[voice.ssml_gender], voice.ssml_gender))

        # Display the natural sample rate hertz for this voice. Example: 24000
        print('Natural Sample Rate Hertz: {}\n'.format(
            voice.natural_sample_rate_hertz))

def synthesize_text(text, output_filepath, voice_id=None, language_code='en-US', gender='male'):
    """Synthesizes speech from the input string of text."""
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    if not voice_id:
        ssml_gender = texttospeech.enums.SsmlVoiceGender.MALE if gender.lower() == 'male' else \
            texttospeech.enums.SsmlVoiceGender.FEMALE
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=ssml_gender)
    else:
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            name=voice_id)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open(output_filepath, 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file {}'.format(output_filepath))
