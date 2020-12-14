import pymysql
connection = pymysql.connect(host='127.0.0.1',   user='root', password='192837465', db='ses', charset='utf8mb4', cursorclass = pymysql.cursors.DictCursor)
try:

    with connection.cursor() as cursor:
        cursor.execute('select * from sessia;')
        print(cursor.fetchall())
        connection.commit()

    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO `ses`.`sessia` (`Id`, `Surname`, `Subject_1`, `Subject_2`, `Mark_1`, `Mark_2`) VALUES ('8', 'Булкин', 'Математика', 'Информатика', '4', '5');""")
        cursor.execute("""INSERT INTO `ses`.`sessia` (`Id`, `Surname`, `Subject_1`, `Subject_2`, `Mark_1`, `Mark_2`) VALUES ('9', 'Жуков', 'Физика', 'Математика', '5', '3');""")
        cursor.execute("""INSERT INTO `ses`.`sessia` (`Id`, `Surname`, `Subject_1`, `Subject_2`, `Mark_1`, `Mark_2`) VALUES ('10', 'Наумов', 'Информатика', 'Математика', '3', '3');""")
        cursor.execute("""INSERT INTO `ses`.`sessia` (`Id`, `Surname`, `Subject_1`, `Subject_2`, `Mark_1`, `Mark_2`) VALUES ('11', 'Мотрошилов', 'Информатика', 'Математика', '5', '5');""")
        connection.commit()

    with connection.cursor() as cursor:
        cursor.execute("UPDATE `ses`.`sessia` SET `Mark_1` = '5', `Mark_2` = '5' WHERE (`Id` = '1');")
        cursor.execute("UPDATE `ses`.`sessia` SET `Mark_2` = '5' WHERE (`Id` = '2');")
        cursor.execute("UPDATE `ses`.`sessia` SET `Mark_1` = '5' WHERE (`Id` = '5');")
        connection.commit()

finally:
    connection.close()




