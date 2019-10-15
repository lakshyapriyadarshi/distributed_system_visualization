def status_report_unicast(process_table):
        print('\n     STATUS OF CLOCKS\n     EVENT       P(A)   P(B)   T(1)   T(2)')
        for index,status in enumerate(process_table):
                data = status[1]
                print(index+1,'. ',str(status[0]).ljust(12),str(data[0]).ljust(6), str(data[1]).ljust(6),str(data[2]).ljust(6),str(data[3]).ljust(5))



def status_report_multicast(process_table):
        print('\n     STATUS OF CLOCKS\n     EVENT       P(A)   P(B)    P(C)   T(1)   T(2)')
        for index,status in enumerate(process_table):
                data = status[1]
                if status[0] == 'INTERNAL':
                        data.insert(1,'x')
                        data.insert(2,'x')
                print(index+1, '. ',str(status[0]).ljust(12), str(data[0]).ljust(6), str(data[1]).ljust(7),
                      str(data[2]).ljust(6), str(data[3]).ljust(6), str(data[4]).ljust(6))

def information():
	print('\nVISUALIZE CLOCK SYNCHRONIZATION IN DISTRIBUTED SYSTEMS\n')
	print('INPUTS: STEP-SIZE, PROCESS(START, END, START_TIME)')
	print('OUTPUT: STATUS(SEND, RECIEVE, START_TIME, END_TIME)\n')
