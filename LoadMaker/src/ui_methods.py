# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import toSelectus

def transform(self):
       raw_txt = self.LoadText.toPlainText()
       self.LoadText.clear()
       result = toSelectus.transform(raw_txt)
       self.LoadText.setPlainText(result)


def copy(self):
    self.LoadText.selectAll()
    self.LoadText.copy()

def paste(self):
    self.LoadText.clear()
    self.LoadText.paste()
    transform(self)

def clear(self):
    self.LoadText.clear()

#    self.Transform.clicked.connect(self.transform)
#    self.Copy.clicked.connect(self.copy)
#    self.Paste.clicked.connect(self.paste)
#    self.Clear.clicked.connect(self.clear)
