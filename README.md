### Comparing the performance of some different ML classifier architectures for detection of diagnostic conditions from ECG signal data

**Indraneel Tambe**

#### Executive summary
I experiment with some different ML models and compare their performance in detecting diagnostic conditions ECG (electrocardiogram) signals to diagnose heart conditions based on the ECG signal morphology. Specifically, I test the performance of a family of ML architectures involving placing different classification heads on top of a basic 1D CNN-based model that I pre-train from scratch in this project.

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

In part III I experimented with five "classical" ML models piped after my trained feature extractor, and compare them with the original base model's performance. (Note: this performance will be tested on a separate test set from the original validation set that was used to select the best-performing base model during training. I will also experiment with num_layers ranging from 1 to 5; here num_layers is the number of layers in the original base model's dense classifier head. (Note num_layers needs to be set before training the base model.)

See Part III in the Jupyter workbook for details on which ML classifier models were used.

#### Results

TODO . . . 

#### Next steps

TODO . . . 

#### Link to Jupyter workbook

TODO . . . 


##### Contact and Further Information
