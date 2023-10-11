import pandas as pd
from pathlib import Path

WORKING_DIRECTORY = Path('fruit_classification')
DATA_ANALYSIS_PATH = WORKING_DIRECTORY / 'data_analysis'
DATA_PATH = WORKING_DIRECTORY / 'data/archive/Date_Fruit_Datasets/Date_Fruit_Datasets.xlsx'

def get_summary_of_input_features(data: pd.DataFrame) -> pd.DataFrame:
    input_features = data.drop('Class', axis='columns')
    data_types = [str(data_type) for data_type in input_features.dtypes.to_list()]
    mins, maxs = input_features.min().to_list(), input_features.max().to_list()
    value_ranges = [f"{min}...{max}" for min, max in zip(mins, maxs)]
    summary = pd.DataFrame({
        'feature_name':     input_features.columns.to_list(),
        'data_type':        data_types,
        'value_range':      value_ranges,
        'std':              input_features.std().to_list(),
        'mean':             input_features.mean().to_list(),
        'unique_count':     input_features.nunique()
    })
    summary.reset_index(inplace=True, drop=True)
    return summary

def get_summary_of_output_feature(data: pd.DataFrame) -> pd.DataFrame:
    output_features = data['Class']
    summary = pd.DataFrame({
        'feature_name':     output_features.name,
        'data_type':        'str',
        'unique_count':     output_features.nunique(),
        'distinct_values':  [output_features.unique().tolist()],
        'value_counts':     [output_features.value_counts().to_list()]
    })
    summary.reset_index(inplace=True, drop=True)
    return summary

if __name__ == '__main__':
    data = pd.read_excel(DATA_PATH)
    pd.set_option('display.max_colwidth', None)

    summary = (
        "Input features summary:\n"
        f"{get_summary_of_input_features(data)}\n"
        "\n"
        "Output feature summary:\n"
        f"{get_summary_of_output_feature(data)}\n"
    )

    with open(DATA_ANALYSIS_PATH / 'summary.txt', 'w') as file:
        file.write(summary)