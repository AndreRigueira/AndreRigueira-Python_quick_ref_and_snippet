#pip install docxtpl

from docxtpl import DocxTemplate
from datetime import datetime

# Dados do contrato
nome_contratante = 'Andre_Rigueira'
dados = {
    'nome': 'Andre Rigueira',
    'cpf': '620.513.501-91',
    'empresa': 'Rigs Software',
    'cnpj': '00.100.200/0001-01',
    'servicos_contratados': 'Desenvolvimento de aplicação de automação',
    'valor_contrato': 'R$ 1.000,00',
    'data_de_inicio': '09/07/2025',
    'data_de_termino': '10/07/2025',
    'data_do_contrato': datetime.today().strftime('%d/%m/%Y')

}

# Carrega o modelo
doc = DocxTemplate('Contrato_modelo.docx')

# Preenche com os dados
doc.render(dados)

# Salva o Contrato gerado
doc.save(f'Contrato_{nome_contratante}.docx')