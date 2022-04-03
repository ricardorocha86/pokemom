import streamlit as st
import pandas as pd 
import random
from pygame import mixer   

st.markdown('# Quem é esse POKEMON???') 
st.markdown('Acerte os nomes para ganhar pokemons e montar o seu time para batalha! Seu objetivo é ganhar 6 pokemons!')
st.markdown('Quando acertar, clique em jogar novamente para tentar outro pokemon!!')
  

dados = pd.read_csv('pokemon.csv', usecols = ['name', 'generation'])
dados = dados[(dados['generation'] == 1)]


st.markdown('---') 
         
sorteio = random.sample(range(dados.shape[0]), 5) 
correto = random.randint(0,4)

if 'sorteio' not in st.session_state:
	st.session_state['sorteio'] = sorteio

if 'correto' not in st.session_state:
	st.session_state['correto'] = correto

if 'acertos' not in st.session_state:
	st.session_state['acertos'] = 0

if 'insigneas' not in st.session_state:
	st.session_state['insigneas'] = 0

certo = st.session_state['sorteio'][st.session_state['correto']]
 
_, col2, _, col1, _ = st.columns([1,2,1,2,1])

pokemons = list(dados.loc[st.session_state['sorteio'], 'name'])
escolha = col1.radio('O nome dele é?', pokemons)
col2.image(f'images2/{certo+1}.png', use_column_width=True)

if col1.button('Checar'): 
	if escolha == dados.loc[certo, 'name']:
		st.success('Acertou, mizeravi!!')
		st.session_state['acertos'] += 1
		mixer.init()
		mixer.music.load('acertou-mizeravi.mp3')
		mixer.music.play() 

	else: 
		st.error('Errrrrooooooou!')
		mixer.init()
		mixer.music.load('faustao-errou.mp3')
		mixer.music.play()
 
 

mensagens = [':bug: Sua jornada Pokemon está no início! Acerte quantos pokemons conseguir!',
			 ':crab: Muito bem! Parece mesmo que você conhece os Pokemons! Continue para conseguir sua primeira Insígnea!',
			 ':beginner: Parabéns! Você ganhou a Insígnea de Bronze! Que treinador promissor!!',
			 ':stadium: Você está ficando esperto! Está preparado para desafios maiores?',
			 ':curly_loop: Caramba! Você é um treinador Sério. Ganhou a sua Insígnia de Prata!',
			 ':small_orange_diamond: Apenas mais um degrau até o grau máximo de treinador Pokemon! Não vai parar agora, né?',
			 ':fleur_de_lis: Mestre Pokemon! Um verdadeiro Ash Ketchum da cidade de Pallet. Pegue sua Insígnia de Ouro!']

premios = ['Pidgey', 'Bulbasauro', 'Squirtle', 'Charmander', 'Pikachu', 'Psyduck']
numeros = [16, 1, 7, 4, 25, 54]

niveis = [0, 10, 20, 30, 40, 50, 100, 10000]

if st.session_state['acertos'] >= niveis[6]:
	st.session_state['insigneas'] = 3
elif st.session_state['acertos'] >= niveis[4]:
	st.session_state['insigneas'] = 2
elif st.session_state['acertos'] >= niveis[2]:
	st.session_state['insigneas'] = 1
else:
	st.session_state['insigneas'] = 0


st.markdown('---')
st.markdown('Os Pokemons que você ganhou são:')

c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
c1.metric('Acertos', st.session_state['acertos'])
c2.metric('Insígneas', st.session_state['insigneas'])



for i in range(len(niveis[:-1])):
	if st.session_state['acertos'] in range(niveis[i], niveis[i+1]):
		st.info(mensagens[i]) 
		for j in range(i): 
			eval(f"c{j+3}.image(f'images2/{numeros[j]}.png', width = 70)")

st.markdown('---')
if st.button('Jogar Novamente'):		 
	del st.session_state['sorteio']
	del st.session_state['correto']
	st.experimental_rerun()
