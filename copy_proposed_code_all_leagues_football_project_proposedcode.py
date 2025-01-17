# -*- coding: utf-8 -*-
"""Copy Proposed Code All_Leagues_Football_Project_ProposedCode.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JEq9SA6Z6veu_E3YkXGI_sPTt9okbTek
"""

from google.colab import drive 
drive.mount('/content/drive')

# Importing pandas library for data  manipulation and analysis
import pandas as pndas

# Importing numpy for numerical operations and array handling
import numpy as nmpy

# Importing matplotlib for data visualization using plots
import matplotlib.pyplot as MtPlot

# Importing seaborn for statistical data visualization
import seaborn as sBorn

# Importing Plotly Express for interactive data visualization
import plotly.express as POX

# Importing LabelEncoder to convert categorical labels to numerical format
from sklearn.preprocessing import LabelEncoder

# Importing ADASYN for handling class imbalance by generating synthetic samples
from imblearn.over_sampling import ADASYN

# Importing label_binarize to convert labels into binary format
from sklearn.preprocessing import label_binarize

# Importing train_test_split to split dataset into training and test sets
from sklearn.model_selection import train_test_split

# Importing ensemble classifiers: RandomForest, GradientBoosting, and Stacking for classification tasks
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier

# Importing Logistic Regression for classification
from sklearn.linear_model import LogisticRegression

# Importing various metrics for evaluating model performance (accuracy, precision, recall, F1 score, and report)
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Importing roc_curve and auc to evaluate model's ROC curve and Area Under Curve (AUC)
from sklearn.metrics import roc_curve, auc

# Importing cycle from itertools for cycling through multiple values, useful for plotting
from itertools import cycle

# Importing Plotly's Graph Objects for detailed and interactive visualizations
import plotly.graph_objects as go

# Importing confusion_matrix to compute the confusion matrix for classification evaluation
from sklearn.metrics import confusion_matrix

# Importing MaxAbsScaler to scale features by their absolute maximum values
from sklearn.preprocessing import MaxAbsScaler

# Importing mutual_info_classif to compute mutual information for feature selection
from sklearn.feature_selection import mutual_info_classif

import warnings  # Importing warnings module to handle warning messages
warnings.filterwarnings('ignore')  # Ignoring all warnings during execution to avoid unnecessary clutter

# loaded the dataset European_Football_Leagues
European_Football_Leagues = pndas.read_csv('/content/drive/MyDrive/Project/Proposed code/datasetEuropeanFootballLeagues.csv', sep=';')

# checking the top five row of European_Football_Leagues
European_Football_Leagues.head()

# checking the shape of European_Football_Leagues
European_Football_Leagues.shape

# checking European_Football_Leagues dataset info
European_Football_Leagues.info()

# checking the null values in the dataset European_Football_Leagues
European_Football_Leagues.isnull().sum()

# Loop through each column in the European_Football_Leagues DataFrame
for column in European_Football_Leagues.columns:
    # Check if the column contains any missing values
    if European_Football_Leagues[column].isnull().any():

        # If the column is of numeric data type
        if pndas.api.types.is_numeric_dtype(European_Football_Leagues[column]):
            # Fill missing values with the mean of the column
            European_Football_Leagues[column].fillna(European_Football_Leagues[column].mean(), inplace=True)
        else:
            # If the column is not numeric, fill missing values with the most frequent value (mode)
            European_Football_Leagues[column].fillna(European_Football_Leagues[column].mode()[0], inplace=True)

# Print the count of missing values in each column after filling
print(European_Football_Leagues.isnull().sum())

# duplicated value in dataset European_Football_Leagues
European_Football_Leagues.duplicated().sum()

# describing the European_Football_Leagues
European_Football_Leagues.describe().T

# Making a new 'league_df' DataFrame for league table information
league_df = pndas.DataFrame({
    'Round': European_Football_Leagues['Round'],  # The 'Round' column in the original DataFrame is being copied.
    'Position': European_Football_Leagues[['PositionHT', 'PositionVT']].stack().reset_index(drop=True),
    # Combining the positions of the home and away teams by stacking the "PositionHT" and "PositionVT" columns
    'Team': European_Football_Leagues[['TeamHT', 'TeamVT']].stack().reset_index(drop=True),
    # Stacking 'TeamHT' and 'TeamVT' to list both home and away teams
    'Matches': European_Football_Leagues[['MatchesHT', 'MatchesVT']].stack().reset_index(drop=True),
    # Stacking 'MatchesHT' and 'MatchesVT' for both home and away teams
    'Wins': European_Football_Leagues[['WinsHT', 'WinsVT']].stack().reset_index(drop=True),
    # Stacking 'WinsHT' and 'WinsVT' for both home and away teams
    'Draws': European_Football_Leagues[['DrawsHT', 'DrawsVT']].stack().reset_index(drop=True),
    # Stacking 'DrawsHT' and 'DrawsVT' for both home and away teams
    'Losses': European_Football_Leagues[['LossesHT', 'LossesVT']].stack().reset_index(drop=True),
    # Stacking 'LossesHT' and 'LossesVT' for both home and away teams
    'GoalsScored': European_Football_Leagues[['GoalsScoredHT', 'GoalsScoredVT']].stack().reset_index(drop=True),
    # Stacking 'GoalsScoredHT' and 'GoalsScoredVT' to capture goals scored by home and away teams
    'GoalsConceded': European_Football_Leagues[['GoalsConcededHT', 'GoalsConcededVT']].stack().reset_index(drop=True),
    # Stacking 'GoalsConcededHT' and 'GoalsConcededVT' for both home and away teams
    'GoalDifference': European_Football_Leagues[['GoalDifferenceHT', 'GoalDifferenceVT']].stack().reset_index(drop=True),
    # Stacking 'GoalDifferenceHT' and 'GoalDifferenceVT' for goal difference of both teams
    'Points': European_Football_Leagues[['PointsHT']].stack().reset_index(drop=True),
    # Stacking 'PointsHT' for the points accumulated by the home team
    'Country': European_Football_Leagues['Country'].repeat(2).reset_index(drop=True),
    # Repeating the 'Country' column twice for both home and away teams
    'League': European_Football_Leagues['League'].repeat(2).reset_index(drop=True)
    # Repeating the 'League' column twice for home and away teams
})

# Creating a CSVfile in the designated_directory and saving the 'league_df' DataFrame
league_df.to_csv('/content/drive/MyDrive/Project/Proposed code/League_Table.csv', index=False)

# Making a new DataFrame for matchstatistics called "match_df"
match_df = pndas.DataFrame({
    'Round': European_Football_Leagues['Round'],  # Duplicating the 'Round' field
    'TeamHT': European_Football_Leagues['TeamHT'],  # Copying 'TeamHT' (home team)
    'TeamVT': European_Football_Leagues['TeamVT'],  # Copying 'TeamVT' (away team)
    'ScoreHalf': European_Football_Leagues['ScoreHalf'],  # Copying 'ScoreHalf' (half-time score)
    'ScoreFull': European_Football_Leagues['ScoreFull'],  # Copying 'ScoreFull' (full-time score)
    'OddsHT': European_Football_Leagues['WinsHT'] / European_Football_Leagues['MatchesHT'],
    # Calculating 'OddsHT' as the ratio of home team wins to matches played
    'OddsX': European_Football_Leagues['DrawsHT'] / European_Football_Leagues['MatchesHT'],
    # Calculating 'OddsX' as the ratio of home team draws to matches played
    'OddsVT': European_Football_Leagues['WinsVT'] / European_Football_Leagues['MatchesVT'],
    # Calculating 'OddsVT' as the ratio of away team wins to matches played
    'Country': European_Football_Leagues['Country'],  # Copying 'Country' column
    'League': European_Football_Leagues['League']  # Copying 'League' column
})

# Saving a CSVfile in the designated location containing the'match_df' DataFrame
match_df.to_csv('/content/drive/MyDrive/Project/Proposed code/Match_Table.csv', index=False)

# Reading the 'League_Table.csv' file into a DataFrame using pandas
# The 'sep' argument specifies that the values are separated by commas
League_Table = pndas.read_csv('/content/drive/MyDrive/Project/Proposed code/League_Table.csv', sep=',')

# Reading the 'Match_Table.csv' file into a DataFrame using pandas
# The 'sep' argument specifies that the values are separated by commas
Match_Table = pndas.read_csv('/content/drive/MyDrive/Project/Proposed code/Match_Table.csv', sep=',')

# shown the top 2 rows in above League_Table
League_Table.head(2)

# shown the top 2 rows in above Match_Table
Match_Table.head(2)

"""### ***EDA***"""

# Selecting only numerical features from the European_Football_Leagues DataFrame
numerical_features = European_Football_Leagues.select_dtypes(include=nmpy.number)

# Calculating the correlation matrix for the selected numerical features
correlation_matrix = numerical_features.corr()

# Setting the figure size for the heatmap
MtPlot.figure(figsize=(20, 16))

# Creating a heatmap using seaborn to visualize correlations, with annotations and a color map
sBorn.heatmap(correlation_matrix, annot=True, cmap='cool', fmt=".2f")

# Adding a title to the heatmap plot
MtPlot.title('Correlation Matrix of Numerical Features in European_Football_Leagues')

# Displaying the plot
MtPlot.show()

# Importing Plotly Express for data visualization
import plotly.express as POX

# Creating a sunburst chart to visualize the hierarchy of Countries and Teams based on Wins
fig = POX.sunburst(
    League_Table,  # Data source is the 'League_Table' DataFrame
    path=['Country', 'Team'],  # Hierarchical path: first by 'Country', then by 'Team'
    values='Wins',  # Size of each sector is based on the 'Wins' column
    color='Wins',  # Coloring the sectors based on the number of 'Wins'
    color_continuous_scale='RdYlBu'  # Using the 'Red-Yellow-Blue' color scale
)

# Updating the layout of the sunburst chart
fig.update_layout(
    title_text='Sunburst Chart of Countries Teams: Wins Ratio',  # Title of the chart
    width=1000,  # Setting the width of the chart
    height=900  # Setting the height of the chart
)

# Displaying the sunburst chart
fig.show()

# Creating a sunburst chart to visualize the hierarchy of Countries and Teams based on Draws
fig = POX.sunburst(
    League_Table,  # Data source is the 'League_Table' DataFrame
    path=['Country', 'Team'],  # Hierarchical path: first by 'Country', then by 'Team'
    values='Draws',  # Size of each sector is based on the 'Draws' column
    color='Draws',  # Coloring the sectors based on the number of 'Draws'
    color_continuous_scale=POX.colors.sequential.Viridis  # Using the 'Viridis' color scale
)

# Updating the layout of the sunburst chart
fig.update_layout(
    title_text='Sunburst Chart of Teams by Country and Draws',  # Title of the chart
    width=1000,  # Setting the width of the chart
    height=900  # Setting the height of the chart
)

# Displaying the sunburst chart
fig.show()

# Creating a sunburst chart to visualize the hierarchy of Countries and Teams based on Losses
fig = POX.sunburst(
    League_Table,  # Data source is the 'League_Table' DataFrame
    path=['Country', 'Team'],  # Hierarchical path: first by 'Country', then by 'Team'
    values='Losses',  # Size of each sector is based on the 'Losses' column
    title='Sunburst Chart of Team Losses by Country',  # Title of the chart
    color='Losses',  # Coloring the sectors based on the number of 'Losses'
    color_continuous_scale='Blues'  # Using the 'Blues' color scale
)

# Updating the layout of the sunburst chart
fig.update_layout(
    width=1000,  # Setting the width of the chart
    height=900  # Setting the height of the chart
)

# Displaying the sunburst chart
fig.show()

# Grouping the European_Football_Leagues DataFrame by 'Country' and summing the 'MatchesHT' for home teams
country_value_counts = European_Football_Leagues.groupby('Country')['MatchesHT'].sum()

# Creating a bar chart to visualize the sum of home matches by country
fig = POX.bar(country_value_counts,  # Data for the bar chart
               x=country_value_counts.index,  # X-axis represents the countries
               y=country_value_counts.values,  # Y-axis represents the sum of home matches
               labels={'x': 'Country', 'y': 'Sum of MatchesHT(Home Team)'},  # Labels for the axes
               title='Sum of TARGET by Country')  # Title of the chart

# Updating the bar chart to display values outside the bars
fig.update_traces(texttemplate='%{y}', textposition='outside')

# Displaying the bar chart
fig.show()

# Grouping the European_Football_Leagues DataFrame by 'Country' and 'TARGET' to count occurrences of each outcome
outcome_counts_by_country = European_Football_Leagues.groupby(['Country', 'TARGET'])['TARGET'].count().unstack()

# Creating a grouped bar chart to visualize the distribution of match outcomes by country
fig = POX.bar(outcome_counts_by_country,  # Data for the bar chart
               barmode='group',  # Setting the bar mode to group bars together
               labels={'value': 'Count', 'variable': 'Match Outcome'},  # Labels for the axes
               title='Distribution of Match Outcomes by Country')  # Title of the chart

# Updating the layout to angle the x-axis ticks for better readability
fig.update_layout(xaxis_tickangle=-45)

# Updating the bar chart to display values outside the bars
fig.update_traces(texttemplate='%{value}', textposition='outside')

# Displaying the bar chart
fig.show()

# Creating a new DataFrame with specific attributes for plotting
plot_df = European_Football_Leagues[['MatchesHT', 'WinsHT', 'DrawsHT', 'LossesHT', 'GoalsScoredHT', 'GoalsConcededHT']]

# Creating a scatter plot matrix using Plotly to visualize the distribution of match attributes
fig = POX.scatter_matrix(
    plot_df,  # Data source is the 'plot_df' DataFrame
    dimensions=plot_df.columns,  # Setting the dimensions for the scatter plot matrix
    color='MatchesHT',  # Coloring the points based on the 'MatchesHT' attribute
    height=800,  # Setting the height of the plot
    width=1150,  # Setting the width of the plot
    title='Distribution of Match Attributes'  # Title of the scatter plot matrix
)

# Displaying the scatter plot matrix
fig.show()

# Grouping the European_Football_Leagues DataFrame by 'Country' and 'League' to count occurrences of each target
country_league_counts = European_Football_Leagues.groupby(['Country', 'League'])['TARGET'].count().reset_index()

# Creating a sunburst chart to visualize the distribution of matches by Country and League
fig = POX.sunburst(
    country_league_counts,  # Data source is the 'country_league_counts' DataFrame
    path=['Country', 'League'],  # Hierarchical path: first by 'Country', then by 'League'
    values='TARGET',  # Size of each sector is based on the count of 'TARGET'
    title='Distribution of Matches by Country and League'  # Title of the sunburst chart
)

# Displaying the sunburst chart
fig.show()

# print the datatype of the European_Football_Leagues
print(European_Football_Leagues.dtypes)

"""### ***Label Encoder***"""

# Importing LabelEncoder from sklearn to encode categorical variables
le = LabelEncoder()

# Looping through each column in the European_Football_Leagues DataFrame
for column in European_Football_Leagues.columns:
    # Checking if the column data type is 'object' (categorical)
    if European_Football_Leagues[column].dtype == 'object':
        # Applying label encoding to the column to convert categorical values to numeric
        European_Football_Leagues[column] = le.fit_transform(European_Football_Leagues[column])

# Displaying the first few rows of the updated DataFrame
print(European_Football_Leagues.head())

# Dropping the 'TARGET' column from the European_Football_Leagues DataFrame to create feature set X
X = European_Football_Leagues.drop(['TARGET'], axis=1)

# Extracting the 'TARGET' column as the target variable y
y = European_Football_Leagues['TARGET']

# checking the values counts of the variable y
y.value_counts()

"""### ***Data Normalization: MaxAbsScaler***"""

# Importing MaxAbsScaler from sklearn for feature scaling
scaler = MaxAbsScaler()

# Fitting the scaler to the feature set X and transforming it to normalize the values
X_normalized = scaler.fit_transform(X)  # X_normalized now contains the scaled feature values

"""### ***Feature Selection: Mututal_Info_Classifier***"""

# Calculating mutual information between the features and the target variable
mutual_info = mutual_info_classif(X_normalized, y)

# Getting the names of the features
feature_names = X.columns

# Creating a DataFrame to store feature names and their corresponding mutual information scores
feature_importance = pndas.DataFrame({'Feature': feature_names, 'Mutual Information': mutual_info})

# Sorting the DataFrame based on mutual information scores in descending order
feature_importance = feature_importance.sort_values('Mutual Information', ascending=False)

# Creating a bar chart to visualize feature importance before feature selection
fig_before = POX.bar(feature_importance,
                    x='Feature',  # X-axis: feature names
                    y='Mutual Information',  # Y-axis: mutual information scores
                    title='Feature Importance Before Feature Selection',  # Title of the chart
                    labels={'Feature': 'Features', 'Mutual Information': 'Mutual Information'},  # Axis labels
                    width=1000, height=600)  # Setting the width and height of the chart
fig_before.update_layout(xaxis_tickangle=-90)  # Angling x-axis ticks for better readability
fig_before.show()  # Displaying the chart

# Selecting the top 15 features based on mutual information scores
top_15_features = feature_importance['Feature'][:15].tolist()

# Creating a new DataFrame with only the top 15 features
X_selected = X[top_15_features]

# Normalizing the selected features
X_selected_normalized = scaler.fit_transform(X_selected)

# Creating a bar chart to visualize feature importance after feature selection (top 15 features)
fig_after = POX.bar(feature_importance.head(15),
                   x='Feature',  # X-axis: feature names
                   y='Mutual Information',  # Y-axis: mutual information scores
                   title='Feature Importance After Feature Selection (Top 15)',  # Title of the chart
                   labels={'Feature': 'Features', 'Mutual Information': 'Mutual Information'},  # Axis labels
                   width=1000, height=600)  # Setting the width and height of the chart
fig_after.update_layout(xaxis_tickangle=-90)  # Angling x-axis ticks for better readability
fig_after.show()  # Displaying the chart

"""### ***Data Balancing: ADASYN***"""

# Importing ADASYN from imblearn to handle class imbalance
adasyn = ADASYN(random_state=42)

# Applying ADASYN to generate a resampled dataset with balanced classes
X_resampled, y_resampled = adasyn.fit_resample(X_selected, y)

# Printing the original dataset shape (class distribution)
print("Original dataset shape:", y.value_counts())

# Printing the resampled dataset shape (class distribution after applying ADASYN)
print("Resampled dataset shape:", y_resampled.value_counts())

"""### ***DataSpliting Into TrainTestSplit***"""

XTrainData, XTestData, yTrainData, yTestData = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

"""### ***Model: Stacking_Model***"""

# Importing necessaryclassifiers for the StackingModel
model1 = LogisticRegression()  # LogisticRegressionModel
model2 = RandomForestClassifier()  # RandomForestModel
model3 = GradientBoostingClassifier()  # GradientBoostingModel

# Defining the metamodel for stacking
meta_model = LogisticRegression()  # Metamodel for the finalPredictions

# Creating a StackingClassifier using the definedmodels
stacking_model = StackingClassifier(
    estimators=[('lr', model1), ('rf', model2), ('gb', model3)],  # Basemodels
    final_estimator=meta_model  # Metamodel
)

# Fitting the stackingmodel on the training data
stacking_model.fit(XTrainData, yTrainData)

# Predicting on the trainingset using the stackingmodel
y_Stack_TrainSetPred = stacking_model.predict(XTrainData)

# Predicting on the testset using the stackingmodel
y_Stack_TestSetPred = stacking_model.predict(XTestData)

"""### ***TrainSet_Model***"""

# Calculating the accuracy of the stacking model on the training set
train_accuracy = accuracy_score(yTrainData, y_Stack_TrainSetPred)

# Calculating the precision of the stacking model on the training set using macro averaging
train_precision = precision_score(yTrainData, y_Stack_TrainSetPred, average='macro')

# Calculating the recall of the stacking model on the training set using macro averaging
train_recall = recall_score(yTrainData, y_Stack_TrainSetPred, average='macro')

# Calculating the F1 score of the stacking model on the training set using macro averaging
train_f1 = f1_score(yTrainData, y_Stack_TrainSetPred, average='macro')

# Printing the evaluation metrics for the training set
print("Training Set Metrics:")
print("Accuracy :", train_accuracy)  # Displayingaccuracy

print("Precision:", train_precision)  # Displayingprecision

print("Recall   :", train_recall)  # Displayingrecall

print("F1 Score :", train_f1)  # DisplayingF1score

"""### ***Accuracy_of_TrainSetModel = Class 0, Class 1, Class 2***"""

# Defining a function to calculate the accuracy for a specific class
def class_accuracy(y_true, y_pred, class_label):
    # Getting the indices of the true labels that match the specified class label
    class_indices = (y_true == class_label)
    # Returning the accuracy score for the predictions corresponding to that class
    return accuracy_score(y_true[class_indices], y_pred[class_indices])

# Printing training set metrics
print("Training Set Metrics:")
# Looping through each class label to calculate and print class-specific accuracy
for class_label in [0, 1, 2]:
    # Calculating accuracy for the current class label
    train_class_acc = class_accuracy(yTrainData, y_Stack_TrainSetPred, class_label)
    # Printing the accuracy for the current class
    print(f"Accuracy for Class {class_label}: {train_class_acc:.4f}")

"""### ***ClassificationReport_TrainSetModel***"""

# Generating a classification report for the training set predictions
train_classification_report = classification_report(yTrainData, y_Stack_TrainSetPred)

# Printing the classification report for the training set
print("Training Set Classification Report:\n", train_classification_report)

"""### ***ConfusionMatrix_TrainSetModel***"""

# Generating the confusion matrix for the training set predictions
com_train = confusion_matrix(yTrainData, y_Stack_TrainSetPred)

# Setting up the figure for the heatmap
MtPlot.figure(figsize=(8, 6))
# Creating a heatmap for the confusion matrix
sBorn.heatmap(com_train,
               annot=True,  # Annotate with the counts
               fmt="d",  # Format the annotations as integers
               cmap="cool",  # Colormap for the heatmap
               cbar=False,  # Disable the color bar
               linewidths=4.0,  # Width of lines separating the cells
               linecolor='black')  # Color of the lines separating the cells

# Adding titles and labels to the plot
MtPlot.title("Confusion Matrix (Training Set)")  # Title of the plot
MtPlot.xlabel("Predicted Labels")  # X-axis label
MtPlot.ylabel("True Labels")  # Y-axis label

# Displaying the confusion matrix heatmap
MtPlot.show()

"""### ***ROC_AUC-Curve of TrainSetModel***"""

# Binarizing the true labels for multi-class ROC analysis
yTrainData_bin = label_binarize(yTrainData, classes=[0, 1, 2])
# Binarizing the predicted labels for multi-class ROC analysis
y_Stack_TrainSetPred_bin = label_binarize(y_Stack_TrainSetPred, classes=[0, 1, 2])

# Initializing dictionaries to store false positive rates, true positive rates, and ROC AUC values
fpr = dict()
tpr = dict()
roc_auc = dict()
n_classes = yTrainData_bin.shape[1]  # Number of classes

# Calculating the ROC curve and AUC for each class
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(yTrainData_bin[:, i], y_Stack_TrainSetPred_bin[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Setting up the figure for the ROC curves
MtPlot.figure()
lw = 2  # Line width for the curves
colors = cycle(['aqua', 'violet', 'brown'])  # Colors for the ROC curves

# Plotting the ROC curve for each class
for i, color in zip(range(n_classes), colors):
    MtPlot.plot(fpr[i], tpr[i], color=color, lw=lw,
                label='ROC curve of class {0} (area = {1:0.2f})'
                      ''.format(i, roc_auc[i]))

# Adding a dashed line representing the chance level
MtPlot.plot([0, 1], [0, 1], 'k--', lw=lw)
# Adding labels and title to the plot
MtPlot.xlabel('False Positive Rate')  # X-axis label
MtPlot.ylabel('True Positive Rate')  # Y-axis label
MtPlot.title('Receiver Operating Characteristic (ROC) for Multi-Class')  # Title of the plot
# Adding the legend for the plot
MtPlot.legend(loc="lower right")
# Displaying the ROC curves
MtPlot.show()

"""### ***TestSet_Model***"""

# Calculating accuracy for the test set predictions
test_accuracy = accuracy_score(yTestData, y_Stack_TestSetPred)

# Calculating precision for the test set predictions
test_precision = precision_score(yTestData, y_Stack_TestSetPred, average='macro')

# Calculating recall for the test set predictions
test_recall = recall_score(yTestData, y_Stack_TestSetPred, average='macro')

# Calculating F1 score for the test set predictions
test_f1 = f1_score(yTestData, y_Stack_TestSetPred, average='macro')

# Printing the evaluation metrics for the testset
print("Test Set Metrics:")
print("Accuracy :", test_accuracy)  # Displayingaccuracy

print("Precision:", test_precision)  # Displayingprecision

print("Recall   :", test_recall)  # Displayingrecall

print("F1 Score :", test_f1)  # DisplayingF1score

"""### ***Accuracy_of_TestSetModel = Class 0, Class 1, Class 2***"""

# Evaluating the accuracy for each class in the test set
for class_label in [0, 1, 2]:
    # Calculating the accuracy for the specified class label
    test_class_acc = class_accuracy(yTestData, y_Stack_TestSetPred, class_label)
    # Printing the accuracy for the current class
    print(f"Test Set Accuracy for Class {class_label}: {test_class_acc:.4f}")

"""### ***ClassificationReport_TestSetMod***"""

# Generating a classificationreport for the test set predictions
report = classification_report(yTestData, y_Stack_TestSetPred)
# Printing the classificationreport
print("Classification Report:\n", report)

"""### ***ConfusionMatrix_TestSetModel***"""

# Creating a confusionmatrix for the testset predictions
confm = confusion_matrix(yTestData, y_Stack_TestSetPred)

# Setting the figure size for the confusionmatrix plot
MtPlot.figure(figsize=(8, 6))
# Plotting the heatmap of the confusionmatrix with annotations
sBorn.heatmap(confm, annot=True, fmt="d", cmap="cool", cbar=False, linewidths=4.0, linecolor='black')

# Adding titles and labels to the plot
MtPlot.title('Confusion Matrix')
MtPlot.xlabel('Predicted Label')
MtPlot.ylabel('True Label')
MtPlot.show()

"""### ***ROC_AUC-Curve of TestSetModel***"""

# Binarizing the test data and predictions for multi-class ROC analysis
yTestData_bin = label_binarize(yTestData, classes=[0, 1, 2])
y_Stack_TestSetPred_bin = label_binarize(y_Stack_TestSetPred, classes=[0, 1, 2])

# Initializing dictionaries to store false positive rates, true positive rates, and AUC values
fpr = dict()
tpr = dict()
roc_auc = dict()
n_classes = yTestData_bin.shape[1]  # Number of classes

# Calculating the ROC curve and AUC for each class
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(yTestData_bin[:, i], y_Stack_TestSetPred_bin[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Creating a new figure for the ROC plot
MtPlot.figure()
lw = 2  # Line width for the plot
# Defining colors for the different classes
colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])

# Plotting the ROC curve for each class
for i, color in zip(range(n_classes), colors):
    MtPlot.plot(fpr[i], tpr[i], color=color, lw=lw,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

# Adding the diagonal line (no discrimination line)
MtPlot.plot([0, 1], [0, 1], 'k--', lw=lw)

# Adding labels and title to the plot
MtPlot.xlabel('False Positive Rate')
MtPlot.ylabel('True Positive Rate')
MtPlot.title('ReceiverOperatingCharacteristic(ROC) for MultiClass')
MtPlot.legend(loc="lower right")
MtPlot.show()

"""### ***Model Result Comparision Trainset and Testset***"""

# Define metrics and their respective values for training and testsets
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
train_values = [train_accuracy, train_precision, train_recall, train_f1]
test_values = [test_accuracy, test_precision, test_recall, test_f1]

# Create a grouped bar chart
fig = go.Figure(data=[
    go.Bar(name='Training Set', x=metrics, y=train_values,
           text=[f'{v:.4f}' for v in train_values],
           textposition='outside'),
    go.Bar(name='Test Set', x=metrics, y=test_values,
           text=[f'{v:.4f}' for v in test_values],
           textposition='outside')
])

# Update the layout for the figure
fig.update_layout(
    barmode='group',
    title='Comparison of Model Performance (Training vs. Test)',
    xaxis_title='Metrics',
    yaxis_title='Score',
    width=1000,
    height=600
)

# Display the figure
fig.show()
