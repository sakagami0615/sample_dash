import json

# Load Parameter
DAILY_PARAM_PATH = 'user_setting/daily_param.json'
USER_PARAM_PATH = 'user_setting/user_param.json'

DAILY_PARAM_DICT = json.load(open(DAILY_PARAM_PATH, 'r', encoding='utf-8'))
USER_PARAM_DICT = json.load(open(USER_PARAM_PATH, 'r', encoding='utf-8'))


# Save Parameter Function
def save_daily_param():
    with open(DAILY_PARAM_PATH, 'w', encoding='utf-8') as f:
        json.dump(DAILY_PARAM_DICT, f, indent=4, ensure_ascii=False)

def save_user_param():
    with open(USER_PARAM_PATH, 'w', encoding='utf-8') as f:
        json.dump(USER_PARAM_DICT, f, indent=4, ensure_ascii=False)
