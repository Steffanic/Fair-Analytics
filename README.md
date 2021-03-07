# Fair-Analytics
We use python to analyze county fair STOP reports from the WFA.

Progress Report 12/31/2020:

Class 1 Fairs have been separated into yearly csv files. 

From year to year the content and organization of the STOP reports changes.

Next steps will be distilling the features from all the years into a cohesive representation of a fair.

It is becoming clear that we will need to compute general features across different years. We need to standardize!

## Feature Map
This table describes the relationship between the features that will be considered for modeling and the rows of each CSV accross the years.

### Class 1

|  COMMON FEATURE                                  |  YEAR RANGE  |  FEATURE NAME                                |
| ------------------------                         | ------------ | ---------------------                        |
| STARTING BALANCE                                 |  2001-2003   |  BEGINNING RESOURCES                         |
|                                                  |  2004-2007   |  Total                                       |
|                                                  |  2008-2018   |  Total Net Resources                         |
| STATE ALLOCATION                                 |  2001-2018   |  State Allocation                            |
| OTHER ACQUIRED RESOURCES                         |  2001-2006   |  Other                                       |
|                                                  |  2007-2018   |  Capital Project Reimbursement Funds + Other |
| TOTAL OPERATING REVENUES                         |  2001-2018   |  Total Operating Revenues                    |
| REVENUES: ADMISSIONS TO GROUNDS                  |  2001-2018   |  Admissions to Grounds                       |
| REVENUES: INDUSTRIAL AND COMMERCIAL SPACE        |  2001-2018   |  Industrial and Commercial Space             |
| REVENUES: CONCESSIONS                            |  2001-2018   |  Concessions                                 |
| REVENUES: EXHIBITS                               |  2001-2018   |  Exhibits                                    |
| REVENUES: HORSE SHOW                             |  2001-2018   |  Horse Show                                  |
| REVENUES: FAIR ATTRACTIONS                       |  2001-2018   |  Fair Attractions                            |
| REVENUES: INTERIM ATTRACTIONS                    |  2002-2018   |  Interim Attractions                         |
| REVENUES: MOTORIZED RACING                       |  2004-2018   |  Motorized Racing                            |
| REVENUES: MISCELLANEOUS FAIR                     |  2001-2018   |  Miscellaneous Fair                          |
| REVENUES: MISCELLANEOUS NON-FAIR                 |  2001-2018   |  Miscellaneous Non-Fair                      |
| REVENUES: INTERIM REVENUE                        |  2001-2018   |  Interim Revenue                             |
| REVENUES: PRIOR YEAR REVENUE ADJUSTMENT          |  2001-2018   |  Prior Year Revenue Adjustment               |
| REVENUES: OTHER OPERATING REVENUE                |  2001-2018   |  Other Operating Revenue                     |
| TOTAL OPERATING EXPENDITURES                     |  2001-2018   |  Total Operating Expenditures                |
| EXPENDITURES: ADMINISTRATION                     |  2001-2018   |  Administration                              |
| EXPENDITURES: MAINTENANCE AND GENERAL OPERATIONS |  2001-2018   |  Maintenance and General Operations          |
| EXPENDITURES: PUBLICITY                          |  2001-2018   |  Publicity                                   |
| EXPENDITURES: ATTENDANCE OPERATIONS              |  2001-2018   |  Attendance Operations                       |
| EXPENDITURES: MISCELLANEOUS FAIR                 |  2001-2018   |  Miscellaneous Fair.1                        |
| EXPENDITURES: MISCELLANEOUS NON-FAIR PROGRAMS    |  2001-2018   |  Miscellaneous Non-Fair Programs             |
| EXPENDITURES: PREMIUMS                           |  2001-2018   |  Premiums                                    |
| EXPENDITURES: EXHIBITS                           |  2001-2018   |  Exhibits.1                                  |
| EXPENDITURES: HORSE SHOW                         |  2001-2018   |  Horse Show.1                                |
| EXPENDITURES: MISCELLANEOUS NON-FAIR PROGRAMS    |  2001-2018   |  Miscellaneous Non-Fair Programs             |
| EXPENDITURES: PREMIUMS                           |  2001-2018   |  Premiums                                    |
| EXPENDITURES: EXHIBITS                           |  2001-2018   |  Exhibits.1                                  |

## Drop Table

This table describes the CSV columns that we are removing due to lack of information from year to year

### Class 1

|  YEARS                 |  FEATURE TO DROP  |
|------------------------|-------------------|
|  2001,-15,-16,-17,-18  |  Horse Racing     |
|  2014,-15,-16,-17,-18  |  Carnivals



## Manual Edits that need to be done in cleaning data

2001 - Class 3 row 4 col BD "Remove note"
2002 - Class 4 row 4 col BO "Remove note"
2003 - Class 5 row 7 col BV "Remove note"
2004 - Class 4 row 10 "Remove row"
2005 - Class 2 row 21 "Remove row"
     - Class 5 row 4 "Remove row"
2006 - Class 2 row 21 "Remove row"
     - Class 7 row 5 "Remove row"
2007 - Class 3 row 19 "Remove row"
2012 - Class 1 row 12 "Remove row"
     - Class 2 row 10 "Remove row"
     - Class 3 row 7 "Remove row"
     - Class 3+ row 15 "Remove row"
2013 - Class 1 row 12 "Remove row"
     - Class 2 row 11 "Remove row"
     - Class 3+ row 15 "Remove row"
2014 - Class 1 row 7,12 "Remove row"
     - Class 3 row 6 "Remove row"
     - Class 5 row 4 "Remove row"
2016 - Class 3 row 6 "Remove row"
2018 - Class 3 row 6 "Remove row"
     - Class 7 row 6 "Remove row"
     - Class 4+ row 2 "Remove row"