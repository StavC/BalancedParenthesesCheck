from Stack import Stack

def balance_check(s):

    if len(s)%2!=0:
        return False
    opening_brackets=set('([{')
    closing_brackets=set([ ('(',')'),('[',']'),('{','}') ])
    my_stack=Stack()

    for paren in s:
        if paren in opening_brackets:
            my_stack.push(paren)
        else:
            if my_stack.size()==0:
                return False

            last_open=my_stack.pop()
            if (last_open,paren) not in closing_brackets:
                return  False
    return my_stack.size()==0


def main():

    print(balance_check('[{{}}({})[]]'))




if __name__ == '__main__':
    main()
