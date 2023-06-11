import datetime

def check_card_date(card_type_val,carddate):
    y=carddate.year
    m=carddate.month
    d=carddate.day
    
    if card_type_val==1:
        y+=10
        
    if card_type_val==2:
        y+=6
 

    if card_type_val==3:
        y+=4
 
    if card_type_val==4:
        y+=10
 
    cardenddate=str(datetime.datetime(y, m, d))
    return cardenddate    






def check_card_type(card_type_val,carddate):
    y=carddate.year
    m=carddate.month
    d=carddate.day
    card_type=1
    if card_type_val=="بطاقة شخصية":
        y+=10
        card_type=1

    if card_type_val=="جواز سفر":
        y+=6
        card_type=2
    if card_type_val=="رخصة قيادة":
        y+=4
        card_type=3    
    if card_type_val=="غير ذلك":
        y+=10
        card_type=4
    
    cardenddate=str(datetime.datetime(y, m, d))
    return card_type,cardenddate    
        


def check_card_type_2(card_type_val):
    card_type=""
    if card_type_val==1:
        card_type="بطاقة شخصية"

    if card_type_val==2:
        card_type="جواز سفر"
    if card_type_val==3:
        card_type="رخصة قيادة"
    if card_type_val==4:
        card_type="غير ذلك"
    
    return card_type
        

def cust_type_check(cust_type_var):
        custtype=1
        if cust_type_var=="مشتري" :
            custtype=1
        if cust_type_var=="بائع" :
            custtype=2
        if cust_type_var=="قابل الشراء" :
            custtype=3
        if cust_type_var=="وكيل البائع" :
            custtype=4
        if cust_type_var=="معرف بالمشتري" :
            custtype=5
        if cust_type_var=="معرف بالبائع" :
            custtype=6
        if cust_type_var=="العدل المثمن" :
            custtype=7
        if cust_type_var=="شاهد" :
            custtype=8


        return custtype

def  checkCustMaleOrFemal(CustMaleOrFemal_var):    
        custMaleOrFemale=1
        if CustMaleOrFemal_var=="ذكر":
            custMaleOrFemale=1
        else:
            custMaleOrFemale=2    
        return(custMaleOrFemale)



def  checkCustMaleOrFemal_2(CustMaleOrFemal_var):    
        custMaleOrFemale=""
        if CustMaleOrFemal_var==1:
            custMaleOrFemale="ذكر"
        else:
            custMaleOrFemale="انثى"    
        return(custMaleOrFemale)