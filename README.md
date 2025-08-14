# FaceRecognitionPython

Este repositório contém um sistema de **identificação de rostos** desenvolvido em **Python** utilizando a biblioteca [DeepFace](https://github.com/serengil/deepface).

## Como usar??

1. Crie uma pasta para cada pessoa que deseja cadastrar.  
   - O nome da pasta será o nome da pessoa.  
   - Dentro dela, adicione as fotos do rosto.  
   - Exemplo de estrutura:  
     ```
     fotos_cadastradas/
     ├── Andre/
     │   ├── foto1.jpg
     │   ├── foto2.jpg
     ├── Alison/
     │   ├── foto1.jpg
     │   ├── foto2.jpg
     ├── Augusto/
         ├── foto1.jpg
         ├── foto2.jpg
     ```

2. Quanto **mais variações de imagens** (ângulos, iluminação, expressões) você fornecer, **melhor será o reconhecimento**.

3. Ative o ambiente virtual (venv):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / MacOS
   venv\Scripts\activate      # Windows
``

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
``

5. Execute o script e aproveite 🎯.
