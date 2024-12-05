# Comprehensive Analysis of Amazon Product Metrics  

This project, developed for the **Big Data System Development Class** at **Beijing Institute of Technology**, involves a comprehensive analysis of Amazon product metrics using advanced big data technologies. The goal was to extract actionable insights and build a recommendation system based on product ratings, sales trends, geographical distribution, and customer demographics.

## Project Overview  

### Objectives  
- Analyze **product ratings** to identify trends and patterns.  
- Investigate **sales trends** over time.  
- Explore the **geographical distribution** of sales.  
- Study **customer demographics** to understand consumer behavior.  
- Build a **recommendation system** using insights derived from the analysis.

### Tools & Technologies  
- **Apache Spark**: Distributed data processing framework for analyzing large datasets.  
- **Apache Hive**: Data warehousing tool for querying and managing big data.  
- **YARN**: Resource management for distributed applications in Hadoop ecosystems.  
- **Matplotlib** & **Seaborn**: Python libraries for creating detailed visualizations.

## Key Features  
- **Data Analysis**: Comprehensive analysis of Amazon product data, including structured queries and aggregations.  
- **Recommendation System**: Leveraged analytical insights to build a system recommending products to users.  
- **Visualization**: Generated insightful visualizations to represent trends and relationships within the data.

## Installation & Setup  
1. **Prerequisites**:  
   - Hadoop with YARN enabled  
   - Apache Spark  
   - Apache Hive  
   - Python environment with `matplotlib` and `seaborn` installed  

2. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/amazon-metrics-analysis.git
   cd amazon-metrics-analysis
   ```

3. Configure Spark and Hive environments based on your cluster setup.

4. Run the analysis scripts:  
   ```bash
   spark-submit analysis_script.py
   ```

## Results & Insights  
The project provided deep insights into customer behavior and sales patterns, which were instrumental in designing the recommendation system. Key findings include:  
- Products with higher ratings correlate with increased sales in specific regions.  
- Certain customer demographics display a preference for specific product categories.  
