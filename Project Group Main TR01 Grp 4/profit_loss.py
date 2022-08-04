def calculate_profit_and_lost(pl_dict_in_list): 
    current_netprofit_value = 0 #why 0? "Python 0 is an indicator of the format method that you need to be replaced by the format's first (index zero) parameter."
    pl_dip_list = list() 
    # creating list object 

    for variable in pl_dict_in_list:
        if float(variable['Net Porfit']) >= float(current_netprofit_value):
            current_netprofit_value = float(variable['Net Profit'])

        else: 
            diff_btw_days = float(current_netprofit_value) - float(variable['Net Profit'])
            # computing the diff in the net profit btw each day 

            pl_dip_list.append({variable['"Day"']: diff_btw_days}) 
            
            current_netprofit_value = float(variable['Net Profit'])

    print("PROFIT LOST DIP RESULTS; [USD]:")
    # IF THERE IS A DIFF 
    for result in pl_dip_list:
        for key, value in result.items():
            print("DAY {0} , AMT {1}".format(key,value))

    return pl_dip_list
