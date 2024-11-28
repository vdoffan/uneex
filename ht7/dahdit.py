class morse:
    def __init__(self, param="", sequence=None):
        self.sequence = sequence or []
        self.param = param
        if not param:
            self.dot = "di"
            self.dit = "dit"
            self.dash = "dah"
            self.end_char = "."
            self.signal_delimiter = " "
            self.letter_delimiter = ", "
            self.message_end = self.end_char
        else:
            if " " in param:
                if param.endswith(" "):
                    self.end_char = " "
                words = param.strip().split()
                if len(words) == 1:
                    self.dot = self.dit = self.dash = words[0]
                elif len(words) == 2:
                    self.dot = self.dit = words[0]
                    self.dash = words[1]
                elif len(words) == 3:
                    self.dot = words[0]
                    self.dit = words[1]
                    self.dash = words[2]
                elif len(words) == 4:
                    self.dot = words[0]
                    self.dit = words[1]
                    self.dash = words[2]
                    self.end_char = words[3]
                else:
                    self.dot = self.dit = self.dash = ""
                self.end_char = self.end_char if hasattr(self, "end_char") else "."
                self.signal_delimiter = " "
                self.letter_delimiter = ", "
                self.message_end = self.end_char
            else:
                chars = list(param)
                if len(chars) == 1:
                    self.dot = self.dit = self.dash = chars[0]
                elif len(chars) == 2:
                    self.dot = self.dit = chars[0]
                    self.dash = chars[1]
                elif len(chars) == 3:
                    self.dot = chars[0]
                    self.dit = chars[1]
                    self.dash = chars[2]
                elif len(chars) == 4:
                    self.dot = chars[0]
                    self.dit = chars[1]
                    self.dash = chars[2]
                    self.end_char = chars[3]
                else:
                    self.dot = self.dit = self.dash = ""
                self.end_char = self.end_char if hasattr(self, "end_char") else ""
                self.signal_delimiter = ""
                self.letter_delimiter = " "
                self.message_end = self.end_char

    def __pos__(self):
        return morse(param=self.param, sequence=["dot"] + self.sequence)

    def __neg__(self):
        return morse(param=self.param, sequence=["dash"] + self.sequence)

    def __invert__(self):
        return morse(param=self.param, sequence=["letter_sep"] + self.sequence)

    def __str__(self):
        seq = self.sequence
        letters = []
        current_letter = []
        for signal in seq:
            if signal == "letter_sep":
                if current_letter:
                    letters.append(current_letter)
                    current_letter = []
            else:
                current_letter.append(signal)
        if current_letter:
            letters.append(current_letter)

        output_letters = []
        for letter in letters:
            signals = []
            for i, signal in enumerate(letter):
                if signal == "dot":
                    if i == len(letter) - 1:
                        signals.append(self.dit)
                    else:
                        signals.append(self.dot)
                elif signal == "dash":
                    signals.append(self.dash)
            output_letters.append(self.signal_delimiter.join(signals))
        output = self.letter_delimiter.join(output_letters)
        output += self.message_end
        return output
