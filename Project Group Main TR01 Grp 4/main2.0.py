
def usd_to_sgd(forex_rate, value_to_convert):
    return float(value_to_convert) * float(forex_rate)

def output_txt(forex, highest_overhead_cat, highest_overhead, coh_empty_flag, coh_dip_list, pl_empty_flag, pl_dip_list):
    output_write = Path.cwd()/"summary_report.txt"
    output_write.touch()

    with open('summary_report.txt', 'w') as file: 
        file.write("[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD" + str("{:.5f}".format(float(forex))) + "\n")
        file.write("[HIGHEST OVERHEADS] " +
                str(highest_overhead_cat).upper() + ": SGD" + str("{:.1f}".format(highest_overhead)) + "\n")
        if coh_empty_flag:
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
        else:
            for item in coh_dip_list:
                for key, value in item.items():
                    file.write("[CASH DEFICIT] DAY: " + str(float(key)) + ", AMOUNT: SGD" +
                            str("{:.1f}".format(value)) + "\n")
        if pl_empty_flag:
            file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
        else:
            for item in pl_dip_list:
                for key, value in item.items():
                    f.write("[PROFIT DEFICIT] DAY: " + str(float(key)) + ", AMOUNT: SGD" +
                            str("{:.0f}".format(value)) + "\n")



print("MAIN EXECUTE")

with open("ti.txt","w") as file:
    file.write(json_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

file.close ()