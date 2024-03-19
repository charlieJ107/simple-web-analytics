from flask import Blueprint, request
import os
import json
from os import path
import datetime

v1bp = Blueprint('web-analysis-v1', "BlueprintV1", url_prefix="/api/v1",
                 template_folder='templates')


@v1bp.route('/report', methods=['POST'])
def report():
    request_data = json.dumps(request.get_json())
    # Get cookies from the request, convert it to a json string
    cookies = json.dumps(request.cookies)
    ua = request.user_agent
    ip = request.remote_addr
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Write these data into a csv file under the /tmp/swa/report-<date>.csv
    # The csv file should have the following columns:
    # ip, user_agent, cookies, request_data

    # Read report_path from config.json
    with open('config.json') as f:
        config = json.load(f)
        # if on windows
        if os.name == 'nt':
            report_path = config['windows']['v1']['report_path']
        # if on linux
        elif os.name == 'posix':
            report_path = config['linux']['v1']['report_path']

    # Check if the file exists, if not create it
    if not os.path.exists(report_path):
        os.makedirs(report_path)
    # Build report file name with datetime, yyyy-mm-dd:
    report_file_name = f"report-{datetime.datetime.now().strftime('%Y-%m-%d')}.csv"
    report_file_path = path.join(report_path, report_file_name)
    if not os.path.exists(report_file_path):
        with open(report_file_path, 'w') as f:
            f.write("ip,user_agent,cookies,request_data\n")
            f.write(f"{ip},{ua},{cookies},{request_data},{timestamp}\n")
    else:
        with open(report_file_path, 'a') as f:
            f.write(f"{ip},{ua},{cookies},{request_data},{timestamp}\n")

    return "OK"
