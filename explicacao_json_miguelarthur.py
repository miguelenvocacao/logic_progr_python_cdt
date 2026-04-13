'''
arquivos *.txt;
arquivos *.cvd;
arquivos *.json;

App, lista os projetos e exibir os projetos pode ser excluidos.


'''

import os
import json

def configurar_sistema():
   if not os. path.existe("Uploads_peojetos"):
      os.makedirs("Uploads_projetos")

      def listar_projetos():
         arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]
         print('\n' + '+'*40)
         print(' PROJETOS LISTADOS ')
         print('+'*40)

         if not arquivos:
            print("Nenhum projeto encontrado.")
            return []
            for i, arquivo in enumerate(arquivos, 1):
               nome_exibicao = arquivo.replace("projeto_","").replace(".json","").replace("_"," ")
               print(f"{i}. {nome_exibicao}")
            return arquivos
         
         def gerenciar_projeto():
            arquivos = listar_projetos()
            if not arquivos: return

            try:
               escolha = int(input('\n Escolha o numero do projeto para gerenciar(ou 0 para voltar):    '))
               if escolha == 0: return

               nome_arquivo = arquivos[escolha - 1]
               caminho = f"uploads_projetos/{nome_arquivo}"

         with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)

                print(f"\n--- Nova Atualização---")
                print(f"Alunos: {dados['aluno']}")
                print(f"projetos: {dados['projetos']}")
                
