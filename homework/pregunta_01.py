def pregunta_01():
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("files/input/news.csv")

    df = df.rename(columns={"Unnamed: 0": "Year"})

    os.makedirs("files/plots", exist_ok=True)

    plt.figure(figsize=(10, 6))

    plt.plot(df["Year"], df["Television"], label="Television")
    plt.plot(df["Year"], df["Newspaper"], label="Newspaper")
    plt.plot(df["Year"], df["Internet"], label="Internet")
    plt.plot(df["Year"], df["Radio"], label="Radio")

    plt.title("News Source")
    plt.xlabel("Year")
    plt.ylabel("Percent")
    plt.legend()

    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()
