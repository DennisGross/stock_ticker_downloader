"""This module downloads ticker data from yahoo finance."""
import argparse
import sys
import os
import yfinance as yf
import pandas as pd
import time
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
    df.to_csv(ticker_file_path, index=False)

def append_stock_info(ticker_symbol:str, data_path:str):
    """Stores/Add Stock info

    Args:
        ticker_symbol (str): Ticker Symbol
        data_path (str): Root path to data folder
    """
    market_cap_file_path = os.path.join(data_path, str(ticker_symbol) + "_info.csv")
    stock = yf.Ticker(ticker_symbol)
    try:
        market_cap = stock.info['marketCap']
    except:
        market_cap = -1
    try:
        currency = stock.info['financialCurrency']
    except:
        currency = "NAN"


    time_stamp = time.time()
    f = open(market_cap_file_path,'a')
    f.write(str(time_stamp) + ',' + str(market_cap) + ',' + str(currency) + '\n')
    f.close()


if __name__=="__main__":
    command_line_arguments = get_arguments()
    data_path = command_line_arguments['data_path']
    if command_line_arguments['symbols']=='semis':
        command_line_arguments['symbols'] = '005930.KS,SILXY,AAOI,EMKR,CXCQ,SSLLF,THPTF,QNCCF,SMTC,AUKUF,RNECY,SILXF,MXL,GTAT,QRVO,ADI,CYBL,INTC,SYNA,PAGDF,NVDA,HIMX,SWKS,AOSL,AMSSY,FORM,STRB,BRCHF,MOSY,OIIM,AVGOP,CEVA,MTSI,DSPG,MPWR,AVGO,TXCCQ,IFNNF,STMEF,MCHP,SKYT,ALGM,TSM,VLN,MRAM,ONTO,ON,XLNX,ITCJ,POETF,NMGC,LSCC,WISA,MLXSF,DIOD,PSFT,MX,TXN,FRDSF,STM,UMC,SANJF,MU,SGH,TSEM,CREE,RNECF,GSIT,WKEY,NXPI,NDCVF,RESN,LEDS,NPTN,IMOS,NRSDY,QUIK,NVEC,SIMO,ROHCY,VSH,SLAB,NLST,INTT,ASX,NVTS,MRVL,WOLF,MTNX,PXLW,QCOM,ROHCF,LASR,HHUSF,AMKR,SQNS,SITM,RMBS,RKLY,PRKR,IFNNY,ODII,POWI,CRUS,MMTIF,AMD'
        # Suppliers
        command_line_arguments['symbols'] += ',ACLS,SUMCF,SESMF,BESIY,SCIA,RNWEF,RNWEY,AXTI,OLED,UCTT,KLIC,TGAN,CAMT,BRKS,ASMVF,TOELY,CCMP,AIXXF,AEHR,AMBA,AMAT,RBCN,ATOM,IQEPF,MMAPF,TOELF,MYBUF,COHU,ASML,ASMIY,SODI,IPGP,PLAB,MCRNF,NVMI,LRCX,ENTG,DSCSY,TER,VECO,STRI,NNOCF,SUOPY,TRT,SFDMY,ASMVY,DQ,DISPF,ICHR,SLOIY,GSTX,ASYS,ADTTF,KLAC,XPER,OXINF,SPVNF,ACMR,ATEYY,ASMLF,ASMXF'
    ticker_symbols = get_ticker_symbols(command_line_arguments['symbols'])
    for ticker_symbol in ticker_symbols:
        ticker_data = yf.download(tickers=ticker_symbol, period=command_line_arguments['period'],interval=command_line_arguments['interval'])
        #append_stock_info(ticker_symbol, data_path)
        store_ticker_data(data_path, ticker_symbol, ticker_data)
