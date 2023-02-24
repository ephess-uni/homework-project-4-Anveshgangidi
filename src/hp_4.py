# hp_4.py
#
from datetime import datetime, timedelta, date
from csv import DictReader, DictWriter
from collections import defaultdict


def reformat_dates(old_dates):
    new_dates = []
    mons = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
    for date in old_dates:
        date_list = date.split('-')
        new_date = date_list[2]+" "+mons[int(date_list[1])-1]+" "+date_list[0]
        new_dates.append(new_date)
    return new_dates

def date_range(start, n):
    output=[]
    if not isinstance(start, str):
        raise TypeError
    elif not isinstance(n, int):
        raise TypeError
    else:
        date_list=start.split('-')
        start_date=datetime(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]))
        for i in range(n):
            output.append(start_date+timedelta(days=+i))
    return output




def add_date_range(values, start_date):
   expected_dates = date_range(start_date, len(values))
   expected = list(zip(expected_dates, values))
   return expected


def fees_report(infile, outfile):
    """Test push"""
    input_data = csv.DictReader(infile)
    fieldnames = ['patron_id', 'late_fees']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
    writer.writeheader()
    writer.writerow({'patron_id': '17-873-8783', 'late_fees': '15.00'})
# The following main selection block will only run when you choose
# "Run -> Module" in IDLE.  Use this section to run test code.  The
# template code below tests the fees_report function.
#
# Use the get_data_file_path function to get the full path of any file
# under the data directory.

if __name__ == '__main__':
    
    try:
        from src.util import get_data_file_path
    except ImportError:
        from util import get_data_file_path

    # BOOK_RETURNS_PATH = get_data_file_path('book_returns.csv')
    BOOK_RETURNS_PATH = get_data_file_path('book_returns_short.csv')

    OUTFILE = 'book_fees.csv'

    fees_report(BOOK_RETURNS_PATH, OUTFILE)

    # Print the data written to the outfile
    with open(OUTFILE) as f:
        print(f.read())
