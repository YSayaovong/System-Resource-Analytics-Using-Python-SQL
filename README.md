# System Resource Analytics with Python and SQLite
## Scope
Academic-style portfolio exercise importing process metrics from Excel into SQLite and querying CPU, memory and process-type summaries. This demonstrates basic data loading, SQL grouping/filtering and Excel export; it is not a production operating-system monitoring service.

## Files
- `ASU_IFT103_OS_Resource_Monitor.xlsx`: input workbook.
- `IFT103_SQL_Resource_Analytics.ipynb`: executable notebook.
- `os_metrics.db`: saved SQLite database.
- `High_CPU_Processes.xlsx`: saved filtered output.

## Notebook behavior
Loads the workbook with pandas, replaces the `process_metrics` table, queries the five processes with highest average CPU, average memory by date, process counts by type and records above 30% CPU. It exports those high-CPU rows to Excel.

## Run
Install pandas, openpyxl and Jupyter. Open the notebook, replace its two personal Windows paths with paths on your machine, then run cells in order. The SQLite module is included in Python. Work in a copy: loading replaces the existing table.

## Limitations
Input provenance, data validity and notebook output freshness require review. The 30% threshold is a fixed example, not a validated anomaly model. SQL query optimization, live collection and measured operational improvements are not demonstrated.
