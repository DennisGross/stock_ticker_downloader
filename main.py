"""This module downloads ticker data from yahoo finance."""
import argparse
import sys
import os
import yfinance as yf
import pandas as pd
from typing import Dict, Any, List

def get_arguments() -> Dict[str, Any]:
    """Parses all the command line arguments
    Returns:
        Dict[str, Any]: dictionary with the command line arguments as key and their assignment as value
    """
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = argparse.Namespace()
    arg_parser.add_argument('--data_path', help='Root Path to the folder of all the ticker data', type=str,
                            default='')
    arg_parser.add_argument('--symbols', help='All Ticker Symbols seperated by a commata.', type=str, default='')
    arg_parser.add_argument('--period', help='Time Period of Ticker data', type=str, default='')
    arg_parser.add_argument('--interval', help='Interval of Ticker data', type=str, default='')

    args, _ = arg_parser.parse_known_args(sys.argv)
    return vars(args)

def get_ticker_symbols(ticker_symbols_input: str)->List[str]:
    """Get ticker symbols from command line argument

    Args:
        ticker_symbols_input (str): Ticker symbols seperated by commata

    Returns:
        List[str]: List of ticker symbols
    """
    return str(ticker_symbols_input).split(",")

def store_ticker_data(data_path:str, ticker_symbol:str, ticker_data:pd.DataFrame):
    """Stores/Add ticker data to file

    Args:
        data_path (str): Root path to data folder
        ticker_symbol (str): Ticker Symbol
        ticker_data (pd.DataFrame): Ticker Data
    """
    ticker_file_path = os.path.join(data_path, str(ticker_symbol) + ".csv")
    # Modify Ticker Data
    ticker_data['Datetime'] = ticker_data.index
    ticker_data.reset_index(drop=True, inplace=True)
    # Check if folder exists?
    if os.path.exists(data_path) is False:
        os.mkdir(data_path)
    if os.path.exists(ticker_file_path):
        df = pd.read_csv(ticker_file_path)
        df['Datetime'] = pd.to_datetime(df['Datetime'])
        df = pd.concat([df,ticker_data]).reset_index(drop=True).drop_duplicates(subset=['Datetime']).sort_values(by=['Datetime'])
    else:
        df = ticker_data
    print(df)
    df.to_csv(ticker_file_path, index=False)



if __name__=="__main__":
    command_line_arguments = get_arguments()
    data_path = command_line_arguments['data_path']
    ticker_symbols = get_ticker_symbols(command_line_arguments['symbols'])
    for ticker_symbol in ticker_symbols:
        ticker_data = yf.download(tickers=ticker_symbol, period=command_line_arguments['period'],interval=command_line_arguments['interval'])
        store_ticker_data(data_path, ticker_symbol, ticker_data)
    print("SUCCESS")
