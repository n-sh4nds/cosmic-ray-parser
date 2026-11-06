# Cosmic Ray Data Parser

## Project Overview 🌐
This program extracts and analyzes cosmic ray data from the Oulu Cosmic Ray Station. It processes the data to compute basic statistics, helping to monitor space weather events.

## What the Code Does 📜
*   **Data Loading & Cleaning:** Reads CSV data using Pandas and renames columns for better readability.
*   **Statistical Analysis:** Uses the `.describe()` method to quickly extract the Mean, Median, Maximum, and Minimum of the `CorrectedCountRate`.
*   **Custom Data Filtering:** Implements a custom function (`greater_than_mean`) to count how many data points exceed the average cosmic ray flux.
*   **Data Summary:** Outputs the total number of rows and columns to verify data integrity.

## Tools Used 🛠️
*   **Python**
*   **Pandas:** Used for data manipulation and statistical analysis

