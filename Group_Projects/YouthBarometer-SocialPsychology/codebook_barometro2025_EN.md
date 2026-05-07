# Social Psychology project: Codebook
## Barómetro Juventud y Género 2025 (*Youth and Gender Barometer 2025*)

> The **Youth and Gender Barometer 2025** is an online survey of 3327 people living in Spain, of whom 1,528 are young people aged 15–29. Fieldwork was carried out between April and May 2025. This work is an powerful resource for understanding how young Spanish people interpret femininity and masculinity, their views on gender roles, and the kinds of relationships they build (among friends, at home, and with partners). It also explores how they see their place in the world: whether they experience discrimination and for what reasons, whether they are exposed to violence, among other issues. The study was funded by the Spanish Government Delegation against Gender Violence.
Source: Kuric Kardelis, S., Gómez Miguel, A. y Sanmartín Ortí, A. (2026). Barómetro Juventud y Género 2025. Centro Reina Sofía de Fad Juventud. https://doi.org/10.5281/zenodo.18482115

Within the context of the SheCodesPsy 2026 workshop, we are using a reduced version of this database, randomly picking a pool of **100 subjects** from the young people population, and a selection of **58 questions** out of the 97 survey items. 

---

## General notes
- **All variables are single-response** (one numeric value per respondent per column).
- **0–10 scales**: anchors described per item.
- **1–4 scales**: 1 = strongly disagree, 4 = strongly agree.

---

## BLOCK A — Sociodemographics

| Variable | Label | Type / Values |
|----------|-------|---------------|
| Num | Respondent ID | String |
| P1 | Age (exact years) | Numeric (15+) |
| P2 | Gender | 1=Woman · 2=Man · 3=Trans woman · 4=Trans man · 5=Other |
| P3 | Current activity | 1=Working · 2=Studying · 3=Both · 4=Unemployed · 5=Retired/pensioner · 6=Unpaid domestic work · 7=Other |
| P4 | Highest educational level completed | 1=Primary or less · 2=Lower secondary (ESO 1st stage) · 3=Lower secondary (ESO 2nd stage/VET basic) · 4=Upper secondary (Bachillerato) · 5=Mid-level VET · 6=Upper-level VET · 7=University · 8=Postgrad/Master/PhD · 9=Other official qualification |
| P6 | Current living arrangement | 1=Alone · 2=With parent(s) · 3=With partner (no children) · 4=With partner and children · 5=With children (no partner) · 6=With others (relatives, friends, etc.) |
| P7 | Disability / chronic illness limiting daily activities | 1=No · 2=Very mild limitations · 3=Mild · 4=Moderately severe · 5=Very severe |
| P8 | Political ideology (self-placement) | Scale 0 (far left) – 10 (far right) |
| P9 | Religiosity | Scale 0 (not at all religious) – 10 (very religious) |
| P10 | National origin | 1=Born in Spain, parents also · 2=Born in Spain, parents foreign · 3=Born in Spain, one parent foreign · 4=Born abroad, parents also · 5=Born abroad, parents Spanish |
| P11 | Current romantic/affective relationship | 1=Yes, currently · 2=No, but had one before · 3=No, never had one |

---

## BLOCK B — Gender Stereotypes (occupational fields)

*"Do you think the following fields are more suitable for women or for men?"*
Scale 0 (much better for women) – 10 (much better for men) · 5 = neutral

| Variable | Field |
|----------|-------|
| P22 | Healthcare / caregiving |
| P23 | Education / teaching |
| P24 | Science / research |
| P25 | Computing / IT |
| P26 | Business management |
| P27 | Engineering |

---

## BLOCK D — Inequalities & Discrimination

| Variable | Label | Type / Values |
|----------|-------|---------------|
| P48 | Size of gender inequalities in Spain today | 1=Very large · 2=Large · 3=Neither · 4=Small · 5=Very small · 6=Do not exist |
| P49 | Size of gender inequalities among young people | Same as P48 |
| P50 | Women vs. men: finding employment | Scale 0 (much worse for women) – 10 (much better for women) |
| P51 | Women vs. men: wages | Scale 0–10 |
| P52 | Women vs. men: access to leadership positions | Scale 0–10 |
| P53 | Women vs. men: work-life balance | Scale 0–10 |
| P54 | Women vs. men: walking alone in the street | Scale 0–10 |
| P55 | Women vs. men: expressing opinions in public | Scale 0–10 |
| P56 | Women vs. men: expressing emotions/vulnerability in public | Scale 0–10 |
| P57 | Women vs. men: dating / finding a partner | Scale 0–10 |

---

## BLOCK E — Diversity / LGBTIQ+

*Agreement scale: 0 (strongly disagree) – 10 (strongly agree)*

| Variable | Label |
|----------|-------|
| P60 | LGBTIQ+ people are discriminated against in our society |
| P61 | Laws are needed to protect LGBTIQ+ rights |
| P62 | Most young people who say they are LGBTIQ+ do it because it is fashionable |
| P63 | A trans woman (assigned male at birth) is a woman |
| P64 | A psychological/medical report should be required for sex reassignment |
| P65 | Sexual orientations are innate, not chosen |

---

## BLOCK F — Feminism & Gender Equality

| Variable | Label | Type / Values |
|----------|-------|---------------|
| P66 | Do you consider yourself a feminist? | 1=Yes · 2=No |

*Agreement scale: 0 (strongly disagree) – 10 (strongly agree)*

| Variable | Label |
|----------|-------|
| P67 | Feminism is necessary for real equality |
| P68 | Feminism should involve both women and men |
| P69 | Feminism is not necessary because equality already exists |
| P70 | Feminism seeks to pit women against men |
| P71 | Equality promotion has gone so far that men are now discriminated against |
| P72 | Current feminism is a tool of political manipulation and indoctrination |
| P73 | Gender equality contributes to a fairer society |
| P74 | Meritocracy is enough to guarantee gender equality at work |
| P75 | No law should favour women to achieve equality (quotas, parity lists…) |
| P76 | The gender pay gap does not exist |
| P77 | Women have to work harder than men to prove they can do the same job |
| P78 | Women carry a greater domestic/care burden which harms their careers |

---

## BLOCK G — Harassment & Violence (last 6 months)

*Frequency scale: 1=Never · 3=Sometimes · 4=Frequently · 5=Very frequently*

| Variable | Label |
|----------|-------|
| P79 | **Experienced**: mockery, insults or threats (in person or online) |
| P80 | **Experienced**: physical violence |
| P81 | **Experienced**: sexual harassment (in person or online) |
| P82 | **Committed**: mockery, insults or threats (in person or online) |
| P83 | **Committed**: physical violence |
| P84 | **Committed**: sexual harassment (in person or online) |

---

## BLOCK H — Gender-Based Violence Attitudes

*Agreement scale: 0 (strongly disagree) – 10 (strongly agree)*

| Variable | Label |
|----------|-------|
| P85 | Low-intensity gender violence is not a problem |
| P86 | Gender violence does not exist; it is an ideological invention |
| P87 | Men have lost the presumption of innocence |
| P88 | Gender violence has always existed and is inevitable |
| P89 | Men are unprotected against false gender violence accusations |
| P90 | We live in a patriarchal society that discriminates and violates women |
| P91 | Gender violence is a very serious social problem |
