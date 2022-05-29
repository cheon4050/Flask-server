from kospeech.infer_ import pred_sentence
import torch
import os
from hanspell import spell_checker

device = torch.device('cpu')
model_path = 'kospeech/trained_model/model.pt'
d_path = 'kospeech/test_data/test_data'

d = os.listdir(d_path)
d = [x for x in d if x.endswith('pcm')]
for data in d:
    if data.startswith('Kspon'):
        print('표준어 데이터')
    else:
        print('방언 데이터')

    audio_path = os.path.join(d_path,data)
    txt = data[:-3] + 'txt'
    txt_path = os.path.join(d_path,txt)
    with open(txt_path, 'r',encoding='utf-8') as f:
        s = f.readline()
    print('target:', s)
    sentence = pred_sentence(audio_path, model_path, device)[0]
    print('pred:',sentence)
    print('spell check:',spell_checker.check(sentence).as_dict()['checked'])
    print('-'*20)
# audio_path, model_path, device