import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://gist.githubusercontent.com/rajkumarboddapati2/022da822d54e968e3f3fcb0f9a8f7a6a/raw/accidentdataset.csv'
df = pd.read_csv(url)

print(" Dataset Loaded — Shape:", df.shape)
print("\n Sample Records:\n", df.head())


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce').dt.hour

df.dropna(subset=['Hour'], inplace=True)

plt.figure(figsize=(10, 5))
sns.countplot(x='Hour', data=df, palette='Set2') 
plt.title(' Accidents by Hour of the Day')
plt.xlabel('Hour (0-23)')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.show()

if 'Accident_Type' in df.columns:
    plt.figure(figsize=(10, 5))
    sns.countplot(y='Accident_Type', data=df,
                  order=df['Accident_Type'].value_counts().index,
                  palette='Paired') 
    plt.title(' Accident Types')
    plt.xlabel('Count')
    plt.ylabel('Type')
    plt.tight_layout()
    plt.show()
else:
    print(" 'Accident_Type' column not found in dataset.")


if 'State' in df.columns:
    plt.figure(figsize=(10, 5))
    top_states = df['State'].value_counts().nlargest(10)
    sns.barplot(x=top_states.index, y=top_states.values, palette='cubehelix')
    plt.title(' Top 10 States with Most Accidents')
    plt.xlabel('State')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.show()
