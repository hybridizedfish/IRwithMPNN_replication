import pandas as pd
import pubchempy as pcp
from tqdm import tqdm
import time

# 1. 读取 CSV（列名大写）
df = pd.read_csv('仅SMILES.csv')
smiles_list = df['SMILES'].tolist()

# 2. 批量获取 PubChem 数据（带进度条 + 错误处理 + 速率限制）
results = []

def safe_get_pubchem_batch(batch):
    """单批安全请求"""
    batch_str = "\n".join(batch)          # 关键：换行符分隔
    try:
        return pcp.get_compounds(batch_str, 'smiles')
    except pcp.PubChemHTTPError as e:
        print(f"\n批次错误: {e}")
        return []                         # 返回空列表，避免中断整体流程

# 用 tqdm 显示进度条
for i in tqdm(range(0, len(smiles_list), 100), desc="Fetching PubChem"):
    batch = smiles_list[i:i+100]
    compounds = safe_get_pubchem_batch(batch)
    for c in compounds:
        results.append({
            'SMILES': c.isomeric_smiles,
            'cid': c.cid,
            'xyz': c.to_dict(properties=['atoms'])['atoms']
        })
    time.sleep(1)   # 每批请求后暂停 1 秒，遵守 PubChem 速率限制

# 3. 保存结果
pd.DataFrame(results).to_csv('pubchem_data.csv', index=False)
print("\n✅ 所有数据获取完成！")