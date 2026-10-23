# System Resource Analytics Using Python and SQL
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
Install pandas, openpyxl and Jupyter. Start Jupyter in this repository directory, open `IFT103_SQL_Resource_Analytics.ipynb`, then run cells in order. Paths resolve from the current working directory; the input workbook, database and export stay in the repository directory. The SQLite module is included in Python. Work in a copy: loading replaces the existing table.

## Limitations
Input provenance and data validity require review. Notebook execution outputs are cleared so historical results are not mistaken for a fresh run; the committed database and exported workbook are saved snapshots. The 30% threshold is a fixed example, not a validated anomaly model. SQL query optimization, live collection and measured operational improvements are not demonstrated.

## Validation of the portable notebook
All code cells were executed against the included workbook after replacing machine-specific paths. The input contains 150 records and the CPU > 30% export contains 24 records. The exported row count and CPU threshold were checked. Saved notebook outputs remain cleared so later users can distinguish their own run.

Path portability and documentation updates were developed with AI assistance. This is portfolio SQL/Python practice, not a claim of workplace programming experience.
