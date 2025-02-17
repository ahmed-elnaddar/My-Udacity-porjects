# Udacity Wrangle and Analyze Data
Real-world data rarely comes clean. Using Python and its libraries, you will gather data from a variety of sources and in a variety of formats, assess its quality and tidiness, then clean it. This is called data wrangling. You will document your wrangling efforts in a Jupyter Notebook, plus showcase them through analyses and visualizations using Python (and its libraries) and/or SQL.

The dataset that I will be wrangling (and analyzing and visualizing) is the tweet archive of Twitter user @dog_rates, also known as WeRateDogs. WeRateDogs is a Twitter account that rates people's dogs with a humorous comment about the dog. These ratings almost always have a denominator of 10. The numerators, though? Almost always greater than 10. 11/10, 12/10, 13/10, etc. Why? Because "they're good dogs Brent." WeRateDogs has over 4 million followers and has received international media coverage.

WeRateDogs downloaded their Twitter archive and sent it to Udacity via email exclusively for us to use in this project. This archive contains basic tweet data (tweet ID, timestamp, text, etc.) for all 5000+ of their tweets as they stood on August 1, 2017. More on this soon.

![Image via [Boston Magazine](http://www.bostonmagazine.com/arts-entertainment/blog/2017/04/18/dog-rates-mit/)](https://video.udacity-data.com/topher/2017/October/59dd378f_dog-rates-social/dog-rates-social.jpg)

# What Software Do I Need?
If you want to run the project, the following software requirements apply:

You need to be able to work in a Jupyter Notebook on your computer.
The following packages (libraries) need to be installed.
You can install these packages via conda or pip.
* pandas
* NumPy
* requests
* tweepy
* json

A text editor, like Sublime, which is free, will be useful but is not required.

# Files
* `wrangle_act.ipynb`: code for gathering, assessing, cleaning, analyzing, and visualizing data
* `wrangle_report.html`: documentation for data wrangling steps: gather, assess, and clean
* `act_report.pdf`: documentation of analysis and insights into final data
* `twitter_archive_enhanced.csv`: file as given
* `image_predictions.tsv`: file downloaded programmatically
    * tweet_id is the last part of the tweet URL after "status/" → https://twitter.com/dog_rates/status/889531135344209921
    * p1 is the algorithm's #1 prediction for the image in the tweet → **golden retriever**
    * p1_conf is how confident the algorithm is in its #1 prediction → **95%**
    * p1_dog is whether or not the #1 prediction is a breed of dog → **TRUE**
    * p2 is the algorithm's second most likely prediction → **Labrador retriever**
    * p2_conf is how confident the algorithm is in its #2 prediction → **1%**
    * p2_dog is whether or not the #2 prediction is a breed of dog → **TRUE**
    * etc.
* `tweet_json.txt`: file constructed via API
* `twitter_archive_master.csv`: combined and cleaned data
