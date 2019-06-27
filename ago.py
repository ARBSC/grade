import timeago, datetime


# date = "2019-01-11T06:00:59.000"



def time_ago(date):
    today = datetime.date.today()
    date = datetime.datetime.strptime(date[:10], '%Y-%m-%d')
    md_ago = timeago.format(date, today)
    return md_ago




