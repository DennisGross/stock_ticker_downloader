"""This module downloads ticker data from yahoo finance."""
import yfinance as yf
import pandas as pd
from typing import Dict, Any, List
from helper import *

if __name__=="__main__":
    command_line_arguments = get_arguments()
    data_path = command_line_arguments['data_path']
    if command_line_arguments['symbols']=='semis':
        command_line_arguments['symbols'] = '005930.KS,SILXY,AAOI,EMKR,CXCQ,SSLLF,THPTF,QNCCF,SMTC,AUKUF,RNECY,SILXF,MXL,GTAT,QRVO,ADI,CYBL,INTC,SYNA,PAGDF,NVDA,HIMX,SWKS,AOSL,AMSSY,FORM,STRB,BRCHF,MOSY,OIIM,AVGOP,CEVA,MTSI,DSPG,MPWR,AVGO,TXCCQ,IFNNF,STMEF,MCHP,SKYT,ALGM,TSM,VLN,MRAM,ONTO,ON,XLNX,ITCJ,POETF,NMGC,LSCC,WISA,MLXSF,DIOD,PSFT,MX,TXN,FRDSF,STM,UMC,SANJF,MU,SGH,TSEM,CREE,RNECF,GSIT,WKEY,NXPI,NDCVF,RESN,LEDS,NPTN,IMOS,NRSDY,QUIK,NVEC,SIMO,ROHCY,VSH,SLAB,NLST,INTT,ASX,NVTS,MRVL,WOLF,MTNX,PXLW,QCOM,ROHCF,LASR,HHUSF,AMKR,SQNS,SITM,RMBS,RKLY,PRKR,IFNNY,ODII,POWI,CRUS,MMTIF,AMD'
        # Suppliers
        command_line_arguments['symbols'] += ',ACLS,SUMCF,SESMF,BESIY,SCIA,RNWEF,RNWEY,AXTI,OLED,UCTT,KLIC,TGAN,CAMT,BRKS,ASMVF,TOELY,CCMP,AIXXF,AEHR,AMBA,AMAT,RBCN,ATOM,IQEPF,MMAPF,TOELF,MYBUF,COHU,ASML,ASMIY,SODI,IPGP,PLAB,MCRNF,NVMI,LRCX,ENTG,DSCSY,TER,VECO,STRI,NNOCF,SUOPY,TRT,SFDMY,ASMVY,DQ,DISPF,ICHR,SLOIY,GSTX,ASYS,ADTTF,KLAC,XPER,OXINF,SPVNF,ACMR,ATEYY,ASMLF,ASMXF'
    ticker_symbols = get_ticker_symbols(command_line_arguments['symbols'])
    for ticker_symbol in ticker_symbols:
        append_stock_info(ticker_symbol, data_path)
        
