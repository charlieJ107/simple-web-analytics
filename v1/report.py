from flask import Blueprint, request

v1bp = Blueprint('web-analysis-v1', "BlueprintV1", url_prefix="/v1",
                 template_folder='templates')


@v1bp.route('/report', methods=['POST'])
def report():
    request_data = request.get_json()
    cookies = request.cookies
    ua = request.user_agent
    ip = request.remote_addr
    # Write these data into a csv file under the /tmp/swa/report-<date>.csv
    # The csv file should have the following columns:
    # ip, user_agent, cookies, request_data
    with open('/tmp/swa/report-<date>.csv', 'a') as f:
        f.write(f"{ip},{ua},{cookies},{request_data}\n")
    return "OK"
