import os
import re
import WAP
import Progpilot

# Tune these variables
project_path = "/etc/example"
project_name = "example"
Directory_to_wap = "/etc/wap-2.1"
Directory_to_progpilot = "/etc/progpilot"

project_path = "/usr/src/myapp/WHIP/example"
Directory_to_wap = "/usr/src/myapp/wap"
Directory_to_progpilot = "/usr/src/myapp/progpilot"

## Extract the function calls and their line numbers from the php OPCODE
## You need to activate the opcache extension in PHP
def gen_methods_assign_include(search_dir,path,project_name):
    if os.path.isdir(path+"methods") == False:
        os.system("mkdir "+path+"methods")
    if os.path.isdir(path+"assign") == False:
        os.system("mkdir "+path+"assign")
    if os.path.isdir(path+"include") == False:
        os.system("mkdir "+path+"include")
    if os.path.isdir(path+"methods_paths") == False:
        os.system("mkdir "+path+"methods_paths")
    #print("Debug: in gen_methods_assign_include function")
    if os.path.exists(path+"methods/"+project_name+".txt") == True and os.path.exists(path+"assign/"+project_name+".txt") == True and os.path.exists(path+"include/"+project_name+".txt") == True and os.path.exists(path+"methods_paths/"+project_name+".txt") == True:
        #print("Debug: break the function call")
        return -2
    #print("Run the command - find " + search_dir + " -name '*.php' > ./temp/temp_out.txt")
    os.system("find " + search_dir + " -name '*.php' > ./temp/temp_out.txt")
    php_files = open("./temp/temp_out.txt","r").read().split("\n")
    #print("Debug: Create file " + path+"methods/"+project_name+".txt")
    methods_file = open(path+"methods/"+project_name+".txt","w")
    assign_file = open(path+"assign/"+project_name+".txt","w")
    include_file = open(path+"include/"+project_name+".txt","w")
    include_line_numbers = open("./temp/include_line_numbers.txt","w")
    methods_paths = open(path+"methods_paths/"+project_name+".txt","w")
    for php_file in php_files:
        if php_file == "":
            continue
        #print("Debug: " + php_file)
        try:
            #print("Run the command - php -d opcache.enable_cli=1 -d opcache.opt_debug_level=0x10000 -r 'opcache_compile_file(\""+php_file+"\");' 2> ./temp/temp_out.txt")
            os.system("php -d opcache.enable_cli=1 -d opcache.opt_debug_level=0x10000 -r 'opcache_compile_file(\""+php_file+"\");' 2> ./temp/temp_out.txt")
        except:
            #print("Debug: skip")
            continue
        lines = open("./temp/temp_out.txt","r", encoding='utf-8', errors='ignore').read().split("\n")
        defined_function = ""
        for line in lines:
            if len(line) > 0 and line[0] != 'L' and "lines" in line and "args" in line and "vars" in line:
                if "::" in line:
                    line = line.split("::")[1]
                defined_function = line.split(":")[0]
                defined_function = defined_function.lower()
                methods_paths.write(php_file + " $$$$ " + defined_function + "\n")
            if "INIT_METHOD_CALL" in line:
                line_num = line.split("(")[1].split(")")[0]
                function_name = line.split(" ")[-1]
                if len(function_name) > 7 and function_name[:7] == "string(":
                    function_name = function_name[8:-2]
                else:
                    continue
                function_name = function_name.lower()
                methods_file.write("INIT_METHOD_CALL $$$$ " + php_file + " $$$$ " + line_num + " $$$$ " + function_name + " $$$$ " + defined_function + "\n")
            if "INIT_STATIC_METHOD_CALL" in line:
                line_num = line.split("(")[1].split(")")[0]
                function_name = line.split(" ")[-1]
                if len(function_name) > 7 and function_name[:7] == "string(":
                    function_name = function_name[8:-2]
                else:
                    continue
                function_name = function_name.lower()
                methods_file.write("INIT_STATIC_METHOD_CALL $$$$ " + php_file + " $$$$ " + line_num + " $$$$ " + function_name + " $$$$ " + defined_function + "\n")
            if "INIT_FCALL" in line:
                line_num = line.split("(")[1].split(")")[0]
                function_name = line.split(" ")[-1]
                if len(function_name) > 7 and function_name[:7] == "string(":
                    function_name = function_name[8:-2]
                else:
                    continue
                function_name = function_name.lower()
                methods_file.write("INIT_FCALL $$$$ " + php_file + " $$$$ " + line_num + " $$$$ " + function_name + " $$$$ " + defined_function + "\n")
            if "INIT_FCALL_BY_NAME" in line:
                line_num = line.split("(")[1].split(")")[0]
                function_name = line.split(" ")[-1]
                if len(function_name) > 7 and function_name[:7] == "string(":
                    function_name = function_name[8:-2]
                else:
                    continue
                function_name = function_name.lower()
                methods_file.write("INIT_FCALL_BY_NAME $$$$ " + php_file + " $$$$ " + line_num + " $$$$ " + function_name + " $$$$ " + defined_function + "\n")
            if "INIT_NS_FCALL_BY_NAME" in line:
                line_num = line.split("(")[1].split(")")[0]
                function_name = line.split(" ")[-1]
                if len(function_name) > 7 and function_name[:7] == "string(":
                    function_name = function_name[8:-2]
                else:
                    continue
                if "\\" in function_name:
                    function_name = function_name.split("\\")[-1]
                function_name = function_name.lower()
                methods_file.write("INIT_NS_FCALL_BY_NAME $$$$ " + php_file + " $$$$ " + line_num + " $$$$ " + function_name + " $$$$ " + defined_function + "\n")
            if " ASSIGN " in line:
                line_num = line.split("(")[1].split(")")[0]
                variable_name = line.split(" ")[-2]
                if len(variable_name) > 4 and variable_name[:2] == "CV":
                    variable_name = variable_name[4:-1]
                else:
                    continue
                assign_file.write("ASSIGN $$$$ " + php_file + " $$$$ " + line_num + " $$$$ " + variable_name + " $$$$ " + defined_function + "\n")
            if "INCLUDE_OR_EVAL" in line:
                line_num = line.split("(")[1].split(")")[0]
                include_line_numbers.write(php_file + " $$$$ " + line_num + "\n")
    include_line_numbers.close()
    assign_file.close()
    methods_file.close()
    include_line_numbers = open("./temp/include_line_numbers.txt","r").read()
    for line in include_line_numbers.split("\n"):
        if line == "":
            continue
        ls = line.split(" $$$$ ")
        os.system("sed '"+str(ls[1])+"!d' "+ls[0]+" > ./temp/temp_out.out")
        fff = open("./temp/temp_out.out","r").read().split('\n')[0]
        file1 = ls[0]
        file2 = re.findall(r"[a-zA-Z0-9._-]*\.php",fff)
        if len(file2) == 0:
            continue
        else:
            file2 = file2[0]
        include_file.write(file1 + " $$$$ " + file2 + "\n")

## Complicated code to deal with different cases to extract the In and Out of a function call
def extract_variables(s):
    vars = []
    eq = []
    if '\n' in s:
        s = s.split('\n')[-1]
    s = s.replace(".=","=")
    s = s.replace("+=","=")
    s = s.replace("-=","=")
    qut_b = 0
    double_qut_b = 0
    for i in range(len(s)):
        if s[i] == "'":
            if double_qut_b == 0:
                if qut_b == 0:
                    qut_b = 1
                else:
                    qut_b = 0
        if qut_b == 1:
            continue
        if s[i] == '"':
            if double_qut_b == 0:
                double_qut_b = 1
            else:
                double_qut_b = 0
        if double_qut_b == 1:
            continue
        if s[i] == '$':
            v = "$"
            brackets = 0
            arr_brackets = 0
            qut = 0
            double_qut = 0
            for j in range(i+1,len(s)):
                c = s[j]
                if c == "'":
                    if double_qut == 0:
                        if qut == 1:
                            qut = 0
                        else:
                            qut = 1
                        v = v + c
                        continue
                if qut == 1:
                    v = v + c
                    continue
                if c == '"':
                    if double_qut == 1:
                        double_qut = 0
                    else:
                        double_qut = 1
                    v = v + c
                    continue
                if double_qut == 1:
                    v = v + c
                    continue
                if c == '(':
                    brackets = brackets + 1
                elif c == '[':
                    arr_brackets = arr_brackets + 1
                elif c == ']':
                    arr_brackets = arr_brackets - 1
                    if brackets != 0:
                        v = v + c
                        continue
                    if arr_brackets == 0:
                        v = v + c
                        vars.append(v)
                        break
                    if arr_brackets < 0:
                        vars.append(v)
                        break
                elif c == ')':
                    brackets = brackets - 1
                    if arr_brackets != 0:
                        v = v + c
                        continue
                    if brackets == 0:
                        v = v + c
                        vars.append(v)
                        break
                    if brackets < 0:
                        vars.append(v)
                        break
                elif (c == ',' or c==';' or c=='?') and brackets == 0:
                    if v != "":
                        vars.append(v)
                        break
                elif c == ':' and j+1!=len(s) and s[j+1] != ":" and j!=0 and s[j-1] != ":":
                    if v != "":
                        vars.append(v)
                        break
                elif c == '=' and j+1!=len(s) and s[j+1] != ">":
                    if v != "":
                        eq.append(v)
                        break
                v = v + c
    return (vars,eq)


def inject_lines_in_original_version(file_methods):
    for fl_path in file_methods:
        try:
            original_php_file = open(fl_path,"r").read().split("\n") 
            php_file = open(fl_path,"r").read().split("\n") 
        except:
            continue 
        checked_lines = {}
        for pr in file_methods[fl_path]:
            line_num = int(pr[1]) - 1
            if line_num in checked_lines:
                continue
            checked_lines[line_num] = 1
            line_code = original_php_file[line_num]
            if line_code.count('(') != line_code.count(')'):
                continue
            if line_code.count('=') != 1:
                continue
            variables,assigned_variables = extract_variables(line_code)
            if len(variables) > 0 and len(assigned_variables) > 0:
                res = assigned_variables[0]
                co = 0
                pre_line_code = php_file[line_num+1]
                for v in variables:
                    co = co + 1
                    php_file[line_num+1] = f"if(round(rand(0,1))){{ \n //InjectedLineKeyWord \n //echo {v}; \n //echo {res}; \n //{res} = {v}; \n }} \n{php_file[line_num+1]}"
                rewrite_file = open(fl_path,"w")
                for a in php_file:
                    rewrite_file.write(a + "\n")
                rewrite_file.close()
                ## If the injection cause an error, then we ignore it
                os.system("php -l "+fl_path+" > ./temp/check_error.out 2>&1")
                compile_out = open("./temp/check_error.out","r").read()
                if "Errors parsing" in compile_out:
                    php_file[line_num+1] = pre_line_code
        rewrite_file3 = open(fl_path,"w")
        for a in php_file:
            rewrite_file3.write(a + "\n")
        rewrite_file3.close()

def inject(project_path,project_name):
    meatadata_path = "./metadata/"
    if os.path.isdir(meatadata_path) == False:
        os.system("mkdir " + meatadata_path)
    gen_methods_assign_include(project_path,meatadata_path,project_name)
    lines = open(meatadata_path+"methods/"+project_name+".txt","r").read().split("\n")
    files_methods = {}
    for line in lines:
        if line == "":
            continue
        line = line.split(" $$$$ ")
        if line[1] not in files_methods:
            files_methods[line[1]] = []
        files_methods[line[1]].append((line[3],line[2]))
    inject_lines_in_original_version(files_methods)

def uncomment_fake_sinks(project_path):
    os.system(f"find {project_path} -name '*.php' > ./temp/list_of_file.txt")
    dir_php_files = open("./temp/list_of_file.txt","r").read().split("\n")
    injected_loc = set()
    for dir_php_file in dir_php_files:
        if dir_php_file == "":
            continue
        cond = False
        php_file = open(dir_php_file,"r").read().split('\n')
        for i in range(len(php_file)):
            if "InjectedLineKeyWord" in php_file[i]:
                #injected_loc[(dir_php_file,i+1)] = 1
                injected_loc.add((dir_php_file,i+2))
                #injected_loc[(dir_php_file,i+2)] = 1
                #injected_loc[(dir_php_file,i+3)] = 1
                php_file[i+1] = php_file[i+1].replace("//","")
                php_file[i+2] = php_file[i+2].replace("//","")
                cond = True
        if cond == True:
            fout = open(dir_php_file,"w")
            for line in php_file:
                fout.write(line+"\n")
            fout.close()
    return injected_loc

def comment_fake_sinks(project_path):
    os.system(f"find {project_path} -name '*.php' > ./temp/list_of_file.txt")
    dir_php_files = open("./temp/list_of_file.txt","r").read().split("\n")
    injected_loc = set()
    for dir_php_file in dir_php_files:
        if dir_php_file == "":
            continue
        cond = False
        php_file = open(dir_php_file,"r").read().split('\n')
        for i in range(len(php_file)):
            if "InjectedLineKeyWord" in php_file[i]:
                if "//" not in php_file[i+1]:
                    php_file[i+1] = "//" + php_file[i+1]
                if "//" not in php_file[i+2]:
                    php_file[i+2] = "//" + php_file[i+2]
                cond = True
        if cond == True:
            fout = open(dir_php_file,"w")
            for line in php_file:
                fout.write(line+"\n")
            fout.close()
    return injected_loc

def stitch(path,line_num):
    fff = open(path,"r").read().split('\n')
    if '//' not in fff[line_num-1]:
        fff[line_num-1] = "//" + fff[line_num-1]
    if '//' not in fff[line_num]:
        fff[line_num] = "//" + fff[line_num]
    fff[line_num+1] = fff[line_num+1].replace("//","")
    fout = open(path,"w")
    for line in fff:
        fout.write(line+"\n")
    fout.close()

def list_stitch(set_alert,set_inject):
    counter = 0
    for pr in set_inject:
        file_dir,line_num = pr
        if (file_dir,line_num) in set_alert and (file_dir,line_num+1) in set_alert:
            stitch(file_dir,line_num)
            counter = counter + 1
    return counter

def scan(project_path,project_name,Directory_to_wap,Directory_to_progpilot):
    WAP.scan_WAP(Directory_to_wap,project_path,project_name)
    Progpilot.scan_Progpilot(Directory_to_progpilot,project_path,project_name)
    ## the scan for the commercial tools are ananymous
    #scan_comm1(project_path,project_name)
    #scan_comm2(project_path,project_name)

def extract_alerts(project_name):
    alerts = set()
    wap_alerts = WAP.process_output(Directory_to_wap,project_name)
    print(f"WAP Alerts: {wap_alerts}")
    alerts = alerts.union(wap_alerts)
    progpilot_alerts = Progpilot.process_output(Directory_to_progpilot,project_name)
    print(f"Progpilot Alerts: {progpilot_alerts}")
    alerts = alerts.union(progpilot_alerts)
    #comm1_alerts = Comm1.process_output(project_name)
    #print(f"Comm1 Alerts: {comm1_alerts}")
    #alerts = alerts.union(comm1_alerts)
    #comm2_alerts = Comm2.process_output(project_name)
    #print(f"Comm2 Alerts: {comm2_alerts}")
    #alerts = alerts.union(comm2_alerts)
    print(f"Joined Alerts: {alerts}")
    return alerts

def InferStitch(set_inject,project_path,project_name):
    global Directory_to_wap
    global Directory_to_progpilot
    set_alert = extract_alerts(project_name)
    stitch_num = list_stitch(set_alert,set_inject)
    iteration = 0
    while stitch_num != 0:
        iteration = iteration + 1
        print(f"Iteration {iteration}")
        scan(project_path,project_name,Directory_to_wap,Directory_to_progpilot)
        set_alert = extract_alerts(project_name)
        stitch_num = list_stitch(set_alert,set_inject)

if os.path.isdir("./temp") == True:
    os.system("rm -rf ./temp")
os.system("mkdir ./temp")

inject(project_path,project_name)

print("Scan original project")
scan(project_path,project_name,Directory_to_wap,Directory_to_progpilot)
original_wap_alerts = WAP.process_output(Directory_to_wap,project_name)
original_progpilot_alerts = Progpilot.process_output(Directory_to_progpilot,project_name)
original_alerts = extract_alerts(project_name)

set_inject = uncomment_fake_sinks(project_path)
scan(project_path,project_name,Directory_to_wap,Directory_to_progpilot)
print(f"Injected Lines: {set_inject}")
InferStitch(set_inject,project_path,project_name)

print("Scan final project")
comment_fake_sinks(project_path)
scan(project_path,project_name,Directory_to_wap,Directory_to_progpilot)
final_wap_alerts = WAP.process_output(Directory_to_wap,project_name)
final_progpilot_alerts = Progpilot.process_output(Directory_to_progpilot,project_name)
final_alerts = extract_alerts(project_name)

print(">>> New only for WAP:")
for alert in final_wap_alerts:
    if alert not in original_wap_alerts and alert in original_alerts:
        print(alert)

print(">>> New only for Progpilot:")
for alert in final_progpilot_alerts:
    if alert not in original_progpilot_alerts and alert in original_alerts:
        print(alert)

print(">>> New for all the tools:")
for alert in final_alerts:
    if alert not in original_alerts:
        print(alert)
