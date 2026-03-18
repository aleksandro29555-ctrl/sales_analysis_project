import pandas as pd
import sqlite3
import plotly.express as px

DB_PATH = "database.db"

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql("SELECT * FROM user_actions", conn)

# 🔹 Выручка по категориям
revenue_by_category = (
    df[df["action"] == "purchase"]
    .groupby("category")["price"]
    .sum()
    .reset_index()
)

# 🔹 Конверсии
views = df[df["action"] == "view"]["user_id"].nunique()
cart = df[df["action"] == "add_to_cart"]["user_id"].nunique()
purchase = df[df["action"] == "purchase"]["user_id"].nunique()

conversion_df = pd.DataFrame({
    "metric": ["view→cart", "cart→purchase", "view→purchase"],
    "value": [
        cart / views if views else 0,
        purchase / cart if cart else 0,
        purchase / views if views else 0
    ]
})

# 🔹 Популярность категорий
popularity = (
    df[df["action"] == "view"]
    .groupby("category")
    .size()
    .reset_index(name="views")
)

# 📊 графики
fig1 = px.bar(popularity, x="category", y="views", title="Category popularity")
fig1.write_html("output/category_popularity.html")

fig2 = px.bar(revenue_by_category, x="category", y="price", title="Revenue by category")
fig2.write_html("output/category_revenue.html")

# 📁 экспорт Excel
with pd.ExcelWriter("output/metrics.xlsx") as writer:
    revenue_by_category.to_excel(writer, sheet_name="Revenue", index=False)
    conversion_df.to_excel(writer, sheet_name="Conversion", index=False)

conn.close()

print("Analysis completed")