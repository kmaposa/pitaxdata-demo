"""
This script prepares the cross-section sample for 2017. For now, we treat this
sample as being representative (even though it may not be). 

We assume that aggregate totals have already been calcuated for the full data.
They must be saved in some form, and we will store them in agg_results.

For now, we produce the sample weight for the entire sample. A subsequent
improvement should produce aggregate results by industry/sector, and produce
weights by industry/sector. 

We may also want to consider weight adjustments to target other results, such
as totals for other measures and the distribution of firm sizes.
"""
import numpy as np
import pandas as pd

# Get data for 2017
data_full = pd.read_excel('ITR6_2017_2013_BAL_PANEL_FINAL.xlsx',
                       sheet_name='Sheet2')

# Rename some variables
renames = {'SHORT_TERM_15PER': 'ST_CG_AMT_1', 'SHORT_TERM_30PER': 'ST_CG_AMT_2',
           'LONG_TERM_10PER': 'LT_CG_AMT_1', 'LONG_TERM_20PER': 'LT_CG_AMT_2',
           'SHORT_TERM_APPRATE': 'ST_CG_AMT_APPRATE',
           'TOTAL_INCOME_ALL':'GTI_BEFORE_LOSSES', 'PAN_NO_HASH': 'ID_NO',
           'AY_0910_AMT_AMT_LOSS_BUSOTHSPL': 'AY_0910_AMT_LOSS_BUSOTHSPL'}
data_full = data_full.rename(renames, axis=1)
data_full = data_full.fillna(0)

"""
The following code handles the losses.
"""
"""
# Create empty loss variables
loss_lag8 = np.zeros(len(data_full))
loss_lag7 = np.zeros(len(data_full))
loss_lag6 = np.zeros(len(data_full))
loss_lag5 = np.zeros(len(data_full))
loss_lag4 = np.zeros(len(data_full))
loss_lag3 = np.zeros(len(data_full))
loss_lag2 = np.zeros(len(data_full))
loss_lag1 = np.zeros(len(data_full))

def get_loss_type(year, lagnum, losstype):
    
    Returns an array of the given loss type with the appropriate lag from the
    given year.
    
    loss = np.zeros(len(data_full))
    lagyear = year - lagnum
    if lagyear < 2007:
        loss = np.zeros(len(data_full))
    elif lagyear == 2007:
        loss = np.array(data_full['AY_0708_AMT_LOSS_' + losstype])
    elif lagyear == 2008:
        loss = np.array(data_full['AY_0809_AMT_LOSS_' + losstype])
    elif lagyear == 2009:
        loss = np.array(data_full['AY_0910_AMT_LOSS_' + losstype])
    elif lagyear == 2010:
        loss = np.array(data_full['AY_1011_AMT_LOSS_' + losstype])
    elif lagyear == 2011:
        loss = np.array(data_full['AY_1112_AMT_LOSS_' + losstype])
    elif lagyear == 2012:
        loss = np.array(data_full['AY_1213_AMT_LOSS_' + losstype])
    elif lagyear == 2013:
        loss = np.array(data_full['AY_1314_AMT_LOSS_' + losstype])
    elif lagyear == 2014:
        loss = np.array(data_full['AY_1415_AMT_LOSS_' + losstype])
    else:
        loss = np.zeros(len(data_full))
    loss2 = np.where(data_full.ASSESSMENT_YEAR == year, loss, 0)
    return loss2

losstypelist = ['HPL', 'BUSOTHSPL', 'LSPCLTVBUS', 'LSPCFDBUS', 'STCL', 'LTCL',
                'OSLHR']

for losstype in losstypelist:
    loss_lag1 += np.where(data_full.ASSESSMENT_YEAR == 2017,
                          get_loss_type(2017, 1, losstype), 0.)
    loss_lag2 += np.where(data_full.ASSESSMENT_YEAR == 2017,
                          get_loss_type(2017, 2, losstype), 0.)
    loss_lag3 += np.where(data_full.ASSESSMENT_YEAR == 2017,
                          get_loss_type(2017, 3, losstype), 0.)
    loss_lag4 += np.where(data_full.ASSESSMENT_YEAR == 2017,
                          get_loss_type(2017, 4, losstype), 0.)
    loss_lag5 += np.where(data_full.ASSESSMENT_YEAR == 2017,
                          get_loss_type(2017, 5, losstype), 0.)
    loss_lag6 += np.where(data_full.ASSESSMENT_YEAR == 2017,
                          get_loss_type(2017, 6, losstype), 0.)
    loss_lag7 += np.where(data_full.ASSESSMENT_YEAR == 2017,
                          get_loss_type(2017, 7, losstype), 0.)
    loss_lag8 += np.where(data_full.ASSESSMENT_YEAR == 2017,
                          get_loss_type(2017, 8, losstype), 0.)

data_full['LOSS_LAG1'] = loss_lag1
data_full['LOSS_LAG2'] = loss_lag2
data_full['LOSS_LAG3'] = loss_lag3
data_full['LOSS_LAG4'] = loss_lag4
data_full['LOSS_LAG5'] = loss_lag5
data_full['LOSS_LAG6'] = loss_lag6
data_full['LOSS_LAG7'] = loss_lag7
data_full['LOSS_LAG8'] = loss_lag8
"""

data13 = data_full[data_full.ASSESSMENT_YEAR == 2013].reset_index()
data14 = data_full[data_full.ASSESSMENT_YEAR == 2014].reset_index()
data15 = data_full[data_full.ASSESSMENT_YEAR == 2015].reset_index()
data16 = data_full[data_full.ASSESSMENT_YEAR == 2016].reset_index()
data17 = data_full[data_full.ASSESSMENT_YEAR == 2017].reset_index()




"""
The following code handles the losses.
"""
# Create empty loss variables
loss_lag8 = np.zeros(len(data13))
loss_lag7 = np.zeros(len(data13))
loss_lag6 = np.zeros(len(data13))
loss_lag5 = np.zeros(len(data13))
loss_lag4 = np.zeros(len(data13))
loss_lag3 = np.zeros(len(data13))
loss_lag2 = np.zeros(len(data13))
loss_lag1 = np.zeros(len(data13))

def get_loss_type(year, lagnum, losstype):
    """
    Returns an array of the given loss type with the appropriate lag from the
    given year.
    """
    loss = np.zeros(len(data_full))
    lagyear = year - lagnum
    if lagyear < 2007:
        loss = np.zeros(len(data_full))
    elif lagyear == 2007:
        loss = np.array(data_full['AY_0708_AMT_LOSS_' + losstype])
    elif lagyear == 2008:
        loss = np.array(data_full['AY_0809_AMT_LOSS_' + losstype])
    elif lagyear == 2009:
        loss = np.array(data_full['AY_0910_AMT_LOSS_' + losstype])
    elif lagyear == 2010:
        loss = np.array(data_full['AY_1011_AMT_LOSS_' + losstype])
    elif lagyear == 2011:
        loss = np.array(data_full['AY_1112_AMT_LOSS_' + losstype])
    elif lagyear == 2012:
        loss = np.array(data_full['AY_1213_AMT_LOSS_' + losstype])
    elif lagyear == 2013:
        loss = np.array(data_full['AY_1314_AMT_LOSS_' + losstype])
    elif lagyear == 2014:
        loss = np.array(data_full['AY_1415_AMT_LOSS_' + losstype])
    else:
        loss = np.zeros(len(data_full))
    loss2 = loss[data_full.ASSESSMENT_YEAR == year]
    return loss2

losstypelist = ['HPL', 'BUSOTHSPL', 'LSPCLTVBUS', 'LSPCFDBUS', 'STCL', 'LTCL',
                'OSLHR']

# Produce the loss lags for 2013
for losstype in losstypelist:
    loss_lag1 += get_loss_type(2013, 1, losstype)
    loss_lag2 += get_loss_type(2013, 2, losstype)
    loss_lag3 += get_loss_type(2013, 3, losstype)
    loss_lag4 += get_loss_type(2013, 4, losstype)
    loss_lag5 += get_loss_type(2013, 5, losstype)
    loss_lag6 += get_loss_type(2013, 6, losstype)
    loss_lag7 += get_loss_type(2013, 7, losstype)
    loss_lag8 += get_loss_type(2013, 8, losstype)
    

def calc_new_lags(dat):
    """
    Calculates the new lags
    """
    LOSS_LAGS = [dat.LOSS_LAG1, dat.LOSS_LAG2, dat.LOSS_LAG3, dat.LOSS_LAG4,
                 dat.LOSS_LAG5, dat.LOSS_LAG6, dat.LOSS_LAG7, dat.LOSS_LAG8]
    PRFT_GAIN_BP_INC_115BBF = np.zeros(len(dat))
    Income_BP = (dat.PRFT_GAIN_BP_OTHR_SPECLTV_BUS + dat.PRFT_GAIN_BP_SPECLTV_BUS +
                 dat.PRFT_GAIN_BP_SPCFD_BUS + PRFT_GAIN_BP_INC_115BBF)
    GTI_Before_Loss = (dat.INCOME_HP + Income_BP + dat.ST_CG_AMT_1 + dat.ST_CG_AMT_2 +
                       dat.ST_CG_AMT_APPRATE + dat.LT_CG_AMT_1 + dat.LT_CG_AMT_2 +
                       dat.TOTAL_INCOME_OS)
    CY_Losses = np.array(dat['CYL_SET_OFF'])
    GTI1 = np.maximum(GTI_Before_Loss - CY_Losses, 0.)
    newloss1 = GTI1 - GTI_Before_Loss + CY_Losses
    USELOSS = [np.zeros(len(dat))] * 8
    for i in range(8, 0, -1):
        USELOSS[i-1] = np.minimum(GTI1, LOSS_LAGS[i-1])
        GTI1 = GTI1 - USELOSS[i-1]
    dat['newloss1'] = newloss1
    dat['newloss2'] = LOSS_LAGS[0] - USELOSS[0]
    dat['newloss3'] = LOSS_LAGS[1] - USELOSS[1]
    dat['newloss4'] = LOSS_LAGS[2] - USELOSS[2]
    dat['newloss5'] = LOSS_LAGS[3] - USELOSS[3]
    dat['newloss6'] = LOSS_LAGS[4] - USELOSS[4]
    dat['newloss7'] = LOSS_LAGS[5] - USELOSS[5]
    dat['newloss8'] = LOSS_LAGS[6] - USELOSS[6]
    return(dat)


data13['LOSS_LAG1'] = loss_lag1
data13['LOSS_LAG2'] = loss_lag2
data13['LOSS_LAG3'] = loss_lag3
data13['LOSS_LAG4'] = loss_lag4
data13['LOSS_LAG5'] = loss_lag5
data13['LOSS_LAG6'] = loss_lag6
data13['LOSS_LAG7'] = loss_lag7
data13['LOSS_LAG8'] = loss_lag8
data13c = calc_new_lags(data13)


carryforward_df = pd.DataFrame({'ID_NO': data13c.ID_NO,
                                'newloss1': data13c.newloss1,
                                'newloss2': data13c.newloss2,
                                'newloss3': data13c.newloss3,
                                'newloss4': data13c.newloss4,
                                'newloss5': data13c.newloss5,
                                'newloss6': data13c.newloss6,
                                'newloss7': data13c.newloss7,
                                'newloss8': data13c.newloss8})
# Update loss lags for 2014 data
data14a = data14.merge(right=carryforward_df, how='outer', on='ID_NO', indicator=True)
merge_info = np.array(data14a['_merge'])
to_update = np.where(merge_info == 'both', True, False)
to_keep = np.where(merge_info != 'right_only', True, False)
data14a['LOSS_LAG1'] = np.where(to_update, data14a['newloss1'], 0)
data14a['LOSS_LAG2'] = np.where(to_update, data14a['newloss2'], 0)
data14a['LOSS_LAG3'] = np.where(to_update, data14a['newloss3'], 0)
data14a['LOSS_LAG4'] = np.where(to_update, data14a['newloss4'], 0)
data14a['LOSS_LAG5'] = np.where(to_update, data14a['newloss5'], 0)
data14a['LOSS_LAG6'] = np.where(to_update, data14a['newloss6'], 0)
data14a['LOSS_LAG7'] = np.where(to_update, data14a['newloss7'], 0)
data14a['LOSS_LAG8'] = np.where(to_update, data14a['newloss8'], 0)
data14b = data14a[to_keep].reset_index()
data14c = calc_new_lags(data14b)

# Repeat for 2015
carryforward_df = pd.DataFrame({'ID_NO': data14c.ID_NO,
                                'newloss1': data14c.newloss1,
                                'newloss2': data14c.newloss2,
                                'newloss3': data14c.newloss3,
                                'newloss4': data14c.newloss4,
                                'newloss5': data14c.newloss5,
                                'newloss6': data14c.newloss6,
                                'newloss7': data14c.newloss7,
                                'newloss8': data14c.newloss8})
# Update loss lags for 2015 data
data15a = data15.merge(right=carryforward_df, how='outer', on='ID_NO', indicator=True)
merge_info = np.array(data15a['_merge'])
to_update = np.where(merge_info == 'both', True, False)
to_keep = np.where(merge_info != 'right_only', True, False)
data15a['LOSS_LAG1'] = np.where(to_update, data15a['newloss1'], 0)
data15a['LOSS_LAG2'] = np.where(to_update, data15a['newloss2'], 0)
data15a['LOSS_LAG3'] = np.where(to_update, data15a['newloss3'], 0)
data15a['LOSS_LAG4'] = np.where(to_update, data15a['newloss4'], 0)
data15a['LOSS_LAG5'] = np.where(to_update, data15a['newloss5'], 0)
data15a['LOSS_LAG6'] = np.where(to_update, data15a['newloss6'], 0)
data15a['LOSS_LAG7'] = np.where(to_update, data15a['newloss7'], 0)
data15a['LOSS_LAG8'] = np.where(to_update, data15a['newloss8'], 0)
data15b = data15a[to_keep].reset_index()
data15c = calc_new_lags(data15b)

# Repeat for 2016
carryforward_df = pd.DataFrame({'ID_NO': data15c.ID_NO,
                                'newloss1': data15c.newloss1,
                                'newloss2': data15c.newloss2,
                                'newloss3': data15c.newloss3,
                                'newloss4': data15c.newloss4,
                                'newloss5': data15c.newloss5,
                                'newloss6': data15c.newloss6,
                                'newloss7': data15c.newloss7,
                                'newloss8': data15c.newloss8})
# Update loss lags for 2016 data
data16a = data16.merge(right=carryforward_df, how='outer', on='ID_NO', indicator=True)
merge_info = np.array(data16a['_merge'])
to_update = np.where(merge_info == 'both', True, False)
to_keep = np.where(merge_info != 'right_only', True, False)
data16a['LOSS_LAG1'] = np.where(to_update, data16a['newloss1'], 0)
data16a['LOSS_LAG2'] = np.where(to_update, data16a['newloss2'], 0)
data16a['LOSS_LAG3'] = np.where(to_update, data16a['newloss3'], 0)
data16a['LOSS_LAG4'] = np.where(to_update, data16a['newloss4'], 0)
data16a['LOSS_LAG5'] = np.where(to_update, data16a['newloss5'], 0)
data16a['LOSS_LAG6'] = np.where(to_update, data16a['newloss6'], 0)
data16a['LOSS_LAG7'] = np.where(to_update, data16a['newloss7'], 0)
data16a['LOSS_LAG8'] = np.where(to_update, data16a['newloss8'], 0)
data16b = data16a[to_keep].reset_index()
data16c = calc_new_lags(data16b)

# Repeat for 2017
carryforward_df = pd.DataFrame({'ID_NO': data16c.ID_NO,
                                'newloss1': data16c.newloss1,
                                'newloss2': data16c.newloss2,
                                'newloss3': data16c.newloss3,
                                'newloss4': data16c.newloss4,
                                'newloss5': data16c.newloss5,
                                'newloss6': data16c.newloss6,
                                'newloss7': data16c.newloss7,
                                'newloss8': data16c.newloss8})
data17a = data17.merge(right=carryforward_df, how='outer', on='ID_NO', indicator=True)
merge_info = np.array(data17a['_merge'])
to_update = np.where(merge_info == 'both', True, False)
to_keep = np.where(merge_info != 'right_only', True, False)
data17a['LOSS_LAG1'] = np.where(to_update, data17a['newloss1'], 0)
data17a['LOSS_LAG2'] = np.where(to_update, data17a['newloss2'], 0)
data17a['LOSS_LAG3'] = np.where(to_update, data17a['newloss3'], 0)
data17a['LOSS_LAG4'] = np.where(to_update, data17a['newloss4'], 0)
data17a['LOSS_LAG5'] = np.where(to_update, data17a['newloss5'], 0)
data17a['LOSS_LAG6'] = np.where(to_update, data17a['newloss6'], 0)
data17a['LOSS_LAG7'] = np.where(to_update, data17a['newloss7'], 0)
data17a['LOSS_LAG8'] = np.where(to_update, data17a['newloss8'], 0)
data17 = data17a[to_keep].reset_index()




#data17 = data_full[data_full['ASSESSMENT_YEAR'] == 2017].reset_index()
count = len(data17)



# Average amounts per company from the 2017 full sample
total_returns = 790443.0

# Calculate weights
#WGT2017 = total_returns / count
WGT2017 = 3954771854602 / sum(data_full['AGGREGATE_LIABILTY'])
# Assume 10% growth rate in number of firms filing
weights_df = pd.DataFrame({'WT2017': [WGT2017] * count,
                           'WT2018': [WGT2017 * 1.1] * count,
                           'WT2019': [WGT2017 * 1.1**2] * count,
                           'WT2020': [WGT2017 * 1.1**3] * count,
                           'WT2021': [WGT2017 * 1.1**4] * count})

# Export results
data17.round(6)
data17.to_csv('cit_cross.csv', index=False)
weights_df.to_csv('cit_cross_wgts.csv', index=False)
