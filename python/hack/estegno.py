import re
from PIL import Image
'''
    Uma simples implementacao de um algoritmo LSB para esconder textos em uma imagem
    codigo por Rafael Alencar
    fonte: https://www.vivaolinux.com.br/artigo/Esteganografia-e-Esteganalise-transmissao-e-deteccao-de-informacoes-ocultas-em-imagens-digitais
'''

# Define quantos pixels serao utilizados para informar o tamanho da mensagem oculta
PIXELS_RESERVADOS = 10

def pixels(tam):
    for y in xrange(tam[1]):
        for x in xrange(tam[0]):
            yield(x,y)

def esteg(img_original, img_esteg, str_bin):
    img = Image.open(img_original)
    largura, altura = img.size
    if img.mode[:3] != 'RGB' or largura * altura * 3 < len(str_bin) + PIXELS_RESERVADOS * 3 :
        raise IndexError('o tamanho da mensagem excede a capacidade da imagem ou nao ha suporte para a mesma')
    # os primeiro pixels definem o tamanho da informacao a ser ocultada
    bits_tam = bin(len(str_bin))[2:].zfill(PIXELS_RESERVADOS * 3)
    str_bin = bits_tam + str_bin

    # completa a informacao tornando-a multipla de 3 e iteravel
    str_bin = enumerate(str_bin + '0' * (3 - len(str_bin) % 3 ))

    #carrega os pixels da imagem para a memoriax
    pix = img.load()
    # percorre cada pixel da imagem
    for x, y in pixels(img.size):
        try:
            # altera o valor dos bits menos significativos
            rgb = map(lambda cor, bit : cor - (cor % 2) + int(bit), pix[x,y][:3],[str_bin.next()[1] for _ in xrange(3)])
            pix[x,y] = tuple(rgb)
        except StopIteration:
            img.save(img_esteg,'PNG',quality=100)
            return

def recuperar(img_esteg):
    #abre a imagem e carrega os pixels para a memoria
    img = Image.open(img_esteg)
    tam = img.size
    pix = img.load()

    #obtem tamanho da informacao
    info_tam = ""
    for p in pixels(tam):
        info_tam += "".join('1' if cor % 2 else '0' for cor in pix[p][:3])
        if len(info_tam) >= PIXELS_RESERVADOS * 3:
            info_tam = int(info_tam,2)
            break
    
    # extrai a informacao binaria da imagem
    info_bin = ''
    for p in pixels(tam):
        info_bin += ''.join('1' if cor % 2 else '0' for cor in pix[p][:3])
    return info_bin[PIXELS_RESERVADOS * 3 : info_tam + PIXELS_RESERVADOS * 3]

def gera_bin(msg):
    '''para cada caractere obtem o valor binario de seu codigo ASCII'''
    return ''.join(bin(ord(caractere))[2:].zfill(8) for caractere in msg)

def recupera_str(str_bin):
    ''' Converte cada grupo de 8 bits no seu respectivo caracter '''
    return ''.join(chr(int(bin,2)) for bin in re.findall(r'.{8}',str_bin))

if __name__ == "__main__":
    msg_bin = gera_bin('um texto muito enorme aqui.')
    # print msg_bin,len(msg_bin)
    # print recupera_str(msg_bin)
    esteg('exemplo01.png','saida.png',msg_bin)

    text = recuperar('saida.png')
    
    print len(text)

    print recupera_str(text)