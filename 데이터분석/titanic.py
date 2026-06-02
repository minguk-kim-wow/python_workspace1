# titanic_visual_analysis.py
# Titanic 데이터 기초 분석 + 시각화 예제
# AI, 머신러닝, 딥러닝 사용하지 않음
# pandas, matplotlib, seaborn 기반 분석
# Windows 환경에서 한글 깨짐 방지 설정 포함

import os

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# =========================================================
# 0. 기본 설정
# =========================================================

CSV_FILE = "./data/titanic_Kaggle.csv"
OUTPUT_DIR = "titanic_output"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# =========================================================
# 0-1. 한글 폰트 설정
# =========================================================

# Windows 기본 한글 폰트: 맑은 고딕
font_path = "C:/Windows/Fonts/malgun.ttf"

if os.path.exists(font_path):
    font_name = fm.FontProperties(fname=font_path).get_name()

    plt.rcParams["font.family"] = font_name
    plt.rcParams["axes.unicode_minus"] = False

    sns.set_theme(style="whitegrid", font=font_name)

    print("적용된 한글 폰트:", font_name)
else:
    print("맑은 고딕 폰트 파일을 찾지 못했습니다.")
    print("한글이 깨질 수 있습니다.")

    plt.rcParams["axes.unicode_minus"] = False
    sns.set_theme(style="whitegrid")


# =========================================================
# 1. 데이터 불러오기
# =========================================================

df = pd.read_csv(CSV_FILE)

print("=" * 70)
print("1. 데이터 기본 정보")
print("=" * 70)

print("\n[데이터 크기]")
print(df.shape)

print("\n[컬럼명]")
print(df.columns.tolist())

print("\n[상위 5개 데이터]")
print(df.head())

print("\n[데이터 정보]")
print(df.info())


# =========================================================
# 2. 기초 통계 확인
# =========================================================

print("\n" + "=" * 70)
print("2. 기초 통계")
print("=" * 70)

print("\n[숫자형 컬럼 기초 통계]")
print(df.describe())

print("\n[문자형 컬럼 기초 통계]")
print(df.describe(include="object"))


# =========================================================
# 3. 결측치 확인
# =========================================================

print("\n" + "=" * 70)
print("3. 결측치 확인")
print("=" * 70)

missing_count = df.isnull().sum()
missing_ratio = df.isnull().mean() * 100

missing_table = pd.DataFrame({
    "결측치 개수": missing_count,
    "결측치 비율(%)": missing_ratio.round(2)
})

print(missing_table)

missing_table.to_csv(
    os.path.join(OUTPUT_DIR, "missing_table.csv"),
    encoding="utf-8-sig"
)


# =========================================================
# 4. 전체 생존율 분석
# =========================================================

print("\n" + "=" * 70)
print("4. 전체 생존율 분석")
print("=" * 70)

survival_count = df["Survived"].value_counts().sort_index()
survival_ratio = df["Survived"].value_counts(normalize=True).sort_index() * 100

survival_table = pd.DataFrame({
    "인원수": survival_count,
    "비율(%)": survival_ratio.round(2)
})

survival_table.index = ["사망", "생존"]

print(survival_table)

survival_table.to_csv(
    os.path.join(OUTPUT_DIR, "survival_table.csv"),
    encoding="utf-8-sig"
)


# =========================================================
# 5. 성별 생존율 분석
# =========================================================

print("\n" + "=" * 70)
print("5. 성별 생존율 분석")
print("=" * 70)

sex_survival = df.groupby("Sex")["Survived"].agg(["count", "sum", "mean"])
sex_survival.columns = ["전체 인원", "생존 인원", "생존율"]
sex_survival["생존율"] = (sex_survival["생존율"] * 100).round(2)

print(sex_survival)

sex_survival.to_csv(
    os.path.join(OUTPUT_DIR, "sex_survival.csv"),
    encoding="utf-8-sig"
)


# =========================================================
# 6. 객실 등급별 생존율 분석
# =========================================================

print("\n" + "=" * 70)
print("6. 객실 등급별 생존율 분석")
print("=" * 70)

pclass_survival = df.groupby("Pclass")["Survived"].agg(["count", "sum", "mean"])
pclass_survival.columns = ["전체 인원", "생존 인원", "생존율"]
pclass_survival["생존율"] = (pclass_survival["생존율"] * 100).round(2)

print(pclass_survival)

pclass_survival.to_csv(
    os.path.join(OUTPUT_DIR, "pclass_survival.csv"),
    encoding="utf-8-sig"
)


# =========================================================
# 7. 성별 + 객실 등급별 생존율 분석
# =========================================================

print("\n" + "=" * 70)
print("7. 성별 + 객실 등급별 생존율 분석")
print("=" * 70)

sex_pclass_survival = df.groupby(["Sex", "Pclass"])["Survived"].agg(["count", "sum", "mean"])
sex_pclass_survival.columns = ["전체 인원", "생존 인원", "생존율"]
sex_pclass_survival["생존율"] = (sex_pclass_survival["생존율"] * 100).round(2)

print(sex_pclass_survival)

sex_pclass_survival.to_csv(
    os.path.join(OUTPUT_DIR, "sex_pclass_survival.csv"),
    encoding="utf-8-sig"
)


# =========================================================
# 8. 나이대별 생존율 분석
# =========================================================

print("\n" + "=" * 70)
print("8. 나이대별 생존율 분석")
print("=" * 70)

age_df = df.dropna(subset=["Age"]).copy()

age_df["AgeGroup"] = pd.cut(
    age_df["Age"],
    bins=[0, 10, 20, 30, 40, 50, 60, 70, 80],
    labels=[
        "0~10세",
        "11~20세",
        "21~30세",
        "31~40세",
        "41~50세",
        "51~60세",
        "61~70세",
        "71~80세",
    ],
    include_lowest=True
)

age_survival = age_df.groupby("AgeGroup", observed=False)["Survived"].agg(["count", "sum", "mean"])
age_survival.columns = ["전체 인원", "생존 인원", "생존율"]
age_survival["생존율"] = (age_survival["생존율"] * 100).round(2)

print(age_survival)

age_survival.to_csv(
    os.path.join(OUTPUT_DIR, "age_survival.csv"),
    encoding="utf-8-sig"
)


# =========================================================
# 9. 승선 항구별 생존율 분석
# =========================================================

print("\n" + "=" * 70)
print("9. 승선 항구별 생존율 분석")
print("=" * 70)

embarked_survival = df.groupby("Embarked")["Survived"].agg(["count", "sum", "mean"])
embarked_survival.columns = ["전체 인원", "생존 인원", "생존율"]
embarked_survival["생존율"] = (embarked_survival["생존율"] * 100).round(2)

print(embarked_survival)

embarked_survival.to_csv(
    os.path.join(OUTPUT_DIR, "embarked_survival.csv"),
    encoding="utf-8-sig"
)


# =========================================================
# 10. 요금 구간별 생존율 분석
# =========================================================

print("\n" + "=" * 70)
print("10. 요금 구간별 생존율 분석")
print("=" * 70)

fare_df = df.copy()

fare_df["FareGroup"] = pd.cut(
    fare_df["Fare"],
    bins=[0, 10, 30, 50, 100, 600],
    labels=[
        "0~10",
        "11~30",
        "31~50",
        "51~100",
        "101 이상",
    ],
    include_lowest=True
)

fare_survival = fare_df.groupby("FareGroup", observed=False)["Survived"].agg(["count", "sum", "mean"])
fare_survival.columns = ["전체 인원", "생존 인원", "생존율"]
fare_survival["생존율"] = (fare_survival["생존율"] * 100).round(2)

print(fare_survival)

fare_survival.to_csv(
    os.path.join(OUTPUT_DIR, "fare_survival.csv"),
    encoding="utf-8-sig"
)


# =========================================================
# 11. 시각화 1 - 전체 생존/사망 인원
# =========================================================

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Survived"
)

plt.title("전체 생존/사망 인원")
plt.xlabel("생존 여부")
plt.ylabel("인원수")
plt.xticks([0, 1], ["사망", "생존"])

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "01_survival_count.png"), dpi=150)
plt.show()


# =========================================================
# 12. 시각화 2 - 성별 생존율
# =========================================================

sex_survival_plot = sex_survival.reset_index()

plt.figure(figsize=(7, 5))

sns.barplot(
    data=sex_survival_plot,
    x="Sex",
    y="생존율"
)

plt.title("성별 생존율")
plt.xlabel("성별")
plt.ylabel("생존율(%)")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "02_sex_survival_rate.png"), dpi=150)
plt.show()


# =========================================================
# 13. 시각화 3 - 객실 등급별 생존율
# =========================================================

pclass_survival_plot = pclass_survival.reset_index()

plt.figure(figsize=(7, 5))

sns.barplot(
    data=pclass_survival_plot,
    x="Pclass",
    y="생존율"
)

plt.title("객실 등급별 생존율")
plt.xlabel("객실 등급")
plt.ylabel("생존율(%)")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "03_pclass_survival_rate.png"), dpi=150)
plt.show()


# =========================================================
# 14. 시각화 4 - 성별 + 객실 등급별 생존율
# =========================================================

sex_pclass_plot = sex_pclass_survival.reset_index()

plt.figure(figsize=(8, 5))

sns.barplot(
    data=sex_pclass_plot,
    x="Pclass",
    y="생존율",
    hue="Sex"
)

plt.title("성별 + 객실 등급별 생존율")
plt.xlabel("객실 등급")
plt.ylabel("생존율(%)")
plt.ylim(0, 100)
plt.legend(title="성별")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "04_sex_pclass_survival_rate.png"), dpi=150)
plt.show()


# =========================================================
# 15. 시각화 5 - 나이 분포
# =========================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Age",
    bins=30,
    kde=True
)

plt.title("승객 나이 분포")
plt.xlabel("나이")
plt.ylabel("인원수")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "05_age_distribution.png"), dpi=150)
plt.show()


# =========================================================
# 16. 시각화 6 - 생존 여부별 나이 분포
# =========================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Age",
    hue="Survived",
    bins=30,
    kde=True,
    multiple="stack"
)

plt.title("생존 여부별 나이 분포")
plt.xlabel("나이")
plt.ylabel("인원수")
plt.legend(title="생존 여부", labels=["생존", "사망"])

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "06_age_distribution_by_survival.png"), dpi=150)
plt.show()


# =========================================================
# 17. 시각화 7 - 나이대별 생존율
# =========================================================

age_survival_plot = age_survival.reset_index()

plt.figure(figsize=(9, 5))

sns.barplot(
    data=age_survival_plot,
    x="AgeGroup",
    y="생존율"
)

plt.title("나이대별 생존율")
plt.xlabel("나이대")
plt.ylabel("생존율(%)")
plt.ylim(0, 100)

plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "07_age_group_survival_rate.png"), dpi=150)
plt.show()


# =========================================================
# 18. 시각화 8 - 요금 분포
# =========================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Fare",
    bins=40,
    kde=True
)

plt.title("승객 요금 분포")
plt.xlabel("요금")
plt.ylabel("인원수")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "08_fare_distribution.png"), dpi=150)
plt.show()


# =========================================================
# 19. 시각화 9 - 요금 구간별 생존율
# =========================================================

fare_survival_plot = fare_survival.reset_index()

plt.figure(figsize=(8, 5))

sns.barplot(
    data=fare_survival_plot,
    x="FareGroup",
    y="생존율"
)

plt.title("요금 구간별 생존율")
plt.xlabel("요금 구간")
plt.ylabel("생존율(%)")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "09_fare_group_survival_rate.png"), dpi=150)
plt.show()


# =========================================================
# 20. 시각화 10 - 상관관계 히트맵
# =========================================================

numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(9, 7))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",
    linewidths=0.5
)

plt.title("숫자형 변수 상관관계 히트맵")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "10_correlation_heatmap.png"), dpi=150)
plt.show()


# =========================================================
# 21. 최종 요약
# =========================================================

print("\n" + "=" * 70)
print("11. 최종 요약")
print("=" * 70)

total_passengers = len(df)
total_survivors = int(df["Survived"].sum())
survival_rate = df["Survived"].mean() * 100

print(f"전체 승객 수: {total_passengers}명")
print(f"전체 생존자 수: {total_survivors}명")
print(f"전체 생존율: {survival_rate:.2f}%")

print("\n[저장 위치]")
print(OUTPUT_DIR)

print("\n[생성된 주요 파일]")
print("missing_table.csv")
print("survival_table.csv")
print("sex_survival.csv")
print("pclass_survival.csv")
print("sex_pclass_survival.csv")
print("age_survival.csv")
print("embarked_survival.csv")
print("fare_survival.csv")
print("01_survival_count.png")
print("02_sex_survival_rate.png")
print("03_pclass_survival_rate.png")
print("04_sex_pclass_survival_rate.png")
print("05_age_distribution.png")
print("06_age_distribution_by_survival.png")
print("07_age_group_survival_rate.png")
print("08_fare_distribution.png")
print("09_fare_group_survival_rate.png")
print("10_correlation_heatmap.png")

print("\n분석 완료")