### Comparing the performance of some different ML classifier architectures for ECG signal diagnosis detection

**Indraneel Tambe**

#### Executive summary
I experiment with some different ML models and compare their performance in detecting diagnostic conditions ECG (electrocardiogram) signals to diagnose heart conditions based on the ECG signal morphology. Specifically, I test the performance of a family of ML architectures involving placing different classification heads on top of a basic 1D CNN-based model that I pre-train from scratch in this project.

#### Research Question
What kinds of design choices for simple classifier models lead to the best results when working with the PTB-XL dataset (specifically their diagnostic superclasses)? Specifically, after training a deep model consisting of a feature extractor followed by a dense classifier head, we will try piping the feature extractor into various non-deep ML models and see how they compare to the original "fully deep" model.  

#### Rationale
Machine learning models for diagnosing conditions from ECG signals are useful as a tool to automate the process of condition detection and diagnosis. Although this diagnostic task can be performed by human clinicians, if it can be automated, then patients' ECG data can be continuously monitored for possible signs of heart conditions on a much larger scale, without the need for human clinicians watching every single patient for long periods of time. 
Moreover, understanding what kinds of simple design choices lead to best results may help inform what choices to make when working with larger models.

#### Data Sources
I'd like to use the publicly available PTB-XL database from Physionet (link: https://physionet.org/content/ptb-xl/1.0.3/).
The dataset consists of over 21k strips of 12-lead ECG signals, each 10 seconds long (and sampled at 500Hz). 
(For those unaware of the clinical terminology, ECG leads are essentially like channels in the signal. Each individual sample is a 16-bit integer, discretized at 1 microvolt.)
The ECG strips are labeled by human clinicians with a list of possible diagnostic conditions.

#### Methodology
For the analysis, I'm planning to start with a base deep-learning model which consists of a 1D CNN-based feature extractor followed by a dense classifier head. Next, in the full capstone project, I will try piping the trained feature extractor into various non-deep ML models for classifications and see if they can outperform the original deep classifier.

#### Results
What did your research find?

#### Next steps
What suggestions do you have for next steps?

#### Outline of project

- [Link to notebook 1]()
- [Link to notebook 2]()
- [Link to notebook 3]()


##### Contact and Further Information
