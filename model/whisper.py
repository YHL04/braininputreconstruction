

from transformers import WhisperProcessor, WhisperForConditionalGeneration


def get_whisper_processor(model_name="openai/whisper-large"):
    processor = WhisperProcessor.from_pretrained(model_name)

    return processor


def get_whisper_model(model_name="openai/whisper-large"):
    model = WhisperForConditionalGeneration.from_pretrained(model_name)
    model.config.forced_decoder_ids = None

    return model


if __name__ == "__main__":
    from transformers import load_dataset

    processor = get_whisper_processor()
    model = get_whisper_model()

    ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
    sample = ds[0]["audio"]
    input_features = processor(sample["array"], sampling_rate=sample["sampling_rate"],
                               return_tensors="pt").input_features

    # generate token ids
    predicted_ids = model.generate(input_features)
    # decode token ids to text
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)

