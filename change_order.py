import trade_tools as t_tool
import trade_api as t_api
import non_trade_api as n_t_api
import pandas as pd

trade_api = t_api.Trade
trade_adjust = n_t_api.Trade_adjustments
trade_tools = t_tool.Trade_tool

def read_data():
    # 读取 Excel 文件
    file_path = test_real
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"读取 Excel 文件时出错：{e}")
        exit()

    # 将 Acc_Name 列设为索引，以便将其用作字典键
    df.set_index("Acc_Name", inplace=True)

    # 准备一个字典来存储匹配结果
    accs_info = {}

    # 匹配 Accs 列表中的每个 Acc_Name，并获取其对应的 Api_key 和 Api_secret
    for acc_name in Accs:
        try:
            api_key = df.loc[acc_name, "Api_key"]
            api_secret = df.loc[acc_name, "Api_secret"]
            accs_info[acc_name] = {"Api_key": api_key, "Api_secret": api_secret}
        except KeyError:
            print(f"无法找到 Acc_Name 为 {acc_name} 的信息。")

    return accs_info

def trading_session_func(acc_name , accs_info):
    print("trading_session_fuc\n")
    trade_session = trade_api(acc_name, accs_info[acc_name]['Api_key'], accs_info[acc_name]['Api_secret'])
    # print(acc_name,accs_info['Api_key'],accs_info['Api_secret'])
    return trade_session

def check_hv_position_func(trade_session,coin_symbol):
    df_position_val = trade_session.get_position_value(coin_symbol)
    position_val = float(df_position_val.loc[0, 'total_val'])
    position_side = df_position_val.loc[0, 'side']
    if position_val > 0 or position_val != "":
        hv_position = True
    else:
        position_side = None
        hv_position = False

    return hv_position,position_side

def new_orders_func(check_orders ,position_side):
    print("new_orders_func\n")

    return [order['orderId'] for order in check_orders if (order['side'] == position_side or position_side == None ) and order["price"] == str(p) ]

def flat_orders_func(check_orders ,hv_position, position_side):

    if position_side == "Buy":
        flat_side = "Sell"
    elif position_side == "Sell":
        flat_side = "Buy"
    else:
        flat_side = None

    return [order['orderId'] for order in check_orders
            if order['side'] == flat_side
            and hv_position == True and order['stopOrderType'] =="" and order["price"] == str(p) ]

def SP_orders_func(check_orders):
    return [order['orderId'] for order in check_orders if order['stopOrderType'] == "TakeProfit"]


def SL_orders_func(check_orders):
    return [order['orderId'] for order in check_orders if order['stopOrderType'] == "StopLoss"]


def type_of_orders_cancel_func(check_orders):

    print("find_out which type of orders do u need\n")
    new_orders = new_orders_func(check_orders ,position_side)
    print(f"new_orders:{new_orders}")
    flat_orders = flat_orders_func(check_orders ,hv_position, position_side)
    print(f"flat_orders:{flat_orders}")
    SP_orders = SP_orders_func(check_orders)
    print(f"SP_orders:{SP_orders}")
    SL_orders = SL_orders_func(check_orders)
    print(f"SL_orders:{SL_orders}")

    if order_type == "add_order":
        order_id = new_orders
    elif order_type == "flat_order":
        order_id = flat_orders
    elif order_type == "SP":
        order_id = SP_orders
    elif order_type == "SL":
        order_id = SL_orders

    return order_id


def change_orders_func(order_id):
    print("cancel_orders_func\n")
    for order_ids in order_id:
        print(f"order_ids:{order_ids}")
        trade_session.change_order(coin_symbol, order_type ,change_p ,order_ids)


if __name__ == "__main__":

    from input import change_orders

    test_real, coin_symbol, order_type, \
    p, change_p, Accs = change_orders().execute_all()
    accs_info = read_data()

    print(f"accs_info:{accs_info}")
    for acc_name, info in accs_info.items():
        trade_session = trading_session_func(acc_name, accs_info)

        check_orders = trade_session.check_orders(coin_symbol)
        print(f"check_orders:{check_orders}")

        hv_position, position_side = check_hv_position_func(trade_session, coin_symbol)
        print(f"hv_position:{hv_position},position_side:{position_side}")
        order_id = type_of_orders_cancel_func(check_orders)
        print(f"order_id:{order_id}")
        change_orders_func(order_id)