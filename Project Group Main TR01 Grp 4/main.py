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