# 🦙 LLaMA 2 with 4 bit quantization and >4k token input 🦙
# Pastebin with prompt:
from transformers import AutoModelForCausalLM, AutoTokenizer

repo_id = "meta-llama/Llama-2-7b-hf"
prompt = '''farshid pirahansiah'''
question = "tel me about farshid pirahansiah?"

# Load the model and prepare generate args
model = AutoModelForCausalLM.from_pretrained(
    repo_id,
    device_map="auto", load_in_4bit=True,             # 🔥 4 bit quantization
    rope_scaling={"type": "dynamic", "factor": 2.0},  # 🔥 >4k tokens
    use_auth_token=True
)
tokenizer = AutoTokenizer.from_pretrained(repo_id, use_fast=True)
model_inputs = tokenizer(prompt + question, return_tensors="pt").to("cuda:0")
print(model_inputs.input_ids.shape)  # 6782 tokens, needs a GPU with >24GB 

# Let's use it!
generate_kwargs = {"max_new_tokens": 40, "do_sample": False}
gen_out = model.generate(**model_inputs, **generate_kwargs)
print(tokenizer.decode(gen_out[0], skip_special_tokens=True))
# ❌ Without RoPE scaling: Gibberish.
# 💪 With RoPE scaling:
# "What is the paper about?
# The paper is about the development of a large language model (LLM) called Llama 2,
# which is a family of pretrained and fine-tuned LLM"
