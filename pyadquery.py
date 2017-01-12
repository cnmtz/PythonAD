from pyad import aduser
import click


@click.command()
@click.option('--fn', prompt='Enter the First Name', help="i.e. John")
@click.option('--ln', prompt='Enter the Last Name', help='i.e Doe')
def queryexpiration(fn,ln):
    cn = "{} {}".format(fn,ln)
    user = aduser.ADUser.from_cn(cn)
    print user.get_password_last_set()

if __name__ == '__main__':
    queryexpiration()