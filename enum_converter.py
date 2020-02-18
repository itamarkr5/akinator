from enum import IntEnum


class Atr(IntEnum):
    """
    Atr -> Attribute
    """
    oracle = 1
    mssql = 2
    hbase = 3
    elastic = 4
    mongo = 5

    schema = 10
    non_schema = 11

    db_size_100_mb = 20
    db_size_1_gb = 21
    db_size_100_gb = 22
    db_size_inf = 23

    db_flow_rate_100_mbd = 30
    db_flow_rate_1_gbd = 31
    db_flow_rate_100_gbd = 32
    db_flow_rate_inf = 33

    store_time_1_month = 40
    store_time_1_year = 41
    store_time_2_years = 42
    store_time_5_years = 43

    text_search = 50
    non_text_search = 51

    spatial_use = 60
    non_spatial_use = 61

    dynamic_schema = 70
    non_dynamic_schema = 71

    complex_select_10 = 80
    complex_select_25 = 81
    complex_select_60 = 82
    complex_select_100 = 83

    select_by_column = 90
    select_by_key = 91

    select_by_user_10 = 100
    select_by_user_25 = 101
    select_by_user_50 = 102
    select_by_user_100 = 103

    select_rate_10_opm = 110
    select_rate_100_opm = 111
    select_rate_1000_opm = 110
    select_rate_inf = 110

    schema_change_1_year = 120
    schema_change_5_year = 121
    schema_change_10_year = 122
    schema_change_dynamic = 123

    data_type_text = 130
    data_type_binary = 131

    scale_up = 140
    scale_out = 141


def enum_to_dict(enum_class):
    enum_dict = {}
    enum_value_list = list(map(int, enum_class))
    for value in enum_value_list:
        enum_dict[Atr(value).name] = value
    return enum_dict


# schema: non_schema / schema
# db_size: db_size_100_mb / db_size_1_gb / db_size_100_gb / db_size_inf
# db_flow_rate: db_flow_rate_100_mbd / db_flow_rate_1_gbd / db_flow_rate_100_gbd / db_flow_rate_inf
# store_time: store_time_1_month / store_time_1_year / store_time_2_years / store_time_5_years
# text_search: text_search / non_text_search
# spatial_use: spatial_use / non_spatial_use
# dynamic_schema: dynamic_schema / non_dynamic_schema
# complex_select: complex_select_10 / complex_select_25 / complex_select_60 / complex_select_100
# select_by: select_by_column / select_by_key
# select_by_user: select_by_user_10 / select_by_user_25 / select_by_user_50 / select_by_user_100
# select_rate: select_rate_10_opm / select_rate_100_opm / select_rate_1000_opm / select_rate_inf
# schema_change: schema_change_1_year / schema_change_5_year / schema_change_10_year / schema_change_dynamic
# data_type = data_type_text / data_type_binary
# scaling = scale_up / scale_out
answers_and_questions = [{'question': 'schema',
                          'answers': ['non_schema', 'schema']
                          },
                         {'question': 'db_size',
                          'answers': ['db_size_100_mb', 'db_size_1_gb', 'db_size_100_gb', 'db_flow_rate_inf']
                          },
                         {'question': 'db_flow_rate',
                          'answers': ['db_flow_rate_100_mbd', 'db_flow_rate_1_gbd', 'db_flow_rate_100_gbd', 'db_flow_rate_inf']
                          },
                         {'question': 'store_time',
                          'answers': ['store_time_1_month', 'store_time_1_year', 'store_time_2_years', 'store_time_5_years']
                          },
                         {'question': 'text_search',
                          'answers': ['text_search', 'non_text_search']
                          },
                         {'question': 'spatial_use',
                          'answers': ['spatial_use', 'non_spatial_use']
                          },
                         {'question': 'dynamic_schema',
                          'answers': ['dynamic_schema', 'non_dynamic_schema']
                          },
                         {'question': 'complex_select',
                          'answers': ['complex_select_10', 'complex_select_25', 'complex_select_60', 'complex_select_100']
                          },
                         {'question': 'select_by',
                          'answers': ['select_by_column', 'select_by_key']
                          },
                         {'question': 'select_by_user',
                          'answers': ['select_by_user_10', 'select_by_user_25', 'select_by_user_50', 'select_by_user_100']
                          },
                         {'question': 'select_rate',
                          'answers': ['select_rate_10_opm', 'select_rate_100_opm', 'select_rate_1000_opm', 'select_rate_inf']
                          },
                         {'question': 'schema_change',
                          'answers': ['schema_change_1_year', 'schema_change_5_year', 'schema_change_10_year', 'schema_change_dynamic']
                          },
                         {'question': 'data_type',
                          'answers': ['data_type_text', 'data_type_binary']
                          },
                         {'question': 'scaling',
                          'answers': ['scale_up', 'scale_out']
                          },
                         ]
