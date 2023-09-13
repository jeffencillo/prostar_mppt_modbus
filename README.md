# modbus_morningstar
morningstar charge controller modbus data acquisition (using python)

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



if you have any questions about this program please email me at jeffencillo@gmail.com
