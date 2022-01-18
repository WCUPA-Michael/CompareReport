# Compare Report

[![Compare Report]({image-url})]({https://drive.google.com/file/d/1Bcfc_PTJhZfEWHpIIe1Ab7w_u-A3wuNY/view?usp=sharing} "Preview Program")

**Data Sources**
- NJMMP: Patient and amount entered into state website.
- Local: Patient and amount entered into local point of sale (POS) system.

**Data Fields**
- First Name: Name
- Last Name: Name
- MMP ID: 123456-78901p
- Amount: ?

**Objectives**
- Compare transactions of users from both data sources.

**Test Scenarios**
- Test 1: local.csv, njmmp.csv
    - incorrect input
    => John
- Test 2: local_1.csv, njmmp_1.csv
    - incorrect input
    - datasets not in sequential order
    => Bob
- Test 3: local_2.csv, njmmp_2.csv
    - incorrect input
    - datasets not in sequential order
    - one patient with multiple purchases: second purchase incorrect input
    => Carmen
- Test 4: local_3.csv, njmmp_3.csv
    - incorrect input
    - datasets not in sequential order
    - multiple patients with multiple purchases: second purchase incorrect input for each
    => Carmen, Dale
- Test 5: local_4.csv, njmmp_4.csv
    - incorrect input
    - datasets not in sequential order
    - multiple patients with multiple purchases: second purchase incorrect input for each
    - Transaction never input into state site
    => Carmen, Dale, Edward
