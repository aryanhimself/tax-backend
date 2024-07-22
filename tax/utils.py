import decimal

def calculate_income_tax(policy, annual_income):
    tax_amount = 0
    taxed_amount = 0
    for key in sorted(policy.keys()):
        if not policy[key]['amount']:
            taxable_amount = annual_income - taxed_amount
        else:
            taxable_amount = policy[key]['amount'] if annual_income > policy[key]['amount'] else annual_income

        tax_amount += policy[key]['percent']/decimal.Decimal(100) * decimal.Decimal(taxable_amount)
        taxed_amount += taxable_amount
        if not policy[key]['amount'] or annual_income <= policy[key]['amount']: break
    return tax_amount


