from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM
from sklearn.linear_model import LogisticRegression
import torch
import pandas as pd
from lightning.pytorch import seed_everything
import random
import os


def configure_environment(device=None, seed=None):
    device = device or "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        os.environ["CUDA_VISIBLE_DEVICES"] = ""
        torch.cuda.is_available = lambda: False
    torch.set_default_device(device)
    seed_everything(seed or random.randint(0, 123456))
    print("Device set to", device)


def load_model(model_name="gpt2", device=None, causal=False):
    device = device or "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    loader = AutoModelForCausalLM if causal else AutoModel
    model = loader.from_pretrained(model_name).to(device)
    return model, tokenizer, device


def load_review_data(path="reviews.txt"):
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            sentiment, review_text = line.strip().split(" ", 1)
            data.append((sentiment == "GOOD", review_text))
    return pd.DataFrame(data, columns=["label", "text"])


def augment_data(df, augmentation, K=3):
    augmented_rows = []

    # For each row in the dataframe
    for _, row in df.iterrows():
        augmented_rows.append(row)

        # Generate K augmented versions of the text
        for _ in range(K):
            augmented_rows.append(augmentation(row.copy()))

    # Create a new dataframe with the augmented rows
    return pd.DataFrame(augmented_rows)


def logistic_regression(x_train, y_train, x_test, y_test):
    clf = LogisticRegression(random_state=0).fit(x_train, y_train)
    return dict(
        train=clf.score(x_train, y_train),
        test=clf.score(x_test, y_test),
    )
