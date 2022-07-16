from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:x>/")
def candidate_page(x):
    candidate = get_candidate(x)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>/")
def search_by_name_page(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    len_ = len(candidates)  # переменная нужна для передачи длины списка в контекст
    return render_template('search.html', candidates=candidates, len_=len_)

@app.route("/skill/<skill_name>/")
def search_by_skill_page(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    len_ = len(candidates)  # переменная нужна для передачи длины списка в контекст
    return render_template('skill.html', candidates=candidates, len_=len_, skill_name=skill_name )

app.run()
