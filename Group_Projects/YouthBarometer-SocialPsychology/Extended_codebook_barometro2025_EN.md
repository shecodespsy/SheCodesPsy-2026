# Codebook — Barómetro Juventud y Género 2025 (FULL)
**Youth and Gender Barometer 2025**
Source: Kuric Kardelis, S., Gómez Miguel, A. y Sanmartín Ortí, A. (2026). Barómetro Juventud y Género 2025. Centro Reina Sofía de Fad Juventud. https://doi.org/10.5281/zenodo.18482115
**Full youth sample: 1,528 respondents · 293 variables**

> The **Youth and Gender Barometer 2025** is an online survey of 3,327 people living in Spain, of whom 1,528 are young people aged 15–29. Fieldwork was carried out between April and May 2025. This fifth edition consolidates a series begun in 2017, making it possible to analyse trends over a decade. The study was funded by the Government Delegation against Gender Violence. It is an essential resource for understanding how young people interpret femininity and masculinity, their views on gender roles, and the kinds of relationships they build — among friends, at home, and with partners. It also explores how they see their place in the world: whether they experience discrimination and for what reasons, whether they are exposed to violence, and much more.

---

## General notes
- **Missing / No answer**: already replaced with `NaN` in this dataset.
- **Multi-response items** (P20, P21, P28, P31, P58, P59, P92–P98): expanded into binary columns (e.g. `P20_1`, `P20_2`…), where `1` = selected, `0`/NaN = not selected.
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
| P5 | Municipality size | 1=<10,000 · 2=10,000–99,999 · 3=100,000–499,999 · 4=500,000–1M · 5=>1M inhabitants |
| P6 | Current living arrangement | 1=Alone · 2=With parent(s) · 3=With partner (no children) · 4=With partner and children · 5=With children (no partner) · 6=With others |
| P7 | Disability / chronic illness limiting daily activities | 1=No · 2=Very mild · 3=Mild · 4=Moderately severe · 5=Very severe |
| P8 | Political ideology (self-placement) | Scale 0 (far left) – 10 (far right) |
| P9 | Religiosity | Scale 0 (not at all religious) – 10 (very religious) |
| P10 | National origin | 1=Born in Spain, parents also · 2=Born in Spain, parents foreign · 3=Born in Spain, one parent foreign · 4=Born abroad, parents also · 5=Born abroad, parents Spanish |
| P11 | Current romantic/affective relationship | 1=Yes, currently · 2=No, had one before · 3=No, never |
| P12 | Went on holiday at least one week/year | 1=Yes · 2=No |
| P13 | Kept home at adequate temperature | 1=Yes · 2=No |
| P14 | Covered unexpected expenses in a month | 1=Yes · 2=No |
| P15 | Paid bills/loans/rent on time | 1=Yes · 2=No |
| P16 | Saved part of monthly income | 1=Yes · 2=No |
| P17 | Afforded a treat at least once a month | 1=Yes · 2=No |
| P18 | Had a computer at home | 1=Yes · 2=No |
| P19 | Participated regularly in leisure activities | 1=Yes · 2=No |

---

## BLOCK B — Gender Stereotypes

**P20_1 – P20_18** — *Which of the following best defines women?* (select up to 5, binary columns)
1=Dynamic/active · 2=Hard-working · 3=Studious · 4=Responsible · 5=Sensitive/tender · 6=Independent · 7=Empathetic · 8=Possessive/jealous · 9=Aggressive/violent · 10=Cold/unemotional · 11=Individualistic/selfish · 12=Promiscuous · 13=Brave · 14=Caring/attentive · 15=Immature · 16=Submissive · 17=Vain/flirtatious · 18=Manipulative

**P21_1 – P21_18** — *Which of the following best defines men?* (select up to 5, binary columns)
Same options as P20.

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

**P28_1 – P28_15** — *Which of the following have made you feel social pressure?* (select all, binary columns)
1=Succeed at work/study · 2=Hide sadness/anxiety · 3=Be physically attractive · 4=Care for others emotionally · 5=Do household chores · 6=Be good at sex · 7=Have a stable partner · 8=Not disappoint others · 9=Hook up a lot · 10=Have children · 11=Take the initiative in flirting · 12=Earn money · 13=Show strength in hard times · 14=Show leadership · 15=No social pressure felt

---

## BLOCK C — Relationships, Partnership & Family

| Variable | Label | Type / Values |
|----------|-------|---------------|
| P29 | Sexual orientation | 1=Heterosexual · 2=Homosexual · 3=Bisexual · 4=Other |
| P30 | Do you have children? | 1=Yes · 2=No, would like to · 3=No, unsure · 4=No, do not want |

**P31_1 – P31_14** — *Most important conditions for having children* (select up to 3, binary columns)
1=Stable relationship · 2=Shared parenting · 3=Sufficient maturity · 4=Good financial situation · 5=Work-life balance · 6=Stable housing · 7=Good public services for children · 8=Not being too old · 9=Having enjoyed life without children · 10=Fits career plan · 11=Professional fulfilment · 12=Friends have children · 13=Social support network · 14=Other

| Variable | Label | Type / Values |
|----------|-------|---------------|
| P32 | Importance of having a partner | 1=Very important · 2=Quite · 3=Neither · 4=Not very · 5=Not at all |
| P33 | Preferred type of relationship | 1=Monogamous · 2=Non-monogamous · 3=Casual/uncommitted · 4=No relationship · 5=Other |
| P34 | Agreement: each partner needs personal space | Scale 0–10 |
| P35 | Agreement: open communication is the basis of a healthy relationship | Scale 0–10 |
| P36 | Agreement: equal rights and responsibilities are fundamental | Scale 0–10 |
| P37 | Agreement: it is normal to check your partner's phone | Scale 0–10 |
| P38 | Agreement: jealousy is a sign of love | Scale 0–10 |
| P39 | Agreement: having a partner means total devotion | Scale 0–10 |
| P40 | Agreement: when you have a partner, friends are less important | Scale 0–10 |
| P41 | Agreement: a relationship should be for life | Scale 0–10 |
| P42 | Agreement: you deserve to know where your partner is at all times | Scale 0–10 |
| P43 | Agreement: true love forgives everything, even being hurt | Scale 0–10 |
| P44 | Who does household/caregiving tasks at home? | 1=Women only · 2=Mostly women · 3=Everyone equally · 4=Men only · 5=Mostly men *(filtered: not living alone)* |
| P45 | Agreement: women should be in charge of home care | 1=Strongly disagree – 4=Strongly agree |
| P46 | Agreement: women are naturally better at caring for children | 1=Strongly disagree – 4=Strongly agree |
| P47 | Agreement: men should be the breadwinners | 1=Strongly disagree – 4=Strongly agree |

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

**P58_1 – P58_99** — *Have you ever felt discriminated against for any of the following?* (select all, binary columns)
1=Gender identity (trans, non-binary…) · 2=Being a man · 3=Being a woman · 4=Ethnic/racial origin · 5=Physical appearance · 6=Nationality · 7=Political opinions · 8=Disability · 9=Religion/beliefs · 10=Being young · 11=Sexual orientation · 12=Being older · 13=Economic situation · 14=Other · 15=Never discriminated

**P59_1 – P59_99** — *In which context did you experience gender-based discrimination?* (select all, binary; filtered to P58=1,2,3)
1=Work · 2=Public services · 3=Education · 4=Police · 5=Housing · 6=Shops/leisure/private services · 7=Family · 8=Street/public · 9=Social media · 10=Other · 11=All contexts

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

## BLOCK H — Gender-Based Violence

*Attitudes (P85–P91): Agreement scale 0 (strongly disagree) – 10 (strongly agree)*

| Variable | Label |
|----------|-------|
| P85 | Low-intensity gender violence is not a problem |
| P86 | Gender violence does not exist; it is an ideological invention |
| P87 | Men have lost the presumption of innocence |
| P88 | Gender violence has always existed and is inevitable |
| P89 | Men are unprotected against false gender violence accusations |
| P90 | We live in a patriarchal society that discriminates and violates women |
| P91 | Gender violence is a very serious social problem |

**P92_1 – P92_99** — *Violence witnessed: behaviours a man did to a woman in respondent's close circle* (binary columns)
1=Hit her · 2=Forced her with threats · 3=Sent threatening/offensive messages · 4=Shared intimate images without consent · 5=Threatened to harm her if she left · 6=Threatened self-harm if she left · 7=Forced sexual intercourse · 8=Filmed/photographed without consent · 9=Controlled who she could talk to · 10=Tried to isolate her from friends · 11=Told her she was worthless · 12=Insulted/humiliated her · 13=Made her feel afraid · 14=Checked her phone · 15=Constantly tracked her location · 16=Told her to delete/not post on social media · 17=Got angry if she didn't reply immediately · 98=None · 99=No answer

**P93_1 – P93_99** — *Violence suffered in own relationship(s)* (binary columns)
Same 17 behaviours as P92, plus: 18=None · 19=Never had a partner

**P94_1 – P94_99** — *Violence perpetrated in own relationship(s)* (binary columns)
Same structure as P93.

**P95_1 – P95_99** — *Actions taken after suffering violence* (binary; filtered to those reporting P93 items)
1=Searched online · 2=Talked to friends · 3=Talked to family · 4=Talked to people in my environment · 5=Confronted partner directly · 6=Ended the relationship · 7=Contacted police/legal aid · 8=Talked to partner's circle · 9=Sought psychological support · 10=Used gender violence services · 11=Told no one · 12=Did nothing

**P96_1 – P96_99** — *Consequences experienced after suffering violence* (select up to 5, binary columns)
1=Reputational damage/humiliation · 2=Guilt/shame · 3=Isolation/loneliness · 4=Avoiding certain places · 5=Loss/change of friends · 6=Reduced in-person or online interactions · 7=Closed/restricted social media · 8=Changes in sexual behaviour · 9=Changes in eating habits · 10=Sleep problems · 11=Self-harm or suicidal thoughts · 12=Alcohol/drug abuse · 13=Physical problems · 14=Mental health problems · 15=Deterioration of self-esteem

**P97_1 – P97_99** — *Reasons for not telling anyone* (binary; filtered to P95=11)
1=Did not consider it serious · 2=Shame/discomfort · 3=Fear of being blamed · 4=Fear of not being believed · 5=Fear of rejection · 6=Fear of further violence · 7=Fear of ending the relationship · 8=Did not think anyone could help · 9=Other

**P98_1 – P98_99** — *Factors that most influence violence against women* (select up to 3, binary columns)
1=Unfavourable socioeconomic conditions · 2=Religious beliefs/practices · 3=Alcohol and drug use · 4=Customs of immigrant communities · 5=Lack of education · 6=Women's provocation · 7=Breakups/separations/conflicts · 8=Violence in video games/films/TV · 9=Impunity of perpetrators · 10=Women not reporting · 11=Changes in women's social role · 12=Gender inequality · 13=Patriarchal upbringing · 14=Gender-specific violence does not exist
