class Solution:
    def sortSentence(self, s: str) -> str:
        split_list = s.split()
        orderd_value = [""]*len(split_list)

        for i in range(len(split_list)):
            wordIndex = split_list[i][-1]
            word = split_list[i][:-1]

            orderd_value[int(wordIndex) - 1] = word
        return " ".join(orderd_value)
