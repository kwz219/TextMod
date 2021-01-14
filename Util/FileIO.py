def read_lines(filename):
    lines=[]
    with open(filename,'r',encoding='utf8')as of:
        for line in of:
            lines.append(line.strip())
        of.close()
    return lines