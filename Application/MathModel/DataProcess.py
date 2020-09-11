import joblib

print('Loading data...')
companies, invoice_in_data, invoice_out_data = joblib.load('data/data_predict.pkl')

# 对于每个公司，计算进项销项发票金额总和，税额总和，发票比数，发票作废率
data_after_process = []

for i in range(len(companies)):

    # 第 i 个公司的发票
    invoice_in = invoice_in_data[i]
    invoice_out = invoice_out_data[i]

    # 进项和
    sum_in_money = 0
    sum_in_tax = 0
    invalid_in = 0

    for invoice in invoice_in:
        if invoice[2] == 0:
            invalid_in += 1
        else:
            sum_in_money += float(invoice[0])
            sum_in_tax += float(invoice[1])

    # 销项和
    sum_out_money = 0
    sum_out_tax = 0
    invalid_out = 0

    for invoice in invoice_out:
        if invoice[2] == 0:
            invalid_out += 1
        else:
            sum_out_money += float(invoice[0])
            sum_out_tax += float(invoice[1])

    # 合成数据向量               进项金额总和，进项税额总和，进项作废率，进项发票比数，销项金额总和，销项税额总和，销项作废率，销项发票比数
    data_after_process.append([sum_in_money, sum_in_tax, invalid_in / len(invoice_in), len(invoice_in), sum_out_money, sum_out_tax, invalid_out / len(invoice_out), len(invoice_out)])

print(data_after_process)

# 直接保存为二进制文件
print('Saving...')
joblib.dump([companies, data_after_process], 'data/data_predict_after_process.pkl')