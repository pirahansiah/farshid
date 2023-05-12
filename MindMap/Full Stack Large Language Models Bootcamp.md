# LLMBC 2023
## 0 
Launch an LLM App in One Hour (LLM Bootcamp)

* Prototyping & Iteration
	* “Foundation models” have unblocked a lot of applications
	* Prototype with a high-capability hosted model in chat first
	* Tinker with prompts and build on open source frameworks
* Deploying an MVP
	* Cloud tooling makes it easy to get started
	* Find a simple UI and start getting feedback from users ASAP
* Zero-Shot prompting 
* Code
	* pip install -qqq  (quiet mode)
		* getpass
		* langchain openai
		* arxiv
		* pypdf
		* faiss-cpu tiktoken
	* code
		* getpass.getpass
		* from IPython.display import Markdown
		* paper=next(arxiv.Search(id_list=["2205.11916:]).results())
		* Markdown(paper.summary)
		* paper_path=paper.download_pdf()
		* from langchain.document_loaders import PyPDFLoader
## 1
* [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy)
* Model Hub: Hugging Face
* Transformers
	* attention is all you need (2017)
		* Transformer Decoder 
			* 1 inputs: 
				* vectors of numbers
				* turn into a sequence of tokens
				* turn into vocabulary IDs				* 
				* input embedding
					* learn an embedding matrix
						* the simplest NN layer type
			* 1.2 positional encoding
				* position-encoding vectors to embedding vectors 
			* 2 transformer architecture
				* 2.1
					* project inputs into query, key, value roles
					* attention
						* masked multi-head 
					* masking attention
				* 2.2
					* skip connections / residual blocks
						* output=module(input) + input
				* 2.3
					* layer Normalisation
				* 2.4 
					* feed forward layer 
			* 3 
		* simultaneously
			* expressive in the forward pass
			* optimisable via back-propagation + gradient descent
			* efficient hight parallelism compute graph 
	* RASP 2021
		* programming language of transformer-implementable operations
* LLMs
	* BERT 2019 - 110M params
		* bidirectional encoder representations from transformers
		* encoder-only (no attention masking)
		* 15% of all words masked out
	* T5 2020 - 11B params
		* Text-to-Text Transfer Transformer
		* Encoder-Decoder architecture
		* T5 training data C4 - 160B tokens
	* GPT / GPT 2 - 2019 - 1.5B params
		* byte pair encoding
	* GPT-3 - 2020 - 175B params
		* exhibited unprecedented few-shot and zero-shot learning
		* 500B tokens
		* but trained on only 300B
	* GPT-4 - 2023 - 
	* Chinchilla 2022
		* optimal model and training set size
	* LLaMA 2023
* Instruction Tuning
	* at the time GPT-3 (2020) 
		* mindset few-shot
			* text completion
	* at the time ChatGPT (2022)
		* mindset zero-shot
			* instruction-following
	* supervised fine-tuning
	* instructGPT/GPT-3.5
	* ChatGPT
		* RLHF on conversations
		* ChatML format (messages from system, assistant, user roles)
* Retrieval-enhanced transformer (2021)

