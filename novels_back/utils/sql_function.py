# 拼接参数化的查询语句
def concat_sql(param_list, str_sql, **kwargs):
    print(kwargs)
    for param_name, param_value in kwargs.items():
        if param_value:
            param_list.append(param_value)
            str_sql += " AND {0} = %s".format(param_name)
    return param_list, str_sql