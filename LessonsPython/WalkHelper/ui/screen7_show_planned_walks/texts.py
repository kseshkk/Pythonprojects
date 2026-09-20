def get_text_for_screen8_show_walk_info(walk):
    return f"Информация о вашей прогулке!\n\nгород: {walk.city_name}\n место: {walk.place_name}\n дата: {walk.walk_date}\nстатус: {walk.get_status()}"
