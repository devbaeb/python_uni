def upper_case_all(f):
    def wrapper(self):
        s = f(self)
        if type(s) == str or type(s) == text:
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

class text(str):

    #@upper_case_all
    #@devide_by_sentences
    def upper_case(self):
        end_of_sentence = ['.', '!', '?']
        escape_characters = ['\n', '\r', '\t', '\b', '\f']
        str1 = str(self)
        arr = []
        count = 0
        for i in range(len(str1)):
            if str1[i-1] in end_of_sentence and not str1[i] in end_of_sentence:
                arr.append(str1[i-count:i])
                count = 0
            if i+1 == len(str1):
                arr.append(str1[i-count:i+1])
            count += 1
        
        arr2 = []
        for sentence in arr:
            list1 = list(sentence)
            for i in range(len(list1)):
                if list1[i] != ' ' and not list1[i] in escape_characters:
                    list1[i] = list1[i].upper()
                    break
            arr2.append(''.join(list1))
                    
        return text(''.join(arr2))
    
    #@upper_case_all
    #@devide_by_sentences
    def remove_characters(self):
        unwanted_characters = r'#$%&*+/<=>@[\]^_`{|}~' # сюда можно добавить символы, которые являются не допустимыми в тексте
        list_of_uc = list(unwanted_characters)
        str1 = str(self)
        for i in str1:
            if i in list_of_uc:
                str1 = str1.replace(i, '')
        return text(str1)

#print(text('вроде этот метод работает. \n даже с троеточием... не плохо ').upper_case())
print(text('проценты - %, скобки - []. Что-то еще.').remove_characters())
#print(text('почему бы и нет?!?... а почему да..а').upper_case())
