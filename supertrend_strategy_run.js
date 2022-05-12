//@version=5
strategy("Supertrend Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=15)
dt_start = timestamp(input(1999, "Y"), input(1, "M") ,input(1, "D"), 0, 0)
dt_end   = timestamp(input(2100, "Y"), input(4, "M") ,input(13, "D"), 0, 0)
test_period() => 
    time >= dt_start and time <= dt_end ? true : false

barsSinceLastEntry() =>
    strategy.opentrades > 0 ? bar_index - strategy.opentrades.entry_bar_index(strategy.opentrades - 1) : 0
    
atrPeriod = input(10, "ATR Length")
factor = input.float(3.0, "Factor", step = 1.0)
[_, direction] = ta.supertrend(factor, atrPeriod)
_change = ta.change(direction)
atr = ta.atr(atrPeriod)

close_atr_short = close - atr * factor
close_atr_long = close + atr * factor
close_atr = close_atr_long
color_atr = color.red
close_atr_gap = close_atr

if _change > 0
    close_atr := close_atr_short
    color_atr := color.red
else if _change < 0
    close_atr := close_atr_long
    color_atr := color.blue
else
    close_atr := close_atr[1]
    color_atr := color_atr[1]
    close_atr_gap := close_atr - barsSinceLastEntry() * (close_atr - close) * input.float(0.2, "gap_ratio", step = 0.1)

if test_period()
    if _change < 0 
        strategy.entry("Long", strategy.long, na, close)
        strategy.close("Short")
    else if _change > 0 
        strategy.entry("Short", strategy.short)
        strategy.close("Long")
    else
        if close <= close_atr_gap
            strategy.close("Short")
        if close >= close_atr_gap
            strategy.close("Long")

p1 = plot(close_atr_gap, color = color.red)
p2 = plot(close)
fill(p1, p2, color=color.new(color_atr, 90))
