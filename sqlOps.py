""" SQL for a SELECT statement """
def select(table, **kwargs):
    query = list()
    query.append("SELECT * FROM %s " % table)
    if kwargs:
        query.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.items()))
    query.append(";")
    return "".join(query)

""" SQL for a INSERT statement """
def insert(table, **kwargs):
    """ insert rows into objects table (update if the row already exists)
        given the key-value pairs in kwargs """
    keys = ["%s" % k for k in kwargs]
    values = ["'%s'" % v for v in kwargs.values()]
    query = list()
    query.append("INSERT INTO %s (" % table)
    query.append(", ".join(keys))
    query.append(") VALUES (")
    query.append(", ".join(values))
    query.append(");")
    return "".join(query)

""" SQL for a DELETE statement """
def delete(table, **kwargs):
    """ deletes rows from table where **kwargs match """
    query = list()
    query.append("DELETE FROM %s " % table)
    query.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.items()))
    query.append(";")
    return "".join(query)