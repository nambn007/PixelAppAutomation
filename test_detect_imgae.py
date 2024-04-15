from PIL import Image
import pyscreeze


def get_positions(screen_shot_path: str, reg_path: str):
    # Mở file ảnh lớn và ảnh nhỏ
    big = Image.open(screen_shot_path)
    small = Image.open(reg_path)

    # Sử dụng pyscreeze để tìm tất cả vị trí của ảnh nhỏ trong ảnh lớn
    locations = pyscreeze.locateAll(small, big)

    # Khởi tạo một danh sách để lưu trữ tất cả các vị trí
    all_positions = []
    # Lặp qua tất cả các vị trí tìm thấy và thêm chúng vào danh sách
    for locate in locations:
        x = locate[0]
        y = locate[1]
        print("click at ", x, y)
        all_positions.append({"x":x,"y":y})
    # print(all_positions)
    return all_positions

if __name__ == '__main__':
    import json

    data = """
    Egg    itm_egg
    Seltsam Egg    itm_seltsamEgg
    Eggsplosive    itm_eggsplosive
    Queen Bee    itm_queenbee
    Wax    itm_beeswax
    Honey    itm_honey
    Heartbeet    itm_heartbeetFruit
    Java Bean    itm_coffeefruit
    Popberry    itm_popberryFruit
    Bluzzleberry Swirl Cotton Candy    itm_cottoncandyFruit_mixed
    Razzleberry Cotton Candy    itm_cottoncandyFruit_pink
    Bluzberry Cotton Candy    itm_cottoncandyFruit_blue
    Orange Grumpkin    itm_grumpFruit
    Butterberry    itm_butterberry
    4 Leaf Clover    itm_clover4LeafFruit
    Clover    itm_cloverFruit
    Grainbow    itm_grainbow
    Grumpkin    itm_grumpkinFruit
    Watermint    itm_wintermintFruit
    Scarrot    itm_scarrotFruit
    Astracactus    itm_tenta
    Hotato    itm_hotato
    Muckchuck    itm_muckchuck
    Softwood    itm_wood
    Hardwood    itm_hard_wood
    Sap    itm_tree_sap
    Ironite    itm_Iron_Ore
    Clay    itm_clay
    Salt Block    itm_Marble
    Voidtonium    itm_void
    Silk Fiber    itm_silkfiber
    Silk Slug Slime    itm_silkslugslime
    Silk Slug Spider    itm_silkslugspider
    Ironite Bar    itm_Iron_Bar
    Brick    itm_brick
    Glue    itm_Glue
    Bomb Shell    itm_Bomb_Shell
    Clearshell    itm_Plastic
    Plain Omelet    itm_plain_omelet
    Popberry Pie    itm_popberryPie
    Pancakes    itm_pancakes
    Popberry Loaf    itm_popberryLoaf
    Grumpkin Pie    itm_grumpkinPie
    Grumpkin Loaf    itm_grumpkinLoaf
    Scarrot Pie    itm_scarrotPie
    Scarrot Loaf    itm_scarrotLoaf
    MooMunch    itm_hay
    Flour    itm_flour
    Java Pod    itm_coffeepod
    Shrapnel    itm_Shrapnel
    Construction Powder    itm_constructionPowder
    Silk Rope    itm_silkrope
    Plaster    itm_plaster
    Silk Cloth    itm_silkcloth
    Wooden Beam    itm_woodenbeam
    Stick    itm_stick
    Plank    itm_plank
    Log Decoration    itm_log_decoration2
    Wooden Stool    itm_Wooden_Stool
    Popberry Wine    itm_popberrywine
    Heartbeet Wine    itm_heartbeetWine
    Grainshine    itm_grainbow_grainshine
    Hotka    itm_hotato_hotka
    Butterbrew    itm_butterberry_butterbrew
    Watermint Whisky    itm_wintermint_whiskey
    Astracactus Tequila    itm_tentacactus_tequila
    Muckchuck Mead    itm_muckchuck_mead
    """

    # Split data into lines and then split each line into items
    items = [line.split() for line in data.split('\n') if line.strip()]

    # Create dictionary from items
    json_data = {item[0]: item[1] for item in items}

    # Convert dictionary to JSON format
    json_output = json.dumps(json_data, indent=0)

    print(json_output)