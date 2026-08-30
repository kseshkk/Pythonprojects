from models.place import Place
from api.places_api import *

def get_text_for_screen5_walk_planning_step3(places: list[Place]):
    
    if len(places) == 0:
        return (
            "ни одного места не найдено."
        )

    output_text = "Планируем прогулку\n3.выберите место прогулки:\n"

    for i in range(0, len(places)):
        output_text += f"{i+1}. {places[i].name}\n"


    return output_text