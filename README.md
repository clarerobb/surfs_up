# Surfs Up: Weather Analysis with SQLite

## Overview
This analysis compares key weather differences for potential investors of an Ice Cream and Surf Shop in Oahu, Hawaii. 

## Data
- **Data Source:** hawaii.sqlite
- **Software:** SQLite, Python 3.9.12, Flask, Jupyter Notebook

## Results
- When comparing the summary statistics below, the average recorded temperature in June and December are both in the 70°F range.
- June is slightly warmer with the average temperature being about 75°F compared to December's average temperature of 71°F. 
- Temperatures in June had a smaller standard deviation than the temperatures in December, which means the December temperatures fluctuate more than they do in June. This is also can be seen when comparing the range of the minimum and maximum temperatures for the two month. There is only a 21° difference between the recorded low and high temperature in June, while there is a 27° difference for December. 

| June Temperatures Statistics  | December Temperatures Statistics| 
|----------------------------|------------------------------|
|![Screen Shot 2022-08-06 at 1 16 53 PM](https://user-images.githubusercontent.com/106405775/183261179-4fcde6b3-b955-466a-a1a7-fb990f125e97.png)| ![Screen Shot 2022-08-06 at 1 17 05 PM](https://user-images.githubusercontent.com/106405775/183261188-a13ea2da-57e7-4ce0-a5ea-f14eba405eb2.png)|

## Summary
Overall, temperatures in Oahu, Hawaii are relatively the same throughout the year and would provide appropriate weather conditions for surfing and ice cream. Business may be busier in June as the weather is slightly warmer and more consistent, but December would still provide appropriate demand. 

#### Temperatures and Percipitation
In addition to comparing temperatures, the investors should compare average precipitation for June and December. When comparing the average temperatures and rainfall for Oahu throughout the year, we see that the temperature is consistent and the precipitation is low throughout the year (see summary statistics below).

| June Temperature and Precipitation Statistics| December Temperature and Precipitation Statistics|
|----------------------------------------------|--------------------------------------------------|
|![Screen Shot 2022-08-06 at 2 14 38 PM](https://user-images.githubusercontent.com/106405775/183263148-e79bd159-406c-4a13-9c82-9fb74a58631a.png)|![Screen Shot 2022-08-06 at 2 14 14 PM](https://user-images.githubusercontent.com/106405775/183263156-3ba39b96-c9e9-43ef-a8d9-65095e192a0d.png)|

#### Temperatures by Station
The investors may also want to compare the average temperature at the different stations on Oahu, Hawaii to see if there is any significant flucation to determine which part of the island to build the Surf and Ice Cream Shop. There are higher average temperatures around the following stations: USC00514830, USC00517948, USC00519397, and USC00519523.

| June Temperatures by Station | December Temperatures by Station|
|----------------------------------------------|--------------------------------------------------|
|![Screen Shot 2022-08-06 at 2 46 35 PM](https://user-images.githubusercontent.com/106405775/183264095-9efb021c-712d-475e-9d8b-620d2f1ef0fb.png)| ![Screen Shot 2022-08-06 at 2 47 29 PM](https://user-images.githubusercontent.com/106405775/183264104-d05bcb62-96d6-46bd-a6fd-612488a539ba.png)|
