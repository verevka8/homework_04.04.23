def nomer_1():
    with connection.cursor() as cursor:
        cursor.execute(
            """ SELECT SUM(`table 1`.`Количество упаковок`) FROM `table 1` JOIN `table 2` ON `table 1`.`Артикул` = `table 2`.`Артикул` JOIN `table 3` ON `table 1`.`ID магазина` = `table 3`.`ID магазина` WHERE `table 3`.`Район` = "Заречный" and `table 1`.`Дата` BETWEEN "01.06.2021" and "08.06.2021" and `table 1`.`Тип операции` = "Поступление" and `table 2`.`Наименование` = "Яйцо диетическое"; """)
        rows = cursor.fetchall()
        sm_entrance = int(rows[0].get("SUM(`table 1`.`Количество упаковок`)"))
        cursor.execute(
            """ SELECT SUM(`table 1`.`Количество упаковок`) FROM `table 1` JOIN `table 2` ON `table 1`.`Артикул` = `table 2`.`Артикул` JOIN `table 3` ON `table 1`.`ID магазина` = `table 3`.`ID магазина` WHERE `table 3`.`Район` = "Заречный" and `table 1`.`Дата` BETWEEN "01.06.2021" and "08.06.2021" and `table 1`.`Тип операции` = "Продажа" and `table 2`.`Наименование` = "Яйцо диетическое"; """)
        rows = cursor.fetchall()
        sm_sale = int(rows[0].get("SUM(`table 1`.`Количество упаковок`)"))
        print("1)", sm_entrance - sm_sale)

def nomer_2():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT SUM(`table 1`.`Количество упаковок`) FROM `table 1` JOIN `table 2` ON `table 1`.`Артикул` = `table 2`.`Артикул` JOIN `table 3` ON `table 1`.`ID магазина` = `table 3`.`ID магазина` WHERE `table 3`.`Район` = "Первомайский" and `table 1`.`Дата` BETWEEN "01.06.2021" and "08.06.2021" and `table 1`.`Тип операции` = "Поступление" and `table 2`.`Наименование`LIKE "Макароны%" and `table 2`.`Производитель` = "Макаронная фабрика";""")
        rows = cursor.fetchall()
        sm_entrance = int(rows[0].get("SUM(`table 1`.`Количество упаковок`)"))

        cursor.execute(
            """SELECT SUM(`table 1`.`Количество упаковок`) FROM `table 1` JOIN `table 2` ON `table 1`.`Артикул` = `table 2`.`Артикул` JOIN `table 3` ON `table 1`.`ID магазина` = `table 3`.`ID магазина` WHERE `table 3`.`Район` = "Первомайский" and `table 1`.`Дата` BETWEEN "01.06.2021" and "08.06.2021" and `table 1`.`Тип операции` = "Продажа" and `table 2`.`Наименование`LIKE "Макароны%" and `table 2`.`Производитель` = "Макаронная фабрика";""")
        rows = cursor.fetchall()
        sm_sale = int(rows[0].get("SUM(`table 1`.`Количество упаковок`)"))
        print("2)",sm_entrance - sm_sale)

def nomer_3():
    with connection.cursor() as cursor:
        cursor.execute(
            """ SELECT `table 3`.`Адрес`,SUM(`table 1`.`Цена` * `table 1`.`Количество упаковок`) as `sum` FROM `table 1` 
            JOIN `table 2` ON `table 1`.`Артикул` = `table 2`.`Артикул` 
            JOIN `table 3` ON `table 1`.`ID магазина` = `table 3`.`ID магазина` 
            WHERE `table 1`.`Дата` = "02.06.2021" and `table 2`.`Отдел` = "Молоко" and `table 3`.`Район` = "Заречный" and 
            `table 1`.`Тип операции` = "Поступление" GROUP BY `table 3`.`Адрес`; """)
        req = cursor.fetchall()
        res = ""
        min = 10**10
        for i in req:
            val, sm = i.items()
            val = val[-1]
            sm = int(sm[-1])
            if min > sm:
                min = sm
                save = val
        print("3)", save)
        cursor.execute(f"""SELECT `table 2`.`Наименование`, `table 2`.`Единица измерения`, `table 2`.`Количество в упаковке`, `table 2`.`Производитель` FROM `table 1` 
        JOIN `table 2` ON `table 1`.`Артикул` = `table 2`.`Артикул` 
        JOIN `table 3` ON `table 1`.`ID магазина` = `table 3`.`ID магазина` 
        WHERE `table 1`.`Тип операции` = "Поступление" and `table 3`.`Адрес` = "{save}"; """)
        req = cursor.fetchall()
        print(*req,sep="\n")









import pymysql
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...\n")

    try:
         nomer_1()
         nomer_2()
         nomer_3()




    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)