#!/usr/bin/python

'''
To add more servers copy & paste the first line.
The last item must end with ,]].
'''

# List of protonvpn servers
# Will not breaking into categories maybe with a 3rd column with login level 1-3
serverList = [
["2", "AU#1", "AU#1"],
["2", "AU#2", "AU#2"],
["3", "AU#3", "AU#3"],
["3", "AU#4", "AU#4"],
["2", "CA#1", "CA#1"],
["2", "CA#2", "CA#2"],
["3", "CA#3", "CA#3"],
["3", "CA#4", "CA#4"],
["2", "CH#1", "CH#1"],
["2", "CH#2", "CH#2"],
["3", "CH#3", "CH#3"],
["3", "CH#4", "CH#4"],
["3", "CH#5", "CH#5"],
["3", "CH#6", "CH#6"],
["3", "CH#7", "CH#7"],
["3", "CH#8", "CH#8"],
["3", "CH#9-TOR", "CH#9-TOR"],
["2", "DE#1", "DE#1"],
["2", "DE#2", "DE#2"],
["3", "DE#3", "DE#3"],
["3", "DE#4", "DE#4"],
["3", "DE#5", "DE#5"],
["3", "DE#6", "DE#6"],
["3", "DE#7", "DE#7"],
["3", "DE#8", "DE#8"],
["2", "ES#1", "ES#1"],
["2", "ES#2", "ES#2"],
["3", "ES#3", "ES#3"],
["3", "ES#4", "ES#4"],
["2", "FR#5", "FR#5"],
["2", "FR#6", "FR#6"],
["3", "FR#7", "FR#7"],
["3", "FR#8", "FR#8"],
["2", "HK#1", "HK#1"],
["2", "HK#2", "HK#2"],
["3", "HK#3", "HK#3"],
["3", "HK#4", "HK#4"],
["3", "HK#5-TOR", "HK#5-TOR"],
["2", "IS#1", "IS#1"],
["2", "IS#2", "IS#2"],
["3", "IS#3", "IS#3"],
["3", "IS#4", "IS#4"],
["2", "JP#1", "JP#1"],
["2", "JP#2", "JP#2"],
["3", "JP#3", "JP#3"],
["3", "JP#4", "JP#4"],
["1", "JP-FREE#1", "JP-FREE#1"],
["2", "NL#1", "NL#1"],
["2", "NL#2", "NL#2"],
["3", "NL#3", "NL#3"],
["3", "NL#4", "NL#4"],
["3", "NL#5", "NL#5"],
["3", "NL#6", "NL#6"],
["3", "NL#7", "NL#7"],
["3", "NL#8", "NL#8"],
["3", "NL#9", "NL#9"],
["3", "NL#10", "NL#10"],
["2", "NL#101", "NL#101"],
["2", "NL#102", "NL#102"],
["2", "NL#103", "NL#103"],
["2", "NL#104", "NL#104"],
["2", "NL#105", "NL#105"],
["2", "NL#106", "NL#106"],
["2", "NL#107", "NL#107"],
["2", "NL#108", "NL#108"],
["2", "NL#109", "NL#109"],
["3", "NL#11", "NL#11"],
["2", "NL#110", "NL#110"],
["2", "NL#111", "NL#111"],
["2", "NL#112", "NL#112"],
["2", "NL#113", "NL#113"],
["2", "NL#114", "NL#114"],
["2", "NL#115", "NL#115"],
["2", "NL#116", "NL#116"],
["2", "NL#117", "NL#117"],
["2", "NL#118", "NL#118"],
["2", "NL#119", "NL#119"],
["3", "NL#12", "NL#12"],
["3", "NL#120", "NL#120"],
["3", "NL#125", "NL#125"],
["3", "NL#126", "NL#126"],
["3", "NL#127", "NL#127"],
["3", "NL#128", "NL#128"],
["3", "NL#129", "NL#129"],
["3", "NL#130", "NL#130"],
["3", "NL#131", "NL#131"],
["3", "NL#132", "NL#132"],
["3", "NL#133", "NL#133"],
["3", "NL#134", "NL#134"],
["3", "NL#135", "NL#135"],
["3", "NL#136", "NL#136"],
["1", "NL-FREE#1", "NL-FREE#1"],
["1", "NL-FREE#2", "NL-FREE#2"],
["2", "SE#1", "SE#1"],
["2", "SE#2", "SE#2"],
["3", "SE#3", "SE#3"],
["3", "SE#4", "SE#4"],
["2", "SE#5", "SE#5"],
["2", "SE#6", "SE#6"],
["3", "SE#7", "SE#7"],
["3", "SE#8", "SE#8"],
["2", "SG#1", "SG#1"],
["2", "SG#2", "SG#2"],
["3", "SG#3", "SG#3"],
["3", "SG#4", "SG#4"],
["3", "UK#1", "UK#1"],
["3", "UK#2", "UK#2"],
["3", "UK#3", "UK#3"],
["3", "UK#4", "UK#4"],
["2", "UK#5", "UK#5"],
["2", "UK#6", "UK#6"],
["3", "UK#7", "UK#7"],
["3", "UK#8", "UK#8"],
["3", "UK#9", "UK#9"],
["3", "UK#10", "UK#10"],
["3", "UK#11", "UK#11"],
["3", "UK#12", "UK#12"],
["3", "US-CA#1", "US-CA#1"],
["3", "US-CA#2", "US-CA#2"],
["3", "US-CA#3", "US-CA#3"],
["3", "US-CA#4", "US-CA#4"],
["3", "US-CA#5", "US-CA#5"],
["3", "US-CA#6", "US-CA#6"],
["3", "US-CA#7", "US-CA#7"],
["3", "US-CA#8", "US-CA#8"],
["3", "US-CA#101", "US-CA#101"],
["3", "US-CA#102", "US-CA#102"],
["3", "US-CA#103", "US-CA#103"],
["3", "US-CA#104", "US-CA#104"],
["3", "US-CA#105", "US-CA#105"],
["3", "US-CA#106", "US-CA#106"],
["3", "US-CA#107", "US-CA#107"],
["3", "US-CA#108", "US-CA#108"],
["3", "US-CA#109", "US-CA#109"],
["3", "US-CA#110", "US-CA#110"],
["3", "US-CA#111", "US-CA#111"],
["3", "US-CA#112", "US-CA#112"],
["3", "US-CO#1", "US-CO#1"],
["3", "US-CO#2", "US-CO#2"],
["3", "US-CO#3", "US-CO#3"],
["3", "US-CO#4", "US-CO#4"],
["3", "US-CO#5", "US-CO#5"],
["3", "US-CO#6", "US-CO#6"],
["3", "US-CO#7", "US-CO#7"],
["3", "US-CO#8", "US-CO#8"],
["1", "US-FREE#1", "US-FREE#1"],
["1", "US-FREE#2", "US-FREE#2"],
["3", "US-IL#1", "US-IL#1"],
["3", "US-IL#2", "US-IL#2"],
["3", "US-IL#3", "US-IL#3"],
["3", "US-IL#4", "US-IL#4"],
["3", "US-IL#5", "US-IL#5"],
["3", "US-IL#6", "US-IL#6"],
["3", "US-IL#7", "US-IL#7"],
["3", "US-IL#8", "US-IL#8"],
["3", "US-IL#101", "US-IL#101"],
["3", "US-IL#102", "US-IL#102"],
["3", "US-IL#103", "US-IL#103"],
["3", "US-IL#104", "US-IL#104"],
["3", "US-NJ#1", "US-NJ#1"],
["3", "US-NJ#2", "US-NJ#2"],
["3", "US-NJ#3", "US-NJ#3"],
["3", "US-NJ#4", "US-NJ#4"],
["3", "US-TX#1", "US-TX#1"],
["3", "US-TX#2", "US-TX#2"],
["3", "US-TX#3", "US-TX#3"],
["3", "US-TX#4-TOR", "US-TX#4-TOR"],
["3", "US-TX#101", "US-TX#101"],
["3", "US-TX#102", "US-TX#102"],
["3", "US-TX#103", "US-TX#103"],
["3", "US-TX#104", "US-TX#104"],
["3", "US-TX#105", "US-TX#105"],
["3", "US-TX#106", "US-TX#106"],
["3", "US-TX#107", "US-TX#107"],
["3", "US-TX#108", "US-TX#108"],
["3", "US-VA#1", "US-VA#1"],
["3", "US-VA#2", "US-VA#2"],
["3", "US-VA#3", "US-VA#3"],
["3", "US-VA#4", "US-VA#4"],
["3", "US-VA#101", "US-VA#101"],
["3", "US-VA#102", "US-VA#102"],
["3", "US-VA#103", "US-VA#103"],
["3", "US-VA#104", "US-VA#104"],
["3", "US-VA#105", "US-VA#105"],
["3", "US-VA#106", "US-VA#106"],
["3", "US-VA#107", "US-VA#107"],
["3", "US-VA#108", "US-VA#108"],
["3", "US-VA#109", "US-VA#109"],
["3", "US-VA#110", "US-VA#110"],
["3", "US-VA#111", "US-VA#111"],
["3", "US-VA#112", "US-VA#112",]]