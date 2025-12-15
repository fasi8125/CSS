print("this is a bill calculator")
name=input("enter your name:")
table_no=int(input("enter your table no:"))
print("how many dishes u have oderred?")
dishes=int(input("enterthe no of dishes u have order:" ))
print("please enter the total bill amount:")
amount=float(input("enter the amount:"))
print("please enter the tip percentage")
tip_percentage=float(input("enter the tip percentage:"))
tip=amount*tip_percentage/100
total_bill=amount+tip
GST=total_bill*0.18
total_bill=total_bill+GST
print(f"the total bill after adding gst is:{total_bill}")
service_charge=total_bill*0.06
total_bill=total_bill+service_charge
print(f"the total bill after adding service charge is:{total_bill}")
discount_percentage=float(input("enter the amt of discount perecentage :"))
discount_percentage_amount=total_bill*discount_percentage/100
total_bill=total_bill-discount_percentage_amount
print(f"{name} ur  total bill after discount is:{total_bill}")
print(f"{name}u have ordered {dishes} total bill amount is:{total_bill}")
print("thank you for using the bill calculator")