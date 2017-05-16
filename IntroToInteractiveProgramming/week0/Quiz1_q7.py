# calculate rate of return
# Future value = present value * (1 + rate)**periods   FV=PV(1+rate)periods
"""The present value (PV) of your money is how much money you have now.
The future value (FV) of your money is how much money you will have in the future.
The nominal interest rate per period (rate) is how much interest you earn during a
particular length of time, before accounting for compounding. This is typically expressed as a percentage.
The number of periods (periods) is how many periods in the future this calculation is for."""

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    return present_value * (1 + rate_per_period)**periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

print "should return 745.317442824", future_value(500, .04, 10, 10)
