from pyad import aduser
import click


@click.command()
@click.option('--names', default='', help='Enter a list of Names')
@click.option('--fn', default='', help="i.e. John")
@click.option('--ln', default='', help='i.e Doe')
def query_expiration(names,fn,ln):
    if fn:
        cn = "{} {}".format(fn,ln)
        user = aduser.ADUser.from_cn(cn)
        print "{}'s expiration date is {}".format(cn, user.get_password_last_set())
    #Example: python pyadquery.py --fn=Christian --ln=Martinez
    elif names:
        name_list = names.split(",")
        for name in name_list:
            user = aduser.ADUser.from_cn(name)
            print "{}'s expiration date is {}".format(name,user.get_password_last_set())
    #Example: python pyadquery.py --names="Christian Martinez,Vu Tran,Alex Acosta,Aaron Gaudin,Joel Chandler,Sean Clark"
    else:
        print "No names given."


if __name__ == '__main__':
    query_expiration()