from sklearn import tree
from SofiPackage.enum_converter import Atr
import numpy

FILE_PATH = 'dataset.txt'


def sample_of_values_to_enum(schema, db_size, db_flow_rate, store_time, text_search, spatial_use, dynamic_schema,
                             complex_select, select_by, select_by_user, select_rate, schema_change, data_type, scaling):
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
    try:
        return [Atr[schema].value,
                Atr[db_size].value,
                Atr[db_flow_rate].value,
                Atr[store_time].value,
                Atr[text_search].value,
                Atr[spatial_use].value,
                Atr[dynamic_schema].value,
                Atr[complex_select].value,
                Atr[select_by].value,
                Atr[select_by_user].value,
                Atr[select_rate].value,
                Atr[schema_change].value,
                Atr[data_type].value,
                Atr[scaling].value
                ]
    except AttributeError as e:
        raise ("Unknown attribute, exception: " + e.__str__())


def load_samples_from_file_to_dataset(file_path):
    samples_array = []
    f = open(file_path, 'r')
    for i in f.readlines():
        tokens = i[:-1].split(', ')
        enum_tokens = sample_of_values_to_enum(tokens[1], tokens[2], tokens[3], tokens[4], tokens[5], tokens[6],
                                               tokens[7], tokens[8], tokens[9], tokens[10], tokens[11], tokens[12],
                                               tokens[13], tokens[14])
        samples_array.append(enum_tokens)
    f.close()
    return samples_array


def load_results_from_file_to_dataset(file_path):
    results_array = []
    f = open(file_path, 'r')
    for i in f.readlines():
        tokens = i[:-1].split(', ')
        results_array.append(Atr[tokens[0]].value)
    f.close()
    return results_array


def tree_builder(file_path):
    samples_array = load_samples_from_file_to_dataset(file_path)
    results_array = load_results_from_file_to_dataset(file_path)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(samples_array, results_array)
    return clf


def db_chooser(predict_enum_array, iteration_amount, file_path):
    max_db_amount = 10
    counter_array = [0] * max_db_amount
    counter_array = numpy.array(counter_array)
    for i in range(iteration_amount):
        clf = tree_builder(file_path)
        predict = clf.predict([predict_enum_array])
        counter_array[predict] += 1
    # for j in range(max_db_amount):
    #     if counter_array[j] > 0:
    #         print(str(Atr(j).name) + ": " + str(counter_array[j]))
    return numpy.where(counter_array == numpy.amax(counter_array))[0][0]


def db_chooser_by_grade(predict_enum_array, iteration_amount, file_path):
    db_grades = {}
    max_db_amount = 10
    counter_array = [0] * max_db_amount
    counter_array = numpy.array(counter_array)
    for i in range(iteration_amount):
        clf = tree_builder(file_path)
        predict = clf.predict([predict_enum_array])
        counter_array[predict] += 1
    for j in range(max_db_amount):
        if counter_array[j] > 0:
            # print(str(Atr(j).name) + ": " + str(counter_array[j]))
            db_grades[str(Atr(j).name)] = (counter_array[j] / iteration_amount) * 100
    return db_grades


if __name__ == '__main__':
    # # predict_enum_array_c = [11, 23, 33, 43, 50, 60, 70, 82, 91, 101, 110, 0, 0, 0]
    # predict_enum_array_c = [11, 23, 33, 43, 50, 60, 70, 0, 0, 0, 0, 0, 0, 141]
    #
    # # print(Atr(db_chooser(predict_enum_array_c, 100, FILE_PATH)).name)
    # print(db_chooser_by_grade(predict_enum_array_c, 10000, FILE_PATH))
    a = 1
