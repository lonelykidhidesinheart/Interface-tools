from Util.handle_excel import HandExcel

handle = HandExcel()
class RunMain:
    def run_case(self):
        rows = handle.get_rows()

        for i in range(rows):
            print(i)
            data = handle.get_rows_value(i+2)
            print(data)


if __name__ == "__main__":
    run = RunMain()
    run.run_case()
