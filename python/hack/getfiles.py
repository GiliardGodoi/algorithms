from urllib.request import urlretrieve
import os
import zipfile

def download_file(url,dest):
    urlretrieve(url, dest)

def validate_cdIBGE(cdIBGE):
    return cdIBGE[:6]

def validate_year(year):
    years = ['2013', '2014', '2015', '2016', '2017']
    if(year in years):
        return year
    else :
        raise TypeError("O parâmetro ano não é válido\nvalor atribuido\t"+year)

def validate_filetype(file_type):
    available_files = {'licitacao': 'Licitacao',
                        'contratos': 'Contrato',
                        'convenios': 'Convenio',
                        'obras': 'Obra',
                        'despesas' : 'Despesa', 
                        'combustivel' : 'Combustivel',
                        'diarias' : 'Diarias',
                        'relacionamentos' : 'Relacionamentos'};
    if file_type in available_files.keys() : 
        return available_files[file_type]
    else :
        raise TypeError("Tipo de arquivo nao é valido! ")

def formatte_url(cdIBGE, year, file_type):
    baseURL = 'http://servicos.tce.pr.gov.br/TCEPR/Tribunal/Relacon/Arquivos/{year}/{year}_{cod}_{type}.zip'
    return baseURL.format(cod=cdIBGE,year=year,type=file_type)

def formatte_dest_file_name(cdIBGE, year, file_type):
    file_name = "{type}_{year}_{cod}.zip"
    return file_name.format(cod=cdIBGE,year=year,type=file_type)

def get_file_with(cdIBGE, year, file_type):
    cdIBGE = validate_cdIBGE(cdIBGE)
    year = validate_year(year)
    file_type = validate_filetype(file_type)
    url = formatte_url(cdIBGE, year, file_type)
    dest = formatte_dest_file_name(cdIBGE, year, file_type)
    download_file(url,dest)

def extract_zip_files():
    files = os.listdir()
    for f in files:
        if zipfile.is_zipfile(f):
            print("extracting... "+f)
            ZipFile = zipfile.ZipFile(f)
            ZipFile.extractall("licitacao")
            
if __name__ == "__main__":
    get_file_with("4119905","2016","licitacao")