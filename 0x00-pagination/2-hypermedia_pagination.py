#!/usr/bin/env python3

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Function to calculate start, end indices
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets the data according to the arguments.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        # for index in range(range_index[0], range_index[1]):
        #      final_data.append(data_list[index])
        if start_index > len(self.dataset()):
            return []
        end_index = min(end_index, len(self.dataset()))
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Gets the dictionary representation of the data
        """
        data = self.get_page(page, page_size)
        next_page = page + 1 if len(data) == page_size else None
        prev_page = page - 1 if page > 1 else None
        total_pages = len(self.dataset()) // page_size + (
            1 if len(self.dataset()) % page_size != 0 else 0
            )
        hypermedia = {
            "page_size":
            page_size if len(data) != 0 else 0,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }
        return hypermedia
