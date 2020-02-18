from SofiPackage.enum_converter import ANSWERS_AND_QUESTIONS
from SofiPackage.db_choise import sample_of_values_to_enum
import random


def choose_from_random(options_dict):
    rand = random.randint(0,100)
    last_weight = 0
    for option in options_dict:
        if last_weight <= rand <= options_dict[option]:
            return option
        last_weight = options_dict[option]


def generate_oracle():
    db_size = choose_from_random({'db_size_inf': 10, 'db_size_100_mb': 20, 'db_size_1_gb': 40, 'db_size_100_gb': 100})
    db_flow_rate = choose_from_random({'db_flow_rate_100_mbd': 5, 'db_flow_rate_1_gbd': 20, 'db_flow_rate_100_gbd': 80, 'db_flow_rate_inf': 100})
    store_time = choose_from_random({'store_time_1_month': 5, 'store_time_1_year': 20, 'store_time_2_years': 80, 'store_time_5_years': 100})
    spatial_use = choose_from_random({'spatial_use': 30, 'non_spatial_use': 100})
    complex_select = choose_from_random({'complex_select_10': 10, 'complex_select_25': 30, 'complex_select_60': 80, 'complex_select_100': 100})
    select_by_user = choose_from_random({'select_by_user_10': 10, 'select_by_user_25': 30, 'select_by_user_50': 70, 'select_by_user_100': 100})
    select_rate = choose_from_random({'select_rate_10_opm': 10, 'select_rate_100_opm': 30, 'select_rate_1000_opm': 80, 'select_rate_inf': 100})
    schema_change = choose_from_random({'schema_change_1_year': 80, 'schema_change_5_year': 90, 'schema_change_10_year': 95, 'schema_change_dynamic': 100})
    sample = ['oracle', 'schema', db_size, db_flow_rate, store_time, 'non_text_search', spatial_use, 'non_dynamic_schema',
              complex_select, 'select_by_column', select_by_user, select_rate, schema_change, 'data_type_text', 'scale_up']
    sample_string = ', '.join(str(elem) for elem in sample)
    sample_string += '\n'
    return sample_string


for i in range(100):
    print(generate_oracle(), end='')
    # oracle = ['schema', none, none, none, 'non_text_search', none, 'non_dynamic_schema',
    #                                        none, 'select_by_column', none, none, none, 'data_type_text', 'scale_up']
    #
    # mssql = ['schema', none, none, none, 'non_text_search', 'non_spatial_use', 'non_dynamic_schema',
    #                                        none, 'select_by_column', none, none, none, none, 'scale_up']
    #
    # hbase = ['non_schema', none, none, none, 'non_text_search', 'non_spatial_use', 'dynamic_schema',
    #                                        'complex_select_10', 'select_by_key', 'select_by_user_10', none, none, none, 'scale_out']
    #
    # elastic = ['non_schema', none, none, none, 'text_search', none, 'dynamic_schema',
    #                                        none, none, none, none, none, 'data_type_text', 'scale_out']
    #
    # mongo = ['non_schema', none, none, none, 'non_text_search', none, 'dynamic_schema',
    #                                        none, none, none, none, none, none, 'scale_out']


# a = {'a': 10, 'b': 30, 'c': 60, 'd': 100}
# print(choose_from_random(a))