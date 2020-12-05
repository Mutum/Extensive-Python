# Epai_Session_16


## Assignment 1 :

The files are:

personal_info.csv - personal information such as name, gender, etc. (one row per person)
vehicles.csv - what vehicle people own (one row per person)
employment.csv - where a person is employed (one row per person)
update_status.csv - when the person's data was created and last updated
Each file contains a key, SSN, which uniquely identifies a person.

This key is present in all four files.

You are guaranteed that the same SSN value is present in every file, and that it only appears once per file.

In addition, the files are all sorted by SSN, i.e. the SSN values appear in the same order in each file.

### Goal 1
Your first task is to create iterators for each of the four files that contained cleaned up data, of the correct type (e.g. string, int, date, etc), and represented by a named tuple.

For now these four iterators are just separate, independent iterators.


### Goal 2
Create a single iterable that combines all the columns from all the iterators.

The iterable should yield named tuples containing all the columns. Make sure that the SSN's across the files match!

All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file.

Make sure the SSN is not repeated 4 times - one time per row is enough!

### Goal 3
Next, you want to identify any stale records, where stale simply means the record has not been updated since 3/1/2017 (e.g. last update date < 3/1/2017). Create an iterator that only contains current records (i.e. not stale) based on the last_updated field from the status_update file.


### Goal 4
Find the largest group of car makes for each gender.

Possibly more than one such group per gender exists (equal sizes).


# Assignment 2

# Goal 1

For this goal, you are given a number of CSV files, each of which have their first row with the field name.

You goal is to create a context manager that you can use to produce the data from each file in a named tuple with field names corresponding to the  header row field names.

You should use the `csv` module's `reader` function to help with parsing the data.

Your context manager should be generic in the sense that it should just need the file name, no other configuration or hardcoded functionality is required. You do not need to worry about data types for this goal - just return every field as a string.

In addition, your context manager should produce lazy iterators.

Implement this using a class that implements the context manager protocol


# Goal 2

The goal is to reproduce the work you did in Goal 1, but using a generator function and the `contextlib` `contextmanager` decorator.
