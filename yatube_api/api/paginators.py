from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPaginator(LimitOffsetPagination):
    def get_paginated_response(self, data):
        if (self.get_next_link() is None
                and self.get_previous_link() is None):
            return Response(data)

        super(CustomPaginator, self).get_paginated_response(data)
