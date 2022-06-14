import sys
import time
import sudoku_np as sdk


def main():
    with (open('test/unfinished.txt', encoding='utf-8') as fin,
          open('test/output.txt', 'a', encoding='utf-8') as sys.stdout):
        for line in fin:
            if '//' not in line:
                puzzle = sdk.parse(line.strip())
                print(sdk.str_3x3(puzzle), end='\n\n')
                if sdk.validator(puzzle):
                    start_time = time.time()
                    attempted, count = sdk.attempt(puzzle)
                    exe_time = time.time() - start_time
                    
                    sdk.check_print(attempted)
                    print('Algorithm: Back Tracking Brutal Force (using NumPy array)')
                    print(f'Count: {count}')
                    print(f'Execution Time: {exe_time} seconds')
                    #print(f'{sudoku.back_tracking_count/exe_time} iterations per second\n\n')
                else:
                    print('The question is not valid!')
                print('-' * 50)
            

if __name__ == '__main__':
    main()