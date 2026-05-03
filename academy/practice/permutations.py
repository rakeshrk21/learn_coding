def permute(str, ans):
    # base: if str length is 0 return
    if len(str)==0:
        print(ans+ " ")

    for i in range(len(str)):
        c = str[i]
        remaining = str[0:i] + str[i+1:]
        permute(remaining, c+ans)

if __name__ == "__main__":
    permute("abb", "")

