__title__ = 'TextPreprocessing'
__version__ = '0.0.5'
__author__ = 'suchoi'
__license__ = 'GPL v3'
__copyright__ = 'Niccompany'


import re
from ckonlpy.tag import Twitter
from ckonlpy.tag import Postprocessor
from konlpy.tag import Okt
import pandas as pd
# import numpy as np

class Nickonlpy():
    def __init__(self, base=False):
        if base == False:
            self.twitter = Twitter()
            self.post = Postprocessor(self.twitter)
        else:
            self.post = Okt()

    #### 사람이름 치환
    def name_check(self, string):
        string_check(string)
        names = [i[0] for i in self.post.pos(string) if i[1] == 'Name']
        if names:
            for name in names:
                return string.replace(name, '')
        else: return string

	#### 토큰화
    def predict_tokennize(self, string):
        string_check(string)
        return ' '.join([i[0] for i in self.post.pos(string)])


#### 사용하지 않은 아스키코드 치환
def ascii_check(string):
    string_check(string)
    string = list(str(string))
    hex_ascii_diff = int('0xfee0', 16)
    hex_ascii_blank = int('0x3000', 16)
    for i in range(len(string)):

        full = string[i]
        # 16진수인 ascii code
        hex_ascii_full = ord(full)
        # 16진수 형태의 string
        # hex_full = hex(hex_ascii_full)

        # 전각일 경우 전각 기준인 값을 차감해 반각으로 변경
        if hex_ascii_full >= hex_ascii_diff:
            string[i] = chr(hex_ascii_full - hex_ascii_diff)
        # 빈칸이 전각일 경우는 위 공식에 어긋나므로 강제로 반각형태의 빈칸을 지정
        elif hex_ascii_full == hex_ascii_blank:
            string[i] = chr(32)
        # (주)가 전각인 형태가 들어올 수 있으므로 주식회사로 변경
        elif hex_ascii_full == 12828:
            string[i] = ' 주식회사 '
    return ''.join(string)


#### ()안에 법인명을 풀어서 치환
def corporatebody(string):
    string_check(string)
    cor_dict = {"(주)": " 주식회사 ",
                "(사)": " 사단법인 ",
                "(재단)": " 재단법인 ",
                "(유)": " 유한회사 ",
                "(재)": " 재단법인 ",
                "(학)": " 학교법인 ",
                "(합)": " 합자회사 ",
                "(복)": " 복지재단 ",
                "(의)": " 의료재단 ",
                "(사복)": " 사회복지법인 ",
                "(유한)": " 유한회사 ",}

    for i, n in cor_dict.items():
        string = string.replace(i, n)
    return string


#### 특수문자 제거
def remove_specialchar(string):
    string_check(string)
    return re.sub(r"[^a-zA-Z0-9가-힣 ]", " ", string)


#### 그냥 숫자로 치환 ( 자릿수에 상관없이 '숫자'로 치환 )
def numbers_check(string):
    string_check(string)
    numbers = re.findall(r'\d+', string) # 숫자로 이루어진 문자열을 리스트 형식으로 반환
    index = list()
    end_index = 0
    for i in numbers:
        start_index = string.find(i, end_index)
        index.append(start_index) # 문자열에서 해당 숫자가 있는 index의 시작지점과 끝지점을 저장
        end_index = string.find(i, end_index)+len(i)
        index.append(end_index)

    string_list = list(string)
    for jump,i in enumerate(index):
        string_list.insert(i+jump, ' ') # 리스트로 변경한 문자열에서 시작지점과 끝지점에 공백을 추가
    # 숫자가 들어간 문자열을 모두 '숫자'라는 단어로 치환
    string_list = ''.join(string_list).split()
    string_list = ['숫자' if i in numbers else i for i in string_list]
    string_list = ' '.join(string_list)
    
    #for n in ['월','차전','개','회차','원','기','호','점', '차', '박', '건', '회', '일','년','동']:
    for n in ['월', '차전', '개', '회차', '원', '기', '호', '차', '건', '회', '일', '년', '동']:
        string_list = string_list.replace('숫자 %s'%n, '숫자%s '%n)
    return string_list

#### 모든 숫자를 0으로 변경
# def numbers_to_zero(string):
#     string_check(string)
#     numbers = re.findall(r'\d+', string) # 숫자로 이루어진 문자열을 리스트 형식으로 반환
#     for i in numbers:
#         string = string.replace(i, '0'*len(i))
#     return string

#### 모든 숫자를 0으로 변경
def numbers_to_zero(string):
    string_check(string)
    string = re.sub('[1-9]', '0', string)
    return string


#### 전처리 결과 빈셀이면 공백이란 단어로 치환
def find_null(string):
    if (string == "") or (pd.isnull(string)):
        return "공백"
    else:
        return string

#### 공백제거
def space_delete(string):
    string_check(string)
    return string.strip()


#### 은행명 뒤에 하이픈 붙은것은 제거
def remove_bank(string):
    if string.startswith(('신한-', 'SC-', '국민-', 'KB-', '기업-', '농협-', '우리-', '금고-', '경남-', '대구-', '우체-', '하나-', '수협-', '부산-', '신협-')):
        return string[3:]
    else:
        return string


#### 모든 알파벳을 대문자로 변경
def change_upper(string):
    string_check(string)
    return string.upper()


#### input 타입체크 
def string_check(x):
    assert type(x) is str, "문자열 형식이 아닙니다. 적요 텍스트의 타입을 확인해주세요. {}".format(x)


