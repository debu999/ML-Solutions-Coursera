from fractions import Fraction
from pprint import pprint as pp
import contextlib


class Connection:
    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        pp(['Starting Transaction', self.xid])
        rslt=self.xid
        self.xid +=1
        return rslt

    def _commit_transaction(self, xid):
        pp(["commiting Transaction ", xid])


    def _rollback_transaction(self, xid):
        pp(["rollback Transaction ", xid])


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)


conn = Connection()
trx = Transaction(conn)
trx.commit()
trx.rollback()
trx = Transaction(conn)
trx.commit()
trx.rollback()
trx = Transaction(conn)
trx.commit()
trx.rollback()
trx = Transaction(conn)
trx.commit()
trx.rollback()

@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)

    try:
        yield tx

    except:
        tx.rollback()
        raise
    tx.commit()

conn = Connection()
try:
    with start_transaction(conn) as trx:
        p = 10
        # raise ValueError("p = p//0")
        q = 23
        pp("Transaction completed with {} {} {}".format(trx.xid, p, q))
except ValueError as verr:
    pp("Oops Transaction failed with details {}".format(str(verr)))




x = 2342.9301
print(dir(x))
pp([getattr(x, "imag"), callable(getattr(x, "conjugate")), x.conjugate.__class__.__name__, hasattr(x,"real")])

p = Fraction("17/3")
pp([p.numerator, p.denominator])

p = 12
pp([p.numerator, p.denominator])


pp([globals(),])
globals()["adf"]=3.1459238
pp([globals(),])

def local_scope(pldip):
    from pprint import pprint as pp1
    ppsdfs=289342
    pp1([locals()], width=10)

local_scope(73987384932)
