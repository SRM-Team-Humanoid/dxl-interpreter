#! /usr/bin/python3

import pypot.dynamixel


def is_a_name(name):
    if len(name)==0: return False
    if not (name[0].isalpha() or name[0]=="_"): return False
    try:
        for n in name[1:]:
            if not (n.isalnum() or n=="_"): return False
    except IndexError:
        pass
    return True


'''def init():
    ports=pypot.dynamixel.get_available_ports()     
    print (ports)
    if not ports :
        raise IOError("no ports found bruh!")
    print ("Connecting to ",ports[0])
    global dxl
    dxl=pypot.dynamixel.DxlIO(ports[0])
    ids=dxl.scan(range(30))
    variables["all"] = list(ids)
    print (ids)
    print (dxl.get_present_position(ids))'''

def init():
    variables["all"] = [1,2,3,4,5,6,7,8]


def movstmt(name, anglelist):
    dxl.set_goal_position(dict(zip((variables[name], anglelist))))

def setspeed(name, speedlist):
    dxl.set_moving_speed(dict(zip((variables[name], speedlist))))

if __name__=="__main__":
    variables = {}
    op = "$"
    while True:
        print(op, end=" ")
        try:
            cmdlst = input().split()
        except KeyboardInterrupt:
            print()
            break
        if len(cmdlst)==0: continue                                                        # empty
        if cmdlst[0] == "env":                                                             # env
            print(variables) if len(cmdlst)==1 else print("Unneeded tokens after env")
        elif cmdlst[0] == "init":                                                          # init
            init() if len(cmdlst)==1 else print("Unneeded tokens after init")
        elif cmdlst[0] == "var":                                                           # var
            try:
                if is_a_name(cmdlst[1]):
                    try:
                        motorlist = [int(x) for x in cmdlst[2:]]
                        variables[cmdlst[1]] = motorlist
                        for motor in motorlist:
                            if not motor in variables["all"]:
                                try:
                                    del variables[cmdlst[1]]
                                except KeyError: pass
                                print("motor", motor, "not detected")
                        
                    except IndexError:
                        print("Name after a var must be followed by list of motor ids")
                    except ValueError:
                        print("Invalid motor ids")
            except IndexError:
                print("var must be followed by a name followed by list of motors")
        elif cmdlst[0] == "quit":                                                          # quit
            if len(cmdlst)==1: break 
            else: print("Unneeded tokens after quit")


