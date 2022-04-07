def upper_case_all(f):
    def wrapper(self):
        s = f(self)
        if type(s) == str:
            return s.upper()
        if type(s) == list:
            s1 = []
            for i in s:
                s1.append(i.upper())
            return s1
    return wrapper

def devide_by_sentences(f):
    def wrapper(self):
        end_of_sentence = ['.', '!', '?']
        str1 = f(self).strip()
        arr = []
        count = 0
        for i in range(len(str1)):
            if str1[i-1] in end_of_sentence and not str1[i] in end_of_sentence:
                arr.append(str1[i-count:i])
                count = 0
            if i == len(str1)-1:
                arr.append(str1[i-count:i+1])
            count += 1
        return arr
    return wrapper

