import mysql.connector
from mysql.connector import errorcode
import datetime


def connectdb():
    try:
        cnx = mysql.connector.connect(user='root', password='aaaaaaaa',
                              host='127.0.0.1',
                              database='documentsys',
                              auth_plugin='mysql_native_password')
   
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
           print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
           print("Database does not exist")
        else:
           print(err)
    else:
       pass # cnx.close()

    mycursor = cnx.cursor()
    return cnx,mycursor


#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

def insert_into_docum_table(D_hijri_date, D_miladi_date, D_hijri_input_date, D_miladi_input_date, D_file_no, D_manual_archiving_no, D_electronic_type, D_old_no, D_bsaieer_or_zowg, D_old_input_date, d_book_no, d_page_no, D_type, D_m_type, D_z_type, D_h_t_date, D_m_t_date, D_t_number, D_full_text, D_qrcode, D_printed_no, d_note, D_Keywords, D_All_price_n, D_All_price_k, C_no_1, C_no_2,d_folder_path):
    cnx,mycursor=connectdb()
    sql = "INSERT INTO docum_table (D_hijri_date, D_miladi_date, D_hijri_input_date, D_miladi_input_date, D_file_no, D_manual_archiving_no, D_electronic_type, D_old_no, D_bsaieer_or_zowg, D_old_input_date, d_book_no, d_page_no, D_type, D_m_type, D_z_type, D_h_t_date, D_m_t_date, D_t_number, D_full_text, D_qrcode, D_printed_no, d_note, D_Keywords, D_All_price_n, D_All_price_k, C_no_1, C_no_2,d_folder_path) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)"
    val =(D_hijri_date, D_miladi_date, D_hijri_input_date, D_miladi_input_date, D_file_no, D_manual_archiving_no, D_electronic_type, D_old_no, D_bsaieer_or_zowg, D_old_input_date, d_book_no, d_page_no, D_type, D_m_type, D_z_type, D_h_t_date, D_m_t_date, D_t_number, D_full_text, D_qrcode, D_printed_no, d_note, D_Keywords, D_All_price_n, D_All_price_k, C_no_1, C_no_2, d_folder_path)
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")
    cnx.close()




def insertintocustomers_table(name,address,pirth_date,cust_maleorfemale,cust_source,cust_note,cust_keywords,job_no):
    cnx,mycursor=connectdb()
    todyDateandTime=datetime.datetime.now()

    sql = "INSERT INTO customers_table (C_name, C_address, C_pirth_date, C_type, C_source, C_input_date, C_input_time, c_update_date, c_update_time, c_note, c_keywords, j_no) VALUES ( %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val =(name,address,pirth_date,cust_maleorfemale,cust_source,todyDateandTime,todyDateandTime,todyDateandTime,todyDateandTime,cust_note,cust_keywords,job_no)
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")
    cnx.close()



def insert_into_id_table(id_card_type, id_card_number, id_card_place, id_card_issue_date, id_card_ending_date,c_no, id_note, Id_Keywords):
    cnx,mycursor=connectdb()
    todyDateandTime=datetime.datetime.now()

    sql = "INSERT INTO id_table (id_card_type, id_card_number, id_card_place, id_card_issue_date, id_card_ending_date, id_input_date, id_input_time, id_update_date, id_update_time, c_no, id_note, Id_Keywords) VALUES ( %s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s)"
    val =(id_card_type, id_card_number, id_card_place, id_card_issue_date, id_card_ending_date,todyDateandTime,todyDateandTime,todyDateandTime,todyDateandTime,c_no, id_note, Id_Keywords)
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")
    cnx.close()



def insert_into_cust_doc_table(c_no, d_no, cd_type, recipient_c_no, Cd_gave_date, Cd_gave_time, Cd_gave_type, cd_note, cd_keywords):
    cnx,mycursor=connectdb()
    sql = "INSERT INTO cust_doc_table (c_no, d_no, cd_type, recipient_c_no, Cd_gave_date, Cd_gave_time, Cd_gave_type, cd_note, cd_keywords) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val =(c_no, d_no, cd_type, recipient_c_no, Cd_gave_date, Cd_gave_time, Cd_gave_type, cd_note, cd_keywords)
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")
    cnx.close()




def insert_into_doc_detaills_connect_table(d_no, sd_no):
    cnx,mycursor=connectdb()
    sql = "INSERT INTO doc_detaills_connect_table (d_no, sd_no)  VALUES ( %s, %s)"
    val =(d_no, sd_no)
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")
    cnx.close()




def insert_into_sales_contact_table(firest_d_no, current_d_no, sc_note, sc_keywords):
    cnx,mycursor=connectdb()
    sql = "INSERT INTO sales_contact_table (firest_d_no, current_d_no, sc_note, sc_keywords)  VALUES ( %s, %s,%s, %s)"
    val =(firest_d_no, current_d_no, sc_note, sc_keywords)
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")
    cnx.close()


def insert_into_sale_details_table(sd_name, Sd_count_n, Sd_count_k, Sd_type, Sd_price_n, Sd_price_k, Sd_total, Sd_total_k, Sd_shape, sd_a1, sd_a2, sd_a3, sd_a4, sd_a5, sd_area, sd_h1, sd_h2, sd_h3, sd_h4, sd_note, sd_keywords):
    cnx,mycursor=connectdb()
    sql = "INSERT INTO sale_details_table ( sd_name, Sd_count_n, Sd_count_k, Sd_type, Sd_price_n, Sd_price_k, Sd_total, Sd_total_k, Sd_shape, sd_a1, sd_a2, sd_a3, sd_a4, sd_a5, sd_area, sd_h1, sd_h2, sd_h3, sd_h4, sd_note, sd_keywords)  VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
    val =(sd_name, Sd_count_n, Sd_count_k, Sd_type, Sd_price_n, Sd_price_k, Sd_total, Sd_total_k, Sd_shape, sd_a1, sd_a2, sd_a3, sd_a4, sd_a5, sd_area, sd_h1, sd_h2, sd_h3, sd_h4, sd_note, sd_keywords)
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")
    cnx.close()


def insertintodoc_detaills_connect_table():
    cnx,mycursor=connectdb()
    sql = "INSERT INTO doc_detaills_connect_table (d_no, sd_no) VALUES (%s, %s)"
    val =('1', '1')
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")




def insertintosales_contact_table():
    cnx,mycursor=connectdb()
    sql = "INSERT INTO sales_contact_table (d_no1, d_no2, C_no) VALUES (%s, %s, %s)"
    val =('1', '1','2')
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")


def insertintosale_details_table():
    cnx,mycursor=connectdb()
    sql = "INSERT INTO sale_details_table (sd_name, Sd_count_n, Sd_count_k, Sd_type, Sd_price_n, Sd_price_k, Sd_total, Sd_total_k, Sd_shape, sd_a1, sd_a2, sd_a3, sd_a4, sd_a5, sd_area)  VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val =('gfdgfd', '1', 'ljk;lj;', '1', '22', 'kjljl', '543', 'lkjlkjl', '1', '1', '2', '3', '3', '4', '22')
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")


def update_docum_table_add_full_text(full_text, d_no):
    cnx,mycursor=connectdb()
    table_name = "docum_table"
    column_name = "D_full_text"
    condition = "D_no = {}".format(d_no)
    sql = "UPDATE " + table_name + " SET " + column_name + " = %s WHERE " + condition
    val = (full_text, )
    mycursor.execute(sql, val)
    cnx.commit()




#insertintosale_details_table()
#insertintosales_contact_table()
#insertintodoc_detaills_connect_table()
#insertintocust_doc_table()
#insertintocustomers_table2()
#mycursor.execute("SELECT * FROM docum_table")

#myresult = mycursor.fetchall()

#for x in myresult:
#  print(x)
#cnx.close()




def check_customers_saved(name):
    cnx,mycursor=connectdb()
    mycursor.execute(" SELECT * FROM customers_table WHERE `C_name`='"+name+"'")

    myresult = mycursor.fetchall()

    counter=0       
    for x in myresult:
        counter+=1
    
    cnx.close()
    return counter , myresult



def check_customers_saved_by_c_no(c_no):
    cnx,mycursor=connectdb()
    mycursor.execute(" SELECT * FROM customers_table WHERE C_no="+str(c_no))

    myresult = mycursor.fetchall()

    counter=0       
    for x in myresult:
        counter+=1
    
    cnx.close()
    return counter , myresult


def select_customers():
    cnx,mycursor=connectdb()
    mycursor.execute(" SELECT * FROM customers_table")

    myresult = mycursor.fetchall()
    name = []
    counter=0
    for x in myresult:
        name.append(str(myresult[counter][1]))
        
        counter+=1
            
    cnx.close()
    return name



def select_id_table(c_no):
    cnx,mycursor=connectdb()
    mycursor.execute(" SELECT * FROM id_table where c_no="+str(c_no))

    myresult = mycursor.fetchall()
    counter=0
    for x in myresult:        
        counter+=1
            
    cnx.close()
    return counter, myresult


def select_max_c_no():
    cnx,mycursor=connectdb()
    mycursor.execute("SELECT max(c_no) FROM customers_table")

    myresult = mycursor.fetchall()
            
    cnx.close()
    return myresult




def select_id_table_with_card_number(id_card_number):
    cnx,mycursor=connectdb()
    mycursor.execute(" SELECT * FROM id_table where id_card_number="+str(id_card_number))

    myresult = mycursor.fetchall()
    counter=0
    for x in myresult:        
        counter+=1
            
    cnx.close()
    return counter,myresult


def select_customers_by_c_no(c_no):
    cnx,mycursor=connectdb()
    mycursor.execute("SELECT * FROM customers_table WHERE C_no="+str(c_no))

    myresult = mycursor.fetchall()

    counter=0       
    for x in myresult:
        counter+=1
    
    cnx.close()
    return counter , myresult


def select_cust_doc_table_by_d_no(d_no):
    cnx,mycursor=connectdb()
    mycursor.execute("SELECT * FROM cust_doc_table WHERE  `cd_type` = 2 and `d_no`="+str(d_no))

    myresult = mycursor.fetchall()

    counter=0       
    for x in myresult:
        counter+=1
    
    cnx.close()
    return counter , myresult



def select_doc_by_d_no(d_no):
    cnx,mycursor=connectdb()
    mycursor.execute("SELECT * FROM docum_table WHERE D_no="+str(d_no))

    myresult = mycursor.fetchall()

    counter=0       
    for x in myresult:
        counter+=1
    
    cnx.close()
    return counter , myresult







def select_doc_by_qr_code(qr_code):
    cnx,mycursor=connectdb()
    mycursor.execute("SELECT * FROM docum_table WHERE D_qrcode LIKE '"+qr_code+"'")

    myresult = mycursor.fetchall()

    counter=0       
    for x in myresult:
        counter+=1
    
    cnx.close()
    return counter , myresult



def select_max_d_no_from_docum():
    cnx,mycursor=connectdb()
    mycursor.execute("SELECT max(D_no) FROM docum_table")

    myresult = mycursor.fetchall()
            
    cnx.close()
    return myresult


def select_max_sd_no_from_sale_details_table():
    cnx,mycursor=connectdb()
    mycursor.execute("SELECT max(sd_no) FROM sale_details_table")

    myresult = mycursor.fetchall()
            
    cnx.close()
    return myresult
