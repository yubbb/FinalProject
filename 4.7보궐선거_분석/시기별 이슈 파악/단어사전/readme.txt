- 모델1을 이용한 단어사전 만들기.ipynb : 모델1 감성분석 모델을 통해 => 긍정/부정 평가에 영향을 준 단어 리스트 추출하는 과정

- 단어 사전
	L 한국어 감성사전: (?) Kosac, KNU 자료를 이용한 단어사전


	L data
		L adjective_list.pickle : 형용사 리스트
		L noun_list.pickle : 명사 리스트
		L verb_list.pickle : 동사 리스트
		L coef_pos_text : 모둔 단어 리스트
	
	L model
		L sentiment_analysis_model.dat : 감성분석 모델
		L tfidf_vectorizer1.dat : tfidf 벡터라이저 
	
	
- 리스트 불러오는 방법
import pickle
with open('data/adjective_list.pickle', 'rb') as f: 
	adjective_list = pickle.load(f) # 리스트 불러오기
