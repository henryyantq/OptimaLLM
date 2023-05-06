import httpx

OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
MODEL = 'gpt-3.5-turbo'
OPTIMODE = 'original'

def send_req_receive(message, model=MODEL):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }
    data = {
        'model': model, 
        'messages': message
    }
    r = httpx.post(url, headers=headers, json=data, timeout=5000)
    return r.json()['choices'][0]['message']


while (1):
    init_prompt = input('\nPlease type in your question here: ')
    max_iters = input('Please type in the maximum iterations of the enhancement: ')

    message = [
        {'role': 'user', 'content': init_prompt}
        ]
    
    received_content = send_req_receive(message=message)
    print('\033[33mThe original first-attempt answer >> ', received_content['content'], '\033[0m\n')
    first_attempt = received_content['content']

    iter_count = 0
    answers = []

    for iter in range(0, int(max_iters)):
        iter_count += 1
        former_feedback = received_content

        flaw_indicating = {'role': 'user',
                           'content': 'Please list the defects of answer "' \
                            + former_feedback['content'] + '" to the question "' + init_prompt + '".' \
                                + ' List the defects in one sentence instead of a list with line breaks!'}
        flaw = send_req_receive(message=[flaw_indicating])
        # print('\n\033[34m' + flaw['content'] + '\033[0m')

        interm_prompt = {'role': 'user', 
                        'content': 'The answer "' + former_feedback['content'] \
                            + '" to the question "' + init_prompt \
                                + '" is not optimal because that' + flaw['content'] \
                                    + ' Please refine the answer by providing a better one regarding the aforementioned flaw.' \
                                        + ' You should provide nothing else but the answer.'}
        # print('\n\033[34m' + interm_prompt['content'] + '\033[0m')
        
        received_content = send_req_receive(message=[interm_prompt])
        print('\n\033[34m' + received_content['content'] + '\033[0m')
        answers.append(received_content['content'])

        if iter_count > 1:
            judge_prompt = {'role': 'user', 
                            'content': 'The question is "' + init_prompt + '", to which there are two optional answers, one is "' \
                                + former_feedback['content'] + '", the other one is "' + received_content['content'] \
                                    + '". Please answer "1" or "2" only if you think any one of them is better, or "0" only if you think they\'re equally good. Do not reply anything else than the number!'}
            # print('\n\033[34m' + judge_prompt['content'] + '\033[0m')
            
            reward = send_req_receive(message=[judge_prompt])
            # print('\n\033[34m' + 'reward for iter {} goes to '.format(iter_count) + reward['content'] + '\033[0m')
            
            if reward['content'] == '1' or reward['content'] == '0':
                received_content = former_feedback
                break

    print('\n\033[32mThe enhanced answer after {} iterations >> '.format(iter_count), received_content['content'], '\033[0m')
    enhanced = received_content['content']

    with open(init_prompt + '.txt', 'w', encoding='utf-8') as file:
        file.write('[' + MODEL + ' - ' + OPTIMODE + ']\n\n')
        file.write('Initial answer: ' + first_attempt + '\n')
        
        count = 0
        
        for ans in answers:
            count += 1
            file.write('\nIntermediate answer {}: '.format(count) + ans)
        
        file.write('\n\nEnhancement result: ' + enhanced)
        
        
