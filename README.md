## kxlu-dvr
A simple stream writing script to record your favorite 88.9FM KXLU radio shows. 

![](https://indiepulsemusic.files.wordpress.com/2018/03/kxlu-logo-revised.png?w=424&h=160&crop=1)

### Introduction
Probably most efficiently utilized as a cron task on a computer with little downtime, this short little script utilizes the `urllib` module to pull stream data from the KXLU live feed and write it to an mp3 file. Inspired by almost always missing the awesome tunes by http://alienairmusic.com on Sunday evenings. 


### Usage  
The script takes three arguments, which must be given positionally. The title of the segment to be recorded, the length of the segment in minutes, and the _full_ output directory path. 

```
./kxlu-dvr <title> <length in minutes> <output path>
```

