import streamlit as st

# Configuração da página
st.set_page_config(page_title="Mary and John's Story", page_icon="📖")

# Título e introdução
st.title("Interactive Story - Mary and John")
st.write("Choose an action for Mary and see John's response.")

# Função para alternar a exibição de resposta
def toggle_response(key, action_text):
    # Se a chave já existir no session_state, alterna o valor entre True e False
    if key in st.session_state:
        st.session_state[key] = not st.session_state[key]
    else:
        # Se a chave não existir, define como True para mostrar o texto na primeira vez
        st.session_state[key] = True
    
    # Exibe ou oculta o texto com base no valor atual da chave
    if st.session_state[key]:
        st.write(action_text)

# Botões para as escolhas de Mary
if st.button("Cook Dinner"):
    toggle_response("cook_dinner", "Mary cooks dinner for John... John eats and soon falls asleep without thanking her.")

if st.button("Take Off John's Clothes"):
    toggle_response("take_off_clothes", "Mary takes off John's clothes, hoping he notices her effort... John doesn't reciprocate, he just enjoys it and soon falls asleep.")

if st.button("Apply Lipstick"):
    toggle_response("apply_lipstick", "Mary applies lipstick to look good when he wakes up... When he wakes up, he doesn't notice, gets dressed, and leaves without saying 'good night'.")

if st.button("End Story"):
    toggle_response("end_story", "Regardless of the choices, Mary realizes that John will never change. She is trapped in a cycle of frustration and disillusionment.")
