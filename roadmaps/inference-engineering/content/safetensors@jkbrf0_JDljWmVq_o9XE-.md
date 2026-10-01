# Safetensors

Safetensors is the standard format for storing and distributing open model weights. It uses memory mapping for fast, zero-copy loading and prevents execution of arbitrary code during deserialization, making it safer than earlier pickle-based formats. All major inference engines load safetensors natively, and most open models on Hugging Face publish weights in this format.