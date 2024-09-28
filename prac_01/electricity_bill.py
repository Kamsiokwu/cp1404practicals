TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")

tariff = input("Enter the tariff which was used here : ")
if tariff == "11":
    price_per_kwh = TARIFF_11
elif tariff == "31":
    price_per_kwh = TARIFF_31
else:
    print("Invalid tariff")
    price_per_kwh = 0

if price_per_kwh > 0:
    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    final_bill = price_per_kwh * daily_use * billing_days
    print(f"Estimated bill: ${final_bill}")
