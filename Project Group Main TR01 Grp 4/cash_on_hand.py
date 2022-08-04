def calculate_dip(coh_dict_in_list):
    #declaring the variable to store monthly average 
    current_coh_value = 0
    coh_dip_list = list()
    #nested list
    
    for item in coh_dict_in_list:
        #for loop used to iterate through nested list. items is used as temporary holder for nested list
        if float(item['Cash On Hand']) >= float(current_coh_value):
            current_coh_value = float(item['Cash On Hand'])
        else:
            diff_between_days = float(current_coh_value) - float(item['Cash On Hand'])
            #obtaining difference between day using formula of subtracting the Cash on Hand on that day from the current Cash on hand. 
            coh_dip_list.append({item["Day"]: diff_between_days})
            current_coh_value = float(item['Cash On Hand'])

    print("COH DIP RESULTS: [USD]:")
   
    for result in coh_dip_list:
        for key, value in result.items():
            print("DAY: {0} | AMT: {1}".format(key, value))

    return coh_dip_list
