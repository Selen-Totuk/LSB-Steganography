from PIL import Image

# MESAJI GİZLE
def encode(image_path, secret_message, output_path):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(i), '08b') for i in secret_message)
    binary_message += '00000000'  # Mesajın sonu

    data = list(img.getdata())
    new_data = []
    msg_index = 0

    for pixel in data:
        if msg_index < len(binary_message):
            new_pixel = list(pixel)
            for i in range(3):  # R, G, B kanalları
                if msg_index < len(binary_message):
                    new_pixel[i] = (new_pixel[i] & 0xFE) | int(binary_message[msg_index])
                    msg_index += 1
            new_data.append(tuple(new_pixel))
        else:
            new_data.append(pixel)

    img.putdata(new_data)
    img.save(output_path)
    print("Mesaj gizlendi!")

# MESAJI ÇÖZ
def decode(image_path):
    img = Image.open(image_path)
    data = list(img.getdata())
    binary_message = ""

    for pixel in data:
        for value in pixel[:3]:  # R, G, B
            binary_message += str(value & 1)

    # Binary'yi metne çevir
    all_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    decoded_message = ""
    for byte in all_bytes:
        if byte == '00000000':
            break
        decoded_message += chr(int(byte, 2))
    return decoded_message

# KULLANIM
encode("normal.png", "404: Comfort Zone Not Found", "gizli.png")
print("Çözülen mesaj:", decode("gizli.png"))
