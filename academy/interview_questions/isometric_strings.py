class IsometricString:

    def isIsomorphic(self, s: str, t: str) -> bool:

        # if the length of strings are not equal then cant be isometric
        if len(s) != len(t):
            return False

        # check the key/value pair exists in a dict
        d = dict()
        for i in range(len(s)):

            # if the value exist in the map, then check if the key is same
            if t[i] in d.values():
                # get the key for that value
                try:
                    for key, value in d.items():
                        if value == t[i]:
                            break

                except KeyError:
                    print("key does not exists")

                if key != s[i]:
                    return False
                elif key == s[i]:
                    continue

            # if the value is not found in the value but the key already exist then return
            elif s[i] in d.keys():
                return False

            # if the key value pair does not exists in the dict then add it
            else:
                d[s[i]] = t[i]

        return True


# print(IsometricString().isIsomorphic("egg", "add")) # expected true
# print(IsometricString().isIsomorphic("badc", "baba")) # expected false
print(IsometricString().isIsomorphic("foo", "bar")) # expected false
