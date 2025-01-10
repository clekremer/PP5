# Mildew Detection in Cherry Leaves

## Table of Contents
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and how to validate](#hypothesis-and-how-to-valide)
4. [Rationale to map the business requirements to the data visualizations and ML tasks](#Rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ML-tasks)
5. [ML Business case](#ml-business-case)
6. [Dashboard design](#dashboard-design-streamlit-app-user-interface)
7. [Unfixed Bugs](#unfixed-bugs)
8. [Deployment](#deployment)
9. [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
10. [Credits](#credits)

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, then you can create a new one with _Regenerate API Key_.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

 - Cherry leaves which are infected with powdery mildew have a white coating and spots on its sureface
 - Infected leaves can clearly be distinguished from healthy leaves and validation can be done by comparing healthy and infected leaves based on images
 - an ML based model is used in an image visualizer to differentiate between healthy and infected cherry leafs
 - the model should have a minimum validity of 97% accuracy
 - By the help of this ML based image visualizer the process should become much more effective for the company in terms of time and money saving

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

Business Requirement 1: Data Visualization

We will display the "mean" and "standard deviation" images for healthy and mildew infected leaves.
We will display the difference between average healthy and mildew infected leaves.
We will display an image montage for either healthy or mildew infected leaves. 


Business Requirement 2: Classification

We want to predict if a given leaf is infected with powdery mildew or not. 
We want to build a binary classifier and generate reports.

## ML Business Case

 - Objective of the project is to develop a ML 2-class, singel-label classification model, which can predict if a a leaf is infected with powdery mildew or not. The model is based on historical image data.
 - The model should offer cherry plantation farmers a more effective diagnostic method for powdery mildew detection
 - the model success metrics are accuracy of 99% or above on the test set.
 - The model output is defined as a flag, indicating if the leaf or the tree is infected with powdery mildew. The idea is that employees of the plantation will take a picture of some leaves of the tree and evaluate them in the App. The prediction is made on the fly.
 - Currently mildew infection is identified manually in a very time-consuming process so any cherry plantation farm would benefit by using this model 
 - The training data can be downloaded from Kaggle. The original image format is 256x256. As we need to consider a max Slug size of 500 MB on Heroku it is required to reduce the image fomat to 40x40. It is considered that this has no negative impact on model performance. 

## Dashboard Design

### Page 1: Quick Project Summary


### Page 2: Leaves Visualizer

### Page 3: Powdery Mildew Detection

### Page 4: Project Hypothesis and Validation

### Page 5: ML Performance Metrics

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
