Aplicação de MLLM na identificação automática de riscos em engenharia elétrica: uma abordagem multimodal para segurança ocupacional

Este projeto utiliza a biblioteca transformers da Hugging Face e o modelo BLIP (Salesforce/blip-image-captioning-base) para gerar legendas automáticas para imagens fornecidas por URL. 
O script mllm_ee.py carrega uma imagem da web, processa-a com o modelo BLIP e gera uma legenda descritiva.

Pré-requisitos

Python 3.6 ou superior
Bibliotecas Python:
transformers
Pillow (PIL)
requests



Instalação

Instale as dependências necessárias usando o pip:pip install transformers pillow requests

Uso

O script carrega uma imagem a partir de uma URL fornecida.
A imagem é processada pelo modelo BLIP, que gera uma legenda descritiva.
A legenda é exibida no console.

Código
O código principal está no arquivo mllm_ee.py. Ele inclui:

Importação das bibliotecas transformers, PIL e requests.
Carregamento do modelo BLIP (Salesforce/blip-image-captioning-base) e seu processador.
Download e processamento de uma imagem a partir de uma URL.
Geração e exibição da legenda da imagem.

Modelo Utilizado

Modelo: Salesforce/blip-image-captioning-base
Descrição: Um modelo de visão e linguagem treinado para gerar legendas descritivas de imagens. Ele combina processamento de imagens e geração de texto para produzir descrições naturais.

Como Executar

Clone este repositório:git clone https://github.com/vitor-souza-ime/pln_bert


Execute o script:python mllm_ee.py
Os testes foram feitos no Google Colab.


Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests no repositório: https://github.com/vitor-souza-ime/pln_bert.
Licença
Este projeto está licenciado sob a MIT License.
