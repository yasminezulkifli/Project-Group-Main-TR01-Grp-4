#imports each python file as modules 
import api, cash_on_hand, overheads, profit_loss, csv_reader

name_list_array = ["cash-on-hand-usd.csv", "overheads-day-90.csv", "profit-and-loss-usd.csv"]
name_list_array_dict = dict()


def execute_api():
    print("-> Entering: execute_api()")
    json_response = api.get_forex()
    if json_response == 0:
        print("-> API RESULT: Error with request. JSON response received but ! 200 OK")
        exit()
    elif json_response == -1:
        print("-> API RESULT: Error with request. JSON response exception caught.")
        exit()
    else:
        print("-> API RESULT: STATUS 200 OK")
        return json_response


def usd_to_sgd(forex_rate, value_to_convert):
    return float(value_to_convert) * float(forex_rate)


def output_txt(forex, highest_overhead_cat, highest_overhead, coh_empty_flag, coh_dip_list, pl_empty_flag, pl_dip_list):
    with open('summary_report.txt', 'w') as f:
        f.write("[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD" + str("{:.5f}".format(float(forex))) + "\n")
        f.write("[HIGHEST OVERHEADS] " +
                str(highest_overhead_cat).upper() + ": SGD" + str("{:.1f}".format(highest_overhead)) + "\n")
        if coh_empty_flag:
            f.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
        else:
            for item in coh_dip_list:
                for key, value in item.items():
                    f.write("[CASH DEFICIT] DAY: " + str(float(key)) + ", AMOUNT: SGD" +
                            str("{:.1f}".format(value)) + "\n")
        if pl_empty_flag:
            f.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
        else:
            for item in pl_dip_list:
                for key, value in item.items():
                    f.write("[PROFIT DEFICIT] DAY: " + str(float(key)) + ", AMOUNT: SGD" +
                            str("{:.0f}".format(value)) + "\n")


print("MAIN EXECUTE")

# Get FOREX
print("Get FOREX data")
json_response = execute_api()
print("-> API RESULTS CONVERTED TYPE: {0}".format(type(json_response)))

# Establish file path
print("Establish file path")
print("-> GET FILE PATH TO CSV REPORTS:\n")
for item in name_list_array:
    path_to_text_files_extension = csv_reader.get_path_to_project_folder(item)
    list_of_dictionaries = csv_reader.read_in_text_file(path_to_text_files_extension)
    name_list_array_dict[item] = list_of_dictionaries

print("-> PRINTING READ IN DATA FROM CSV FILES:\n")
for key, value in name_list_array_dict.items():
    print("{0} | {1}".format(key, value))

maxPricedItem_usd = overheads.get_highest_overhead(name_list_array_dict["overheads-day-90.csv"])
maxPricedItem_sgd = \
    usd_to_sgd(json_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"], maxPricedItem_usd["Overheads"])
print("-> OVERHEAD: [USD] = {0} | [SGD] = {1}".format(maxPricedItem_usd["Overheads"], maxPricedItem_sgd))

# Determine cash on hand dip between days
print("Determine COH dip between days")
coh_dip_list = cash_on_hand.calculate_dip(name_list_array_dict["cash-on-hand-usd.csv"])
print("\n-> COH DIP RESULTS: [SGD]:")
for result in coh_dip_list:
    for key, value in result.items():
        new_value = usd_to_sgd(json_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"], value)
        result[key] = new_value
        print("DAY: {0} | AMT: {1}".format(key, new_value))

print("\n-> LENGTH OF LIST coh_dip_list: {0}".format(len(coh_dip_list)))
coh_empty_flag = False
if len(coh_dip_list) == 0:
    coh_empty_flag = True
print("-> EMPTY STATE OF LIST coh_dip_list: {0}".format(coh_empty_flag))

# Determine profit and loss dip between days
print("Determine PL dip between days")
pl_dip_list = profit_loss.calculate_pl(name_list_array_dict["profit-and-loss-usd.csv"])
print("\n-> PL DIP RESULTS: [SGD]:")
for result in pl_dip_list:
    for key, value in result.items():
        new_value = usd_to_sgd(json_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"], value)
        result[key] = new_value
        print("DAY: {0} | AMT: {1}".format(key, new_value))

print("\n-> LENGTH OF LIST pl_dip_list: {0}".format(len(pl_dip_list)))
pl_empty_flag = False
if len(pl_dip_list) == 0:
    pl_empty_flag = True
print("-> EMPTY STATE OF LIST pl_dip_list: {0}".format(pl_empty_flag))


# Output all data to txt file
print("Output to text file")
with open("summary_report.txt","w") as file: #CREATE TXT
     file.write(json_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"],
           maxPricedItem_usd["Category"],
           maxPricedItem_sgd,
           coh_empty_flag,
           coh_dip_list,
           pl_empty_flag,
           pl_dip_list)

file.close()