# Beneath the Cream

This is the repository for the [Beneath Cream](https://resume.fmorenovr.com/documents/papers/book_chapters/2024_CSCML.pdf) paper.  
Here we analyze the [PostCog dataset](https://postcog.cambridgecybercrime.uk/) to classify textual information and justify categories using GPT-based models.

# Requirements

- **Python**>=3.12

## Overview
"Beneath the Cream" performs Natural Language Processing (NLP) and Large Language Models (LLM) to analyze and categories threat level of exploitations in dark hack forums. We also apply explanations to understand and study what are the relevant keywords in messages.

### Dataset

The PostCog framework is a data exploration and analysis system built to work on large cybercrime forum datasets such as [CrimeBB dataset](https://www.repository.cam.ac.uk/items/6f20f707-d52f-4655-b944-5da5ef8b98ba) and [ExtremeBB](https://www.repository.cam.ac.uk/items/dbd78f16-82cb-4d81-8842-8a8dc1e8deb0).

### Download

To download the dataset, use [this link](https://www.cambridgecybercrime.uk/process.html). Or send an e-mail asking for data.

## Data Preparation

* Clone this repository:

  ```bash
  git clone https://github.com/famveer/CreamSkimming
  git submodule add -b main https://github.com/fmorenovr/nlpToolkit.git py/nlpToolkit
  git submodule update --remote
  ```

* Download dataset [here]().  
* Create a `.env` file, and add the path of the data downloaded and models.  
  ```
    DATA_PATH=/path_to/datasets/
    MODEL_PATH=/path_to/models/
  ```
  
* First, run the notebook `notebooks/SQL/Extracting_Zip.ipynb`.  
  Then, execute `notebooks/SQL/SQL_backup.ipynb`
  and `notebooks/SQL/SQL_to_CSV.ipynb`
  
* Choose the best model to segment images.  
  Next, run the notebook `notebooks/Data/ADE20k/Generate_Segmentations.ipynb`.  
  Then, run the notebook `notebooks/Data/ADE20k/Group_Segmentations.ipynb`.  

* Second, run the notebook `notebooks/Data/UPD4k/Generate_UPD4k.ipynb`.  
  Next, run the notebook `notebooks/Data/UPD4k/Group_UPD4k.ipynb`.  
  
* Train the safety classifier at `notebooks/Models/Ensemble_Classifications.ipynb`.  

* Generates Post-Hoc SHAP Explanations at `notebooks/Explanations/SHAP.ipynb`.  
* Generates CounterFactuals at `notebooks/Explanations/CounterFactuals.ipynb`.  

* Generates LLM human-language Interpretations at `notebooks/LLM/Interpretations.ipynb`.  


# Citation
If you use this data, please cite:

```
@incollection{moreno2024beneath,
  title={Beneath the Cream: Unveiling Relevant Information Points from CrimeBB Underground Forums with Its Ground Truth Labels},
  author={Moreno-Vera, Felipe and Menasche, Daniel and Lima, Cabral},
  booktitle={International Symposium on Cyber Security, Cryptology and Machine Learning},
  pages={280--290},
  year={2024},
  publisher={Springer}
}
```

# Contact us  
For any issue please kindly email to `felipe [dot] moreno [at] ppgi [dot] ufrj [dot] br`
