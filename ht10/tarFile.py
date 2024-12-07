import sys
import tarfile
import io

def hex_to_bytes(hex_str):
    hex_str = hex_str.replace("\n", "").replace(" ", "")
    return bytes.fromhex(hex_str)

def extract_tar_info(dump_data):
    tar_data = io.BytesIO(dump_data)
    
    try:
        with tarfile.open(fileobj=tar_data, mode='r') as tar:
            file_count = 0
            total_size = 0
            
            for member in tar.getmembers():
                if member.isreg():
                    file_count += 1
                    total_size += member.size
                    
            return file_count, total_size
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0

if __name__ == "__main__":
    input_data = sys.stdin.read()
    
    dump_data = hex_to_bytes(input_data)
    
    file_count, total_size = extract_tar_info(dump_data)

    print(total_size, file_count)
