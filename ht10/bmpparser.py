import sys
import struct


def read_bmp(data):
    file_length = len(data)

    if file_length < 26:
        print("Incorrect size")
        return

    try:
        bmp_header = data[:14]
        signature, file_size, reserved1, reserved2, pixel_array_offset = struct.unpack(
            "<2sIHHI", bmp_header
        )
    except struct.error:
        print("Incorrect size")
        return

    if signature != b"BM":
        print("Not a Windows BMP")
        return

    if file_size != file_length:
        print("Incorrect size")
        return

    try:
        dib_header_size = struct.unpack("<I", data[14:18])[0]
    except struct.error:
        print("Incorrect size")
        return

    valid_dib_sizes = [12, 16, 40, 52, 56, 64, 108, 124]

    if dib_header_size not in valid_dib_sizes:
        print("Incorrect header size")
        return

    if file_length < 14 + dib_header_size:
        print("Incorrect size")
        return

    dib_header = data[14 : 14 + dib_header_size]

    if dib_header_size == 12:
        try:
            _, width, height, planes, bits_per_pixel = struct.unpack(
                "<IHHHH", dib_header[:12]
            )
            compression = 0
            pixel_array_size = 0
        except struct.error:
            print("Incorrect size")
            return
    elif dib_header_size >= 40:
        try:
            unpack_format = "<IiiHHII"
            unpack_size = struct.calcsize(unpack_format)
            fields = struct.unpack(unpack_format, dib_header[:unpack_size])
            _, width, height, planes, bits_per_pixel, compression, pixel_array_size = (
                fields
            )
        except struct.error:
            print("Incorrect size")
            return
    else:
        print("Incorrect header size")
        return

    if planes != 1:
        print("Incorrect header size")
        return

    abs_width = abs(width)
    abs_height = abs(height)

    if bits_per_pixel <= 0:
        print("Incorrect header size")
        return

    bits_per_row = abs_width * bits_per_pixel
    bytes_per_row = (bits_per_row + 7) // 8
    padding = (4 - (bytes_per_row % 4)) % 4
    row_size_padded = bytes_per_row + padding
    computed_pixel_array_size = row_size_padded * abs_height

    if dib_header_size >= 40:
        specified_pixel_array_size = pixel_array_size
    else:
        specified_pixel_array_size = 0

    size_matches = False
    padding_size = 0
    if specified_pixel_array_size == 0:
        size_matches = True
    elif specified_pixel_array_size == computed_pixel_array_size:
        size_matches = True
    elif specified_pixel_array_size == computed_pixel_array_size + 2:
        size_matches = True
        padding_size = 2
    else:
        size_matches = False

    if not size_matches:
        print("Incorrect image size")
        return

    compression_method = compression if dib_header_size >= 40 else 0
    print(abs_width, abs_height, bits_per_pixel, compression_method, padding_size)


bmp_file = sys.stdin.buffer.read()
read_bmp(bmp_file)
