import struct

# 校验和
def check(data):
    sum=0
    #判断字节的长度为奇数还是偶数，为奇数则需要补字节
    if (len(data)/2) % 2:                              
        data += '00'
    for i in range(0,len(data),4):
        # print(data[i:i+4])
        val = int(data[i:i+4],16)
        sum = sum + val
        sum = sum & 0xffffffff
 
    sum = (sum >> 16) + (sum & 0xffff)
    if sum > 65535:
        sum = (sum >> 16) + (sum & 0xffff)
    return 65535-sum

# 替换多个字符
def replace_char(string,p,c):
    new = []
    for s in string:
        new.append(s)
    for index,point in enumerate(p):
        new[point] = c[index]
    return ''.join(new)


if __name__ == "__main__":
    for i in range(1,6):
        file_name = 'test'+ str(i) + '.txt'
        content = ''
        with open(file_name) as file_obj:
            for line in file_obj:
                content += line.rstrip('\n')
            content = content.replace(" ", "")
            file_obj.close()
        protoco = content[46:48]                  #第46,47位为协议位
        if protoco == '06':                       #TCP
            print('Protocol:TCP')
            # 需要更改Time to live为00,Header checksum为14,还有校验和位为0000
            s1 = [44,45,48,49,50,51,100,101,102,103]   
            e1 = ['0','0','0','0','1','4','0','0','0','0']
            content = replace_char(content,s1,e1)
            tcp_check= check(content[44:])        #从第44位开始为有效检验数据（有伪首部）
            print(hex(tcp_check))
        elif protoco == '11':                     #UDP
            print('Protocol:UDP')
            a,b,c,d = content[76],content[77],content[78],content[79]
            # 需要更改Time to live为00,Header checksum为14,还有校验和位为0000
            s1 = [44,45,48,49,50,51,80,81,82,83]
            e1 = ['0','0',a,b,c,d,'0','0','0','0']
            content = replace_char(content,s1,e1)
            udp_check= check(content[44:])        #从第44位开始为有效检验数据（有伪首部）
            print(hex(udp_check))
        elif protoco == '01':                     #ICMP
            print('Protocol:ICMP')
            # 需要更改校验和位为0000
            s1 = [72,73,74,75]
            e1 = ['0','0','0','0']
            content = replace_char(content,s1,e1)          
            icmp_check= check(content[68:])       #从第68位开始为有效检验数据（无伪首部）
            print(hex(icmp_check))
