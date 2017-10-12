import sys

print(sys.getdefaultencoding())

def main(filename):
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        for ln in f:
            print(ln.strip())
            sys.stdout.write(ln)
        f.close()
    except:
        print("File opearation met with error.")
    finally:
        f.close()

if __name__ == "__main__":
    main(sys.argv[1])

