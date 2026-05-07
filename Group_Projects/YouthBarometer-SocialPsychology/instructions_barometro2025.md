# Social Psychology project: Instructions
## Barómetro Juventud y Género 2025 (*Youth and Gender Barometer 2025*)

> **Before you start:** upload the file `database_barometro2025.csv` to your Colab session using the folder icon on the left panel, then run the cells in order.

---

### 1 — Load & explore the data

#### 1.1 Import libraries and load the dataset

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("barometro_juventud_genero_2025_muestra100.csv")
```

#### 1.2 Explore basic properties of the dataset

How many respondents are there? How many variables?
Preview the first rows ot the table, list the columns names.
Look at the min/max/mean for different variables (survey items): which are their range of response? 

---

### 2 — Visualise distributions the database variables 

Try to visualize the distribution (histograms, boxplots) of differnt variables. You can start with demographic variables such as age (P1) or gender (P2). You can also visualize the some survey items to see how are they distributed. 
___

### 3 — Build some variables of interest combining different items

Let's turn individual survey items into meaningful summary scores by **averaging** related questions together. 

> **Note:** When averaging, you'll have to indicate the *dimension* (across rows or across columns) where you want to comptue the mean. **`axis=0`** (option by deafult) averages across rows (or participants) for each item. **`axis=1`** averages across columns (or **items**) for each respondent.

**Anti-feminism score: P69–P72.** Items: *feminism is unnecessary · feminism pits women vs men · equality promotion discriminates men · feminism is political manipulation*.

**Gender equality beliefs: P67, P68, P73, P77, P78.** Items: *feminism is necessary · feminism should include men · equality makes society fairer · women must work harder to prove themselves · women carry greater domestic burden.*

**Gender-Based Violence Attitudes: P85-91.** Items: *gender violence is not a problem, gender violence does not exist and is an ideological invention, Men have lost the presumption of innocence, Gender violence has always existed and is inevitable, Men are unprotected against false gender violence accusations, We live in a patriarchal society that discriminates and violates women. Gender violence is a very serious social problem*

> **Note:** Do all items of these variables go in the same direction, i.e., greater score = more equalitarian or more sexist? Whenever that's not the case, you must identify those items and invert them. E.g., in a scale from 1 to 10, an inverse item scored with a 2 would turn into an 9. 


#### 3.1 Plot the distribution of the three variables 

Which scale shows the most spread (variability)? Which is most skewed?

#### 3.2. Compute descriptive statistics of the three variables

If just computing the mean and standard deviation is too straight-forward, you can also to compute them separately by gender. 

---

### Phase 4 — Correlations & scatter plots

#### 4.1 Correlate the three variables 

Compute the Pearson's r coefficient and associated p value between:
- Antifeminism & gender equality beliefs
- Antifeminism & gender violence beliefs
- Antifeminism & gender equality beliefs

#### 4.2 Plot your final results!

The most effictive plots for your dataset are **scatter plots**, where each dimension (x,y) correspond to one of your variables, and individual plots reflect participants averages. Generate a plot for each pair of variables correlated above. When you're already there, try to add a regression line on top of it. 

#### 4.3 Correlation matrix heatmap

You can also try to build and plot a correlation matrix, where each column and row represent a variable, and the cells within, r coefficients. Hence, you should get a 3 by 3 matrix, where the diagonal is 1 (one variable correlated against itself: r = 1).

---

### EXTRA — Open analysis: your own question

If the above exercises were too easy, now it's your turn to get this database to the next level! Choose a research question that interests you and try to contrast it agains the data. Once you have your hypothesis, identify the key items and/or build new variables, carry out the required analysis and try to plot its result in a meaningful fashion. 

Here are som ideas...
- Gender equality belifs predicts adherence to LGBTIQ+ rights (`gender-equality` vs P60, P61, P62)
- Anti-feminism correlates with denying the gender pay gap (`antifeminism` vs P76)
- Young women and men differ in their antifemist attitudes, and gender equality and gender violence beliefs.
---


Project designed for the SheCodesPsy: Reprogramming stereotypes! workshop (13-15 May, 2026, Granada).  
Database: Kuric Kardelis, S., Gómez Miguel, A. y Sanmartín Ortí, A. (2026). Barómetro Juventud y Género 2025. Centro Reina Sofía de Fad Juventud. https://doi.org/10.5281/zenodo.18482115
