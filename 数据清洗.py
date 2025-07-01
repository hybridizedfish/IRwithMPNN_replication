import pandas as pd
import re

# 定义允许的原子列表
ALLOWED_ATOMS = {'C', 'H', 'O', 'N', 'Si', 'P', 'S', 'F', 'Cl', 'Br', 'I'}

def clean_smiles(smiles):
    # 获取SMILES字符串中出现的所有原子
    atoms = re.findall(r'[A-Z][a-z]?', smiles)
    # 检查是否有不在允许列表中的原子
    for atom in atoms:
        if atom not in ALLOWED_ATOMS:
            return False
    return True

def clean_data(file_path, output_file, smiles_file):
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)
        
        # 检查并处理SMILES表达式为NAN的行
        df = df.dropna(subset=[df.columns[0]])
        
        # 处理光谱数据中有0值的行
        df = df.loc[~(df.iloc[:, 1:] == 0).any(axis=1)]
        
        # 检查SMILES表达式是否含有不允许的原子
        valid_smiles = df[df.columns[0]].apply(lambda x: clean_smiles(x) if pd.notna(x) else False)
        df = df[valid_smiles]
        
        # 保存清洗后的数据到新文件
        df.to_csv(output_file, index=False)
        
        # 保存仅包含SMILES表达式的文件
        df[[df.columns[0]]].to_csv(smiles_file, index=False)
        
        print(f"数据清洗完成，已保存到 {output_file} 和 {smiles_file}")
        
    except Exception as e:
        print(f"处理过程中出现错误: {e}")

if __name__ == '__main__':
    clean_data('IR_database_full.csv', '清洗后的数据.csv', '仅SMILES.csv')