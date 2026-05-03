from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QPushButton, QGridLayout, QVBoxLayout)
from PyQt5.QtCore import Qt
from collections import deque
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(500, 200, 400, 600)
        self.expression = deque()
        self.UI()

    def UI(self):
        self.central_widget = QWidget()
        self.central_widget.setObjectName("BG")
        self.central_widget.setStyleSheet("#BG { background: #203a43; }")
        self.setCentralWidget(self.central_widget)
        
        self.window_layout = QGridLayout(self.central_widget)
        self.master_container = QWidget()
        self.master_container.setFixedSize(380, 550)
        self.master_container.setStyleSheet("background: white; border-radius: 25px;")
        
        self.master_layout = QVBoxLayout(self.master_container)
        self.master_layout.setContentsMargins(0, 0, 0, 0)

        self.top_container = QWidget()
        self.top_container.setFixedHeight(120)
        self.top_container.setStyleSheet("background: #2c3e50; border-top-left-radius: 25px; border-top-right-radius: 25px;")
        top_layout = QVBoxLayout(self.top_container)
        
        self.expression_label = QLabel("")
        self.expression_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.expression_label.setStyleSheet("color: white; font-size: 28px; font-weight: bold;")
        
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.result_label.setStyleSheet("color: #bdc3c7; font-size: 18px;")

        top_layout.addWidget(self.expression_label)
        top_layout.addWidget(self.result_label)
        self.master_layout.addWidget(self.top_container)

        self.bottom_section = QWidget()
        self.grid_layout = QGridLayout(self.bottom_section)
        
        btns = ['AC','()','%','/','7','8','9','*','4','5','6','-','1','2','3','+','0','.','X','=']
        for i in range(5):
            for j in range(4):
                text = btns[i*4+j]
                btn = QPushButton(text)
                btn.setFixedSize(70, 60)
                btn.setStyleSheet("QPushButton { background: #f8f9fa; border-radius: 10px; font-size: 18px; }")
                btn.clicked.connect(self.click_registered)
                self.grid_layout.addWidget(btn, i, j)

        self.master_layout.addWidget(self.bottom_section)
        self.window_layout.addWidget(self.master_container, 1, 1)

    def click_registered(self):
        btn = self.sender()
        val = btn.text()

        if val == 'AC':
            self.expression.clear()
        elif val == 'X':
            if self.expression: self.expression.pop()
        elif val == '=':
            self.evaluate(True)
            return
        elif val == '()':
            val = self.handle_brackets()
            self.expression.append(val)
        else:
            self.expression.append(val)

        self.update_ui_and_calc()

    def handle_brackets(self):
        open_count = list(self.expression).count('(')
        close_count = list(self.expression).count(')')
        if not self.expression or self.expression[-1] == '(':
            return '('
        if open_count > close_count:
            if self.expression[-1].isdigit() or self.expression[-1] == ')':
                return ')'
        return '('

    def update_ui_and_calc(self):
        self.expression_label.setText("".join(list(self.expression)))
        self.evaluate(False)

    def evaluate(self, is_final):
        if not self.expression:
            self.result_label.setText("")
            return
        
        try:
            tokens = self.tokenize()
            postfix = self.infix_to_postfix(tokens)
            result = self.calculate_postfix(postfix)
            
            res_str = f"{result:g}" # Formats number nicely (removes .0)
            
            if is_final:
                self.expression.clear()
                for char in res_str: self.expression.append(char)
                self.expression_label.setText(res_str)
                self.result_label.setText("")
            else:
                self.result_label.setText(res_str)
        except:
            if is_final: self.result_label.setText("Error")

    def tokenize(self):
        raw_chars = list(self.expression)
        tokens = []
        i = 0
        
        while i < len(raw_chars):
            if raw_chars[i].isdigit() or raw_chars[i] == '.':
                num_str = ""
                while i < len(raw_chars) and (raw_chars[i].isdigit() or raw_chars[i] == '.'):
                    num_str += raw_chars[i]
                    i += 1
                tokens.append(float(num_str))
            else:
                tokens.append(raw_chars[i])
                i += 1
        
        return self.inject_multiplication(tokens)

    # for things like 7/5(4-5)15.....to 7/5*(4-5)*15
    def inject_multiplication(self, tokens):
        final = []
        for i in range(len(tokens)):
            curr = tokens[i]
            if i > 0:
                prev = tokens[i-1]
                # earlier number....current ( 
                if curr == '(' and isinstance(prev, float):
                    final.append('*')
                # earlier ) ....current )
                elif isinstance(curr, float) and prev == ')':
                    final.append('*')
            final.append(curr)
        return final

    def infix_to_postfix(self, tokens):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
        output = []
        stack = []
        for t in tokens:
            if isinstance(t, float):
                output.append(t)
            elif t == '(':
                stack.append(t)
            elif t == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and prec.get(stack[-1], 0) >= prec.get(t, 0):
                    output.append(stack.pop())
                stack.append(t)
        while stack:
            output.append(stack.pop())
        return output

    def calculate_postfix(self, postfix):
        stack = []
        for t in postfix:
            if isinstance(t, float):
                stack.append(t)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == '+': stack.append(num1 + num2)
                elif t == '-': stack.append(num1 - num2)
                elif t == '*': stack.append(num1 * num2)
                elif t == '/': stack.append(num1 / num2)
                elif t == '%': stack.append(num1 % num2)
        return stack[0]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = MainWindow()
    calc.show()
    sys.exit(app.exec_())
