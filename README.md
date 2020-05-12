# Project Title

DSC160 Data Science and the Arts - Midterm Project Repository - Spring 2020

Project Team Members: 
- Firstname Lastname1, name1@ucsd.edu
- Sabrina Ho, ssh026@ucsd.edu
- Xinrui Zhan, x5zhan@ucsd.edu
- Amir Uqdah, auqdah@ucsd.edu
- Yiheng Ye, yiy291@ucsd.edu

## Abstract

(10 points) 

  This project aims to compare the changes in emotion in Pixar movie scenes based on the frames of different pixar movies. We used  30 scenes 50 seconds apart from each other and 3 frames within each scene in the popular animated Pixar movies Big Hero 6, Incredibles 2, Toy Story 4, Cars 3, and Wall E.  We attempt to qualify the emotion content of each scene based on features of images such as warmth of colors, brightness, and  hue saturation value. We expect to see a correlation between the features used in the film and the emotions that are perceived or felt during the film. Also, we want to figure out the general trend of “how does a Pixar movie ‘feel’ over time”. After extracting features we need, we will build our own color-emotion map to label our data. Then we will use them to feed our classification models. Afterwards, we will make several analysis visualizations such as cluster plots or sound wave plots using online tools or python libraries. We plan to display our results in the form of visualizations such as t-SNE graphs or bitmaps.
  
  As animated filmmakers have full control over the visual medium, visual cues signaling the changing of emotion in animated films are always intentional. As such, this analysis can shed light on what visual features popular culture looks for different emotions.


## Data

(10 points) 

  Our data is collected from the website Animation Screencaps (link: https://animationscreencaps.com). This website contains over 500 movies including the series of Disney, Pixar, and so much more. As mentioned earlier, in this project we are using the following movies’ screencaps as our data: Big Hero 6, Incredibles 2, Toy Story 4, Cars 3, and Wall E. This Animation Screencaps website contains screencaps for each movie. We are scraping 30 scenes in total and 3 cap per scene, and they are all 50 seconds apart from each scene. The next section will talk in detail on how we scraped the screencaps.


## Code

(20 points)

- Data acquisition/scraping: **Scraping.ipynb**
  This notebook uses bs4 BeautifulSoup and requests libraries to scrape movies‘ screencaps from the Animation Screencaps website mentioned in the previous data section. You can see in the notebook that there is a scratch function that scrapes a total of 30 scenes and 3 caps per scene which are all 50 seconds apart from each scene. 
  
- Cleaning: **Main Notebook Preprocessing and Features Extraction.ipynb**
This notebook preprocesses the scenes we scraped using the first notebook and extracts features including PAD (Pleasure, Arousal, Dominance), blur, brightness, saturation, and optical flow. We iterate all caps we scraped and we resize them to (320, 768). We then use these feature functions to find the averages of all features within each scene and compile them into a dataframe, and save them as a csv file. 
- Analysis:
  - Features:
      - Brightness: We calculate the brightness for each image by calculating the mean of the third channel in image hsv format. The bigger the result, the more bright the image is. The brightness data will be used in calculating PAD (Pleasure, Arousal, Dominance). Below are the images with the biggest and smallest brightness in the movie toy story 4.
      - Saturation: We calculate the saturation for each image by calculating the mean of the second channel in image hsv format. The bigger the result, the more saturated the image is. The saturation data will be used in calculating PAD (Pleasure, Arousal, Dominance). Below are the images with the biggest and smallest saturation in the movie Big Hero 6.
      - Blur: While skimming through our dataset, we found out that some images are blur. Also, we thought that the degree of blur could be related to the emotion: A more blur scene could have a higher ability to contain certain emotion’s information such as surprise, excitement or fear. Based on https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/, we implement a method to calculate the degree of blur in a single image. The higher the number of degrees of blur, the less blur this image is. Below are the least blur and most blur images in movie Cars 3. 
      - PAD: Based on Machajdik and Hanbury’s paper (http://www.imageemotion.org/machajdik_hanbury_affective_image_classification.pdf), we calculate the degree of Pleasure, Arousal, and Dominance based on the three equations. We will use there three in our baseline model. 
      - Faces: Tbd 
      - Optical flow: We used the norm of the optical flow vector to represent how much changes are inside of two images’ transition. Since we have three caps per scene, we calculate both 2 transitions and get the mean of the norms to represent how many changes are inside of a scene. 
  - Baseline model(equations from the paper): **Baseline Model's Evaluation and Results.ipynb**
Based on Oana et.al’s paper, we labeled all scenes with 6 different emotions calculating by equations below. Here, we use the pleasure to represent valence. The prediction are stored in the baseline_celana_df.csv
  - Logistic regression model trained on outside dataset: **model trained on outside data.ipynb**
      - We found an emotion labeled images dataset (http://www.imageemotion.org/testImages_artphoto.zip). We select images with label anger, joy, disgust, fear, and sadness and we use all features we extracted (except the optical flow, since we are training on static single images) to train a logistic regression model and labeling our screencaps for all scenes with corresponding emotions. The predictions are stored in logistic_regression_trained_on_outside.csv.
  - An unsupervised clustering: Model unsupervised and viz.ipynb
  - Facial recognition: ??

- Generating results:
  - Output prediction made by models: Baseline Model's Evaluation and Results.ipynb,  model trained on outside data.ipynb
  - Visualization of high-dimensional feature data and clusters:Model unsupervised and viz.ipynb
  - Visualization of supervised model predictions after dimension reduction:Viz of supervised, Dimension Reduction.ipynb
  - Visualization of features: More viz about feature.ipynb
  
- Testing: (the following notebooks are examples of each functions we used in the main preprocess and feature extraction notebook)
  - Brightness and Example.ipynb:
    - This notebook contains example of getting the mean image brightness with the library cv2
  - Degree of blur and Example.ipynb:
    - This notebook contains examples of calculating the blurriness of an image that uses the library cv2
  - Saturation and Example.ipynb:
    - This notebook contains examples of getting the mean saturation of an image with the library cv2
  - opticalFlow.ipynb:
    - This notebook calculates the optical flows between images using the library cv2. It returns an array in order to calculate the distances. 








## Results

(30 points) 

This section will contain links to documentation of your results. This can include figures, sound files, videos, bitmaps, as appropriate to your domain of analysis. Each result should include a brief textual description, and all should be listed below: 

- image files (`.jpg`, `.png` or whatever else is appropriate)
- audio files (`.wav`, `.mp3`)
- written text as `.pdf`

## Discussion

(30 points, three to five paragraphs)

The first paragraph should be a short summary describing your results.

The subsequent paragraphs could address questions including:
- Why is this culturally relevant?
- How does your computational approach differ from the traditional art historical, musicological, manuel/subjective approach to analyzing your cultural subject? 
- How do you think the original artists/musicians would respond to this type of analysis? Would it change/inform their practice in some way?
- How do your results relate to broader social, cultural, economic political, etc., issues? 
- In what future directions could you expand this work?

## Team Roles

Provide an account of individual members and their efforts/contributions to the specific tasks you accomplished.

## Technical Notes and Dependencies

Any implementation details or notes we need to repeat your work. 
- Additional libraries you are using for this project
- Does this code require other pip packages, software, etc?
- Does this code need to run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
- Blog posts
