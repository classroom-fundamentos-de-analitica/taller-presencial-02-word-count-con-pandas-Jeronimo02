"""Taller evaluable"""

import glob

import pandas as pd

import string

def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
    
    filenames = glob.glob(input_directory + '/*.txt')
    dataframes = pd.concat((pd.read_csv(f, sep='\t', header=None, names=['text']) for f in filenames), ignore_index=True)
    
    return dataframes
    
    
    
def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    
    dataframe['clean_text'] = dataframe['text'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)).lower())
    return dataframe
    


def count_words(dataframe):
    """Word count"""
    words = dataframe['clean_text'].str.split(expand=True).stack()
    
    wordCounts = words.value_counts().reset_index()
    wordCounts.columns = ['word', 'count']
    
    return wordCounts

def save_output(dataframe, output_filename):
    """Save output to a file."""
    
    dataframe.to_csv(output_filename, sep='\t', index=False, header=False)



#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    dataframe = load_input(input_directory)
    cleanDataframe = clean_text(dataframe)
    WordCountDataframe = count_words(cleanDataframe)
    
    save_output(WordCountDataframe, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
