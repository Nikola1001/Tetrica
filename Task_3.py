# Task 3
from flask_restful import Api, Resource, reqparse
from flask import Flask


def task_3(intervals):

    less = intervals['lesson']
    stud = intervals['pupil']
    teach = intervals['tutor']

    less_interv = [less[0], less[1]]
    stud_interv = [stud[0], stud[1]]
    teach_interv = [teach[0], teach[1]]
    res_int = list()
    i_teach = i_stud = 2

    while(i_teach+1 < len(teach) or i_stud+1 < len(stud)):
        if stud_interv[0] >= teach_interv[0] and stud_interv[0] <= teach_interv[1] and stud_interv[0] >= less_interv[0] and stud_interv[0] <= less_interv[1]:
            res_int.append(stud_interv[0])
        if teach_interv[0] >= stud_interv[0] and teach_interv[0] <= stud_interv[1] and teach_interv[0] >= less_interv[0] and teach_interv[0] <= less_interv[1]:
            res_int.append(teach_interv[0])
        if less_interv[0] >= teach_interv[0] and less_interv[0] <= teach_interv[1] and less_interv[0] >= stud_interv[0] and  less_interv[0] <= stud_interv[1]:
            res_int.append(less_interv[0])
        if stud_interv[1] >= teach_interv[0] and stud_interv[1] <= teach_interv[1] and stud_interv[1] >=  less_interv[0] and stud_interv[1] <= less_interv[1]:
                res_int.append(stud_interv[1])
        if teach_interv[1] >= stud_interv[0] and teach_interv[1] <= stud_interv[1] and teach_interv[1] >= less_interv[0] and teach_interv[1] <= less_interv[1]:
            res_int.append(teach_interv[1])
        if less_interv[1] >= teach_interv[0] and less_interv[1] <= teach_interv[1] and less_interv[1] >= stud_interv[0] and  less_interv[1] <= stud_interv[1]:
            res_int.append(less_interv[1])

        if ((stud_interv[1] < teach_interv[1]) and i_stud+1 < len(stud)) or (teach[len(teach)-1] == teach_interv[1] and i_stud+1 < len(stud)):
            stud_interv[0] = stud[i_stud]
            stud_interv[1] = stud[i_stud+1]
            i_stud += 2

        elif i_teach+1 < len(teach) or (stud[len(stud)-1] == stud_interv[1] and i_teach+1 < len(teach)):
            teach_interv[0] = teach[i_teach]
            teach_interv[1] = teach[i_teach + 1]
            i_teach += 2

    if stud_interv[0] >= teach_interv[0] and stud_interv[0] <= teach_interv[1] and stud_interv[0] >= less_interv[0] and  stud_interv[0] <= less_interv[1]:
        res_int.append(stud_interv[0])
    if teach_interv[0] >= stud_interv[0] and teach_interv[0] <= stud_interv[1] and teach_interv[0] >= less_interv[0] and  teach_interv[0] <= less_interv[1]:
        res_int.append(teach_interv[0])
    if less_interv[0] >= teach_interv[0] and less_interv[0] <= teach_interv[1] and less_interv[0] >= stud_interv[0] and  less_interv[0] <= stud_interv[1]:
        res_int.append(less_interv[0])
    if stud_interv[1] >= teach_interv[0] and stud_interv[1] <= teach_interv[1] and stud_interv[1] >= less_interv[0] and stud_interv[1] <= less_interv[1]:
        res_int.append(stud_interv[1])
    if teach_interv[1] >= stud_interv[0] and teach_interv[1] <= stud_interv[1] and teach_interv[1] >= less_interv[0] and teach_interv[1] <= less_interv[1]:
        res_int.append(teach_interv[1])
    if less_interv[1] >= teach_interv[0] and less_interv[1] <= teach_interv[1] and less_interv[1] >= stud_interv[0] and  less_interv[1] <= stud_interv[1]:
        res_int.append(less_interv[1])

    print("Интервалы присутсвия", res_int)
    time_presence =0
    for i in range(0, len(res_int), 2):
        time_presence += res_int[i+1] - res_int[i]
    return time_presence

#### Post

app = Flask(__name__)
api = Api(app)


tests = [
    {
        "lesson": [],
        'pupil': [],
        "tutor": []
    },
]

class Test(Resource):
    def get(self):
        return tests, 200

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("lesson")
        parser.add_argument('pupil', type=list)
        parser.add_argument("tutor")
        params = parser.parse_args()

        test = {
            "lesson": params["lesson"],
            'pupil': params['pupil'],
            "tutor": params["tutor"]
        }
        tests.append(test)
        return test, 201



api.add_resource(Test, "/tests", "/tests/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)
