#Условие:
#Дана строка, содержащая только символы '(', ')', '{', '}', '[' и ']'. Проверьте, является ли расстановка скобок в этой строке правильной.
#
#Примеры:
#python
#Copy code
#is_valid("()")              # Вернет True
#is_valid("()[]{}")          # Вернет True
#is_valid("(]")              # Вернет False
#is_valid("([)]")            # Вернет False
#is_valid("{[]}")            # Вернет True
#is_valid("{{[()()]}}")      # Вернет True

def is_valid(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False
        else:
            return False

    return not stack

print(is_valid("{}"))

