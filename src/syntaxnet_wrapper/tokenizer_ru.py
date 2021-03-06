# -*- coding: utf-8 -*-

import string

abbrevs = ['акад\.',
'б\.',
'вл\.',
'абл\.',
'абс\.',
'абх\.',
'авар\.',
'авг\.',
'австр\.',
'австрал\.',
'авт\.',
'агр\.',
'адж\.',
'адм\.',
'адыг\.',
'азерб\.',
'акад\.',
'акк\.',
'акц\.',
'алб\.',
'алг\.',
'алж\.',
'алт\.',
'алф\.',
'альм\.',
'альп\.',
'амер\.',
'анат\.',
'англ\.',
'ангол\.',
'аннот\.',
'антич\.',
'ап\.',
'апр\.',
'арам\.',
'аргент\.',
'арифм\.',
'арт\.',
'архип\.',
'архим\.',
'асср',
'асс\.',
'ассир\.',
'астр\.',
'ат\.',
'атм\.',
'афг\.',
'афр\.',
'балк\.',
'балт\.',
'башк\.',
'безв\.',
'безл\.',
'бельг\.',
'библ\.',
'биогр\.',
'биол\.',
'бирм\.',
'бол\.',
'болг\.',
'буд\.',
'бюдж\.',
'бюлл\.',
'вал\.',
'вв\.',
'вдхр\.',
'вед\.',
'вел\.',
'венг\.',
'вкл\.',
'внеш\.',
'внутр\.',
'вод\. ст\.',
'воен\.',
'возв\.',
'возд\.',
'воскр\.',
'вост\.',
'вт\.',
'вьетн\.',
'г\.',
'гг\.',
'га\.',
'гав\.',
'газ\.',
'гвин\.',
'гВт\.',
'ГГц\.',
'ген\.',
'ген\. л\.',
'ген\. м\.',
'ген\. п\.',
'геогр\.',
'геод\.',
'геол\.',
'геом\.',
'герм\.',
'г­жа\.',
'гл\.',
'гор\.',
'гос\.',
'госп\.',
'град\.',
'греч\.',
'гр\.',
'гражд\.',
'греч\.',
'груз\.',
'губ\.',
'Гц\.',
'ГэВ\.',
'дптр\.',
'д\. б\. н\.',
'Д\. В\.',
'д\. г\. н\.',
'д\. г\.­м\. н\.',
'дер\.',
'д\. и\. н\.',
'д\. иск\.',
'д\. м\. н\.',
'д\. н\.',
'д\. о\.',
'д\. п\.',
'д\. т\. н\.',
'д\. ф\. н\.',
'д\. ф\.­м\. н\.',
'д\. х\. н\.',
'д\. ч\.',
'дБ\.',
'деепр\.',
'действ\.',
'дек\.',
'дер\.',
'Дж\.',
'диак\.',
'диал\.',
'диал\.',
'диам\.',
'див\.',
'диз\.',
'дир\.',
'дисс\.',
'дист\.',
'дифф\.',
'дкг\.',
'дкл\.',
'дкм\.',
'дм\.',
'доб\.',
'док\.',
'докт\.',
'долл\.',
'доп\.',
'доц\.',
'драм\.',
'дубл\.',
'евр\.',
'европ\.',
'егип\.',
'ед\.',
'ед\. ч\.',
'ежедн\.',
'ежемес\.',
'еженед\.',
'ефр\.',
'ж\.',
'ж\. д\.',
'жен\.',
'жит\.',
'женск\.',
'журн\.',
'засл\. арт\.',
'з\. д\.',
'зав\.',
'зав\. хоз\.',
'загл\.',
'зал\.',
'зам\.',
'заруб\.',
'зем\.',
'зол\.',
'др\.',
'пр\.',
'и\. о\.',
'и\.о\.',
'игум\.',
'иером\.',
'им\.',
'иностр\.',
'инд\.',
'индонез\.',
'итал\.',
'канд\.',
'коп\.',
'корп\.',
'кв\.',
'ква\.',
'квт\.',
'кг\.',
'кгс\.',
'кгц\.',
'кд\.',
'кдж\.',
'кирг\.',
'ккал\.',
'кл\.',
'км\.',
'кмоль\.',
'книжн\.',
'кэв\.',
'л\.с\.',
'лаб\.',
'лат\.',
'латв\.',
'лейт\.',
'лит\.',
'м\.',
'мин\.',
'м­р\.',
'муж\.',
'м\.н\.с\.',
'макс\.',
'матем\.',
'мат\.',
'маш\.',
'м­во\.',
'мгц\.',
'мдж\.',
'мед\.',
'мес\.',
'мин­во\.',
'митр\.',
'мка\.',
'мкал\.',
'мкв\.',
'мквт\.',
'мкм\.',
'мкмк\.',
'мком\.',
'мкпа\.',
'мкр\.',
'мкф\.',
'мкюри\.',
'мл\.',
'млк\.',
'млн\.',
'млрд\.',
'мн\.ч\.',
'моск\.',
'мпа\.',
'мс\.',
'мужск\.',
'мэв\.',
'н\.э\.',
'нем\.',
'обл\.',
'пос\.',
'пер\.',
'пр\.',
'пл\.',
'р\.',
'рис\.',
'стр\.',
'сокр\.',
'ст\.н\.с\.',
'ст\.',
'т\.',
'т\.д\.',
'т\.е\.',
'т\.к\.',
'т\.н\.',
'т\.о\.',
'т\.п\.',
'т\.с\.',
'тыс\.',
'тел\.',
'тов\.',
'трлн\.',
'ул\.',
'франц\.',
'ч\.',
'чел\.']

rules = ['[-\w.]+@(?:[A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}', #e-mail
         '(?:[01]?[0-9]|2[0-4]):[0-5][0-9]', # times
         '(?:mailto:|(?:news|http|https|ftp|ftps)://)[\w\.\-]+|^(?:www(?:\.[\w\-]+)+)', # urls
         '[\w\.\-]+\.(?:com|org|net)', # url2
         '--',
         '\.\.\.',
         '\d+\.\d+',
         '[' + string.punctuation + ']',
         '[а-яА-ЯёЁa-zA-Z0-9]+',
         '\S']

final_regex = '|'.join(abbrevs + rules)

def create_tokenizer_ru():
    from nltk.tokenize import RegexpTokenizer
    
    return RegexpTokenizer(final_regex)
