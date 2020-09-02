from Util.handle_excel import HandExcel
try:
	print(HandExcel(r"\Case\1.xlsx").load_excel())
except EOFError as e:
	print(123)
