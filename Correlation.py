import pandas as pd
from scipy.stats import spearmanr

# Load the Excel files into DataFrames
df_metabolites = pd.read_excel("D:/Metabolites.xlsx")
 
df_microbiome = pd.read_excel("D:/Microbe.xlsx")

# Ensure that only data columns (not indices) are used for correlation
# Reset the indices if necessary to align both DataFrames
df_metabolites = df_metabolites.reset_index(drop=True)
df_microbiome = df_microbiome.reset_index(drop=True)

# Initialize an empty DataFrame for the correlation matrix
correlation_matrix_df = pd.DataFrame(index=df_metabolites.columns, columns=df_microbiome.columns)

# Compute the Spearman correlation for each pair of columns
for metabolites_col in df_metabolites.columns:
    for microbiome_col in df_microbiome.columns:
        correlation_matrix_df.loc[metabolites_col, microbiome_col], _ = spearmanr(df_metabolites[metabolites_col], df_microbiome[microbiome_col])

# Save the correlation matrix to an Excel file if needed
correlation_matrix_df.to_excel("D:/correlation.xlsx")

# Extract metabolite names (index) and microbe names (columns)
metabolite_names = correlation_matrix_df.index
microbe_names = correlation_matrix_df.columns

# Convert the correlation values to numeric, coercing errors to NaN
correlation_values = correlation_matrix_df.apply(pd.to_numeric)

# Initialize a list to store the results
results = []

# Iterate over the rows (metabolites) and columns (microbes) of the DataFrame
for metabolite in metabolite_names:
    for microbe in microbe_names:
        correlation_value = correlation_values.loc[metabolite, microbe]
        # Check if correlation meets the condition and is not NaN
        if not pd.isna(correlation_value) and (correlation_value > 0.1 or correlation_value < -0.1):
            results.append([metabolite, microbe, correlation_value])

# Create a new DataFrame from the results list
results_df = pd.DataFrame(results, columns=['Metabolite', 'Microbe', 'Correlation'])

# Sort the results DataFrame by correlation value for better readability
results_df = results_df.sort_values(by='Correlation', ascending=False)

# Reset the index of the DataFrame
results_df.reset_index(drop=True, inplace=True)

# Save the results to an Excel file with formatting
output_file = "D:/relevent_scorrelation.xlsx"
results_df.to_excel(output_file, index=False)

print(f"Results saved to {output_file}")
