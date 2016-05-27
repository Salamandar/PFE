import qti
table_normalisation = qti.app.table("Table2")

t = qti.app.table("Table10")

# Normalize to zero
#my_min = min( t.colData(2) )
#t.setColData(2,[e-my_min for e in t.colData(2)])
#print max ( t.colData(2) )

t.addColumn()
t.setColData(3,[a/(b+1) for a,b in zip(t.colData(2),table_normalisation.colData(2))])
