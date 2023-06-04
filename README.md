
# FNO Prerequisites

A rough-and-ready method to set up some config files ahead of open.

These files will help us smoothly deal with freeze quantities and lot sizes for different indices based on their expiries.






## Usage/Examples

Load TOML Configuration file
```python

import toml
from typing import Optional, Dict, Any


def load_configurations(file_path) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r') as file:
            config = toml.load(file)
            return config
    except FileNotFoundError as FFE:
        print(f"{FFE.__str__()}")
        return None
    except Exception as E:
        print(f"{E.__str__()}")
        return None
```

For Index Futures
```python

index_FUT = load_configurations(file_path="IDX_FUT.toml")

print(index_FUT)

```
Result 
```javascript
{
   "NIFTY":[
      {
         "tradingsymbol":"NIFTY23JUNFUT",
         "expiry":"2023-06-29",
         "lot_size":50,
         "freeze_qty":1800
      },
      {
         "tradingsymbol":"NIFTY23JULFUT",
         "expiry":"2023-07-27",
         "lot_size":50,
         "freeze_qty":1800
      },
      {
         "tradingsymbol":"NIFTY23AUGFUT",
         "expiry":"2023-08-31",
         "lot_size":50,
         "freeze_qty":1800
      }
   ],
   "BANKNIFTY":[
      {
         "tradingsymbol":"BANKNIFTY23JUNFUT",
         "expiry":"2023-06-29",
         "lot_size":25,
         "freeze_qty":900
      },
      {
         "tradingsymbol":"BANKNIFTY23JULFUT",
         "expiry":"2023-07-27",
         "lot_size":15,
         "freeze_qty":900
      },
      {
         "tradingsymbol":"BANKNIFTY23AUGFUT",
         "expiry":"2023-08-31",
         "lot_size":15,
         "freeze_qty":900
      }
   ],
   "FINNIFTY":[
      {
         "tradingsymbol":"FINNIFTY23JUNFUT",
         "expiry":"2023-06-27",
         "lot_size":40,
         "freeze_qty":1800
      },
      {
         "tradingsymbol":"FINNIFTY23JULFUT",
         "expiry":"2023-07-25",
         "lot_size":40,
         "freeze_qty":1800
      },
      {
         "tradingsymbol":"FINNIFTY23AUGFUT",
         "expiry":"2023-08-29",
         "lot_size":40,
         "freeze_qty":1800
      }
   ]
}

```
For Index Options 
```python

index_OPT = load_configurations(file_path="IDX_OPT.toml")
print(index_OPT)

```
Result
```javascript
{
   "FINNIFTY":[
      {
         "expiry":"2023-06-06",
         "lot_size":40,
         "exp_frmt":"23606",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-06-13",
         "lot_size":40,
         "exp_frmt":"23613",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-06-20",
         "lot_size":40,
         "exp_frmt":"23620",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-06-27",
         "lot_size":40,
         "exp_frmt":"23JUN",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-07-04",
         "lot_size":40,
         "exp_frmt":"23704",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-07-25",
         "lot_size":40,
         "exp_frmt":"23JUL",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-08-29",
         "lot_size":40,
         "exp_frmt":"23AUG",
         "freeze_qty":1800
      }
   ],
   "NIFTY":[
      {
         "expiry":"2023-06-08",
         "lot_size":50,
         "exp_frmt":"23608",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-06-15",
         "lot_size":50,
         "exp_frmt":"23615",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-06-22",
         "lot_size":50,
         "exp_frmt":"23622",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-06-29",
         "lot_size":50,
         "exp_frmt":"23JUN",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-07-06",
         "lot_size":50,
         "exp_frmt":"23706",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-07-27",
         "lot_size":50,
         "exp_frmt":"23JUL",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-08-31",
         "lot_size":50,
         "exp_frmt":"23AUG",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-09-28",
         "lot_size":50,
         "exp_frmt":"23SEP",
         "freeze_qty":1800
      },
      {
         "expiry":"2023-12-28",
         "lot_size":50,
         "exp_frmt":"23DEC",
         "freeze_qty":1800
      },
      {
         "expiry":"2024-03-28",
         "lot_size":50,
         "exp_frmt":"24MAR",
         "freeze_qty":1800
      },
      {
         "expiry":"2024-06-27",
         "lot_size":50,
         "exp_frmt":"24JUN",
         "freeze_qty":1800
      },
      {
         "expiry":"2024-12-26",
         "lot_size":50,
         "exp_frmt":"24DEC",
         "freeze_qty":1800
      },
      {
         "expiry":"2025-06-26",
         "lot_size":50,
         "exp_frmt":"25JUN",
         "freeze_qty":1800
      },
      {
         "expiry":"2025-12-24",
         "lot_size":50,
         "exp_frmt":"25DEC",
         "freeze_qty":1800
      },
      {
         "expiry":"2026-06-25",
         "lot_size":50,
         "exp_frmt":"26JUN",
         "freeze_qty":1800
      },
      {
         "expiry":"2026-12-31",
         "lot_size":50,
         "exp_frmt":"26DEC",
         "freeze_qty":1800
      },
      {
         "expiry":"2027-06-24",
         "lot_size":50,
         "exp_frmt":"27JUN",
         "freeze_qty":1800
      },
      {
         "expiry":"2027-12-30",
         "lot_size":50,
         "exp_frmt":"27DEC",
         "freeze_qty":1800
      }
   ],
   "BANKNIFTY":[
      {
         "expiry":"2023-06-08",
         "lot_size":25,
         "exp_frmt":"23608",
         "freeze_qty":900
      },
      {
         "expiry":"2023-06-15",
         "lot_size":25,
         "exp_frmt":"23615",
         "freeze_qty":900
      },
      {
         "expiry":"2023-06-22",
         "lot_size":25,
         "exp_frmt":"23622",
         "freeze_qty":900
      },
      {
         "expiry":"2023-06-29",
         "lot_size":25,
         "exp_frmt":"23JUN",
         "freeze_qty":900
      },
      {
         "expiry":"2023-07-06",
         "lot_size":25,
         "exp_frmt":"23706",
         "freeze_qty":900
      },
      {
         "expiry":"2023-07-27",
         "lot_size":15,
         "exp_frmt":"23JUL",
         "freeze_qty":900
      },
      {
         "expiry":"2023-08-31",
         "lot_size":15,
         "exp_frmt":"23AUG",
         "freeze_qty":900
      },
      {
         "expiry":"2023-09-28",
         "lot_size":25,
         "exp_frmt":"23SEP",
         "freeze_qty":900
      },
      {
         "expiry":"2023-12-28",
         "lot_size":25,
         "exp_frmt":"23DEC",
         "freeze_qty":900
      },
      {
         "expiry":"2024-03-28",
         "lot_size":25,
         "exp_frmt":"24MAR",
         "freeze_qty":900
      }
   ]
}

```