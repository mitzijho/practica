def computepay(Hours, Rate) :
    Hours = input("Enter hours:")
    H = float(Hours)
    Rate = input("Enter rate:")
    R = float(Rate)
    if H > 40 :
        Pay = (H - 40) * 1.5 * R + 40 * R
        return Pay
    else :
        Pay = H * R        
        return Pay
x = computepay("Hours", "Rate") 
print("Pay", x)