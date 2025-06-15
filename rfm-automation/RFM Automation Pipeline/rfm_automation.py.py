import pandas as pd

# Step 1: Load the CSV
file_path = 'C:/Users/Prabhu/Downloads/rfm_segmented_export.csv'  # Adjust path if needed
df = pd.read_csv(file_path)

# Step 2: Display first few rows
print("Preview of your data:")
print(df.head())
# Step 3: Get unique segments
segments = df['Segment'].unique()

# Step 4: Create folder to save outputs
import os
output_folder = 'segment_exports'
os.makedirs(output_folder, exist_ok=True)

# Step 5: Loop through each segment and save file
for segment in segments:
    segment_df = df[df['Segment'] == segment]
    clean_name = segment.replace(' ', '_').lower()
    file_name = f"{output_folder}/{clean_name}_customers.csv"
    segment_df.to_csv(file_name, index=False)
    print(f"Exported: {file_name}")
# Step 6: Create summary of segment-wise stats
summary_df = df.groupby('Segment').agg({
    'CustomerID': 'count',
    'Monetary': 'sum'
}).reset_index()

# Rename columns for clarity
summary_df.columns = ['Segment', 'Customer Count', 'Total Revenue']

# Step 7: Save summary to Excel/CSV
summary_file = 'rfm_segment_summary.csv'
summary_df.to_csv(summary_file, index=False)

print("\n✅ Segment Summary Created and Saved as:", summary_file)
print(summary_df)



