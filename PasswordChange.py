# /[]ú check_password_strength ö_/[ password ~
# W1. üov/ 8ÿo+1
# W2. üov/[ÿo+1
# W3. üov/[/ÿo+1
# W4. üov/[/ÿo+1
# W5. üov/[ëÿo+1
# Þóÿ0-2Þó"", 3-4Þó"o", 5Þó""
def check_password_strength(password):
    """
    檢查給定密碼的強度。

    強密碼需符合：
        1. 至少 8 字元
        2. 至少一個大寫字母
        3. 至少一個小寫字母
        4. 至少一個數字
        5. 至少一個特殊符號 (!@#$%^&*()-_+=)

    參數：
        password (str): 欲檢查的密碼

    回傳：
        str: "Strong"（強）或 "Weak"（弱）
    """

    if len(password) < 8:
        return "Weak"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_+=" for c in password)

    if all([has_upper, has_lower, has_digit, has_special]):
        return "Strong"
    else:
        return "Weak"

def generate_strong_password(length=12):
    """
    產生一組強密碼，符合所有強度條件。

    參數：
        length (int): 密碼長度，預設 12

    回傳：
        str: 強密碼
    """
    import random
    import string
    if length < 8:
        length = 8
    # 至少一個大寫、一個小寫、一個數字、一個特殊符號
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()-_+=")
    # 剩餘隨機填充
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
    remain = [random.choice(all_chars) for _ in range(length - 4)]
    pwd_list = [upper, lower, digit, special] + remain
    random.shuffle(pwd_list)
    return ''.join(pwd_list)


if __name__ == "__main__":
    """
    主程式入口：
    1. 若有命令列參數，檢查該密碼強度。
    2. 若無參數，自動產生強密碼並顯示。
    """
    import sys
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(f"密碼強度：{check_password_strength(password)}")
    else:
        pwd = generate_strong_password()
        print(f"自動產生強密碼：{pwd}")
        print(f"密碼強度：{check_password_strength(pwd)}")