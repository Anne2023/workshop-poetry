import random

lista_de_desculpas = [
  "Desculpe, professor, tive um encontro inesperado com um unicórnio e perdi o horário.",
  "Ah, eu queria ir à aula, mas meu gato me trancou para fora de casa. Ele está aprendendo truques novos, sabe?",
  "Eu juro que estava indo para a aula, mas acabei me perdendo no labirinto das mensagens não lidas do WhatsApp.",
  "Hoje é o dia internacional do cochilo, então pensei em comemorar isso adequadamente em casa.",
  "Infelizmente, fui mordido por um vampiro ontem à noite e estou me sentindo meio... desfalecido.",
  "Eu estava a caminho da aula quando encontrei uma reunião de pombos conspirando contra a humanidade. Alguém tinha que detê-los!",
  "Desculpe, mas meu despertador se tornou autônomo e decidiu tirar o dia de folga por conta própria.",
  "Eu estava a caminho da aula quando me deparei com uma horda de zumbis... Aparentemente, eles precisavam de ajuda com o dever de casa.",
  "Hoje eu descobri que sou alérgico a matemática. Só de pensar na aula, comecei a espirrar fórmulas trigonométricas.",
  "Tive um confronto épico com minha cama esta manhã e, bem, ela venceu. Estou me recuperando."
]

def gerar_desculpa_por_faltar_na_aula_do_gabriel() -> str:
    return random.choice(lista_de_desculpas)

def gerar_desculpa_por_faltar_na_aula_do_gabriel_cli():
    print(random.choice(lista_de_desculpas))

# Testando a função no CLI
gerar_desculpa_por_faltar_na_aula_do_gabriel_cli()
