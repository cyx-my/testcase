import json

# 打开并加载 JSON 文件
with open('duolinguo_cases.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 要提取的 case ID
target_case_id = 'case3'

# 查找目标 case
for case in data['cases']:
    if case['case_id'] == target_case_id:
        for i, step in enumerate(case['steps'], start=1):
            print(f"Step {i}:")
            print(f"  State : {step['state']}")
            print(f"  Action: {step['action']}\n")
        break
