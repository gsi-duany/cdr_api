import django_filters
from django_filters import DateRangeFilter,DateFilter

class CdrFilters(django_filters.FilterSet):
    start_date = DateFilter(name='calldate', lookup_type=('gt'), )
    end_date = DateFilter(name='calldate', lookup_type=('lt'))
    date_range = DateRangeFilter(name='calldate')