from transliterate import translit
from torch import tensor, load
import json
from models import Output
from argparse import Namespace
from classes import SurnameClassifier, SurnameVectorizer


args = Namespace(
    # Пути к директориям
    vectorizer_file="model_storage/ch4/surname_mlp/vectorizer.json",
    model_state_file="model_storage/ch4/surname_mlp/model.pth",
    # Гиперпараметры модели
    hidden_dim=300
)


def predict_nationality(surname, classifier, vectorizer):
    vectorized_surname = vectorizer.vectorize(surname)
    vectorized_surname = tensor(vectorized_surname).view(1, -1)
    result = classifier(vectorized_surname, apply_softmax=True)

    probability_values, indices = result.max(dim=1)
    index = indices.item()

    predicted_nationality = vectorizer.nationality_vocab.lookup_index(index)
    probability_value = probability_values.item()

    return {'nationality': predicted_nationality, 'probability': probability_value}


def predict(surnameKyrillic):
    surname = ""
    for el in surnameKyrillic:
        if el != "ь":
            surname += el

    try:
        new_surname = translit(surname, reversed=True)
    except:
        new_surname = surname

    with open(args.vectorizer_file) as fp:
        vectorizer = SurnameVectorizer.from_serializable(json.load(fp))
    classifier = SurnameClassifier(input_dim=len(vectorizer.surname_vocab), 
                                    hidden_dim=args.hidden_dim, 
                                    output_dim=len(vectorizer.nationality_vocab))

    classifier.load_state_dict(load(args.model_state_file))
    classifier.eval()

    classifier = classifier.to("cpu")
    prediction = predict_nationality(new_surname, classifier, vectorizer)

    output = Output(prediction=prediction["nationality"],
                    score=prediction["probability"])
    return output