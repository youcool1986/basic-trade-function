#qty =  0 to trade test
def test_m_small():#1
    """
    Buy: Done!!!
    Flat: Done!!!
    Big_bit: Done!!!
    small_bit: Done!!!
    med_bit: Done!!!
    """

    flat_order = True
    randomize = False
    split_no = 1
    no_time_idex = 10
    time_str = "sec"
    coin_symbol = "XCNUSDT"
    order_type_input = "Market"
    limited_price = 0.0011142442342
    capital_ratio = 20
    side_input = "Buy"
    Accs = ['testnet']
    test_real_input = "New_Testnet_Api_Acc_name.xlsx"
    accs_info = {'testnet': {'Api_key': 'Spm9ezsVIdKTpVuFc1', 'Api_secret': '24jbLNUNsc2tpLUHarItASOvcMvEmeYuRORp'}}

    return flat_order,randomize,split_no ,no_time_idex,time_str,coin_symbol, order_type_input,limited_price,capital_ratio,side_input,Accs,test_real_input,accs_info

def test_l_small():#2

    """
    Buy: Done!!!
    Flat: Done!!!
    Big_bit: Done!!
    small_bit: Done!!!
    med_bit: Done!!!
    """
    flat_order = True
    randomize = False
    split_no = 1
    no_time_idex = 10
    time_str = "sec"
    coin_symbol = "XCNUSDT"
    order_type_input = "Limit"
    limited_price = 0.0011142442342
    capital_ratio = 20
    side_input = "Buy"
    Accs = ['testnet']
    test_real_input = "New_Testnet_Api_Acc_name.xlsx"

    accs_info = {'testnet': {'Api_key': 'Spm9ezsVIdKTpVuFc1', 'Api_secret': '24jbLNUNsc2tpLUHarItASOvcMvEmeYuRORp'}}

    return flat_order,randomize,split_no ,no_time_idex,time_str,coin_symbol, order_type_input,limited_price,capital_ratio,side_input,Accs,test_real_input,accs_info


def test_m_big():#3
    """
     Buy: Done!!!
     Flat: Done!!!
     Big_bit: Done!!!
     small_bit: Done!!!
     med_bit: Done!!!
    """

    flat_order = True
    randomize = False
    split_no = 1
    no_time_idex = 10
    time_str = "sec"
    coin_symbol = "BTCUSDT"
    order_type_input = "Market"
    limited_price = 57837.2768773
    capital_ratio = 100
    side_input = "Buy"
    Accs = ['testnet']
    test_real_input = "New_Testnet_Api_Acc_name.xlsx"

    accs_info = {'testnet': {'Api_key': 'Spm9ezsVIdKTpVuFc1', 'Api_secret': '24jbLNUNsc2tpLUHarItASOvcMvEmeYuRORp'}}

    return flat_order, randomize,split_no ,no_time_idex,time_str,coin_symbol, order_type_input,limited_price,capital_ratio,side_input,Accs,test_real_input,accs_info

def test_l_big():#4
    """
     Buy: Done!!!
     Flat: Done!!!
     Big_bit: Done!!!
     small_bit: Done!!!
     med_bit: Done!!!
    """
    flat_order = False
    randomize = False
    split_no = 1
    no_time_idex = 10
    time_str = "sec"
    coin_symbol = "BTCUSDT"
    order_type_input = "Limit"
    limited_price = 57837.2768773
    capital_ratio = 100
    side_input = "Buy"
    Accs = ['testnet']
    test_real_input = "New_Testnet_Api_Acc_name.xlsx"

    accs_info = {'testnet': {'Api_key': 'Spm9ezsVIdKTpVuFc1', 'Api_secret': '24jbLNUNsc2tpLUHarItASOvcMvEmeYuRORp'}}

    return flat_order,randomize,split_no ,no_time_idex,time_str,coin_symbol, order_type_input,limited_price,capital_ratio,side_input,Accs,test_real_input,accs_info

def test_r_l_small():#5
    """
     Buy: Done!!!
     Flat: Done!!!
     Big_bit: Done!!!
     small_bit: Done!!!
     med_bit: Done!!!
     p:Done!!!
    """

    flat_order = False
    randomize = True
    split_no = 10
    no_time_idex = 10
    time_str = "sec"
    coin_symbol = "XCNUSDT"
    order_type_input = "Limit"
    limited_price = 0.0011142442342
    capital_ratio = 20
    side_input = "Buy"
    Accs = ['testnet']
    test_real_input = "New_Testnet_Api_Acc_name.xlsx"

    accs_info = {'testnet': {'Api_key': 'Spm9ezsVIdKTpVuFc1', 'Api_secret': '24jbLNUNsc2tpLUHarItASOvcMvEmeYuRORp'}}

    return flat_order,randomize,split_no ,no_time_idex,time_str,coin_symbol, order_type_input,limited_price,capital_ratio,side_input,Accs,test_real_input,accs_info

def test_r_m_small():#6
    """
     Buy: Done!!!
     Flat: Done!!!
     Big_bit: Done!!!
     small_bit: Done!!!
     med_bit: Done!!!
     p:Done!!!
    """

    flat_order = False
    randomize = True
    split_no = 10
    no_time_idex = 10
    time_str = "sec"
    coin_symbol = "XCNUSDT"
    order_type_input = "Market"
    limited_price = 0.0011142442342
    capital_ratio = 20
    side_input = "Buy"
    Accs = ['testnet']
    test_real_input = "New_Testnet_Api_Acc_name.xlsx"

    accs_info = {'testnet': {'Api_key': 'Spm9ezsVIdKTpVuFc1', 'Api_secret': '24jbLNUNsc2tpLUHarItASOvcMvEmeYuRORp'}}

    return flat_order,randomize,split_no ,no_time_idex,time_str,coin_symbol, order_type_input,limited_price,capital_ratio,side_input,Accs,test_real_input,accs_info

def test_r_l_big():#7

    """
    Buy: Done!!!
    Flat: Done!!!
    Big_bit: Done!!!
    small_bit: Done!!!
    med_bit: Done!!!
    p:Done!!!
    """

    flat_order = False
    randomize = True
    split_no = 10
    no_time_idex = 10
    time_str = "sec"
    coin_symbol = "BTCUSDT"
    order_type_input = "Limit"
    limited_price = 57837.2768773
    capital_ratio = 100
    side_input = "Buy"
    Accs = ['testnet']
    test_real_input = "New_Testnet_Api_Acc_name.xlsx"

    accs_info = {'testnet': {'Api_key': 'Spm9ezsVIdKTpVuFc1', 'Api_secret': '24jbLNUNsc2tpLUHarItASOvcMvEmeYuRORp'}}

    return flat_order,randomize,split_no ,no_time_idex,time_str,coin_symbol, order_type_input,limited_price,capital_ratio,side_input,Accs,test_real_input,accs_info

def test_r_m_big():#8

    """
    Buy: Done!!!
    Flat: Done!!!
    Big_bit: Done!!!
    small_bit: Done!!!
    med_bit: Done!!!
    p:Done!!!
    """
    flat_order = True
    randomize = True
    split_no = 10
    no_time_idex = 10
    time_str = "sec"
    coin_symbol = "BTCUSDT"
    order_type_input = "Market"
    limited_price = 57837.2768773
    capital_ratio = 100
    side_input = "Buy"
    Accs = ['testnet']
    test_real_input = "New_Testnet_Api_Acc_name.xlsx"

    accs_info = {'testnet': {'Api_key': 'Spm9ezsVIdKTpVuFc1', 'Api_secret': '24jbLNUNsc2tpLUHarItASOvcMvEmeYuRORp'}}

    return flat_order,randomize,split_no ,no_time_idex,time_str,coin_symbol, order_type_input,limited_price,capital_ratio,side_input,Accs,test_real_input,accs_info
