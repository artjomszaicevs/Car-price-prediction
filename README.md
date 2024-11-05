# Car Price Category Prediction Project

## Description

This project focuses on using Data Science methods to predict car price categories based on their parameters. The main goal of the project is to develop a model capable of estimating the price of cars based on provided data.

## Main Components of the Project

- **Prediction Model**: The model is trained on a dataset that allows it to determine the price category of a car. The model is saved in `.pkl` format for ease of use.
- **Service**: The project is implemented as a service running through Apache Airflow, enabling the management of ETL (Extract, Transform, Load) processes and automating task execution.
- **DAG File**: In Airflow, a DAG (Directed Acyclic Graph) file is used to define the service's logic and manage the dependencies between tasks.
- **Test Data**: To demonstrate the service's functionality, test JSON files containing information about various cars are used, which are passed to the model for predicting their price categories.
- **Results**: The prediction results are saved in a separate file for further analysis.

## Why is a Pipeline Needed?

A pipeline in the context of Data Science represents a sequence of steps that process data from start to finish. Each step may include data extraction, cleaning, transformation, and finally, model training. A pipeline allows for:

- **Process Automation**: All stages of data handling are organized and can be executed automatically, reducing the likelihood of errors and simplifying reproducibility.
- **Easier Maintenance**: When each step is clearly defined, it is easier to identify and fix problems if something goes wrong.
- **Scalability**: It is easier to add new steps to the pipeline if you want to improve the model or change the way data is processed.

## `.pkl` Format

The `.pkl` (Pickle) format is used in Python for object serialization. Using Pickle, you can save the state of an object (in this case, the model) to a file and then restore it later. Advantages of using the `.pkl` format include:

- **Convenient Storage**: The model is stored in a compact format, making it easier to save and transfer.
- **Quick Recovery**: You can easily load the model from the file and use it for predictions without needing to retrain it.

## DAG (Directed Acyclic Graph)

A DAG (Directed Acyclic Graph) is a structure used in Apache Airflow to describe the sequence of tasks that need to be executed. Each node in the graph represents a task, and the edges define the dependencies between these tasks. Key benefits of using a DAG include:

- **Clear Structure**: A DAG allows you to visualize the order of task execution, helping you better understand the logic of the workflow.
- **Dependency Management**: Airflow automatically manages dependencies, ensuring that tasks are executed in the correct order.
- **Reusability**: The same DAG can be run multiple times with different parameters, making it a versatile tool for automation.
