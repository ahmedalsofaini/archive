

def sale_full_text(buyers_names,check_buyers_acount,sellers_names,check_sellers_acount,buyer_agent,seller_agent,buyer_identifier,seller_identifier,the_appraiser_name,witness_name,sd_table,sc_table,docum_no,today_date,D_hijri_date,D_miladi_date,D_hijri_input_date,D_miladi_input_date,D_file_no,d_book_no,d_page_no,D_All_price_n,D_All_price_k,agency_doc):
    d_full_text="\n \n \n \n \n \n"
    d_full_text+="اشترى"
    d_full_text+=buyers_names


    if buyer_agent!="":
        if check_buyers_acount==1:
            d_full_text+="القابل له الشراء"+buyer_agent
        
        if check_buyers_acount==2:
            d_full_text+="القابل لهما الشراء"+buyer_agent
        if check_buyers_acount>2:
            d_full_text+="القابل لهم الشراء"+buyer_agent


    if buyer_identifier!="":
        if check_buyers_acount==1:
            d_full_text+="المعرفان به"+buyer_identifier
        
        if check_buyers_acount==2:
            d_full_text+="المعرفان بهما"+buyer_identifier
        if check_buyers_acount>2:
            d_full_text+="المعرفان بهم"+buyer_identifier



    if check_sellers_acount==1 and check_buyers_acount==1:
        d_full_text+="من البائع عليه"

    if check_sellers_acount==1 and check_buyers_acount==2:
        d_full_text+="من البائع عليهما"
        
    if check_sellers_acount==1 and check_buyers_acount>2:
        d_full_text+="من البائع عليهم"
    
    if check_sellers_acount>=2 and check_buyers_acount==1:
        d_full_text+="من البائعين عليه"
        
    
    if check_sellers_acount>=2 and check_buyers_acount==2:
        d_full_text+="من البائعين عليهما"
        
    
    if check_sellers_acount>=2 and check_buyers_acount>2:
        d_full_text+="من البائعين عليهم"
        
    d_full_text+=sellers_names
    if seller_agent!="":
        if check_sellers_acount==1:
            d_full_text+="البائع عنه وكيله"+seller_agent
        
        if check_sellers_acount==2:
            d_full_text+="البائع عنهما وكيلهما"+seller_agent
        if check_sellers_acount>2:
            d_full_text+="البائع عنهم وكيلهم"+seller_agent
    if agency_doc!="":
        d_full_text+=agency_doc+" "





    if seller_identifier!="":
        if check_sellers_acount==1:
            d_full_text+="المعرفان به"+seller_identifier
        
        if check_sellers_acount==2:
            d_full_text+="المعرفان بهما"+seller_identifier
        if check_sellers_acount>2:
            d_full_text+="المعرفان بهم"+seller_identifier
    

    d_full_text+="وذلك المبيع"
    d_full_text+=sd_table
    if check_sellers_acount==1:
        d_full_text+=" متصلا للبائع"

    if check_sellers_acount>=2:
        d_full_text+=" متصلا للبائعين"

    d_full_text+=sc_table
    d_full_text+=" وثمن ذلك المبيع مبلغ وقدره"
    d_full_text+=D_All_price_n+" "
    d_full_text+=D_All_price_k+" ريال يمني جمهوري "
    if the_appraiser_name!="":
        d_full_text+=" حسبما ثمنه العدل المثمن"
        d_full_text+=the_appraiser_name
    else:
        d_full_text+=" حسبما اتفق عليه الطرفان"    

    d_full_text+=" اقر لدينا"
    if check_sellers_acount==1:
        d_full_text+=" البائع"


    if check_sellers_acount==2:
        d_full_text+=" البائعان"
    
    if check_sellers_acount>2:
        d_full_text+=" البائعون"

    d_full_text+=" باستلام كامل الثمن عدا ونقدا بالوفاء والتمام واصبح ذلك المبيع ملكا"

    if check_buyers_acount==1:
        d_full_text+=" للمشتري من جملة املاكه يتصرف به متى يشاء وانعقد المبيع انعقادا شرعيا من الطرفين بالإيجاب والقبول"

    if check_buyers_acount==2:
        d_full_text+=" للمشتريين من جملة املاكهما يتصرفان به كيف يشاءان وانعقد المبيع انعقادا شرعيا من الطرفين بالإيجاب والقبول"

    if check_buyers_acount>2:
        d_full_text+=" للمشترين من جملة املاكهم يتصرفون به كيف يشاءون وانعقد المبيع انعقادا شرعيا من الطرفين بالإيجاب والقبول"

    d_full_text+=" وحرر بحضور الشهود وهم"
    d_full_text+=witness_name
    d_full_text+=" والله خير الشاهدين وهو حسبنا ونعم الوكيل ولا حول ولا قوة الا بالله العلي العظيم وصلى الله وسلم على محمد وعلى اله وصحبه اجمعين وحرر هذا بتأريخ"
    d_full_text+=D_hijri_date+" هـ"
    d_full_text+=" الموافق"
    d_full_text+=D_miladi_date+" م"

    d_full_text = d_full_text.replace('  ', ' ')

    return d_full_text