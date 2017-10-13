#  Imported Tax Libraries/Modules
import IRS_Single_Weekly
import IRS_Married_Weekly

#  Function that calls the appropriate library/module
def status(payfreq, filing_status, ftc):
    if payfreq == 'w' and filing_status == 's':
        x = IRS_Single_Weekly.Single_Weekly(ftc)
        return x.weekly_single_tax_table()
    if payfreq == 'w' and filing_status == 'm':
        x = IRS_Married_Weekly.Married_Weekly(ftc)
        return x.weekly_married_tax_table()

#  Questions that will eventually be asked through the GUI or web App
#payfreq = str(raw_input("What is your pay frequency? "))
#payfreq = payfreq.lower()

#filing_status = str(raw_input("What is your filing status? "))
#filing_status = filing_status.lower()

#ftc = int(raw_input("What is the taxable comp? "))

#  Sends results to function to call the tax table
#status(payfreq, filing_status, ftc)

#  Preliminary printing of results until GUI has been built
#print(type(payfreq))
#print(type(filing_status))
#print(status(payfreq, filing_status, ftc))
