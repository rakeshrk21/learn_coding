import re

def findMatch(path):
    with open(path, 'r') as infile:
        found = False
        for line in infile:
            if '193.245.245.23' in line:
                print(line)
                found = True
                break

    return found
    # infile.write("write something!")

def readIps(path1, path2):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ips = []
    with open(path1, 'r+') as infile:
        for line in infile:
            found_ips = re.findall(ip_pattern, line)
            for ip in found_ips:
                octets = ip.split('.')
                for oct in octets:
                    if 0 < int(oct) >= 256:
                        print(f'found invalid ip: {ip}')
                        found_ips.remove(ip)
            ips.extend(found_ips)

    with open(path2, 'a') as outfile:
        for ip in ips:
            outfile.write(f"found IP: {ip}\n")

    return ips


if __name__ == "__main__":
    path1 = '/Users/rakeshra/code/learn_coding/academy/file_operations/rk.txt'
    path2 = '/Users/rakeshra/code/learn_coding/academy/file_operations/ips.txt'
    print(readIps(path1, path2))