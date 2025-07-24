

def encode_pool(df):
    df_pool = df.copy()
    df_pool['pool'] = df_pool.apply(lambda x: 1 if x['PoolArea'] > 0 else 0, axis=1)
    df_pool.drop(columns=['PoolArea', 'PoolQC'], inplace=True)
    return df_pool


def encode_misc_alley(df):
    df_misc = df.copy()
    df_misc['misc'] = df_misc['MiscFeature'].notna().astype(int)
    df_misc['alley'] = df_misc['Alley'].notna().astype(int)
    df_misc.drop(columns=['MiscFeature', 'Alley'], inplace=True)
    return df_misc

def encode_fence(df):
    df_fence = df.copy()
    df_fence['fence'] = df_fence['Fence'].notna().astype(int)
    df_fence.drop(columns=['Fence'], inplace=True)
    return df_fence

def encode_mas_vnr(df):
    df_mas_vnr = df.copy()
    df_mas_vnr['mas_vnr'] = df_mas_vnr.apply(lambda x: 1 if x['MasVnrType'] == 'Stone' else 0, axis=1)
    df_mas_vnr.drop(columns=['MasVnrType'], inplace=True)
    return df_mas_vnr

def encode_fireplace(df):
    df_fireplace = df.copy()
    df_fireplace['fireplace'] = df_fireplace['FireplaceQu'].notna().astype(int)
    df_fireplace = df_fireplace.drop(columns=['FireplaceQu', 'Fireplaces'])
    return df_fireplace


def encode_nans(df):
    df_nans = df.copy()
    df_pool = encode_pool(df_nans)
    df_misc = encode_misc_alley(df_pool)
    df_fence = encode_fence(df_misc)
    df_mas_vnr = encode_mas_vnr(df_fence)
    df_fireplace = encode_fireplace(df_mas_vnr)
    return df_fireplace


