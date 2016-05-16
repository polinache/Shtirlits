class Caesar:
    global alphabet
    alphabet = "ЯяЮюЭэЬьЫыЪъЩщШшЧчЦцХхФфУуТтСсРрПпОоНнМмЛлКкЙйИиЗзЖжЁёЕеДдГгВвБбАа"
    global key
    key = -38

    def __init__(self):
        self.alphabet = alphabet
        lowercase_code = {self.alphabet[i]:self.alphabet[(i+key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[(i+key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}


    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])


    def decode(self, line):
        self.line = line
        translated = ''
        for symbol in self.line:
            if symbol in alphabet:
                num = alphabet.find(symbol)

                num = num +key
                if num >= len(alphabet):
                    num = num - len(alphabet)
                elif num < 0:
                    num = num + len(alphabet)
                translated = translated + alphabet[num]
        return translated
cipher = Caesar()
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()