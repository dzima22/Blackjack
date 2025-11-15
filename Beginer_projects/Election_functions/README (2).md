# :open_file_folder: Content
- [code_for functions](https://github.com/dzima22/writing-election-functions-/blob/main/two%20functions.ipynb) – Jupyter Notebook script
- [excel data](https://github.com/dzima22/writing-election-functions-/tree/main/datasets) – all necessary data 
# 🔑 Description

## First function named `election_statistics`
- ***The function returns a DataFrame with the names of 8 districts (powiaty) which had the lowest voter turnout in the parliamentary elections (wybory do Sejmu) in year n.The DataFrame also includes the level of voter turnout in those counties for both year n and year m.***
- Args:
     + year(list of strings): A list of string values.
     + jst(string value)= string 'Powiat' albo 'Gmina'
     + jst_number(integer_number)= integer 
     + sort(Boolean value)=Bool
     + sort_year(integer value)=-integer
     + stat(string)=string 
- Returns:
     dataframe: dataframe with districts and statistics 

- Example:
        >>> `election_statistics`(year = [2015, 2019], jst=’powiat’, jst_number=8, sort=True, stat=‘frekwencja’)
        sorted data frame of 8 counties with highest turnout in 2015 and 2019
## Second  function named `election`
- ***The function returns a data frame showing the average statistics in the n districts with the highest total number of votes cast separately in each province and year***
- Args:
   + year (list of int): A list of integer values.
   + parties (list of string): A list of string values.
   + count (integer): Integer.

- Returns:
        dataframe: Sorted dataframe with counties and statistics.

- Example:
        >>> `election`(year=[2015, 2019], parties=['PIS', 'KO', 'PSL'], count=2)
        dataset of two districts with the highest number of votes separately in each province with statistics for 2015 and 2019
