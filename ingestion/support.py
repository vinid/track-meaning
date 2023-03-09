import pandas as pd


def eebo_file_to_date(mapper:str, file_name:str):
    mapped_date = int(mapper[file_name.split("/")[-1].split(".")[0]])
    return mapped_date

def year_to_bin(year: int, bins_range: int=50):
    """
    Converts years to bin defined by bins_range.

    if bins_range = 50, year_to_bin(1949) = 1900, year_to_bin(1951) = 1950...

    :param year:
    :param bins_range:
    :return:
    """
    return int(year/bins_range)*bins_range

def load_book_to_date_mapper_eebo(path: str):
    """
    Load the file that maps EEBO ids to Dates
    :param path:
    :return:
    """
    dates = pd.read_csv(path, header=None, sep="\t")
    date_mapper = dates.set_index(0).to_dict()[1]
    return date_mapper


