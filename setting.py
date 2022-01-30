import yaml


# common
PARAM_TITLE_LABEL_CLASS = 'param-title-label-cls'
PARAM_DESC_LABEL_CLASS = 'param-desc-label-cls'
PARAM_INPUT_TEXT_CLASS = 'param-input-text-cls'
PARAM_INPUT_NUMBER_CLASS = 'param-input-number-cls'
PARAM_TEXTBOX_CLASS = 'param-textarea-cls'
PARAM_TABLE_CLASS = 'param-table-cls'
PARAM_SINGLE_COLUMN_CLASS = 'param-single-column-cls'
PARAM_TABLE_ADD_BTN_CLASS = 'param-table-add-btn-cls'
PAGE_LAYOUT_CLASS = 'page-layout-cls'
PAGE_DESC_LABEL_CLASS = 'page-desc-label-cls'


# dashboard


# create_daily
DAILY_CREATE_DIALOG_ID = 'daily-create-dialog-id'
DAILY_TEXT_AREA_ID = 'daily-textarea-id'
DAILY_CREATE_BUTTON_ID = 'create-daily-btn-id'
DAILY_SEND_BUTTON_ID = 'send-daily-btn-id'

DAILY_TEXTAREA_CLASS = 'daily-textarea-cls'
DAILY_CREATE_BUTTON_CLASS = 'create-daily-btn-cls'
DAILY_SEND_BUTTON_CLASS = 'send-daily-btn-cls'


# menutree
MENU_TREE_BUTTON_CLASS = 'menu-tree-btn-cls'
MENU_TREE_LAYOUT_CLASS = 'menu-tree-layout-cls'


# setting_daily
SET_DAILY_DIALOG_ID = 'save-daily-config-dialog-id'
SET_DAILY_CATEGORY_TABLE_ADD_BUTTON_ID = 'category-table-add-btn-id'
SET_DAILY_EMAIL_TABLE_ADD_BUTTON_ID = 'email-table-add-btn-id'
SET_DAILY_MATTER_ITEMS_TABLE_ADD_BUTTON_ID = 'matter-table-add-btn-id'

SET_DAILY_SUBJECT_TEXT_ID = 'subject-text-id'
SET_DAILY_HEADER_TEXT_ID = 'header-text-id'
SET_DAILY_FOOTER_TEXT_ID = 'fooder-text-id'
SET_DAILY_EOM_TEXT_ID = 'eom-text-id'
SET_DAILY_CATEGORY_TABLE_ID = 'category-table-id'
SET_DAILY_MATTER_ITEMS_TABLE_ID = 'matter-item-table-id'
SET_DAILY_CHAPTER_MARK_TABLE_ID = 'chapter-mark-table-id'
SET_DAILY_ADD_LAST_MAIL_CHECKBOX_ID = 'add-last-mail-flag-id'
SET_DAILY_EMAIL_FOLDER_TEXT_ID = 'email-folder-text-id'
SET_DAILY_SEARCH_EMAIL_ITER_NUM_ID = 'last-email-iter-id'
SET_DAILY_SEND_EMAIL_TABLE_ID = 'send-address-table-id'

SET_DAILY_PARAM_ID_ARGS = [
    [SET_DAILY_SUBJECT_TEXT_ID, 'value'],
    [SET_DAILY_HEADER_TEXT_ID, 'value'],
    [SET_DAILY_FOOTER_TEXT_ID, 'value'],
    [SET_DAILY_EOM_TEXT_ID, 'value'],
    [SET_DAILY_CATEGORY_TABLE_ID, 'data'],
    [SET_DAILY_MATTER_ITEMS_TABLE_ID, 'data'],
    [SET_DAILY_CHAPTER_MARK_TABLE_ID, 'data'],
    [SET_DAILY_ADD_LAST_MAIL_CHECKBOX_ID, 'value'],
    [SET_DAILY_EMAIL_FOLDER_TEXT_ID, 'value'],
    [SET_DAILY_SEARCH_EMAIL_ITER_NUM_ID, 'value'],
    [SET_DAILY_SEND_EMAIL_TABLE_ID, 'data']
]


# setting_user
SET_USER_DIALOG_ID = 'save-user-config-dialog-id'

SET_USER_RNAME_TEXT_ID = 'user-name-text-id'
SET_USER_ADDRESS_TEXT_ID = 'email-address-text-id'
SET_USER_EXCEL_PATH_TEXT_ID = 'excel-file-text-id'
SET_USER_DAILT_SHEET_TEXT_ID = 'daily-sheet-text-id'
SET_USER_MASTER_SHEET_TEXT_ID = 'master-sheet-text-id'

SET_USER_PARAM_ID_ARGS = [
    [SET_USER_RNAME_TEXT_ID, 'value'],
    [SET_USER_ADDRESS_TEXT_ID, 'value'],
    [SET_USER_EXCEL_PATH_TEXT_ID, 'value'],
    [SET_USER_DAILT_SHEET_TEXT_ID, 'value'],
    [SET_USER_MASTER_SHEET_TEXT_ID, 'value']
]


# Load Parameter
DAILY_CONFIG_PATH = 'configs/daily_config.yml'
with open(DAILY_CONFIG_PATH, 'r', encoding='utf-8') as f:
    DAILY_CONFIG = yaml.safe_load(f)

USER_CONFIG_PATH = 'configs/user_config.yml'
with open(USER_CONFIG_PATH, 'r', encoding='utf-8') as f:
    USER_CONFIG = yaml.safe_load(f)
