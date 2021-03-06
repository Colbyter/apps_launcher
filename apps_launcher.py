"""Apps_Launch Script"""

from subprocess import Popen, check_output, CalledProcessError
import click
import signal
import os
import time


def get_pid(name):
	"""Func to func the process by name and then kills it"""
	try:
		#command = "ps -A | grep -m1 '{}' | awk '{{print $1}}'".format(name)
		command = "ps -ef | grep '{}' | grep -v grep | awk '{{print $2}}' | xargs  kill -9".format(name)
		print(command)
		#return int(check_output(command, shell=True))
		check_output(command, shell=True)
		
	except CalledProcessError as cpe:
		click.echo("Process failed: {}".format(cpe))

	except OSError as ose:
		click.echo("Execution failed: {}".format(ose))
	return 'ok'

@click.command()
@click.option('-state', help="State of the app. ON or OFF")

def main(state):
	"""Main part handling the commands"""
	apps = [ '/Applications/Microsoft Outlook.app', '/Applications/Webex Teams.app', '/Applications/Colloquy.app']
	
	if state in ("ON", "on"):
		try:
			for app in apps:
				app_name = app.split("/", 2)
				app_name = app_name[2].replace(".app", "")
				app_name = app_name.strip()
				p = Popen(['open', '-a', app])
				p.wait()	
				click.echo("{} returned: {}".format(app_name, p.returncode))

		except OSError as oe:
			click.echo("Execution failed for ON:{}".format(oe))

	elif state in ("OFF", "off"):

		try:
			#import atexit
			for app in apps:
				app_name = app.split("/", 2)
				app_name = app_name[2].replace(".app", "")
				app_name = app_name.strip()
				print(app_name)
				get_pid(app_name)
				#print(pid)
				#os.kill(pid, signal.SIGKILL)
				click.echo("{} closed".format(app_name))
                

		except OSError as oe:
			click.echo("Execution failed for OFF:{}".format(oe))
		


if __name__ == '__main__':
	main()
	#import atexit
	#atexit.register(main)
    
