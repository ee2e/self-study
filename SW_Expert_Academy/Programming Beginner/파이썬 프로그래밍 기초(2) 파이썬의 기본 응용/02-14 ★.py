'''
입력 받은 문자열 리스트를 가나다 순으로 따로 묶으려고 합니다.
다음과 같은 리스트가 주어졌을 때 결과처럼 가나다순(사전순)으로
따로 묶은 리스트가 출력되도록 리스트 내포를 이용한 프로그램을 작성하십시오.
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),
            ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',
                '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
                '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']

출력)
[['계시다', '가지다', '그', '개'], ['놀이'], ['들다', '다', '뒤', '듣다', '데리다'], [],
['막', '무척', '마리'], ['부모님', '비용', '비행기', '보이다'], ['싶다', '수출'],
['원래', '아이', '옳다'], ['좀', '자르다', '정도'], ['처리', '최초'], [], [], [], ['함께']]
'''

dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),
            ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',
                '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
                '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
                


print([[word for word in inputWord if cha1 < word < cha2] for cha1, cha2 in dicBase])