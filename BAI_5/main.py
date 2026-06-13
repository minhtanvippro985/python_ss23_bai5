import data.players as data_module
import reports.dungeon_report as report_module
import utils.item_utils as items_modules
import utils.battle_utils as battle_module



# dungeon_util.display_people_bylist
# print(data_module.player_records)



while True:
    choice = input("""
===== RIKKEI DUNGEON - PYTHON MODULE ADVENTURE =====
 1. Hiển thị danh sách người chơi
 2. Mở rương báu ngẫu nhiên
 3. Mua vật phẩm trong cửa hàng
 4. Chiến đấu với quái vật
 5. Xem bảng xếp hạng người chơi                    
 6. Thoát chương trình                                
====================================================
 Chọn chức năng (1-6): 
""")
    match choice:
        case "1":
            report_module.display_people_bylist(data_module.player_records)
        case "2":
            items_modules.open_treasure_chest(data_module.player_records)
        case "3":
            items_modules.buy_item(data_module.player_records)
        case "4":
            battle_module.fight_monster(data_module.player_records)
        case "5":
            report_module.show_leaderboard(data_module.player_records)
        case "6":
            print("Thoat chuong trinh")
            break
        case _:
            print("Vui long chon 1 - 6")

        