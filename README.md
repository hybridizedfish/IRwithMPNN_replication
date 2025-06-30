# 红外光谱预测结果复现

这是厦门大学 **《人工智能化学分析》** 课程作业

由于算力远远不够，所以仅在一个很小型的数据集上进行了复现，是原文的mini/air/青春版

> 原文链接：[Predicting Infrared Spectra with Message Passing Neural Networks](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00055)

## 1.数据集
- NIST
- PNNL
- AIST
- the Coblentz Society

## 2.数据处理
### 2.1.数据清洗
### 2.2.光谱归一化
数据中存在的间隙在训练与预测时不被考虑
### 2.3.计算光谱及处理
计算的分子来自PubChem数据库，仅选择分子量<500的中性分子

## 3.网络架构
### 3.1.端到端学习架构
### 3.2. 超参数优化

## 4.模型训练
### 4.1.预训练
### 4.2.正式训练

## 5.光谱损失函数SID

## 6.光谱信息相似性度量SIS

## 7.模型评估
