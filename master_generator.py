import datetime as dt
import os
from pathlib import Path
from pprint import pprint
from typing import Union, Dict

import pandas as pd
import toml
import logging

DEV_MODE = False

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('execution.log')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
if DEV_MODE:
    logger.addHandler(console_handler)
logger.addHandler(file_handler)


class FNOPR:
    def __init__(self):
        self.INSTRUMENTS_URL = "https://api.kite.trade/instruments/NFO"
        self.NSE_FREEZE_QTY_URL = "https://archives.nseindia.com/content/fo/qtyfreeze.xls"
        self.INSTRUMENT_FILENAME = "master_instruments.csv"
        self.MASTER_FILENAME = "master.toml"
        self.FUT_FILENAME = "IDX_FUT.toml"
        self.OPTIONS_FILENAME = "IDX_OPT.toml"
        self.INDICES = ["NIFTY", "BANKNIFTY", "FINNIFTY"]
        self.FREEZE_QTY = self.get_freeze_quantity()

        if self.last_update():
            self.download_latest_file()
        else:
            print(f"Instrument File already up to date. Proceed further.")
            logging.info(f"Instrument File already up to date. Proceed further.")

        self.get_index_futures_info()
        self.get_index_options_info()

    def download_latest_file(self) -> None:
        try:
            df = pd.read_csv(self.INSTRUMENTS_URL)
            df.to_csv(self.INSTRUMENT_FILENAME)

            timestamp = dt.datetime.now()
            data = {"generated_timestamp": str(timestamp)}
            self.write_master(self.MASTER_FILENAME, toml_data=data)
            logger.info(f"Instruments File downloaded successfully.")

        except OSError as OSE:
            logger.exception(OSE)
        except RuntimeError as RE:
            logger.exception(RE)
        except Exception as E:
            logger.exception(E)

    @staticmethod
    def read_master(
            master_file_path: Union[str, Path]
    ):
        try:
            with open(master_file_path, "r") as f:
                master_data = toml.load(f)
                return master_data
        except FileNotFoundError:
            logger.error(f"{master_file_path} not found.")
            return None
        except Exception as E:
            logger.exception(E)
            return None

    @staticmethod
    def write_master(
            master_file_path: Union[str, Path],
            toml_data: Dict
    ) -> None:
        try:
            with open(master_file_path, "w") as f:
                toml.dump(toml_data, f)
            logger.info(f"{master_file_path} prepared successfully.")
        except Exception as E:
            logger.exception(E)

    @staticmethod
    def update_master(
            master_file_path: Union[str, Path],
            data_list: Dict
    ) -> None:
        try:
            toml_data = FNOPR.read_master(master_file_path)
            if toml_data is not None:
                toml_data.update(data_list)
                FNOPR.write_master(master_file_path, toml_data)
        except Exception as E:
            logger.exception(E)

    def last_update(self) -> bool:
        try:
            data = self.read_master(self.MASTER_FILENAME)
            if data is not None:
                given_timestamp = dt.datetime.strptime(data["generated_timestamp"], '%Y-%m-%d %H:%M:%S.%f')
                current_time = dt.datetime.now()
                time_difference = current_time - given_timestamp
                return time_difference >= dt.timedelta(hours=12)
            else:
                return True

        except ValueError as VE:
            logger.error(f"Invalid Time Format {VE.__str__()}")
            return False
        except Exception as E:
            logger.exception(E)
            return True

    def get_index_futures_info(self) -> None:
        try:
            data = pd.read_csv(self.INSTRUMENT_FILENAME)

            df = data.query("segment == 'NFO-FUT' and name in @self.INDICES")[
                ["name", "tradingsymbol", "expiry", "lot_size"]]
            df['freeze_qty'] = df['name'].map(self.FREEZE_QTY)

            result = {
                name: sorted([
                    {
                        'tradingsymbol': trading_symbol,
                        'expiry': expiry,
                        'lot_size': lot_size,
                        'freeze_qty': freeze_qty
                    }
                    for trading_symbol, expiry, lot_size, freeze_qty in zip(
                        df[df['name'] == name]['tradingsymbol'],
                        df[df['name'] == name]['expiry'],
                        df[df['name'] == name]['lot_size'],
                        df[df['name'] == name]['freeze_qty']
                    )
                ],
                    key=lambda r: r["expiry"]
                )
                for name in df['name'].unique()
            }

            self.write_master(self.FUT_FILENAME, toml_data=result)
        except Exception as E:
            logger.exception(E)

    def get_index_options_info(self) -> None:
        try:
            data = pd.read_csv(self.INSTRUMENT_FILENAME)
            df = data.query("segment == 'NFO-OPT' and name in @self.INDICES")[
                ["name", "tradingsymbol", "expiry", "lot_size"]].drop_duplicates(subset=["name", "expiry"],
                                                                                 keep="first").sort_values("expiry")
            df['freeze_qty'] = df['name'].map(self.FREEZE_QTY)
            df['exp_frmt'] = df.apply(lambda row: row['tradingsymbol'].replace(row['name'], '')[:5], axis=1)
            df.drop('tradingsymbol', axis=1, inplace=True)

            result = {
                name: sorted([
                    {
                        'expiry': expiry,
                        'lot_size': lot_size,
                        'exp_frmt': exp_frmt,
                        'freeze_qty': freeze_qty

                    }
                    for expiry, lot_size, exp_frmt, freeze_qty in zip(
                        df[df['name'] == name]['expiry'],
                        df[df['name'] == name]['lot_size'],
                        df[df['name'] == name]['exp_frmt'],
                        df[df['name'] == name]['freeze_qty']
                    )
                ],
                    key=lambda x: x["expiry"]
                )
                for name in df['name'].unique()
            }

            self.write_master(self.OPTIONS_FILENAME, toml_data=result)
        except Exception as E:
            logger.exception(E)

    def get_freeze_quantity(self):
        try:
            df = pd.read_excel(self.NSE_FREEZE_QTY_URL, index_col=0)
            df.columns = df.columns.str.replace(' ', '')
            df["SYMBOL"] = df["SYMBOL"].str.strip()
            df = df.query("SYMBOL in @self.INDICES")
            return df.set_index('SYMBOL')['VOL_FRZ_QTY'].to_dict()

        except Exception as E:
            logger.error(f"Freeze Quantity Fetch Failed {E.__str__()}")


if __name__ == '__main__':
    FNOPR = FNOPR()
