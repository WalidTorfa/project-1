"""
To add any template you want for any product/country
"""

def get_template(entries, template_type = "template 1"):
    template1 = f"""
HELLO IN TEMPLATE 1
Required Documents For S/C No. {entries["contract_number"]} on {entries["date"]} TO {entries["destination"]} :

1)  Shipping Commercial Invoice Signed & Sealed By Beneficiary In 6 Copies Made Out In The Name Of: 

{entries["invoice_name"]}

{entries["product"]}

Of Which One Original Should Be Certified By CCPIT, Showing Batch No. of Each Item, Production & Expiry Dates.  Containing The Syrian Declarations As Follows:

- We Certify That This Invoice Is Authentic And Is The Only Invoice Issued For The Goods Described Herein, That Mentions The Exact Value Of The Said Goods Without Deduction Of Any Advance Payment And That The Origin Of The Goods Exclusively From {entries["origin"]} .
- Goods Mentioned In This Invoice Are Produced by {entries["producer"]} And Exported By {entries["exporter"]}
- We Are Not Represented In Syria And Syria Is Not Included In The Territory Of Any Agent Who Would Benefit What So Ever From Any Commission On Our Product Exported To Syria.
- The Merchandise Mentioned In This Invoice Is Neither of Israeli Origin Nor It Contains Any Israeli Material.

2) Full Set Of Clean On Board Bills Of Lading Made Out To The Order Of  :

{entries["BL_name"]}
And Notify   
{entries["BL_notify_name"]} 
Showing Freight Prepaid & shipped On Board And Free Demurrage Not Less Than 21 Days. Issued By Liner Shipping Line Not From Forwarder Agent.

3) Certificate Of Origin Showing The Name Of The Exporters, Batch No. of Each Item , Production & Expiry Dates, And Not Mentioning The Value, Issued Before B/L Date But Not More Than 10 Days.

4) sanitary  Certificate Issued & Stamped By CIQ, Showing The Inspection Date. Should Be Issued Not More Than 10 Days Before The Date Of Shipment Shown On The B/L, Certified By CCPIT Batch No. Of Each Item, Production & Expiry Dates

5) Health Certificate Issued By Competent Authority, Attesting That Goods Are Fit For Human Consumption, Issued Not More Than 10 Days Before The Date Of Shipment Shown On The B/L, Certified By CCPIT Batch No. Of Each Item, Production & Expiry Dates

6) Quality/Weight Certificate Issued By Survey Company or by your manufacturer letterhead. Mentioning Batch No. Of Each Item, Production & Expiry Dates

7) Analysis Certificate Issued by your manufacturer letterhead Mentioning Batch No. Of Each Item, Production & Expiry Dates, Should Be Certified By CCPIT.

8) Packing List In 4 Copies.

10) Certificate From Beneficiary That cartons Are Marked In Arabic & English Wording.

11) Validity Certificate Issued By Beneficiary Attesting That The Shipped Goods Are Valid For Two Years, And The Consumption Period Is Not Less Than Two Thirds Of The Announced Validity From The Time Of Its Arrival.

12) veterinary certificate : Issued by your manufacturer letterhead Mentioning Batch No. Of Each Item, Production & Expiry Dates, Should Be Certified By CCPIT.

Notes:
{entries["notes"]}
    """

    template2 = f"""
        HELLO IN TEMPLATE 2
        Required Documents For S/C No. {entries["contract_number"]} on {entries["date"]} TO {entries["destination"]} :

        1)  Shipping Commercial Invoice Signed & Sealed By Beneficiary In 6 Copies Made Out In The Name Of: 

        {entries["invoice_name"]}

        {entries["product"]}


        Of Which One Original Should Be Certified By CCPIT, Showing Batch No. of Each Item, Production & Expiry Dates.  Containing The Syrian Declarations As Follows:

        - We Certify That This Invoice Is Authentic And Is The Only Invoice Issued For The Goods Described Herein, That Mentions The Exact Value Of The Said Goods Without Deduction Of Any Advance Payment And That The Origin Of The Goods Exclusively From {entries["origin"]} .
        - Goods Mentioned In This Invoice Are Produced by {entries["producer"]} And Exported By {entries["exporter"]}
        - We Are Not Represented In Syria And Syria Is Not Included In The Territory Of Any Agent Who Would Benefit What So Ever From Any Commission On Our Product Exported To Syria.
        - The Merchandise Mentioned In This Invoice Is Neither of Israeli Origin Nor It Contains Any Israeli Material.


        2) Full Set Of Clean On Board Bills Of Lading Made Out To The Order Of  :

        {entries["BL_name"]}

        And Notify   

        {entries["BL_notify_name"]} 

        Showing Freight Prepaid & shipped On Board And Free Demurrage Not Less Than 21 Days. Issued By Liner Shipping Line Not From Forwarder Agent.

        3) Certificate Of Origin Showing The Name Of The Exporters, Batch No. of Each Item , Production & Expiry Dates, And Not Mentioning The Value, Issued Before B/L Date But Not More Than 10 Days.

        4) sanitary  Certificate Issued & Stamped By CIQ, Showing The Inspection Date. Should Be Issued Not More Than 10 Days Before The Date Of Shipment Shown On The B/L, Certified By CCPIT Batch No. Of Each Item, Production & Expiry Dates

        5) Health Certificate Issued By Competent Authority, Attesting That Goods Are Fit For Human Consumption, Issued Not More Than 10 Days Before The Date Of Shipment Shown On The B/L, Certified By CCPIT Batch No. Of Each Item, Production & Expiry Dates

        6) Quality/Weight Certificate Issued By Survey Company or by your manufacturer letterhead. Mentioning Batch No. Of Each Item, Production & Expiry Dates

        7) Analysis Certificate Issued by your manufacturer letterhead Mentioning Batch No. Of Each Item, Production & Expiry Dates, Should Be Certified By CCPIT.

        8) Packing List In 4 Copies.

        10) Certificate From Beneficiary That cartons Are Marked In Arabic & English Wording.

        11) Validity Certificate Issued By Beneficiary Attesting That The Shipped Goods Are Valid For Two Years, And The Consumption Period Is Not Less Than Two Thirds Of The Announced Validity From The Time Of Its Arrival.
        12) veterinary certificate : Issued by your manufacturer letterhead Mentioning Batch No. Of Each Item, Production & Expiry Dates, Should Be Certified By CCPIT.





        Notes:

        {entries["notes"]}
    """
    
    if template_type == "template 1":
        return template1
    else:
        return template2
