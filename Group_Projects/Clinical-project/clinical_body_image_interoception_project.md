# Clinical Psychology Group Project: Body Image and Interoception

## Project overview

In this project, you will analyse a synthetic clinical psychology dataset.

The dataset was generated **in silico** for teaching purposes. It does **not** contain real patient data and should not be used to make clinical claims.

The simulated study compares two groups of participants:

- `control`
- `eating_disorder_risk`

The second group should be interpreted as a **clinical-risk group**, not as a confirmed diagnosis.

Your goal is to explore whether participants in the eating-disorder-risk group show stronger body-image concerns and altered interoceptive processing compared with controls.

---

## Clinical background

Eating-disorder risk is often associated with changes in how people experience, perceive, and evaluate their own body.

In this project, we focus on three psychological dimensions:

1. **Body image**: how negatively participants evaluate their own body.
2. **Body-size estimation**: whether participants tend to overestimate or underestimate their body size.
3. **Interoception**: how accurately participants perceive internal bodily signals.

The general research question is:

> Do participants in the eating-disorder-risk group show stronger body-image concerns and altered interoceptive processing compared with controls?

---

## Dataset

Before you start, upload the file `clinical_body_image_interoception_dataset.csv` to your Colab session.

Each row corresponds to one participant.

### Variables

| Column | Meaning |
|---|---|
| `participant_id` | Participant identifier |
| `age` | Age in years |
| `gender` | Gender category |
| `group` | `control` or `eating_disorder_risk` |
| `bmi` | Body mass index |
| `body_dissatisfaction` | Higher values indicate stronger body dissatisfaction |
| `drive_for_thinness` | Higher values indicate stronger desire to be thinner |
| `eating_concern` | Higher values indicate stronger eating-related concerns |
| `body_size_estimation_error` | Positive values indicate body-size overestimation; negative values indicate underestimation |
| `interoceptive_accuracy` | Accuracy in an interoceptive task, from 0 to 1 |
| `alexithymia_score` | Higher values indicate greater difficulty identifying and describing feelings |
| `meal_anxiety_pre` | Anxiety before a simulated meal-related task |
| `meal_anxiety_post` | Anxiety after a simulated meal-related task |

---

## Important note about synthetic clinical data

This dataset is simulated. The variables were designed to resemble realistic clinical psychology data, but they are not validated clinical scales.

For this reason, your conclusions should be written carefully.

Write:

> In this synthetic dataset, the eating-disorder-risk group showed higher body dissatisfaction.

Do **not** write:

> Eating disorders cause body dissatisfaction.

---

## Suggested workflow

### 1 — Load and inspect the data

Start by loading the CSV file and inspecting the dataset.

Questions to answer:

- How many participants are there?
- How many variables are there?
- What are the column names?
- Which variables are numerical?
- Which variables are categorical?
- Are there missing values?
- Are all values within plausible ranges?

Suggested Python tools:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("clinical_body_image_interoception_dataset.csv")
```

Useful methods:

```python
data.head()
data.shape
data.info()
data.describe()
data.isna().sum()
```

---

### 2 — Clean the data

Clinical datasets often contain missing or implausible values. Before analysing the data, inspect whether any values should be removed or treated as missing.

Things to check:

- missing values in questionnaire variables;
- impossible values in `interoceptive_accuracy`;
- implausible values in `bmi`;
- whether each group has enough participants after cleaning.

Hints:

- `interoceptive_accuracy` should be between 0 and 1;
- extremely high or low BMI values should be inspected;
- do not remove data without explaining your decision.

Suggested questions:

- Which rows contain missing values?
- Which values are impossible or implausible?
- How many participants remain after cleaning?

---

### 3 — Describe the clinical profile of each group

Compute descriptive statistics separately for the two groups.

Suggested variables:

- `body_dissatisfaction`
- `drive_for_thinness`
- `eating_concern`
- `bmi`
- `interoceptive_accuracy`
- `alexithymia_score`

Questions to answer:

- Which group has higher body dissatisfaction?
- Which group has higher eating-related concerns?
- Which group has lower interoceptive accuracy?
- Are the groups similar or different in BMI?

Useful Python reminders:

```python
data.groupby("group")["body_dissatisfaction"].mean()
data.groupby("group")["body_dissatisfaction"].agg(["mean", "std", "count"])
```

---

### 4 — Visualise group differences

Create clear plots comparing the two groups.

Recommended plots:

- boxplot of `body_dissatisfaction` by group;
- boxplot of `drive_for_thinness` by group;
- boxplot of `interoceptive_accuracy` by group;
- histogram of `body_size_estimation_error`;
- stripplot to show individual participants.

Suggested questions:

- Do the two groups overlap?
- Are the differences large or small?
- Are there possible outliers?
- Does the plot support the descriptive statistics?

Useful Python reminders:

```python
sns.boxplot(data=data, x="group", y="body_dissatisfaction")
sns.stripplot(data=data, x="group", y="body_dissatisfaction", alpha=0.6)
```

---

### 5 — Research question 1: body-image differences

Main question:

> Does the eating-disorder-risk group show higher body dissatisfaction than the control group?

Suggested analysis:

1. Compute the mean and standard deviation of `body_dissatisfaction` in each group.
2. Visualise the data using a boxplot and/or stripplot.
3. Run an independent-samples t-test.
4. Interpret the result.

Optional extension:

Repeat the same analysis for:

- `drive_for_thinness`
- `eating_concern`

---

### 6 — Research question 2: body-size estimation

Main question:

> Does the eating-disorder-risk group show stronger body-size overestimation?

Use the variable:

```text
body_size_estimation_error
```

Positive values indicate overestimation.

Suggested analysis:

1. Plot `body_size_estimation_error` by group.
2. Compute group means and standard deviations.
3. Run a t-test comparing the two groups.
4. Interpret whether the clinical-risk group shows stronger overestimation.

---

### 7 — Research question 3: interoception

Main question:

> Is interoceptive accuracy lower in the eating-disorder-risk group?

Use the variable:

```text
interoceptive_accuracy
```

Suggested analysis:

1. Check whether values are between 0 and 1.
2. Plot interoceptive accuracy by group.
3. Compare the two groups using a t-test.
4. Interpret the result.

Optional correlation:

> Are participants with higher alexithymia scores less accurate in the interoceptive task?

Variables:

- `alexithymia_score`
- `interoceptive_accuracy`

---

### 8 — Research question 4: meal-related anxiety

Participants rated their anxiety before and after a simulated meal-related task.

Create a new variable:

```text
meal_anxiety_change = meal_anxiety_post - meal_anxiety_pre
```

Interpretation:

- positive values mean anxiety increased after the task;
- negative values mean anxiety decreased after the task.

Questions to answer:

- Does meal-related anxiety change differently in the two groups?
- Which group shows the largest increase or decrease?
- Is the anxiety change associated with eating concern?

Suggested analysis:

1. Create the new variable.
2. Compute descriptive statistics by group.
3. Plot the new variable by group.
4. Run a t-test comparing the two groups.
5. Correlate `meal_anxiety_change` with `eating_concern`.

---

### 9 — Correlation analyses

Choose at least two correlations to test.

Suggested pairs:

1. `body_dissatisfaction` and `body_size_estimation_error`
2. `drive_for_thinness` and `eating_concern`
3. `alexithymia_score` and `interoceptive_accuracy`
4. `eating_concern` and `meal_anxiety_change`

For each pair:

1. create a scatterplot;
2. add a regression line;
3. compute Pearson correlation;
4. interpret the direction, strength, and p-value.

Useful Python reminder:

```python
from scipy.stats import pearsonr

r_value, p_value = pearsonr(data["body_dissatisfaction"], data["body_size_estimation_error"])
```

---

### 10 — Optional: create a clinical severity index

You can create a simple synthetic severity index by averaging three eating-related variables:

```text
clinical_severity_index = mean(body_dissatisfaction, drive_for_thinness, eating_concern)
```

Important: this is a **teaching variable**, not a validated clinical score.

Suggested questions:

- Is the severity index higher in the eating-disorder-risk group?
- Is it correlated with body-size estimation error?
- Is it correlated with meal-related anxiety change?

---

## Final report

At the end of the project, prepare a short summary of your findings.

Your summary should include:

1. the research question you focused on;
2. the cleaning steps you applied;
3. the main descriptive statistics;
4. at least two plots;
5. the result of at least one t-test;
6. the result of at least one correlation;
7. a short interpretation in plain language;
8. one limitation of the analysis.

Example conclusion:

> In this synthetic dataset, participants in the eating-disorder-risk group showed higher body dissatisfaction and larger body-size overestimation than controls. Body dissatisfaction was also positively associated with body-size estimation error. These results are consistent with the simulated clinical scenario, but they should not be interpreted as evidence from real patients.

---

## Tips for working as a group

- Start simple.
- Make sure everyone understands the dataset before writing code.
- Keep track of every cleaning decision.
- Use clear variable names.
- Add comments to your code.
- Save your plots with meaningful filenames.
- Do not focus only on p-values: look at the data, the means, and the plots.
- Be careful with clinical language: this is a risk group in synthetic data, not a diagnostic dataset.

---

## Useful Python reminders

### Select one group

```python
control_data = data[data["group"] == "control"]
risk_data = data[data["group"] == "eating_disorder_risk"]
```

### Select one column

```python
data["body_dissatisfaction"]
```

### Compute group summaries

```python
data.groupby("group")["body_dissatisfaction"].agg(["mean", "std", "count"])
```

### Create a new variable

```python
data["meal_anxiety_change"] = data["meal_anxiety_post"] - data["meal_anxiety_pre"]
```

### Make a boxplot

```python
sns.boxplot(data=data, x="group", y="body_dissatisfaction")
plt.show()
```

### Make a scatterplot with regression line

```python
sns.regplot(data=data, x="body_dissatisfaction", y="body_size_estimation_error")
plt.show()
```

---

Project designed for the SheCodesPsy: Reprogramming stereotypes! workshop  
13–15 May, 2026 · University of Granada, Spain
