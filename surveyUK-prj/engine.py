from models import QuestionsResults
from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_cors import CORS
from calculation import SurveyCalculator,loadJSON
import settings
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY
app.config.from_object(__name__)
cors = CORS(app, resources={r"/app/*": {"origins": "*"}})
jsonData=loadJSON(settings.CONFIG_JSON)


@app.route('/',methods=['POST','GET'])
def surveyPage():  
    if request.method=='POST':
        clientData=request.get_json(silent=True)
        calculator=SurveyCalculator(clientData)
        calculator.calculateCategories(jsonData['Questions'])
    return render_template('index.html')



@app.route('/m/',methods=['POST','GET'])
def mobSurveyPage():  
    if request.method=='POST':
        clientData=request.get_json(silent=True)
        calculator=SurveyCalculator(clientData)
        calculator.calculateCategories(jsonData['Questions'])
        return 'ok'
    return render_template('mobile.html')



@app.route('/survey_page.js')
def s_config_js():
    with open(settings.CONFIG_JSON, encoding='utf8') as f:
        JS = """
            const S_CONFIG = {}
            """.format(f.read()) 
    return JS


@app.route('/login',methods=['POST','GET'])
def loginPage():
    if request.method=='POST':
        ...
        return redirect(url_for('survey_page'))


if __name__=="__main__":
    app.run(debug=True)
    

