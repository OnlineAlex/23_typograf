import re


def del_reiteration_space(text):
    text = re.sub(' {2,}', ' ', text)
    text = re.sub(' *(\n+|\r\n+) *', '\n', text)
    return re.sub('^\s', '', text)


def del_tabs(text):
    return re.sub('\t', ' ', text)


def change_special_signs(text):
    text = re.sub(' *\((r|R)\) *', '&#174; ', text)
    text = re.sub(' *\((c|C)\) *', ' &#169; ', text)
    text = re.sub(' *\((tm|TM)\) *', '&#153; ', text)
    return text


def add_space_around_brackets(text):
    text = re.sub(' *(\(+|\)+) *',  r'\1', text)
    text = re.sub(r'\b(\()', r' \1', text)
    text = re.sub(r'(\))\b', r'\1 ', text)
    return text


def add_space_after_punctuation(text):
    return re.sub(r' *([^\w\s\)\(\-+]+) *', '\\1 ', text)


def format_phone_number(text):
    return re.sub(
        '''
        (\+7|7|8)                  # country code  
        [ \(-]*(\d{3,4})[ \)-]*    # sity code
        (\d)[^\d]*(\d)[^\d]?(\d)   # main telephone XXX-xx-xx
        [^\d]?(\d)[^\d]?(\d)       # main telephone xxx-XX-xx
        [^\d]?(\d)[^\d]?(\d)       # main telephone xxx-xx-XX
        ''',
        r'\1 (\2) \3\4\5&#150;\6\7&#150;\8\9',
        text,
        flags=re.VERBOSE
    )


def change_quotes(text):
    text = re.sub('[\"\'] *([^\"]*) *[\"\']', r'&laquo;\1&raquo;', text)
    return text


def change_hyphen_to_dash(text):
    return re.sub(' +-|- +', ' — ', text)


def get_correct_word_wrap(text):
    return re.sub(
        ' +([А-Яа-яёЁ]{1,2}) *\n'
        '| +([А-Яа-яёЁ]{1,3}) *\n(\w{1,2})',
        r'\n\1\2 \3',
        text
    )


def get_correct_punctuation_wrap(text):
    return re.sub('([^\w ]+) *(\n|\r\n)([^\w ]+) *', r'\1\3\2', text)


def add_dot_to_end(text):
    return re.sub('(\w+)$', r'\1.', text)


def add_non_breaking_spaces(text):
    return re.sub('(\d+) *([А-Яа-яёЁ])', r'\1&nbsp;\2', text)


def typograph(text):
    typograph_filters = [
        change_hyphen_to_dash,
        del_reiteration_space,
        del_tabs,
        add_space_after_punctuation,
        change_special_signs,
        add_space_around_brackets,
        format_phone_number,
        change_quotes,
        get_correct_word_wrap,
        get_correct_punctuation_wrap,
        add_dot_to_end,
        add_non_breaking_spaces
    ]

    for typograph_filter in typograph_filters:
        text = typograph_filter(text)
    return text
