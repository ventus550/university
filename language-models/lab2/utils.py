from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model(model_name="gpt2", device="cuda"):
	tokenizer = AutoTokenizer.from_pretrained(model_name)
	model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

	def generate_response(prompt, max_new_tokens=16, **kwargs):
		inputs = tokenizer(prompt, return_tensors="pt").to(device)
		outputs = model.generate(
			inputs.input_ids,
			max_new_tokens=max_new_tokens,
			num_return_sequences=1,
			attention_mask=inputs.attention_mask,
			pad_token_id=tokenizer.eos_token_id,
			**kwargs
		)
		response = tokenizer.decode(outputs[0], skip_special_tokens=True)
		return response.removeprefix(prompt)

	return generate_response
