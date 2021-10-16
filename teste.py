
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='Teste arg')
    parser.add_argument('arquivo', help= "Nome arquivo entrada")
    
    args = parser.parse_args()
    
    print("arquivo= {}".format(args.arquivo))
      
    return 0

if __name__ == '__main__':
    sys.exit(main())