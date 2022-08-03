def calculate_dip(coh_dict_in_list):
    current_coh_value = 0
    coh_dip_list = list()

    for item in coh_dict_in_list:
        if float(item['Cash On Hand']) >= float(current_coh_value):
            current_coh_value = float(item['Cash On Hand'])
        else:
            diff_between_days = float(current_coh_value) - float(item['Cash On Hand'])
            coh_dip_list.append({item["Day"]: diff_between_days})
            current_coh_value = float(item['Cash On Hand'])

    print("COH DIP RESULTS: [USD]:")
    #new line 
    for result in coh_dip_list:
        for key, value in result.items():
            print("DAY: {0} | AMT: {1}".format(key, value))

    return coh_dip_list
