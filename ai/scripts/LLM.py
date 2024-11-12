import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AdamW
from torch.utils.data import Dataset, DataLoader

class LLM_bot:
    def __init__(self, model_name="EleutherAI/gpt-neo-125M", learning_rate=1e-4):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token

        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        self.optimizer = AdamW(self.model.parameters(), lr=learning_rate)

    async def generate_text(self, prompt, max_len, temperature=0.7, top_k=50, top_p=0.9):
        self.model.eval()
        inputs = self.tokenizer(prompt, padding=True, truncation=True, return_tensors="pt").to(self.device)

        outputs = self.model.generate(
            inputs['input_ids'],
            attention_mask=inputs['attention_mask'],
            max_length=max_len,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            num_return_sequences=1,
            do_sample=True,
            pad_token_id=self.tokenizer.pad_token_id
        )

        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        first_sentence = re.split(r'[.!?]', generated_text)[0].strip()
        return first_sentence if len(first_sentence) < max_len else generated_text[:max_len]