#This script is a wrapper that executes a few other scripts. It is to be used as a scheduled task.
import datetime, os, subprocess, webbrowser, re, sys

#Since it's not going to be run in interactive mode, we need to load PYTHONSTARTUP to
if os.path.isfile(os.environ['PYTHONSTARTUP']):
	exec(open(os.environ['PYTHONSTARTUP']).read())
else:
	sys.exit("You don't have a .pythonrc file in your PYTHONSTARTUP environment variable.")

#Note: M:\ is \\pwdoows\oows\Watershed Sciences\GSI Monitoring
#It's mapped to a drive letter because certain Windows services can't handle non letter-mapped paths

#Note regarding filepath separators: In order to represent a literal '\', we must type \\ (an escaped \)
#However, when specifying file paths that will be read by the R command, we must type \\\\
#Because specifying \\ in the Python script will cause R to see \, and it will choke on the singleton \ just like Python would


###Section 1: Set execution parameters
#Date string for filenames.
current_date = datetime.datetime.now()
datestring = current_date.strftime("%Y%m%dT%H%M")

###Section 2: Run the python script that will compress the video files in the folder
#We'll be calling the python script from within this python script
#We'll be composing a string that will be sent to the command line via a subprocess

#Instantiate log file and folders
if not os.path.exists("output")
	os.mkdir("output")

if not os.path.exists("logs")
	os.mkdir("logs")
	

#Note: Reserve this section for passing runtime parameters currently set to default values within the video compression python script.

#Where is the python executable?
#Note: This filepath is used by Python and CMD.EXE, and thus needs \\ as a separator (CMD.EXE doesn't choke on singleton \)
r_exe = "Rscript.exe"

#Compose the R command that will be passed to r_exe
r_command = "rmarkdown::render(" + r_script + ", params = list(database=" + database + ", write=" + writeflag + ", datestring=" + datestring +")" + ", output_file =" + output_file + ")"

print(r_command)

#Invoke the R commands to run the script and knit the output
# -e means Rscript.exe is getting the commands from stdin and not from a file
#More info: https://www.rdocumentation.org/packages/utils/versions/3.5.1/topics/Rscript
subprocess.call([r_exe, "-e", r_command])

#Open the output file in your web browser
outputexists = os.path.isfile(MAINTENANCEFOLDER + "\\update_accessdb_tables\\" + re.sub('\\\\\\\\', '\\\\', output_file.strip("'")))
if outputexists:
	webbrowser.open(os.path.realpath(MAINTENANCEFOLDER + "\\update_accessdb_tables\\" + re.sub('\\\\\\\\', '\\\\', output_file.strip("'"))))
else:
	webbrowser.open(os.path.realpath(MAINTENANCEFOLDER + "\\update_accessdb_tables\\accessdb_error.html"))