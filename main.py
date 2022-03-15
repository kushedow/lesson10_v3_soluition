from flask import Flask

import utils

app = Flask(__name__)


@app.route("/")
def page_index():

    candidates = utils.get_candidates_all()

    page_content = utils.build_preformnatted_list(candidates)
    return page_content


@app.route("/skill/<skill_name>")
def page_skill(skill_name):

    candidates = utils.get_candidates_by_skill(skill_name)

    page_content = utils.build_preformnatted_list(candidates)
    return page_content


@app.route("/candidate/<int:uid>")
def page_candidate(uid):

    candidate = utils.get_candidate_by_id(uid)

    candidates = [candidate]
    page_content = utils.build_preformnatted_list(candidates)
    return page_content


app.run(debug=True)
