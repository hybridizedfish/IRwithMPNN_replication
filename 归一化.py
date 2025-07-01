import pandas as pd

def normalize_spectra(file_path, output_file):
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)
        
        # 获取SMILES列
        smiles_col = df.iloc[:, 0]
        
        # 获取光谱数据部分
        spectra_data = df.iloc[:, 1:]
        
        # 对每一行进行归一化，使每行的和为1
        # 首先计算每行的总和
        row_sums = spectra_data.sum(axis=1)
        
        # 避免除以零的情况，将总和为0的行设为NaN
        row_sums[row_sums == 0] = float('nan')
        
        # 归一化操作
        normalized_data = spectra_data.div(row_sums, axis=0)
        
        # 将SMILES列和归一化的光谱数据合并
        normalized_df = pd.concat([smiles_col, normalized_data], axis=1)
        
        # 保存归一化后的数据到新文件
        normalized_df.to_csv(output_file, index=False)
        
        print(f"数据归一化完成，已保存到 {output_file}")
        
    except Exception as e:
        print(f"处理过程中出现错误: {e}")

if __name__ == '__main__':
    normalize_spectra('清洗后的数据.csv', '归一化后的数据.csv')