s = input('Enter your file name: ')
if s != "sample.txt":
    print(f'Error: the file {s} does not exist')
else:
    try:
        with open(s, 'r') as file1:
            print('Reading file content:')
            r = file1.readlines()
            if len(r) >= 2:
                r1 = r[0].rstrip('\n')
                r2 = r[1].rstrip('\n')
                print(f'Line 1: {r1}\nLine 2: {r2}')
            else:
                print('Error: The file does not have at least two lines.')
    except FileNotFoundError:
        print(f'Error: The file {s} was not found.')


file1=open('output.txt','w')
w=file1.write(input('enter text to write to the file :'))
print('data successfully written to output.txt')
file1.close()

file1=open('output.txt','a')
w=(input('enter additional text to append : '))
file1.write('\n'+w)
print('data successfully appended')
file1.close()

file1=open('output.txt','r')
print('final content of output.txt :')
r = file1.readlines()
r1 = r[0].rstrip()
r2 = r[1].rstrip()
print(f'{r1}\n{r2}')
file1.close()
