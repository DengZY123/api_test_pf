
class  Utils :
    def sha256_encode(data):
        import hashlib
        data_sha = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return data_sha

if __name__ == "__main__":
    utils = Utils
    utils.sha256_encode()