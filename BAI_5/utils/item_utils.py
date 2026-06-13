import random


def open_treasure_chest(records):

    player_id_input = input("Nhập mã người chơi muốn mở rương: ").strip().upper()
    
    current_player = None
    for player in records:
        if player['player_id'] == player_id_input:
            current_player = player
            break            
    if current_player is None:
        print(f"Không tìm thấy người chơi có mã '{player_id_input}'!")
        return
    if 'inventory' not in current_player:
        current_player['inventory'] = []

    rewards = ["Potion", "Iron Sword", "Magic Scroll", "100 Gold", "Mana Stone"]
    
    lucky_reward = random.choice(rewards)
    print(f"\nChúc mừng người chơi {current_player['name']} đã nhận được: {lucky_reward}!")

    if lucky_reward == "100 Gold":
        current_player['gold'] = int(current_player.get('gold', 0)) + 100
        print(f"Số vàng hiện tại của bạn: {current_player['gold']} GOLD.")
    else:
        current_player['inventory'].append(lucky_reward)
        print(f"Túi đồ hiện tại: {', '.join(current_player['inventory'])}")


def buy_item(records):
    shop_items = {
        "Potion": 50,
        "Iron Sword": 200,
        "Magic Book": 300,
        "Mana Stone": 150
    }

    print("========== CỬA HÀNG VẬT PHẨM ==========")
    for index, (item, price) in enumerate(shop_items.items(), start=1):
        print(f"{index}. {item} - Giá: {price} GOLD")
    print("=======================================")

    player_id_input = input("Nhập mã người chơi muốn mua đồ: ").strip()
    
    current_player = None
    for player in records:
        if player['player_id'] == player_id_input:
            current_player = player
            break

    if current_player is None:
        print(f"Không tìm thấy người chơi có mã '{player_id_input}'!")
        return
    if 'inventory' not in current_player:
        current_player['inventory'] = []
    item_name = input("Nhập chính xác TÊN vật phẩm muốn mua: ").strip()

    chosen_item = None
    for shop_item in shop_items:
        if shop_item.lower() == item_name.lower():
            chosen_item = shop_item
            break

    if chosen_item is None:
        print("Vật phẩm này không có trong cửa hàng!")
        return

    item_price = shop_items[chosen_item]
    player_gold = int(current_player.get('gold', 0))

    if player_gold >= item_price:
        current_player['gold'] = player_gold - item_price
        current_player['inventory'].append(chosen_item)
        
        print(f"Mua thành công {chosen_item}!")
        print(f"-> Tài khoản còn lại: {current_player['gold']} GOLD.")
        print(f"-> Túi đồ hiện tại: {', '.join(current_player['inventory'])}")
    else:
        print(f"Bạn không đủ tiền! (Cần {item_price} GOLD nhưng bạn chỉ có {player_gold} GOLD)")