import argparse
ver="aaa"
parser=argparse.ArgumentParser(description='hello description')
#parser.add_argument("e")
parser.add_argument("--hello",default='sipingroad',help="help for hello")
parser.add_argument("--hay",default='hay',help="help for hay")

parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

args = parser.parse_args()
print(args.hello)
##print(args.e)
'''
parser = argparse.ArgumentParser(prog='mico',
    description="Code management tool for MXCHIP MiCO OS - https://code.aliyun.com/mico/mico-os\nversion %s\n\nUse 'mico <command> -h|--help' for detailed help.\nOnline manual and guide available at https://code.aliyun.com/mico/mico-cube" % ver,
    formatter_class=argparse.RawTextHelpFormatter)
subparsers = parser.add_subparsers(title="Commands", metavar="           ")
parser.add_argument("--version", action="store_true", dest="version", help="print version number and exit")
'''