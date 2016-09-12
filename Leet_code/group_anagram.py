def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    lol = []

    temp_list = []

    while strs:
        anagram = ''.join(sorted(strs[0]))
        print "--"
        print anagram
        temp_list = []
        for i in strs:
            print "i is " + i
            if anagram == ''.join(sorted(i)):
                temp_list.append(i)
                strs.remove(i)
                print "+++"
                print strs
        lol.append(temp_list)

    print lol

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

        