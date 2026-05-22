accessibility. You can choose to enable a more compact line height from the view settings menu.

‎Calculator .py‎
+18
Lines changed: 18 additions & 0 deletions
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,18 @@
def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"
# --- How to use it ---
print(calculate(10, '+', 5))  
print(calculate(20, '*', 3)) 
print(calculate(8, '/', 0))   
