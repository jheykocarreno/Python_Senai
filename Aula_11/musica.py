#importando biblioteca de Sistema operacional
import os

#defina o caminho da pasta e o nome do arquivo pasta="C:\Users\Suporte\Documents\Jheyko\Aula_11\musica"
pasta="C:\Users\Suporte\Documents\Jheyko\Aula_11\musica"

#veja se o nome certo é Documents ou Documentos
nome_arquivo = "Radio.txt"

#cria a pasta caso não exista
os.makedirs(pasta, exist_ok=True)

#Junta o caminho com o nome do arquivo
caminho_completo = os.path.join(pasta, nome_arquivo)

#cria e escreve no arquivo
with open(caminho_completo, "w", encoding="utf-8") as arquivo:
    arquivo.write("I'd sit alone and watch your light\nMy only friend through teenage nights\nAnd everything I had to know\nI heard it on my radio\n\nYou gave them all those old time stars\nThrough wars of worlds invaded by Mars\nYou made 'em laugh, you made 'em cry\nYou made us feel like we could fly\n\nSo don't become some background noise\nA backdrop for the girls and boys\nWho just don't know or just don't care\nAnd just complain when you're not there\n\nYou had your time\nYou had the power\nYou've yet to have your finest hour\nRadio\n\nAll we hear is radio ga ga\nRadio goo goo\nRadio ga ga\nAll we hear is radio ga ga\nRadio blah blah\n\nRadio, what's new?\nRadio, someone still loves you\n\nWe watch the shows, we watch the stars\nOn videos for hours and hours\nWe hardly need to use our ears\nHow music changes through the years\n\nLet's hope you never leave, old friend\nLike all good things, on you we depend\nSo stick around, 'cause we might miss you\nWhen we grow tired of all this visual\n\nYou had your time\nYou had the power\nYou've yet to have your finest hour\nRadio\n\nAll we hear is radio ga ga\nRadio goo goo\nRadio ga ga\nAll we hear is radio ga ga\nRadio goo goo\nRadio ga ga\nAll we hear is radio ga ga\nRadio blah blah\n\nRadio, what's new?\nSomeone still loves you\n\nRadio ga ga\nRadio ga ga\nRadio ga ga\n\nYou had your time\nYou had the power\nYou've yet to have your finest hour\nRadio")
    
#lendo o texto inserido
with open(caminho_completo, "r", encoding="utf-8") as arquivo:
    print("Texto salvo: ", arquivo.read())