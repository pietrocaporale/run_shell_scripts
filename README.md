
<picture>
<img alt="" src="https://www.devuty.altervista.org/gh/run_shell_scripts/run_sh_logo.png" align="left">
</picture>

# Run Shell Scripts

### _Python application to launch shell scripts organized by folders from a GUI_
<br>
<p align="center" width="100%">
<img src="https://www.devuty.altervista.org/gh/run_shell_scripts/run_sh.png">
<br>
</p>


## Application files
| File | Description |
| --- | --- |
| dist/run_shell_scripts                | Linux executable application file  |
| dist/run_shell_scripts                | Windows 10(+) executable application file  |
| run_shell_scripts.py                  | Source |
| run_sh.png                            | Icon |
| support/run_shell_scripts.desktop     | Linux launch applications |
| .init                                 | File created for storing window position and size |
| lastdir.txt                           | File created for storing last folder used |
| favdir.txt                            | File created for storing favorite folders |

## Installation
Copy the executable file to any folder dedicated to it. In this folder the configuration files `.init`, `lastdir.txt`, `favdir.txt` will be stored.<br>
Create your own [Desktop Entry], I've included one I used in Manjaro distro.


## Getting Started
Opening the application will place itself on its startup folder.
Select the folder containing the scripts to run.<br>
A launch button will be created for each `.sh/.bat` file.
Just click the button to start the script.<br>
Add the selected folder to your favorites for quick access.<br>
It might be convenient to group the scripts in folders by type of work.

The scripts are run in parallel multiprocesses, so a separate terminal will open for each start.<br>
If you want to start them sequentially with a single process just change the public variable `MULTIPROCESSING = 0` in the application.

`Note`
If you have a lot of folders to work with you can also add them manually in the favdir.txt file, one line per folder.

## Example
I'll give you the example of how I set up the backup with Borg using scripts dedicated to each single backup.

I created a folder backup/borg, inside I created a folder for each backup to be performed eg. _dev_android_, _dev_python_,_dev_public_html_ where I copied the bootable script files.<br>
I have bookmarked these folders so I can get there quickly.<br>
Then I start each backup or check script by clicking on its button.<br>
Clearly everyone can organize his scripts in the way he finds most comfortable.
<br>

```bash

```
## Usage
<br>

<img align="left" src="https://www.devuty.altervista.org/gh/run_shell_scripts/app_run_sh_buttons.png">
<br><br><br><br><br><br><br>
&nbsp;&nbsp;&nbsp;The scripts available are shown in the main window
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

<img align="left" src="https://www.devuty.altervista.org/gh/run_shell_scripts/app_run_sh_refresh.png">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
&nbsp;&nbsp;&nbsp;Button for folder refresh if you made changes to the files in the folder
<br><br><br><br><br><br><br><br><br>

<img align="left" src="https://www.devuty.altervista.org/gh/run_shell_scripts/app_run_sh_workon.png">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
&nbsp;&nbsp;&nbsp;The selected folder will be shown in the label
<br><br><br><br><br><br><br><br>

<img align="left" src="https://www.devuty.altervista.org/gh/run_shell_scripts/app_run_sh_combo.png">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
&nbsp;&nbsp;&nbsp;And in combo select too, list where you can select your favorite folder
<br><br><br><br><br><br>

<img align="left" src="https://www.devuty.altervista.org/gh/run_shell_scripts/app_run_sh_addfav.png">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
&nbsp;&nbsp;&nbsp;Button to add the selected folder to favourites
<br><br><br><br><br>

<img align="left" src="https://www.devuty.altervista.org/gh/run_shell_scripts/app_run_sh_delfav.png">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
&nbsp;&nbsp;&nbsp;Or remove it from favourites folders
<br><br><br><br><br><br>

<img align="left" src="https://www.devuty.altervista.org/gh/run_shell_scripts/app_run_sh_select.png">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
&nbsp;&nbsp;&nbsp;Select new folder to work on.
<br><br><br><br>

<br><br>
A short video on how to use it<br><br>
[<img align="center" alt="Video link" src="https://www.devuty.altervista.org/gh/run_shell_scripts/video_cover.png"/>](https://www.youtube.com/watch?v=40zeYaM6HYg)


