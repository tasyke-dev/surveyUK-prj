import os
import json

from flask_cors.core import CONFIG_OPTIONS

SECRET_KEY = 'x81k\xe5p\x9fBP\xea+b\xdfD\xd2\xbe3\xb6+\xf1\xc6@\xe6\xb7\xe8\xcc'

APP_PATH  = os.path.abspath(os.path.dirname(__file__))
DATA_PATH = os.path.join(APP_PATH, 'survey_questions')

pj = os.path.join
pjd = lambda *s:pj(DATA_PATH, *s)
pja = lambda *s:pj(APP_PATH, *s)

CONFIG_JSON='data\survey_questions.json'

DATABASE = 'sqlite:///' + pjd('data.db')


