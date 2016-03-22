import htcondor
import os

collector_url = os.environ['COLLECTOR_URL']
schedd_name = os.environ.get('SCHEDD_NAME', None)

coll = htcondor.Collector(collector_url)

print "Slots available:"

for slot in coll.query(htcondor.AdTypes.Startd, "true", ["Name", "State"]):
    print slot["Name"], slot["State"]

scheddAd = None
if schedd_name:
    scheddAd = coll.locate(htcondor.DaemonTypes.Schedd, schedd_name)
else:
    scheddAd = coll.locate(htcondor.DaemonTypes.Schedd)
schedd = htcondor.Schedd(scheddAd)

print "Jobs:"

for job in schedd.query("true", ["User", "Cmd", "JobStatus"]):
    print job["User"], job["Cmd"], {0: "Unexpanded", 1: "Idle", 2: "Running", 3: "Removed", 4: "Completed", 5: "Held", 6: "Submission Error"}.get(job["JobStatus"], "unknown state")

print "Last 10 jobs"

for job in schedd.history("true", ["User", "IpcUsername", "IpcExe"], 10):
    print job["User"], job["IpcUsername"], job["IpcExe"]
