import xlrd


class ExcelRead:
	def __init__(self, excel_path=None, encoding='utf-8', index=0):
		self.data = xlrd.open_workbook(excel_path)  # 获取文本对象
		self.table = self.data.sheets()[index]     # 根据index获取某个sheet
		self.rows = self.table.nrows   # 获取当前sheet页面的总行数,把每一行数据作为list放到 list
		self.list = []

	def get_data(self):
		global col
		result = []
		for i in range(1):
			col = self.table.row_values(i)  # 获取第一行的数据
		for j in range(1, self.rows):
			self.list.append(self.table.row_values(j))
		return self.list


bang_1 = ExcelRead(r"C:\Users\qiook\Desktop\Demo_text\Case\1.xlsx").get_data()
bang_2 = ExcelRead(r"C:\Users\qiook\Desktop\Demo_text\Case\2.xlsx").get_data()
sum = ExcelRead(r"C:\Users\qiook\Desktop\Demo_text\Case\sum.xlsx").get_data()
cz = {}
for i in bang_1:
	for j in bang_2:
		if j[0] == i[0]:
			cz[i[0]] = int(j[1]) + int(i[1])
for i in sum:
	try:
		if cz[i[0]] != int(i[1]):
			print(i[0] , i[1])

	except:
		pass