import random


def fight_monster(records):
    player_id_input = input("Nhập mã người chơi chiến đấu: ").strip()
    current_player = None
    for player in records:
        if player['player_id'] == player_id_input:
            current_player = player
            break
             
    if current_player is None:
        print(f"Không tìm thấy người chơi có mã '{player_id_input}'!")
        return

    current_hp = int(current_player.get('hp', 0))
    if current_hp <= 0:
        print(f"Người chơi {current_player['name']} đã hết HP ")
        return

    monsters = [
        {"name": "Bug Python", "damage": 20, "reward_gold": 100},
        {"name": "Import Error", "damage": 35, "reward_gold": 150},
        {"name": "Module Not Found", "damage": 50, "reward_gold": 250}
    ]
    
    lucky_monster = random.choice(monsters)
    monster_name = lucky_monster["name"]
    monster_damage = lucky_monster["damage"]
    monster_reward = lucky_monster["reward_gold"]
    
    print(f">> Quái vật xuất hiện: {monster_name}")

    new_hp = current_hp - monster_damage
    current_player['hp'] = new_hp if new_hp > 0 else 0  

    print(f">> {current_player['name']} bị mất {monster_damage} HP.")

    if current_player['hp'] > 0:
        current_player['gold'] = int(current_player.get('gold', 0)) + monster_reward
        print(f">> Chiến thắng! Bạn nhận được {monster_reward} vàng.")
        print(f">> HP còn lại: {current_player['hp']}")
    else:
        print(f">> Bạn đã bị {monster_name} hạ gục.")
        print(f">> HP còn lại: 0 (Bạn không nhận được vàng).")