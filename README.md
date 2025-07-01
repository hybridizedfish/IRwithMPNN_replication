# 红外光谱预测结果复现

这是厦门大学 **《人工智能化学分析》** 课程作业

相较于原文，仅在一个较小型的数据集上进行了复现

> 原文链接：[Predicting Infrared Spectra with Message Passing Neural Networks](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00055)

## 1.数据集
选用了一个[数据集](https://github.com/hybridizedfish/IRwithMPNN_replication/blob/main/IR_database_full.csv.7z)，其中包含8654个不同分子的实验光谱。


## 2.数据处理
### 2.1.数据清洗
可供使用的实验光谱的数据需要满足以下几点：
- **实验光谱的完整性**：红外光谱连续
- **有效SMILES字符串**：红外光谱必须与有效SMILES字符串相关联
- **只能包含特定原子**：分子必须只包含以下原子：C、H、O、N、Si、P、S、F、Cl、Br和I

根据以上条件，运行[数据清洗.py](https://github.com/hybridizedfish/IRwithMPNN_replication/blob/main/%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97.py)筛选数据集中符合要求的光谱数据

最终获得6215个实验光谱，存储为[清洗后的数据.csv]()，并将第一列单独存储为[仅SMILES.csv]()，便于后续计算光谱。

### 2.2.光谱归一化
对清洗后的数据运行[归一化.py](https://github.com/hybridizedfish/IRwithMPNN_replication/blob/main/%E5%BD%92%E4%B8%80%E5%8C%96.py)，进行归一化处理。将处理好的数据存储为[归一化的数据.csv]()

### 2.3.计算光谱
~~访问pubchem太频繁被限制访问了只好~~ 采用将已有数据分割的方法模拟原文献的SMILES扩充。

将已有数据分割为4215条、2000条，并利用后2000条用GFN2-xTB方法计算光谱用于预训练。

### 2.4.峰形加宽

## 3.网络架构
### 3.1.端到端学习架构
### 3.2. 超参数优化

## 4.模型训练
### 4.1.预训练
### 4.2.正式训练

## 5.光谱损失函数SID

## 6.光谱信息相似性度量SIS

## 7.模型评估
