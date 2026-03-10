def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_count = 0
    n = len(s)

    # 枚举所有长度为 k 的子串的起始索引
    for i in range(n - k + 1):
        current_count = 0
        # 统计当前子串中的元音数量
        for j in range(i, i + k):
            if s[j] in vowels:
                current_count += 1
        # 更新最大元音数
        max_count = max(max_count, current_count)

    return max_count
# 下面是测试代码，用来调用函数看结果
if __name__ == "__main__":
    # 对应题目里的示例1，预期输出3
    s1 = "abciiidef"
    k1 = 3
    print("示例1 运行结果:", maxVowels(s1, k1))

    # 对应示例2，预期输出2
    s2 = "aeiou"
    k2 = 2
    print("示例2 运行结果:", maxVowels(s2, k2))

    # 对应示例3，预期输出2
    s3 = "leetcode"
    k3 = 3
    print("示例3 运行结果:", maxVowels(s3, k3))