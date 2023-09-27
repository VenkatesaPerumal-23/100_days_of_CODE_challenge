#Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        split_str=s.split() 
        temp=""
        for char in split_str[::-1]:
            ans=""
            for i in char[::-1]:
                ans+=i 
            ans=ans[::-1]
            temp+=ans+" "

        return temp.strip()