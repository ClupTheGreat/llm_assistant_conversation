import argparse

# this below is for positional arguments, i believe if i place arguments one by one, that's what positionally it will accept
#                                                                           specifying the type for the argument
# add_argument("name of argument", help = "add in help for this argument", type = int, )
# 
# to add an optional arugument have, for eg: --verbose have a double dash infront of it, if the optional argument
# is not provided then the value of args.verbose will be None, so we can use an if statement
# using it with a -v will add a short option
# 
# with arguments we can have choices, donated by adding a choices = [list of choices] in the add_argument() method as an argument
#
# we can also have an actions, for eg: actions = "count", this counts the number of time and argument is repeated, like -v , -vv, -vvv
# which acts like the list of choices, and args.verbosity would have the count of of the times it has occured.
#
# to have short options, we will implement it like add_argument("-v", "--verbosity", .....) this both will result in args.verbosity having
# the value for both -v and --verbosity
#
# action = "store_true" will assign the value of args.verbose = True

def cli_parser():
    parser = argparse.ArgumentParser()

    # Used for one off question with the LLM
    parser.add_argument("-a","--ask", help='Talk to the LLM! Make sure to contain your text within "double quotes"')

    # Used for a chat, which saves conversation history with the LLM
    parser.add_argument("-c", "--chat", help='Have a conversation with the LLM, unlike ask, this will store a memory of the current conversation you are having with the LLM.')

    return parser.parse_args()



    #if args.ask:
    #    return f"{args.ask}"

if __name__ == "__main__":
    args_parser = cli_parser()
    print(args_parser)
