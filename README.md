# modbus_morningstar
morningstar charge controller modbus data acquisition (using python)

<!--
**jeffencillo/jeffencillo** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.


This is a python script that download the 256 days logged data from Morningstar MPPT Prostar charge controller thru TCP/IP Modbus protocol.

Command syntax:  python modbus_logger.py “ip address”

Sample output:

hourmeter, alarm_daily, load_fault_daily, array_fault_daily, Vb_min_daily, Vb_max_daily, Ahc_daily, Ahl_daily, Va_max_daily, Time in Absorption(HR)), Time in Equalize(HR), Time in Float(HR)
10012,No alarms,no faults,no faults,26.14,28.28,6.4,6.6,35.66,3.000277777777778,0.0,2.996111111111111
10036,No alarms,no faults,no faults,26.06,28.28,6.3,6.6,36.88,3.000277777777778,0.0,2.0766666666666667
10060,No alarms,no faults,no faults,26.02,28.3,6.0,6.7,35.84,3.000277777777778,0.0,3.096111111111111
10084,No alarms,no faults,no faults,25.98,28.28,5.7,6.5,37.06,3.000277777777778,0.0,2.0233333333333334
10108,No alarms,no faults,no faults,25.95,28.28,5.7,6.6,36.16,3.000277777777778,0.0,2.3897222222222223
10132,No alarms,no faults,no faults,25.94,28.28,5.4,6.6,36.47,3.000277777777778,0.0,1.5441666666666667
10155,No alarms,no faults,no faults,25.9,28.31,5.9,6.4,35.66,2.6244444444444444,0.0,0.0
10180,No alarms,no faults,no faults,25.89,28.31,5.4,6.6,36.53,3.000277777777778,0.0,1.1613888888888888
10202,No alarms,no faults,no faults,25.86,28.31,6.2,6.0,35.9,4.554166666666666,0.0,0.7188888888888889
10227,No alarms,no faults,no faults,25.89,28.28,5.9,6.9,36.88,3.000277777777778,0.0,3.07
10251,No alarms,no faults,no faults,25.89,28.3,5.6,6.7,36.5,3.000277777777778,0.0,1.8719444444444444
10275,No alarms,no faults,no faults,25.86,28.3,5.4,6.5,36.06,3.000277777777778,0.0,2.700277777777778
10299,No alarms,no faults,no faults,25.86,28.33,6.3,6.5,35.2,5.166111111111111,0.0,0.0
10323,No alarms,no faults,no faults,25.88,28.3,5.0,6.5,35.97,3.000277777777778,0.0,3.174722222222222
10347,No alarms,no faults,no faults,25.86,28.31,5.2,6.7,36.44,3.000277777777778,0.0,2.5780555555555558
10371,No alarms,no faults,no faults,25.84,28.28,5.3,6.6,36.66,3.000277777777778,0.0,2.9816666666666665


if you have any questions about this program please email me at jeffencillo@gmail.com
