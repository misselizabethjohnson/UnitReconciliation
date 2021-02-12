# Unit Reconciliation

## Project Overview
This directory contains Python (3.x) scripts for unit reconciliation, 
the process of comparing financial transaction history to the
bank's records. For example, at the beginning of a day a 
shareholder may own 100 shares of Apple stock. During the day, 
the shareholder then buys 5 more shares. We'd expect the bank
record to show 105 shares of Apple stock at the end of the day. 
We can use this project to check the records and report 
differences.

## Getting Started
To jump right in, assuming you have installed required dependencies
listed below, open a Terminal/Command Prompt and navigate to this
directory. Then run: 
```
python UnitReconciliation.py
```
The resulting output file, "recon.out" will appear in this 
directory.

## Requirements
* Python 3.x 
* "recon.in" text file w/ appropriate formatting: 
### recon.in
This required text file contains the initial account cash 
and positions, the transactions that occurred, and the final 
reported cash and positions. A simple example is as follows: 
>D0-POS
>AAPL 100
>GOOG 200
>SP500 175.75
>Cash 1000
>
>D1-TRN
>AAPL SELL 100 30000
>GOOG BUY 10 10000
>Cash DEPOSIT 0 1000
>Cash FEE 0 50
>GOOG DIVIDEND 0 50
>TD BUY 100 10000
>
>D1-POS
>GOOG 220
>SP500 175.75
>Cash 20000
>MSFT 10

## Authorship and Acknowledgements
Elizabeth Johnson wrote the contents of this directory based on
a prompt posed by YCharts. The recon.in example input file 
was provided by YCharts.

## Contact Information
Please reach out to Elizabeth Johnson with questions: 
misselizabethjohnson@gmail.com