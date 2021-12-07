import uuid

from pip._vendor.distlib.compat import raw_input
from sqlalchemy.orm import aliased

import database
from tables import Partner, Debts, Products

database.initTables()

def operation_proc():
 go=True
 while(go):
    operation = raw_input('operation ')
    if operation=="new partner":
        name=raw_input('name ')
        code = raw_input('code ')
        new_partner(name,code)
    elif operation=="get partners":
        recs=database.session.query(Partner).all()
        for rec in recs:
            print("name "+str(rec.name)+" code "+str(rec.code))

    elif operation == "add debt":
       name=raw_input('name ')
       sum = raw_input('sum ')
       recs=database.session.query(Partner).where(Partner.name==name).all()
       for rec in recs:
         newrec= Debts(partner_id=rec.id,id=str(uuid.uuid1()),sum=sum)
         database.session.add(newrec)
         database.session.commit()
    elif operation == "get debts":
          recs = database.session.query(Debts,Partner).outerjoin(Partner,Debts.partner_id==Partner.id).all()
          for debts,partner in recs:
            print(partner.name+" "+str(debts.sum))
    elif operation == "new product":
        name = raw_input('name ')
        parent = raw_input('name ')
        parent_id=""
        if parent!="":
            recs=database.session.query(Products).where(Products.name==parent).all()
            if len(recs)>0:
                rec_par=recs[0]
                parent_id=rec_par.id;
        newrec = Products(id=str(uuid.uuid1()), name=name, parent_id=parent_id)
        database.session.add(newrec)
        database.session.commit()
    elif operation == "get products":
          Products1 = aliased(Products)
          Parents = aliased(Products)
          recs = database.session.query(Products1,Parents).outerjoin(Parents,Products1.parent_id==Parents.id).all()
          for pr,par in recs:
              parent_name="<>"
              if par!= None:
                  parent_name= str(par.name)

              print(pr.name+" in group "+parent_name)
    elif operation == "x":
        go=False

def new_partner(name,code):
    p1=Partner(id=str(uuid.uuid1()),name=name,code=code)
    database.session.add(p1)
    database.session.commit()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    operation_proc()

