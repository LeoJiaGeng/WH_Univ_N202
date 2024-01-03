from math import sqrt

def is_sqr(x):  # 判断δ开方后是否为整数
    num1 = sqrt(x)
    return int(num1) == num1

def sqr(x):     # 将开方后的δ取整
    num2 = sqrt(x)
    return int(num2)

def sec_func(a, b, c):
    ret = {"ret_val": "未计算", "ret_data":[]}

    d = b ** 2 - a * c * 4  # 判断δ情况
    a0 = a * 2

    if d < 0:
        ret["ret_val"] = "此方程无实数根"
    elif d == 0:
        ret["ret_val"] = "此方程仅有一个实数根"
        ret["ret_data"].append("      ", -b, "\n", "X =-------", "\n", "      ", 2 * a, sep="")      # 强制转化为分数形式
    elif d > 0:
        print("此方程有两个实数根")
        if is_sqr(d):   # 当δ为能开尽时
            s1 = -b + sqr(d)
            s2 = -b - sqr(d)
            x1 = s1 / a0    # 方程的根1
            x2 = s2 / a0    # 方程的根2
            if s1 % a0 == 0 and s2 % a0 == 0:   # 两根都是整数
                ret["ret_data"].append("X1 = ", x1, "\n",)
                ret["ret_data"].append("X2 = ", x2, "\n",)
            elif s1 % a0 == 0 and s2 % a0 != 0:     # 有一根为整数
                ret["ret_data"].append("X1 = ", x1, "\n",)
                ret["ret_data"].append("      ", -b - sqrt(d), "\n", "X2 =-------", "\n", "      ", a0, "\n", sep="")
            elif s1 % a0 != 0 and s2 % a0 == 0:     # 有一根为整数
                ret["ret_data"].append("      ", -b + sqrt(d), "\n", "X1 =-------", "\n", "      ", a0, "\n", sep="")
                ret["ret_data"].append("X2 = ", x2, "\n",)
            else:       # 两根都为浮点数时
                ret["ret_data"].append("      ", -b + sqrt(d), "\n", "X1 =-------", "\n", "      ", a0, "\n", sep="")
                ret["ret_data"].append("      ", -b - sqrt(d), "\n", "X2 =-------", "\n", "      ", a0, "\n", sep="")
        else:       # 当δ为开不尽时
            ret["ret_data"].append("      ", -b, "+ √", d, "\n", "X1 =-------", "\n", "      ", a0, "\n", sep="")
            ret["ret_data"].append("      ", -b, "- √", d, "\n", "X2 =-------", "\n", "      ", a0, "\n", sep="")
    return ret

if __name__ == "__main__":
    print(sec_func(1, 5, 3))
