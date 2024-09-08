# 读取文件1和文件2中的信号名
with open('apilist.txt', 'r', encoding='utf-8') as f1, open('swrs.txt', 'r', encoding='utf-8') as f2:
    signals1 = set(line.strip().lower() for line in f1)
    signals2 = set(line.strip().lower() for line in f2)

# 找到两个文件共同的信号并记录在common.txt中
with open('common.txt', 'w', encoding='utf-8') as f_common:
    common_signals = signals1.intersection(signals2)
    for signal in common_signals:
        f_common.write(signal + '\n')
        print(f"{signal} is in common part")

# 记录不同部分的信号
with open('diff.txt', 'w', encoding='utf-8') as f_diff:
    for signal in signals2:
        if signal.lower() not in common_signals:
            f_diff.write(signal + '\n')
            print(f"{signal} is not in common part")