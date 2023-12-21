# Mid Project Week | Exploratory Data Analysis on Global Plastic Pollution

## Problem definition:

“Plastic pollution is a global problem. Every year 19-23 million tonnes of plastic waste leaks into aquatic ecosystems, polluting lakes, rivers and seas. Plastic pollution can alter habitats and natural processes, reducing ecosystems’ ability to adapt to climate change, directly affecting millions of people’s livelihoods, food production capabilities and social well-being.” [UN](https://www.unep.org/plastic-pollution)


## Project Purpose

The overarching purpose of this project is to:

- Understand the global landscape of plastic usage, disposal, and waste management.
- Identify regional disparities and variations in plastic consumption and waste production.
- Explore potential correlations between plastic waste and environmental, socio-economic, or industrial factors.
- Lay the groundwork for further analysis, potentially leading to solutions for mitigating plastic pollution.


## Project Questions

1. Are there significant regional variations for plastic waste?
How does the distribution of plastic pollution vary geographically based on the OECD data?
2. Can you identify regions where plastic usage is relatively high but produces less plastic waste, suggesting more efficient use or better recycling practices.
3. Are there correlations between plastic pollution and other environmental factors (e.g., GDP, population, ..)?
4. Is there a correlation between the amount of plastic used in a region and the corresponding plastic waste generated in that region?


## Data Sources

Most datasets used for this analysis are sourced from [OECD's Global Plastic Outlook](https://www.oecd-ilibrary.org/environment/data/global-plastic-outlook_c0821f81-en). 
Additionally, 2010 data from [World Bank](https://ourworldindata.org/grapher/per-capita-plastic-waste-vs-gdp-per-capita) was added as this provides GDP per capita data for more context.

The raw datasets are stored in the `data/raw_data` folder of this repository.

The cleaned and joined data sets can be found within the `data/cleaned_data`folder.

The cleaned files are the basis for the conducted exploratory data analysis.
The corresponding jupyter notebooks are stored


## Data challenges we have identified:

- Low availability of country-specific data → only for 2010
The lack of country-specific data makes it difficult to test correlations with factors such as GDP and population, and ultimately to build machine learning module to predict future waste trends.
- Grouping of countries into OECD regions leads to less data points→ only 15 regions available, class imbalance has been reduced at the cost of losing a lot of detail and creating meaningful insights.
- Country-specific differences may not be properly reflected, data from 2010 suggest that Germany, for example, has one of the highest per capita waste and arguably therefore high total waste volumes → grouping into OECD EU leads to responsibility for waste generation being shared equally among all OECD EU countries, while some may have much lower waste generation than Germany


## Findings

An overview with all our findings and data visualisations can be found in a [Tableau slide presentation](https://public.tableau.com/app/profile/simone.fischer/viz/MidProjectPlasticWaste_17030854304850/Presentation).

Initial analysis and exploration have revealed several noteworthy aspects:

1. Plastic and Recycling Waste Trends:
- Global plastic waste surged from 156.17 to 353.29 million tonnes (2000 to 2019), marking a 126.22% rise.
- An average of 16.74 million tonnes of plastic was wasted annually, with 996,623 tonnes leaking into aquatic environments.
- India experienced a remarkable 430.35% increase in waste generation from 2000 to 2019, reaching 18.52 million tonnes.

2. Global Distribution of Plastic Waste:
- Regions with consistently high waste levels include China, the United States, OECD EU, and Latin America.
- Top waste contributors such as China and the United States showcase a significant impact on plastic waste generation.
- Plastic waste levels reached extreme values, with some regions surpassing 72.84 million tonnes.

3. Plastic Usage vs. Waste and Recycling:
- In 2019, 459.7 million tonnes of plastic were used, with 77% (353.3 million tonnes) ending up as waste.
- Despite 54.6 million tonnes collected, only 32.8 million tonnes were recycled, highlighting poor waste management.

4. Efficiency in Plastic Use and Recycling Practices:
- The 77% waste rate signifies significant environmental impact, urging better recycling strategies or reduced plastic consumption.
- The packaging and consumer sectors exhibit high usage rates, hinting at potential inefficiencies or inadequate recycling.

5. Causes of Plastic Waste:
-The packaging industry contributes 40% (142.6 million tonnes) of total plastic waste due to widespread usage.
- Single-use plastics, poor recycling systems, and inadequate waste management contribute significantly to plastic pollution.

6. Disposal Methods for Plastic Waste:
- Landfilling is the predominant disposal method, reflecting higher mean and maximum values.
- Recycling practices account for a smaller share, indicating gaps in effective recycling.

7. Correlations Between Plastic Pollution and Environmental Factors:
- Statistical analysis supports a relationship between plastic waste per capita and GDP per capita.
- The significant relationship found suggests a dependency between these variables.

8. Recycling Ratio in OECD vs. Non-OECD Regions:
- The hypothesis test indicates no significant difference in recycling rates between OECD and non-OECD countries.


## Instructions

To replicate the analysis or contribute to the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies listed in `requirements.txt`.
3. Access the Jupyter notebooks in the `notebooks` directory to explore the analysis.


## Next Steps

Based on the preliminary findings, the project's next steps include:

- Deeper analysis into regional disparities to understand the underlying factors contributing to efficient plastic use or better waste management practices.
- Exploration of environmental correlations to determine the impact of various factors on plastic pollution.
- Further modeling and hypothesis testing to validate initial observations and derive actionable insights.
- Engaging in collaborative efforts to propose potential solutions or strategies for reducing plastic pollution.
- Correlations between plastic waste and environmental factors such as GDP, population density, and industrial activities are emerging and warrant further investigation.
