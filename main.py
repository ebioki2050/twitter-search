# twitter-search
## read library

## define function and type

## initialization


## GET tweet data and put in dataframe



## render tweet data
### save row tweet-status 

### save tweet-status data into csv file

#### read csv file if already exists.


#### make new csv file if doesn't exist. 


## save tweet-media data if it isnt dowloaded
### parse media-url from tweet status
### detect media-type
### set media path named after status data
### detect the media already downloaded in local by searching the media path

##### download image(s) if media-type == image and needDownloadImage == true

##### download video if media-type == video and needDownloadVideo == true

##### download GIF if media-type == GIF and needDownloadGIF == true
