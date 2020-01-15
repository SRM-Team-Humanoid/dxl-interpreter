import pypot.dynamixel


def init():
    ports=pypot.dynamixel.get_available_ports()     
    print (ports)
    if not ports :
        raise IOError("no ports found bruh!")
    print ("Connecting to ",ports[0])
    global dxl
    dxl=pypot.dynamixel.DxlIO(ports[0])
    ids=dxl.scan(range(30))
    print (ids)
    print (dxl.get_present_position(ids))


def movstmt(name, anglelist):
    dxl.set_goal_position(dict(zip((variables[name],anglelist))))



if __name__=='__main__':
    variables = {}
    while True:
        cmd = input()
