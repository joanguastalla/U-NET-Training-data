# U-NET-Training-data
Conjunto de dados utilizados para treinar uma rede neural do tipo U-NET.

Neste repositório a pasta Dataset contém os 139 modelos de velocidade 2D utilizados
para gerar parte do  conjunto de treinamento da U-NET proposta na tese. Os diretórios
ali presentes tem os prefixos "XLine" e "YLine", indicando que trata-se de $x$ ou $y$ fixo
no cubo de velocidades gerado pelo pacote python Synthoseis. Em cada uma das pastas, 
temos o modelo de velocidade "vp.bin" e  as seção de afastamento nulo real e simulada pelo empilhamento CMP proposto, respectivamente "zo.bin" e "zostack.bin". 
Além disso, também temos a máscara de tempos de trâmsito dos eventos primários "zomask.bin". Os arquivos binários estão todos armazenados em formato float32, com o modelo de velocidade de dimensões $(nz,nx)=(335,600)$. Já as seções em tempo e a máscara de tempos de trânsito têm dimensões $(n_t,n_m)=(876,134)$.

O Dataset inteiro pode ser visualizado através da função "plotModels.py". As únicas dependências sãs os pacotes: OS, Matplotlib e Numpy. 








