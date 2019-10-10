def status_report_unicast(process_table):
        print('\n     STATUS OF CLOCKS\n     EVENT       P(A)   P(B)   T(1)   T(2)')
        for index,status in enumerate(process_table):
                data = status[1]
                print(index+1,'. ',str(status[0]).ljust(12),str(data[0]).ljust(6), str(data[1]).ljust(6),str(data[2]).ljust(6),str(data[3]).ljust(5))



def status_report_multicast(process_table):
        print('\nSTATUS\nEVENT       P_0    P_1   P_2   T_1   T_2')
        for status in process_table:
                data = status[1]
                if status[0] == 'INTERNAL':
                        data.insert(1,'x')
                        data.insert(2,'x')
                print(str(status[0]).ljust(12), str(data[0]).ljust(5), str(data[1]).ljust(5),\
                      str(data[2]).ljust(5), str(data[3]).ljust(5), str(data[4]).ljust(5))

def information():
	print('\nVISUALIZE CLOCK SYNCHRONIZATION IN DISTRIBUTED SYSTEMS\n')
	print('INPUTS: STEP-SIZE, PROCESS(START, END, START_TIME)')
	print('OUTPUT: STATUS(SEND, RECIEVE, START_TIME, END_TIME)\n')