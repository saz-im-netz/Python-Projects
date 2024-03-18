# Add a scalebar to your REM images (or any other images ...)


## Description

To add scalebars to your REM images, put all images with the same magnification in one folder and change the folder_path variable at the beginning to match your folder. Then change the bar_length and scale_label parameters in the given function in the for loop, so it will match the correct pixel / nm ratio for the given magnification.

When running the program first a new folder will be created inside the provided folder to store the images and then all images inside the folder will be given a scalebar. If you don't want them to be opened right away, comment out line 42 in the function add_scale_bar()

Good luck with your projects!