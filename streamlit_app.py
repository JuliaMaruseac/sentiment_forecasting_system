import streamlit as st
import pandas as pd
from app import data_loader, preprocessing, sentiment_analyzer, trend_forecaster, visualizer

analyzer = sentiment_analyzer.MultiLangSentimentAnalyzer()
forecaster = trend_forecaster.TrendForecaster()

st.title("📈 Система анализа настроений и прогнозирования трендов")
st.markdown("Введите тему или загрузите CSV-файл")

query = st.text_input("Поисковый запрос", "искусственный интеллект")

if st.button("Собрать и проанализировать"):
    df = data_loader.load_tweets(query, 300)
    df['clean'] = df['text'].apply(preprocessing.clean_text).apply(preprocessing.lemmatize_text)
    sentiments = analyzer.batch_predict(df['clean'])
    df_sent = pd.DataFrame(sentiments)
    df_final = pd.concat([df, df_sent], axis=1)

    st.subheader("📊 Распределение тональностей")
    st.plotly_chart(visualizer.plot_sentiment_distribution(df_final))

    st.subheader("⏳ Прогноз трендов")
    ts_data = forecaster.prepare_data(df)
    forecast = forecaster.fit_and_predict(ts_data)
    st.plotly_chart(visualizer.plot_forecast(forecast))

    st.download_button("📥 Скачать результаты (CSV)", df_final.to_csv(index=False), file_name="results.csv")
