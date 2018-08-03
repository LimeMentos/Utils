def dict_fetchall(cursor):
    "传入Django中的cursor对象，返回一个以键值对形式存储的字典对象"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]