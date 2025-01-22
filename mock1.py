import re
paragraph = '"Bob hit a ball, the hit BALL flew far after it was hit.",'
banned = ["hit"]

paragraph = "a."
banned = []
def mostCommonWord( paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    list_dict = {}
    # res= re.split('!?,;. ',paragraph) !?',;.
    res= re.split(r'[`\!;\'\\,.? ]',paragraph)
    print(res)
    
    b = 0
    i = 0
    temp = 0
    for b in range(len(banned)):
        res = [k for k in res if banned[b] not in k]
        
    # print(res)
    # print(len(res))
    while i in range(len(res)-1):
        key = res[i].lower()
        if key in list_dict:
            list_dict[key] = list_dict[key] + 1 
        else:
            list_dict[key] = 1 
            
        if list_dict[key] > temp :
            temp = list_dict[key]
        
        i = i+ 1
    
    keys = [key for key, val in list_dict.items() if val == temp]
    print(keys)   
    # print(list_dict)
    # print(res)
    return(keys)
            
   
    
mostCommonWord( paragraph, banned)
    