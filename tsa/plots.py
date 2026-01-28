from pathlib import Path

from loguru import logger
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
import typer

from tsa.config import FIGURES_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


def sns_lineplot(title, x, xlabel, y, ylabel, data):
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x=x, y=y)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

