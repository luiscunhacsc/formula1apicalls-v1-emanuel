import streamlit as st
import requests

ERGAST_API_URL = "https://ergast.com/api/f1"

import pandas as pd

def get_f1_seasons():
    url = f"{ERGAST_API_URL}/seasons.json?limit=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        seasons = data['MRData']['SeasonTable']['Seasons']
        return [s['season'] for s in seasons][::-1]  # Mais recente primeiro
    else:
        st.error("Erro ao buscar temporadas de F1.")
        return []

def get_f1_races(season):
    url = f"{ERGAST_API_URL}/{season}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        races = data['MRData']['RaceTable']['Races']
        return races
    else:
        st.error("Erro ao buscar corridas da temporada.")
        return []

def get_f1_race_results(season, round_):
    url = f"{ERGAST_API_URL}/{season}/{round_}/results.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data['MRData']['RaceTable']['Races'][0]['Results']
        return results
    else:
        st.error("Erro ao buscar resultados da corrida.")
        return []

def show_driver_info(driver_result):
    driver = driver_result['Driver']
    constructor = driver_result['Constructor']
    st.subheader(f"{driver['givenName']} {driver['familyName']} ({driver['code'] if 'code' in driver else driver['permanentNumber'] if 'permanentNumber' in driver else ''})")
    st.write(f"**Nacionalidade:** {driver['nationality']}")
    st.write(f"**Data de nascimento:** {driver['dateOfBirth']}")
    st.write(f"**Equipe:** {constructor['name']} ({constructor['nationality']})")
    st.write(f"**Posição final:** {driver_result['position']}")
    st.write(f"**Grid:** {driver_result['grid']}")
    st.write(f"**Voltas:** {driver_result['laps']}")
    st.write(f"**Tempo:** {driver_result['Time']['time'] if 'Time' in driver_result else 'N/A'}")
    st.write(f"**Status:** {driver_result['status']}")
    st.markdown('---')

def main():
    st.title("Consulta de Corridas e Pilotos de Fórmula 1 (Ergast API)")

    # Seleção da temporada
    with st.spinner("A carregar temporadas..."):
        seasons = get_f1_seasons()
    if not seasons:
        st.stop()
    selected_season = st.selectbox("Escolha a Temporada:", seasons, index=0)

    # Seleção de corrida
    with st.spinner("A carregar corridas..."):
        races = get_f1_races(selected_season)
    if not races:
        st.stop()
    race_options = [f"{r['round']} - {r['raceName']} ({r['date']})" for r in races]
    selected_race = st.selectbox("Escolha a Corrida:", race_options)
    race_idx = race_options.index(selected_race)
    race = races[race_idx]
    round_ = race['round']

    # Resultados da corrida
    if st.button("Mostrar Resultados da Corrida"):
        with st.spinner("A carregar resultados..."):
            results = get_f1_race_results(selected_season, round_)
        if not results:
            st.warning("Nenhum resultado encontrado.")
        else:
            st.info(f"Resultados da corrida {race['raceName']} ({race['date']}):")
            for driver_result in results:
                show_driver_info(driver_result)

if __name__ == "__main__":
    main()
