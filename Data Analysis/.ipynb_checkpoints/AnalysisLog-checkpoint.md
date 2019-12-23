#####Data Preprocessing


#\#Suning Product: 340
#\#HKTVMall Product: 1350
#\#Suning Comments: 49162 (242)
#\#HKTVMall Commments: 287

1. Price

-> hktvmall cannot find transactions.
-> But Suning can imply by # of comments.

#成交金额
  - how to determine how many they bought?


#订单数量
  - suning: # of comments
  - hktvmall: unknown
  - 



#销售额 = (流量（UV）* 转化率（CR） * 客单价)
#价格区间 - 散点图 饼图

2. Product Variety

laptop - how to differentiate variety?

Combination
  - type  
    - brand
      - model type


#Top 100销量图片
  - Class - high, med, low
  - Brand compare
      1. 评分
      2. 成交量 -> 成交额
      3. 

3. Uniqueness
  - 

4. Customer Sentiment
  - filter nil comments
  - Sentiment Analysis
  - word cloud for most bought product
  - Rates

#词频分析

#时间


平台:


Seller:


Customer:



- Recency – How recently did the customer purchase?
- Frequency – How often do they purchase?
- Monetary Value – How much do they spend?

- match users with products
  - Products with buying records
  - Products without

- Products Info - Computers and tablets
  - Most bought products
  - product classification
  - sort by Brands
    - tablets ? lt ? moobile phone
      - 


- Comments Analysis

1. 用户打分 - 平均 中位
2. 价格分布散点 
3. 用户评价 词云





####current algorithm for check similarities in item name:

###token_sort_ratio()

- threshold = 80


- HKTVMall Grouping: -> Variety 





## PPT
- 1. suning & hktvmall 价格分布box plot
- 2. regression 分析对价格的影响因素
- 3. title, labels, axis-name写好
- 4. 大目标：如何提高销量
     - 4.1 小目标：
       - 4.1.1 顾客的消费特点（比较两家店的正态分布）
       - 4.1.2 两家店的定位（用box plot来看）
- 5. 情感分析：评分、评论分析（NLP）
- 6. 商品规格爬虫