
import pandas as pd

def drop_not_needed_columns(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_drop = ['Flag Codes', 'Flags', 'TIME']

    # Check if columns exist in the DataFrame before dropping
    existing_columns = [col for col in columns_to_drop if col in df.columns]
    if existing_columns:
        df.drop(columns=existing_columns, inplace=True)

    return df

def location_cluster(df: pd.DataFrame) -> pd.DataFrame:
    location_dict = {
        'Latin America': ['Latin America'],
        'Europe': ['OECD EU ', 'OECD Non-EU', 'Other EU', 'Other Eurasia'],
        'Asia (excl. China and India)': ['OECD Asia', 'Other non-OECD Asia'],
        'Oceania': ['OECD Oceania'],
        'Middle East & North Africa': ['Middle East & North Africa', 'Other Africa'],
        'Americas (excl. USA)': ['Other OECD America', 'Canada'],
        'United States': ['United States'],
        'China': ['China'],
        'India': ['India']
    }

    # Mapping each country to its corresponding region cluster
    df['location_cluster'] = df['location'].map({val: key for key, values in location_dict.items() for val in values})
    pass
