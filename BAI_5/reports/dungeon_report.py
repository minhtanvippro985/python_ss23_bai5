def display_people_bylist(list_here):
    if len(list_here) == 0:
        print("Danh sách người chơi hiện đang trống")
    else:
        print("------ DANH SÁCH NGƯỜI CHƠI --------")
        for index , player in enumerate(list_here , start=0):
            if player['hp'] <=0:
                status = "Gục"
            elif player['hp'] >= 1 and player['hp'] < 50:
                status = "Nguy hiểm"
            elif player['hp'] >= 50 and player['hp'] < 100:
                status = "Ổn định"
            else:
                status = "Sung sức"
            print(f"{index + 1} Mã {player['player_id']} |Tên : {player['name']} | HP :  {player['hp']} | MANA : {player['mana']} | GOLD : {player['gold']} |Level : {player['level']} |Trạng thái : {status}")

def show_leaderboard(records):
    if len(records) == 0:
        print("Danh sách người chơi trống, không thể lập bảng xếp hạng!")
        return

    sorted_records = sorted(
        records,
        key=lambda player: (
            int(player['level']), 
            int(player['gold']), 
            int(player['hp'])
        ),
        reverse=True
    )

    print("--- BẢNG XẾP HẠNG NGƯỜI CHƠI ---")
    for index, player in enumerate(sorted_records, start=1):
        print(f"{index}. {player['name']} | Level: {player['level']} | Gold: {player['gold']} | HP: {player['hp']}")
    print("--------------------------------")