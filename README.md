Backup-Renamer
Simple python script to rename files to their original names after transferring them off of my backup drive.

Problem: REAPER Digital Audio Workstation stem file names get renamed with a date and time of the backup when I use my back up hard drive.

I needed to install REAPER on a fresh computer, and in order for it to still recognize my stem files, I would have needed to rename them 
manually or by reassociating each recorded part with the new filename. An example of a bad filename is "17-spare gtr-181219_1657 (2019_01_03 00_41_18 UTC)"
An example of a good filename is "17-spare gtr-181219_1657", so the names already are not user-friendly.

My python script and the associated files need to be placed in the directory with all these stem files. It will rewrite the names without the additional UTC date/time.
