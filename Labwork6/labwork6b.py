import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("scores.csv")
scores_df = df[['math', 'python','database']]
scores_df.plot(style="o")
plt.title("scattered")
plt.xlabel("")
plt.ylabel("score")
plt.savefig("scattered.png")
scores_df.plot.hist(subplots = True, title = "histogram")
plt.tight_layout()
plt.savefig("histo.png")
scores_df.plot.box()
plt.ylabel("math, python, database")
plt.savefig("box.png")



