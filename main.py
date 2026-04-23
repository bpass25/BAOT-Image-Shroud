import os

print("""
██████╗  █████╗  ██████╗ ████████╗
██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝███████║██║   ██║   ██║   
██╔══██╗██╔══██║██║   ██║   ██║   
██████╔╝██║  ██║╚██████╔╝   ██║   
      BAOT | Image Stegano
""")
print("1. Encode a message in an image\n2. Decode a message from an image")
ch = input("Choose (1 or 2): ")



if ch == '1':
    img = input("Enter the image name with type : " )
    msg = input("Enter the message to hide : ") 
    mark = "::BAOT_SE::"
    se_data = mark + msg
    with open(img, "ab") as f:
        f.write(se_data.encode())
    print("Done")
elif ch == '2':
    img = input("Enter image name to decrypt: ")
    with open(img, "rb") as f:
        content = f.read()
        mark = "::BAOT_SE::"
        marker_b = mark.encode()
        if marker_b in content:
            index = content.index(marker_b) + len(marker_b)
            sec_m = content[index:].decode()
            print(f"Message Found: {sec_m}")
            
            out_file = "dec_" + img.split('.')[0] + ".txt"
            with open(out_file, "w", encoding="utf-8") as out:
                out.write(sec_m)
            
            print(f"Message saved to: {out_file}")
        else:
            print("No data found in this image.")


