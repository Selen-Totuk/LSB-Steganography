# LSB Steganography Tool / LSB Stenografi Aracı

Bir resmin içine gizli mesajlar saklamak için basit bir Python aracı. / A simple Python tool to hide secret messages inside images using the Least Significant Bit method.

## Kullanım / Usage

### Mesaj Gizleme / Encode Message
```bash
python stego.py encode -i input.png -m "Gizli mesajın" -o secret.png
python stego.py encode -i input.png -m "Your secret" -o secret.png
