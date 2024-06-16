from huggingface_hub import hf_hub_download


model_name = "TheBloke/law-LLM-GGUF"
model_file = "law-llm.Q2_K.gguf"

model_path = hf_hub_download(model_name, filename=model_file)