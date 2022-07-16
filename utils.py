import json


def load_candidates_from_json(path):
    '''возвращает список кандидатов из файла'''
    with open(path, 'r', encoding='utf-8') as file:
        tmp = file.read()
        candidates = json.loads(tmp)
    return candidates


def get_candidate(candidate_id):
    '''возвращает кандидата с указанным id'''
    candidates = load_candidates_from_json('candidates.json')
    for can in candidates:
        if can['id'] == candidate_id:
            return can


def get_candidates_by_name(candidate_name):
    '''возвращает кандидата с указанным именем
    нужно реализовать регистра'''
    result = []
    candidates = load_candidates_from_json('candidates.json')
    for can in candidates:
        if candidate_name.lower() in can['name'].lower():
            result.append(can)
    return result


def get_candidates_by_skill(skill_name):
    '''возвращает список кандидатов с указанным навыком
    '''
    result = []
    candidates = load_candidates_from_json('candidates.json')
    for can in candidates:
        if skill_name.lower() in can['skills'].lower().split(', '):
            result.append(can)
    return result


print(get_candidates_by_name('dela'))
