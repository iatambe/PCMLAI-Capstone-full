### Comparing the performance of some different ML classifier architectures for detection of diagnostic conditions from ECG signal data

**Indraneel Tambe**

#### Problem statement
We aim to answer the question of what kinds of design choices for simple classifier models lead to the best results in automating the task of annotating ECG signals with diagnostic conditions. Specifically, after training a deep model consisting of a feature extractor followed by a dense classifier head, we will try piping the feature extractor into various non-deep ML models and see how they compare to the original "fully deep" model.  

#### Model outcomes
This problem is a classification task, and we will use supervised learning algorithms because we will use ECG data that is already human-labeled with diagnostic conditions. We expect that a simple 1-D CNN-based model should manage to achieve a reasonable baseline performance on the data (this is Part II of the workbook), then we will experiment further by trying different classification heads on top of the pre-trained model (this is Part III).

#### Data acquisition
We use the publicly available PTB-XL database from Physionet ([link](https://physionet.org/content/ptb-xl/1.0.3/)).
The dataset consists of over 21k strips of 12-lead ECG signals, each 10 seconds long (and sampled at 500Hz). 
(For those unfamiliar with the clinical terminology, ECG leads are essentially like channels in the signal. Each individual sample is a 16-bit integer, discretized at 1 microvolt.)
The ECG strips have been annotated by human clinicians from a list of possible diagnostic conditions.

#### Data preprocessing
Before feeding the signal data into the ML model, we first apply some preprocessing to the data: we apply certain signal-processing filters to the signal to smooth it out (for this we use the neurokit2 library, which has these filters pre-built), and Z-score each signal.
The data doesn't seem to have missing values (although it does include a representation of an "unknown" confidence value for diagnoses; I've chosen to impute these as a low positive confidence). 
The PTB-XL dataset comes with suggested stratified splittings into 10 folds, and it suggests to use folds 9 and 10 respectively as the validation and test sets; we have used this suggestion.

#### Modeling
We start with a "base" model that consists of a 1D CNN-based feature extractor followed by a dense classifier head. Next, we try piping the trained feature extractor into various non-deep ML models for classifications and see if they can outperform the original deep classifier.

Here is an outline of our analysis (the Jupyter workbook is organized in the same way):

- Part I: data cleaning, preprocessing, and preparation
- Part II: setup and training of "base" deep model
- Part III: experimenting with different non-deep classifiers piped after the base model's feature extractor

Details regarding Parts I and II, including the choices made in preprocessing the data and in the design of the "base" model, can be seen in this project's Jupyter workbook.

In part III we experimented with five "classical" ML models piped after my trained feature extractor, and compare them with the original base model's performance. (Note: this performance will be tested on a separate test set from the original validation set that was used to select the best-performing base model during training, to prevent validation leakage.) See Part III in the Jupyter workbook for details on which ML classifier models were used.

We also experiment with num_layers ranging from 1 to 5; here num_layers is the number of layers in the original base model's dense classifier head. (Note num_layers needs to be set before training the base model.)


#### Results

After running the full workbook with different values of num_layers multiple times, we collected the results from Part III into [this csv file](Results/Results%20from%20different%20classifier%20heads%20for%20different%20num_layers.csv) (included in this project).

We averaged the Part III results for each choice of model and num_layers, resulting in the below graph:

![](Results/part%20III%20model%20comparison.png)

- It seems the **best** overall performance is attained by Model B (consisting of a logistic regression head chained after our pre-trained feature extractor from Part II) with num_layers=1. In fact, with num_layers=1, Model B even outperformed the original Model A.
- We see the performance for each of these models degrades as num_layers increases. This suggests that for our base model design, configurations with num_layers>1 tend to overfit on the training set.
- We only kept data for Models A,B,F as these were consistently the best-performing models.

#### Next steps

A further next step could be to try tuning other hyperparameters, such as other hyperparameters of the base model (like num_layers) from Part II or hyperparameters of the various non-deep ML models that are piped after the feature extractor in Part III. Due to constraints on computation time available, in this project I only experimented with different classifier heads and with num_layers.

#### Link to Jupyter workbook

[Workbook (full).ipynb](Workbook%20(full).ipynb)

<!-- 

------

#### Executive summary
I experiment with some different ML architectures and compare their performance in detecting diagnostic conditions ECG (electrocardiogram) signals to diagnose heart conditions based on the ECG signal morphology. Specifically, I test the performance of a family of ML architectures involving placing different classification heads on top of a basic 1D CNN-based model that I pre-train from scratch in this project.

#### Research Question
We aim to answer the question of what kinds of design choices for simple classifier models lead to the best results when working with the PTB-XL dataset (specifically their diagnostic superclasses). After training a deep model consisting of a feature extractor followed by a dense classifier head, we will try piping the feature extractor into various non-deep ML models and see how they compare to the original "fully deep" model.  

#### Rationale
Machine learning models for diagnosing conditions from ECG signals are useful as a tool to automate the process of condition detection and diagnosis. Although this diagnostic task can be performed by human clinicians, if it can be automated, then patients' ECG data can be continuously monitored for possible signs of heart conditions on a much larger scale, without the need for human clinicians watching every single patient for long periods of time. 
Moreover, understanding what kinds of simple design choices lead to best results may help inform what choices to make when working with larger models.

#### Data Sources
I use the publicly available PTB-XL database from Physionet ([link](https://physionet.org/content/ptb-xl/1.0.3/)).
The dataset consists of over 21k strips of 12-lead ECG signals, each 10 seconds long (and sampled at 500Hz). 
(For those unfamiliar with the clinical terminology, ECG leads are essentially like channels in the signal. Each individual sample is a 16-bit integer, discretized at 1 microvolt.)
The ECG strips are labeled by human clinicians with a list of possible diagnostic conditions.

#### Methodology and outline
For the analysis, I'm planning to start with a "base" model that consists of a 1D CNN-based feature extractor followed by a dense classifier head. Next, in the full capstone project, I will try piping the trained feature extractor into various non-deep ML models for classifications and see if they can outperform the original deep classifier.

Here is an outline of our analysis (the Jupyter workbook is organized in the same way):

- Part I: data cleaning, preprocessing, and preparation
- Part II: setup and training of "base" deep model
- Part III: experimenting with different non-deep classifiers piped after the base model's feature extractor

Details regarding Parts I and II, including the choices made in preprocessing the data and in the design of the "base" model, can be seen in this project's Jupyter workbook.

In part III I experimented with five "classical" ML models piped after my trained feature extractor, and compare them with the original base model's performance. (Note: this performance will be tested on a separate test set from the original validation set that was used to select the best-performing base model during training, to prevent validation leakage.)

I will also experiment with num_layers ranging from 1 to 5; here num_layers is the number of layers in the original base model's dense classifier head. (Note num_layers needs to be set before training the base model.)

See Part III in the Jupyter workbook for details on which ML classifier models were used.

-->

