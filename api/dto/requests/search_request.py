from dataclasses import dataclass, asdict


@dataclass
class SearchRequest:

    def __init__(self):
        self.search_endpoint = "/images/search"
        self.search_endpoint_by_id = "/images/{id}"

