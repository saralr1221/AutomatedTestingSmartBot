#!/usr/bin python
# -*- coding: utf-8 -*-

#srieck 4.11.2025

import pandas as pd 

df = pd.read_csv(r'C:\Users\Sara.Rieck\OneDrive - FDA\Documents\DAS TO 9050\Code\docuBridgeTestSmartBot1\test2.csv', dtype={'Sequence': str})

i_start = 0
i_end = len(df)
# i_end = 20
#5