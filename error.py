import json, re, csv

try:
    with open("logs.json") as jsonFile:
        logs_py = json.load(jsonFile)
        # print(logs_py[0]['level'])
        error_logs = []
        # error_logs_num = 0
        for log in logs_py:
            pattern = r"ERROR"
            match = re.search(pattern,log['level'],re.IGNORECASE)
            if match:
                error_logs.append(log)
        #         error_logs_num += 1
        # print(error_logs_num)
        try:
            with open("error_logs.csv",'w',newline='') as csvFile:
                writer = csv.writer(csvFile)
                headers = ['timestamp','level','message']
                writer.writerow(headers)
                for log in error_logs:
                    templist = [log[header] for header in headers]
                    writer.writerow(templist)
                    templist.clear()
        except:
            print("Error occured")
except FileNotFoundError:
    print("Error occured: File not found")