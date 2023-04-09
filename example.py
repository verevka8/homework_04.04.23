# cursor = connection.cursor()

# create table
# with connection.cursor() as cursor:
#     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
#                          " name varchar(32)," \
#                          " password varchar(32)," \
#                          " email varchar(32), PRIMARY KEY (id));"
#     cursor.execute(create_table_query)
#     print("Table created successfully")

# insert data
# with connection.cursor() as cursor:
#     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Anna', 'qwerty', 'anna@gmail.com');"
#     cursor.execute(insert_query)
#     connection.commit()

# with connection.cursor() as cursor:
#     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Victor', '123456', 'victor@gmail.com');"
#     cursor.execute(insert_query)
#     connection.commit()
#
# with connection.cursor() as cursor:
#     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '112233', 'olegan@mail.ru');"
#     cursor.execute(insert_query)
#     connection.commit()

# with connection.cursor() as cursor:
#     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', 'kjlsdhfjsd', 'ole2gan@mail.ru');"
#     cursor.execute(insert_query)
#     connection.commit()
#
# with connection.cursor() as cursor:
#     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '889922', 'olegan3@mail.ru');"
#     cursor.execute(insert_query)
#     connection.commit()

# update data
# with connection.cursor() as cursor:
#     update_query = "UPDATE `users` SET password = 'xxxXXX' WHERE name = 'Oleg';"
#     cursor.execute(update_query)
#     connection.commit()

# delete data
# with connection.cursor() as cursor:
#     delete_query = "DELETE FROM `users` WHERE id = 5;"
#     cursor.execute(delete_query)
#     connection.commit()

# drop table
# with connection.cursor() as cursor:
#     drop_table_query = "DROP TABLE `users`;"
#     cursor.execute(drop_table_query)

# select all data from table
# with connection.cursor() as cursor:
#     select_all_rows = "SELECT * FROM `users`"
#     cursor.execute(select_all_rows)
#     # cursor.execute("SELECT * FROM `users`")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     print("#" * 20)



# SELECT `table 3`.`Адрес`, SUM(`table 1`.`Цена` * `table 1`.`Количество упаковок`) as sum FROM `table 1`
# JOIN `table 2` ON `table 1`.`Артикул` = `table 2`.`Артикул`
# JOIN `table 3` ON `table 1`.`ID магазина` = `table 3`.`ID магазина`
# WHERE `table 1`.`Дата` = "01.06.2021" and `table 2`.`Отдел` = "Молоко" and `table 3`.`Район` = "Заречный" and `table 1`.`Тип операции` = "Поступление" GROUP BY `table 3`.`Адрес`