# coding: utf-8
from array import array
import numpy as numeros
import pandas as pd
import matplotlib.pyplot as grafico

arquivo = pd.read_csv("/home/brunohelghast/PROFISSIONAL/PYTHON/SCIKIT_LEARN/livrosAmazonSales/final_book_dataset_kaggle.csv")

""" QUESTÃO 1 - A qtd de páginas influencia no preço ?
print(arquivo["pages"].describe())

grafico.scatter(arquivo["price"],arquivo["pages"])
grafico.xlabel("preco")
grafico.ylabel("paginas")
grafico.grid()
grafico.show() """

""" QUESTÃO 2 - Existe diferença de preço entre as editoras ?
print(arquivo["publisher"].value_counts())
reily = arquivo[arquivo["publisher"] == "OReilly Media"].sample(30)
springer = arquivo[arquivo["publisher"] == "Springer"].sample(30)
wiley = arquivo[arquivo["publisher"] == "Wiley"].sample(30)
packtpub = arquivo[arquivo["publisher"] == "Packt Publishing"].sample(30)
pearson = arquivo[arquivo["publisher"] == "Pearson"].sample(30)
mediaDasVariancias = numeros.mean([
    numeros.var(reily["price"]),
    numeros.var(springer["price"]),
    numeros.var(wiley["price"]),
    numeros.var(packtpub["price"]),
    numeros.var(pearson["price"])
])
varianciaDasMedias = numeros.var([
    numeros.mean(reily["price"]),
    numeros.mean(springer["price"]),
    numeros.mean(wiley["price"]),
    numeros.mean(packtpub["price"]),
    numeros.mean(pearson["price"])
])
# graus de liberdade 4,145
grafico.boxplot([
    reily["price"],
    springer["price"],
    wiley["price"],
    packtpub["price"],
    pearson["price"]
])
grafico.xticks([1,2,3,4,5],["OReilly","Springer","Wiley","Packt","Pearson"])
grafico.ylabel("Preco")
grafico.grid()
grafico.show()
razaoF = (varianciaDasMedias*30)/mediaDasVariancias
print(razaoF) """

""" QUESTÂO 3 - A qtd de páginas influencia na avaliação ? 
print(arquivo.corr()["pages"].sort_values(ascending=False))"""

""" QUESTÃO 4 - O preço influencia na avaliação ? 
fiveStars = arquivo[arquivo["star5"] > 0.5]
print("{:.2f} por cento dos livros receberam 5 estrelas em mais da metade das avaliações.".format((len(fiveStars["price"])*1.0/len(arquivo["price"]))*100))
grafico.subplot(2,3,1)
grafico.scatter(arquivo["price"],arquivo["star1"])
grafico.xlabel("preco")
grafico.ylabel("percentual 1 estrelas")
grafico.grid()
grafico.subplot(2,3,2)
grafico.scatter(arquivo["price"],arquivo["star2"])
grafico.xlabel("preco")
grafico.ylabel("percentual 2 estrelas")
grafico.grid()
grafico.subplot(2,3,3)
grafico.scatter(arquivo["price"],arquivo["star3"])
grafico.xlabel("preco")
grafico.ylabel("percentual 3 estrelas")
grafico.grid()
grafico.subplot(2,3,4)
grafico.scatter(arquivo["price"],arquivo["star4"])
grafico.xlabel("preco")
grafico.ylabel("percentual 4 estrelas")
grafico.grid()
grafico.subplot(2,3,5)
grafico.scatter(arquivo["price"],arquivo["star5"])
grafico.xlabel("preco")
grafico.ylabel("percentual 5 estrelas")
grafico.grid()
grafico.show()"""

"""
    fórmula_excel_avaliacao_media = ((G2*5)+(H2*4)+(I2*3)+(J2*2)+K2)/15
"""

""" You can perform an exploratory data analysis of the dataset, working with Pandas or Numpy.
Interesting visualizations can be performed too using, for instance, Python libraries to plot the different features.
This dataset can be also used to practice queries using SQL or Pandas.
Moreover, you can rank the books based on the number of positive reviews, or you can explore the dataset to have a reference for buying data-science-related books in the future. """ 