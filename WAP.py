import os

def scan_WAP(Directory_to_wap,project_path,project_name):
    output_path = Directory_to_wap + "/output_WAP"
    if os.path.isdir(output_path) == False:
        os.system(f"mkdir {output_path}")
    if os.path.exists(f"{output_path}/{project_name}.txt") == True:
        os.system(f"rm {output_path}/{project_name}.txt")
    print(f"cd {Directory_to_wap}; echo | timeout 900s ./wap -a -all -out {output_path}/{project_name}.txt -p {project_path}")
    os.system(f"cd {Directory_to_wap}; echo | timeout 900s ./wap -a -all -out {output_path}/{project_name}.txt -p {project_path} > temp.txt")

def process_output(Directory_to_wap,project_name):
    output_path = Directory_to_wap + "/output_WAP"
    lines = open(f"{output_path}/{project_name}.txt","r").read().split("\n")
    alerts = set()
    file = ""
    cond = False
    line_num = -1
    for line in lines:
        line = line.strip()
        if "> > > >  File: " in line:
            file = line.split("> > > >  File: ")[1].split(" < < < <")[0]
        if "Vulnerable code:" in line:
            cond = True
            continue
        if cond == True:
            if line == "":
                cond = False
                if line_num != -1:
                    alerts.add((file,int(line_num)))
            else:
                line_num = line.split(":")[0]
    return alerts

        