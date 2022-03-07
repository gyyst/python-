import xlwt

workbook=xlwt.Workbook(encoding="utf-8")#创建workbook对象
worksheet=workbook.add_sheet('sheet1')
for i in range(1,10):
    for j in range(i,10):
        worksheet.write(j-1,i-1,str(i)+"×"+str(j)+"="+str(i*j)) #第一行参数‘行’，第二参数‘列’，第三参数内容
workbook.save('student.xls')