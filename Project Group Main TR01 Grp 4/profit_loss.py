def calculate_profit_and_lost(pl_dict_in_list): 
    current_netprofit_value = 0 
    pl_dip_list = list() #creating list object 

    for variable in pl_dict_in_list:
        if float(variable['Net Porfit']) >= float(current_netprofit_value):
            current_netprofit_value = float(variable['Net Profit'])

        else: 
            diff_btw_days = float(current_netprofit_value) - float(variable['Net Profit'])
            # computing the diff in the net profit btw each day 
            pl_dip_list.append({variable['"Day"']: diff_btw_days}) #from nested list
            current_netprofit_value = float(variable['Net Profit'])

    print("PROFIT LOST DIP RESULTS; [USD]:")
    for result in pl_dip_list:
        for key, value in result.items():
            print("DAY {0} , SALES {1}".format(key,value))

    return pl_dip_list

print (pl_dict_in_list)
