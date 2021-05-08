- 폴더 설명

- '0409_최종수집된 데이터 사용'
    L data
        L '재보궐선거댓글데이터_최종.zip' : 진보 언론사(경향신문 등)이 수집된 최종 데이터
        L '한국 불용어 사전.xlsx' : 불용어 사전
        L 'korean_stopwords.txt' : 불용어 사전
        L '재보궐선거댓글데이터_최종_by_model2.zip': 최종데이터를 이용해 model2로 후보자를 예측했고 이 라벨값을 최종데이터에 컬럼으로 추가한 데이터
        L 'adj_list_by_model1_0409.pickle': model1을 통해 진행된 감성분석 결과 추출한 단어사전( 회귀계수와 형태소 )
    L model
        L pos_neg_logi_model_0409.dat : 후보자, 당명을 제거하지 않고 진행한 감성분석 모델
        L tfidf_vectorizer_0409.dat : 후보자, 당명을 제거하지 않고 감성분석할 때 사용한 tfidf 
        L pos_neg_logi_mode2_0409.dat : ▣ 모델2(후보자예측)를 의미하는게 아님. 후보자, 당명을 제거하고 진행한 감성분석 모델
        L tfidf_vectorizer2_0409.dat :  ▣ 후보자, 당명을 제거하고 감성분석할 때 사용한 tfidf
        L model2_1637
            L 21-0.39536339044570923: 후보자를 예측할 때 사용된 모델2 -> DNN 방식 ( LSTM,CNN+LSTM, DNN 중 가장 성능 좋았던 모델)