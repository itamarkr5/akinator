from flask import Flask
from flask import request
from SofiPackage.db_choise import db_chooser
from SofiPackage.db_choise import db_chooser_by_grade
from SofiPackage.db_choise import sample_of_values_to_enum
from SofiPackage.db_choise import FILE_PATH
from SofiPackage.enum_converter import Atr
from SofiPackage.enum_converter import answers_and_questions
from flask import jsonify

app = Flask(__name__)


@app.route('/choose_db', methods=['POST'])
def choose_db():
    req = request.get_json()
    db_spec = [req['schema'], req['db_size'], req['db_flow_rate'],
               req['store_time'], req['text_search'], req['spatial_use'],
               req['dynamic_schema'], req['complex_select'], req['select_by'],
               req['select_by_user'], req['select_rate'], req['schema_change'],
               req['data_type'], req['scaling']]
    enum_sample = sample_of_values_to_enum(db_spec[0], db_spec[1], db_spec[2], db_spec[3], db_spec[4], db_spec[5],
                                           db_spec[6], db_spec[7], db_spec[8], db_spec[9], db_spec[10], db_spec[11],
                                           db_spec[12], db_spec[13])
    return Atr(db_chooser(enum_sample, 100, FILE_PATH)).name


@app.route('/choose_db_and_grade', methods=['POST'])
def choose_db_and_grade():
    req = request.get_json()
    db_spec = [req['schema'], req['db_size'], req['db_flow_rate'],
               req['store_time'], req['text_search'], req['spatial_use'],
               req['dynamic_schema'], req['complex_select'], req['select_by'],
               req['select_by_user'], req['select_rate'], req['schema_change'],
               req['data_type'], req['scaling']]
    enum_sample = sample_of_values_to_enum(db_spec[0], db_spec[1], db_spec[2], db_spec[3], db_spec[4], db_spec[5],
                                           db_spec[6], db_spec[7], db_spec[8], db_spec[9], db_spec[10], db_spec[11],
                                           db_spec[12], db_spec[13])
    return jsonify(db_chooser_by_grade(enum_sample, 100, FILE_PATH))


@app.route('/train_the_algorithm', methods=['POST'])
def train_the_algorithm():
    req = request.get_json()
    db_spec = [req['db_type'], req['schema'], req['db_size'], req['db_flow_rate'],
               req['store_time'], req['text_search'], req['spatial_use'],
               req['dynamic_schema'], req['complex_select'], req['select_by'],
               req['select_by_user'], req['select_rate'], req['schema_change'],
               req['data_type'], req['scaling']]

    sample_string = ', '.join(str(elem) for elem in db_spec)
    sample_string += '\n'
    f = open(FILE_PATH, 'a+')
    f.write(sample_string)
    f.close()
    return jsonify({"status": "success"})


@app.route('/get_question_and_answers', methods=['GET'])
def get_question_and_answers():
    return jsonify(answers_and_questions)


if __name__ == '__main__':
    app.run()
