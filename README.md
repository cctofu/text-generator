# Text Generation with Transformer Decoder

This project focuses on **text generation using a Transformer Decoder**. Both **training from scratch** and **fine-tuning a pretrained model** were compared, with experiments analyzing **loss curves, perplexity, BLEU scores, decoding strategies, and the effects of pre-training**.

---

## 📦 Environment

- **Python**: 3.8  
- **PyTorch**: 1.1  
- **NLTK**: 3.5  
- **Hardware**: MacBook Pro (Apple M1 chip)  

---

## ⚙️ Models

- **Tfmr-scratch**: Transformer trained from random initialization.  
- **Tfmr-finetune**: Transformer fine-tuned from pretrained checkpoints.  

---

## 📊 Results

### Training and Validation Loss
- Fine-tuned model converges faster and achieves consistently lower loss.  
- Validation loss plateaus at ~3.0 for scratch vs ~2.9 for fine-tuned:contentReference[oaicite:0]{index=0}.  

### Test Set Performance
| Model          | Perplexity | Forward BLEU-4 | Backward BLEU-4 | Harmonic BLEU-4 |
|----------------|------------|----------------|-----------------|-----------------|
| Tfmr-scratch   | 18.74      | 0.577          | 0.424           | 0.489           |
| Tfmr-finetune  | **15.41**  | 0.570          | 0.430           | 0.490           |:contentReference[oaicite:1]{index=1}

**Key insight:** Fine-tuned models achieve significantly **lower perplexity**, though BLEU scores show only marginal differences.  

---

## 🔍 Decoding Strategies

### BLEU-4 Scores (Sampled)
- **Top-p sampling (p = 0.9)** generally yields **more coherent and diverse text**.  
- **Random sampling with lower temperature (τ = 0.7)** provides a better balance, improving harmonic BLEU:contentReference[oaicite:2]{index=2}.  

### Temperature Effects
- Lower τ increases predictability and forward BLEU, but does not always improve harmonic BLEU.  
- High τ (τ = 1) increases diversity but risks incoherent sentences.  

---

## ✍️ Generated Sentences

Examples from **Tfmr-scratch** and **Tfmr-finetune** runs:  
- Scratch: *“A street corner with a fire hydrant and a street light lit up.”*  
- Fine-tune: *“A man and woman sitting on a bench in a very large field.”*  

**Observation:** Fine-tuned sentences are slightly more consistent and grammatically correct:contentReference[oaicite:3]{index=3}.  

---

## 🧪 Final Network Settings

- **Decoding strategy:** Random  
- **Temperature:** 0.7  
- Other hyperparameters: unchanged  

---

## 📝 Analysis

### Transformer vs RNN
- **Complexity**: Transformers enable parallel processing (faster but higher memory), while RNNs are sequential (slower but memory-efficient).  
- **Performance**: Transformers excel in long-range dependencies; RNNs work better for short-range contexts.  
- **Positional Encoding**: Required in Transformers; inherent in RNNs:contentReference[oaicite:4]{index=4}.  

### Inference Complexity
- **Single token:** O(n × d), where n = attention heads, d = hidden dimension.  
- **Full sequence (L tokens):** O(L × n × d).  
- **Self-attention dominates** when sequence length is large (O(L² × d)).  
- **Feed-forward dominates** when hidden dimension d is large relative to L:contentReference[oaicite:5]{index=5}.  

### Pre-training Effects
- Improves **generation quality** (more coherent, fluent text).  
- Significantly **reduces convergence time**.  
- Benefits align with expectations when fine-tuning tasks resemble pre-training data:contentReference[oaicite:6]{index=6}.  

---

## ✅ Key Takeaways

1. **Pre-training helps**: Lower perplexity, faster convergence, better quality text.  
2. **BLEU scores are limited**: They don’t always capture semantic correctness or fluency.  
3. **Best decoding balance**: Random sampling with τ = 0.7.  
4. **Transformers > RNNs** for text generation, especially in long contexts.  
