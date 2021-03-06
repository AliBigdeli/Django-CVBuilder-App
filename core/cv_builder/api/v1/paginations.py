from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from urllib.parse import urlparse

def get_relative_path(url):
    if url is not None:
        url = urlparse(url)
        return f"{url.path}?{url.query}"
    return None
    

class DefaultPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": get_relative_path(self.get_next_link()),
                    "previous": get_relative_path(self.get_previous_link()),
                    "current": self.request.query_params.get("page", 1),
                },
                "total_items": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )