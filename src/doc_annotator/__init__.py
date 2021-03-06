import os, sys

if not sys.version_info == (3, 6, 4, 'final', 0) or sys.version.find('64 bit (AMD64)') == -1:
    raise Exception("Wrong python version, your are using %s, required 3.6.4 x64. Download from here https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe" % sys.version)

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

app.config['UPLOAD_FOLDER'] = './pdf_files'
app.config['TRAINING_FOLDER'] = './training_data'
app.config['NETWORK_DATA'] = './network_data'
app.config['NUMBER_OF_CHARACTERISTICS'] = 6
app.config['PRImA_EXE'] = './bins/TesseractToPAGE 1.4/bin/PRImA_Tesseract-1-4-144.exe'
app.config['DBG'] = True

from doc_annotator.repository.volatile.parse_results import ParseResultsRepo
from doc_annotator.repository.volatile.training_metadata import TrainingMetadataRepo
from doc_annotator.utils.neural_network.network import Network

parse_results_repository = ParseResultsRepo()
training_metadata_repository = TrainingMetadataRepo()
training_network = Network()

from doc_annotator.utils.jobs_queue import JobsQueue, Parser

jobs_queue = JobsQueue(Parser)

import doc_annotator.controllers.default
import doc_annotator.controllers.parse
import doc_annotator.controllers.training
import doc_annotator.repository.volatile.parse_results
import doc_annotator.repository.volatile.training_metadata

if not os.path.exists(app.config['UPLOAD_FOLDER']) or not os.path.exists(app.config['TRAINING_FOLDER']):
    raise Exception("Check if you have folder 'pdf_files' and 'training_data")

if not os.path.abspath(os.curdir).split(os.sep)[-1].startswith('pdf2article'):
    raise Exception("Invalid current working directory! Your current working directory is '%s' and should be the pdf2article folder.\nIf you are in the right folder then rename the folder to begin with pdf2article" % os.path.abspath(os.curdir))
