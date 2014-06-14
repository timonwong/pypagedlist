# -*- coding: utf-8 -*-
from pagedlist import PagedListBase


class SimplePagedList(PagedListBase):
    def _query_limit_offset_fn(self, query, limit, offset):
        return query[offset:offset + limit]

    def _query_count_fn(self, query):
        return len(query)
