import streamlit as st


class ElectricityBill:
    def __init__(self,customer_name,consumer_number,units):
        self.customer_name = customer_name
        self.consumer_number = consumer_number
        self.units = units
       
    def calculate_energy_charge(self):
        units = self.units
        
        if units<=100:               #First 100 units	₹2.00
            charge = units*2

        elif units<=200:             #Next 100 units (101–200)	₹3.00
            charge = (100*2) + ((units-100) * 3)

        elif units<=300:             #Next 100 units (201–300)	₹5.00
            charge = (100*2) + (100*3) + ((units-200) * 5)

        else:
            charge = ((100*2) + (100*3) + (100*5) + ((units-300) * 7))

        return charge

    def calculate_surcharge(self, energy_charge):
        if self.units > 300:
            return energy_charge * 0.05
        else:
            return 0

       
    def calculate_total(self):
        energy_charge = self.calculate_energy_charge()
        surcharge = self.calculate_surcharge(energy_charge)
        total = energy_charge + surcharge
        return total, energy_charge, surcharge


st.title("Electricity Bill Generator")
st.write("Enter the consumer details to calculate the bill.")

# Input section
with st.form("electricity_bill_form"):
    customer_name = st.text_input("Customer Name")
    consumer_number = st.text_input("Consumer Number")
    units = st.number_input(
        "Electricity Units Consumed",
        min_value=0,
        max_value=100000,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Generate Bill")
if submitted:

    if not customer_name.strip() or not consumer_number.strip():
        st.error("Please enter both customer name and consumer number.")

    else:
        bill = ElectricityBill(
            customer_name.strip(),
            consumer_number.strip(),
            int(units)
        )

        total, energy_charge, surcharge = bill.calculate_total()

        st.success("Electricity bill generated successfully!")

        st.subheader("Customer Bill Details")

        st.write(f"**Customer Name:** {bill.customer_name}")
        st.write(f"**Consumer Number:** {bill.consumer_number}")
        st.write(f"**Units Consumed:** {bill.units}")

        st.divider()

        st.write(f"Energy Charges: ₹{energy_charge:.2f}")
        st.write(f"Surcharge: ₹{surcharge:.2f}")

        st.divider()

        st.metric("Total Electricity Bill", f"₹{total:.2f}")
