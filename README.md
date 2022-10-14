# Shark-Bite
This project uses openCV to detect sharks teeth from images

### To Create Samples
```commandline
opencv_createsamples.exe -info .\pos.txt -w 24 -h 24 -num 1000 -vec pos.vec 
```


### To Train Samples
```commandline
opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 170 -num
Neg 1000 -numStages 12 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999  
```

### To Run
Just run main.py.  Use comments to test different inputs.