from flask import Flask, jsonify, request, render_template

import os

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Hello,' + name + '!'

    }
    return jsonify(response)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)


'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    @property
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

    @gotmarks.setter
    def gotmarks(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks


st = Student("Jaki", "25")
print(st.name)
print(st.marks)
print(st.gotmarks)
print("##################")
st.name = "Anusha"
print(st.name)
print(st.gotmarks)
print("##################")
st.gotmarks = 'Golam obtained 36'
print(st.gotmarks)
print(st.name)
print(st.marks)
'''