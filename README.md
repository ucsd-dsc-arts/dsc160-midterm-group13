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

- Data acquisition/scraping: Scraping.ipynb
  This notebook uses bs4 BeautifulSoup and requests libraries to scrape movies‘ screencaps from the Animation Screencaps website mentioned in the previous data section. You can see in the notebook that there is a scratch function that scrapes a total of 30 scenes and 3 caps per scene which are all 50 seconds apart from each scene. 
  
- Cleaning: Main Notebook Preprocessing and Features Extraction.ipynb
This notebook preprocesses the scenes we scraped using the first notebook and extracts features including PAD (Pleasure, Arousal, Dominance), blur, brightness, saturation, and optical flow. We iterate all caps we scraped and we resize them to (320, 768). We then use these feature functions to find the averages of all features within each scene and compile them into a dataframe, and save them as a csv file. 
- Analysis:
  - Features:
      - Brightness: We calculate the brightness for each image by calculating the mean of the third channel in image hsv format. The bigger the result, the more bright the image is. The brightness data will be used in calculating PAD (Pleasure, Arousal, Dominance). Below are the images with the biggest and smallest brightness in the movie toy story 4.


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
