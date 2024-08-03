import httpx
from tqdm import tqdm

API_KEY = 'sk-chatAILogcgCom9hhswPg3Mucx8VLxVEDKgo1gb5y54XSPa6d'
MODEL = 'gpt-4o'
OPTIMODE = 'original'

def chat(message, model=MODEL, temperature=0.8):
    url = 'https://api.chatai.beauty/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'model': model, 
        'messages': message,
        'temperature': temperature
    }
    while True:
        try:
            r = httpx.post(url, headers=headers, json=data, timeout=200)
            return r.json()['choices'][0]['message']
        except:
            continue


def refiner(init_prompt, max_iters, model=MODEL, temperature=0.8):
    message = [{'role': 'user', 'content': init_prompt}]
    received_content = chat(
        message=message, 
        model=model, 
        temperature=temperature
    )
    first_attempt = received_content['content']
    iter_count = 0
    answers = []
    for _ in tqdm(range(0, int(max_iters))):
        iter_count += 1
        former_feedback = received_content
        flaw_indicating = {'role': 'user',
                           'content': 'Please list the defects of answer "' \
                            + former_feedback['content'] + '" to the question "' + init_prompt + '".' \
                                + ' List the defects in one sentence instead of a list with line breaks!'}
        flaw = chat(message=[flaw_indicating])
        interm_prompt = [{
            'role': 'user',
            'content': 'The answer "' + former_feedback['content'] \
                + '" to the question "' + init_prompt \
                    + '" is not optimal because that' + flaw['content'] \
                        + ' Please refine the answer by providing a better one regarding the aforementioned flaw.' \
                            + ' You should provide nothing else but the answer.'
        }]
        received_content = chat(
            message=interm_prompt,
            model=model, 
            temperature=temperature
        )
        answers.append(received_content['content'])
        if iter_count > 1:
            judge_prompt = [{
                'role': 'user',
                'content': 'The question is "' + init_prompt + '", to which there are two optional answers, one is "' \
                      + former_feedback['content'] + '", the other one is "' + received_content['content'] \
                        + '". Please answer "1" or "2" only if you think any one of them is better, or "0" only if you think they\'re equally good. Do not reply anything else than the number!'
            }]
            reward = chat(
                message=judge_prompt,
                model=model, 
                temperature=temperature
            )
            if reward['content'] == '1' or reward['content'] == '0':
                received_content = former_feedback
                break
    enhanced = received_content['content']
    return first_attempt, answers, enhanced


def main():
    while (1):
        init_prompt = input('\nPlease type in your question here: ')
        max_iters = input('\nPlease type in the maximum iterations of the enhancement: ')
        first_attempt, answers, enhanced = refiner(
            init_prompt=init_prompt,
            max_iters=max_iters
        )
        trace = f'## Initial answer: \n\n{first_attempt}'
        count = 1
        for ans in answers:
            count += 1
            trace += f'\n\n---\n## Intermediate answer {count}:\n\n{ans}'
        trace += f'\n\n---\n## Enhancement result\n\n{enhanced}'
        with open('result.md', 'w', encoding='utf-8') as f:
            f.write(trace)
        

main()
