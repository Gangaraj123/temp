# <p align='center'>IT496 - Introduction to Data Mining</p>
**Course Project**: 1 <br/>
**Lab Group**: T06<br />
**Dataset**: EV Charging Station


## **Introduction**
The Electric Vechilce(EV) Charging station dataset provides the information about the usage patterns of EV Charging stations in the city of Palo Alto, California. This includes data of the time from July 2011 to Jan 2021. It is an open dataset that provides information about the availaabillity, utilization and demand for EV charging infrastructure. This helps in a deeper understanding for the Local EV Market and thus helps researchers, analysts and businesses for sustainable transportation practices. This dataset contains the information on how much Energy is consumed in charging, how much GHG(Green House Gases) are saved by avoiding other fuel based vehicles. This helps to decide whether it is a better eco-friendly alternative or not.The dataset also includes the type of charging port, plugs, energy consumptions which enables to analyze the charging infrastructure performance. <br/>
* The dataset is of dimensions $259415\times33$. There are $259415$ instances of data and there are $33$ columns in each instance.<br/>
A summary of all the columns present in the dataset:
1. Station Name : Name of the EV Charging Station <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 47
2. MAC Address : MAC Address associated with Electric Charger <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 83
3. Org Name : City Name of charging station <br/> **Attribute Type**: Nomnial $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 1
4. Start Date : Start Data and  time stamp of charging <br/>**Attribute Type**: Interval scaled $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 244798
5. Start Time zone: Time zone where charging is being performed <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unqiue value counnt**:3
6. End Date : End Date and time stamp of charging <br /> **Attribute Type**: Interval scaled $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 244159
7. End Time zone: Time zone where charging is being ended <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 3
8. Transaction Date (Pacific Time): Transaction Date and Time <br/> **Attribute Type**: Interval scaled $\hspace{3cm}$ **Null count**: 209 <br/> **Unique value count**: 240905
9. Total Duration : Total Duration at the charging station <br/> **Attribute Type**: Interval scaled $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 31025
10. Charging Time : Time actually used for charging (can be less than total time) <br/> **Attribute Type**: Interval scaled $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 22473
11. Energy: Energy(in kwh) consumed for charging<br/> **Attribute Type**: Numerical $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 118061
12. GHG savings: Amount of Green House Gases(in KG) saved by using electricity instead of other fuels<br/> **Attribute Type**: Numerical $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 15535
13. Gasoline savings: Equivalent amount of Gasoline(in gallons) needed and saved <br/> **Attribute Type**: Numerical $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 6333
14. Port Type: Type of port used for charging(Level 1 or Level 2 port)<br/> **Attribute Type**: Binary $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 2
15. Port Number: Port Number used for charging <br/> **Attribute Type**: Binary $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 2
16. Plug Type: Type of plug used for charging($J1772$ or $NEMA 5-20R$)<br/> **Attribute Type**: Binary $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 2
17. EVSE ID: Electric vehicle Supply Equipment ID is a unqiue id for each charging point<br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 78948 <br/> **Unique value count**: 51
18. Address 1: Address of charging station <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 20
19. City: City where charging station is located <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 1
20. State/Province: Stat/Province where charging station is located<br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 1
21. Postal Code: Postal code of charging station location<br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 3
22. Country: Country of charging station<br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 1
23. Latitude: Latitude of charging station<br/> **Attribute Type**: Numerical $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 62
24. Longitude: Longitude of cahrging station<br/> **Attribute Type**: Numerical $\hspace{3cm}$ **Null count**: 0 <br /> **Unique value count**:64
25. Currency: type of currency used for transaction <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 1788 <br/> **Unique value count**: 4
26. Fee: Free amount for transaction<br/> **Attribute Type**: Numerical $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 1817
27. Ended by: How charging is ended  <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 248 <br/> **Unique value count**: 16
28. Plug In Event Id: unique ID for plugin event<br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 0 <br/> **Unique value count**: 36838
29. Driver Postal Code: Postal Code of location of driver <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 8402 <br/> **Unique value count**: 985
30. User Id: Id of user<br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 7677 <br/> **Unique value count**: 21441
31. County: The county(terrestrial division) to which chargin station belongs to <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 84665 <br/> **Unique value count**: 2
32. System S/N: System Serial Number <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 78948 <br/> **Unique value count**: 61
33. Model Number: Model Number of Charging Equipment <br/> **Attribute Type**: Nominal $\hspace{3cm}$ **Null count**: 78948 <br/> **Unique value count**: 10


## **Data Visualizations and insights through EDA**

