
def Permutations(map_string):
    map_dict = {"1": ["a", "b", "c"], "2": ["d","e"], "3": ["f","g"]}
    if len(map_string) <= 0:
        return []
    elif len(map_string) == 1:
        return map_dict[map_string[0]]
    else:
        ans = []
        for i in range(len(map_dict[map_string[0]])):
            for str in Permutations(map_string[1:]):
                ans.append(map_dict[map_string[0]][i] + str)
        return ans

if __name__ == "__main__":
    print(Permutations("213"))
