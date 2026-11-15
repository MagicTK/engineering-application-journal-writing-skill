# Reading a measurement dictionary and a window summary

## A fictional filter skid

A historian stores two columns under the same tag in kPa. The commissioning sheet identifies one as outlet pressure and the other as inlet pressure minus outlet pressure. Can the columns be merged when preparing the variable list?

Retain both columns. A tag and a unit match in both entries, but the physical quantities differ. Record the pressure tap for the first field and the ordered pair of taps for the pressure difference. Establish the number of instruments separately from the equipment register.

## A fictional drying cycle

A dryer schedules four temperature readings during each cycle. Its historian reports a mean when at least one reading is available. All four readings in one cycle are 60 °C. In a second cycle only the first and last readings arrive, also at 60 °C. The exported table contains the two cycle means and a flag for each mean. What coverage can the table establish?

Both reported means are 60 °C and both flags are set. The summary table alone establishes that both cycle means are present. The underlying acquisition log gives a different denominator and shows that six of eight scheduled readings arrived. The identical summary rows cannot identify which two times were missed. If a different historian enforces and documents a rule that releases a mean only after receiving all four scheduled readings, a present mean would establish complete coverage for that cycle.
