import os
import json

def scan_Progpilot(Directory_to_progpilot,project_path,project_name):
    output_path = "./output_progpilot"
    if os.path.isdir(output_path) == False:
        os.system(f"mkdir {output_path}")
    if os.path.exists(f"{output_path}/{project_name}.txt") == True:
        os.system(f"rm {output_path}/{project_name}.txt")
    os.system(f"{Directory_to_progpilot}/progpilot {project_path} >  {output_path}/{project_name}.txt")

def process_output(project_name):
    output_path = "/mnt/tp/code_whip/output_progpilot"
    content = open(f"{output_path}/{project_name}.txt","r").read()
    json_objects = json.loads(content)
    alerts = set()
    for json_object in json_objects:
        alerts.add((json_object['sink_file'],int(json_object['sink_line'])))
    #print(alerts)
    return alerts