from PIL import Image, ImageDraw, ImageFont
from utils.sqliteHelper import sqliteHelper
import os


class TestDataDB:
    product_name = ""
    manufacturer = ""
    model = ""
    meta = ""
    img_url = ""

    def __init__(self, p_name, man_name, mod_name, meta_name, img_url):
        self.product_name = p_name
        self.manufacturer = man_name
        self.model = mod_name
        self.meta = meta_name
        self.img_url = img_url


def create_image(pre, dev, model, scl):
    img = Image.new('RGB', (200 * scl, 200 * scl), color='black')
    fnt = ImageFont.truetype('/usr/share/fonts/opentype/NotoSansCJK-Regular.ttc', 16 * scl)
    d = ImageDraw.Draw(img)
    color1 = (0, 0, 0)
    color2 = (0, 0, 0)
    if pre == "Mac":
        color1 = (200, 200, 255)
        color2 = (220, 220, 255)
    elif pre == "Win":
        color1 = (100, 100, 255)
        color2 = (220, 220, 255)
    elif pre == "Lin":
        color1 = (150, 100, 255)
        color2 = (220, 220, 255)
    elif pre == "Bag":
        color1 = (150, 150, 150)
        color2 = (220, 220, 220)

    if (dev == "Desk"):
        d.rectangle(xy=[(20 * scl, 20 * scl), (180 * scl, 180 * scl)], fill=color1)
        d.rectangle(xy=[(40 * scl, 40 * scl), (160 * scl, 160 * scl)], fill=color2)
        d.rectangle(xy=[(20 * scl, 185 * scl), (180 * scl, 198 * scl)], fill=color1)
        d.rectangle(xy=[(25 * scl, 190 * scl), (170 * scl, 193 * scl)], fill=(30, 30, 30))
        d.text((45 * scl, 35 * scl), model, font=fnt, fill=(255, 0, 0))
    elif (dev == "Pad"):
        d.rectangle(xy=[(20 * scl, 20 * scl), (180 * scl, 180 * scl)], fill=color1)
        d.rectangle(xy=[(40 * scl, 40 * scl), (160 * scl, 160 * scl)], fill=color2)
        d.text((45 * scl, 160 * scl), model, font=fnt, fill=(255, 0, 0))
    elif (dev == "Book"):
        d.rectangle(xy=[(20 * scl, 20 * scl), (180 * scl, 150 * scl)], fill=color1)
        d.rectangle(xy=[(40 * scl, 40 * scl), (160 * scl, 140 * scl)], fill=color2)
        d.text((45 * scl, 160 * scl), model, font=fnt, fill=(255, 0, 0))
    elif (dev == "Phone"):
        d.rectangle(xy=[(40 * scl, 20 * scl), (160 * scl, 150 * scl)], fill=color1)
        d.rectangle(xy=[(60 * scl, 40 * scl), (140 * scl, 140 * scl)], fill=color2)
        d.text((45 * scl, 160 * scl), model, font=fnt, fill=(255, 0, 0))
    if scl == 1:
        img.save('../Data/images/min/' + model + '_min.png')
    else:
        img.save('../Data/images/' + model + '.png')


def generate_data():
    """
    Затирает предыдущую БД с картинками и генерирует данные на основе несокльких списков, в итоге получим 576 продуктов..
    ОСНОВНОЙ МЕТОД
    :return:
    """
    os.system("rm -rf ../Data/images")
    os.system("mkdir ../Data/images")
    os.system("rm -rf ../Data/test.db")
    db = sqliteHelper()
    db.build_db_table()
    result = []
    ven = ['Apple', 'Microsoft', 'someoneGuy', 'RosTech']
    pre = ['Mac', 'Win', 'Lin', 'Bag']
    dev = ['Book', 'Desk', 'Pad', 'Phone']
    num = range(1, 10)
    mod = ['s', 'x', 'pro', 'air']
    i = 0
    last_id = 0
    vendor = ""
    for p in pre:
        for d in dev:
            for n in num:
                for m in mod:
                    model = str(p) + str(d) + str(n) + str(m)
                    if p == 'Mac':
                        vendor = str(ven[0])
                    elif p == 'Win':
                        vendor = str(ven[1])
                    elif p == 'Lin':
                        vendor = str(ven[2])
                    elif p == 'Bag':
                        vendor = str(ven[3])
                    product_name = vendor + " " + model
                    print("generating " + str(i) + " product")
                    result.append({'id': i,
                                   'product_name': product_name,
                                   'manufacturer': vendor,
                                   'model': model,
                                   'meta': vendor,
                                   'img_url': '../Data/images/' + model + '.png',
                                   'used': 0
                                   })
                    create_image(p, d, model, 3)
                    i += 1
    last_id = i

    for r in result:
        print("adding " + str(r['id']) + " product from " + str(last_id) + " to test.db")
        db.add_product(r['product_name'], r['manufacturer'], r['model'], r['meta'], r['img_url'], r['used'])


def show_all_data():
    dbhelper = sqliteHelper()
    database = "../Data/test.db"
    conn = dbhelper.create_connection(database)
    dbhelper.get_all_data(conn)


def show_data():
    dbhelper = sqliteHelper()
    database = "../Data/test.db"
    conn = dbhelper.create_connection(database)
    dbhelper.get_data(conn)


def get_test_data():
    """
    Отдает объект с полями тестовых данных с данными из БД.
    После получения данных поле used выставляется в 1
    При следующем вызове будут выданы новые данные.
    :return:dict with new product test data
    """

    dbhelper = sqliteHelper()
    database = "../Data/test.db"
    conn = dbhelper.create_connection(database)
    data = dbhelper.get_data(conn)
    dbhelper.upd_product(data[0])
    data_dict = {'product_name': data[1],
                 'manufacturer': data[2],
                 'model': data[3],
                 'meta': data[4],
                 'img_url': data[5]
                 }
    obj_data = TestDataDB(data[1], data[2], data[3], data[4], data[5])
    return obj_data
