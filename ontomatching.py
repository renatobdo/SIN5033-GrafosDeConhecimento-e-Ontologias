from owlready2 import get_ontology
from difflib import SequenceMatcher

# Função de similaridade entre strings
def label_similarity(label1, label2):
    return SequenceMatcher(None, label1.lower(), label2.lower()).ratio()

# Carregar as ontologias
onto1 = get_ontology("C:\\testes\\ontologymatching\\doenca2.owl").load()
onto2 = get_ontology("C:\\testes\\ontologymatching\\sintoma2.owl").load()

# Coletar labels das classes
classes1 = [(cls.name, cls.label[0]) for cls in onto1.classes() if cls.label]
classes2 = [(cls.name, cls.label[0]) for cls in onto2.classes() if cls.label]

# Comparar e identificar possíveis matches
print("\n--- Possíveis Matches ---\n")
for name1, label1 in classes1:
    for name2, label2 in classes2:
        sim = label_similarity(label1, label2)
        if sim > 0.7:  # limiar de 70%
            print(f"Match encontrado:")
            print(f"  {label1} ({name1})  ≃  {label2} ({name2})")
            print(f"  Similaridade: {sim:.2f}\n")
