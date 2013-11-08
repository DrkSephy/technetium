"""
Module for filtering various Bitbucket data.

Handles:
    - Filtering changesets by time/user/date.
    - Filtering issues by type.
    - Filtering issues by priority.
    - Filtering issues by user.
    - Filtering issues by date.
    - Filtering issues by status.
"""
import simplejson as json
import requests
import datetime

def filter_issues(request, parsed_json):
    """
    Main filter dispatcher for issues
    """

    filtered_json = parsed_json
    for name, value in request.GET.iteritems():
        n_strip = name.strip()
        v_strip = value.strip().lower()
        if n_strip.lower() == 'type':
            filtered_json = filter_issues_by_type(filtered_json, v_strip)
        if n_strip.lower() == 'priority':
            filtered_json = filter_issues_by_priority(filtered_json, v_strip)
        if n_strip.lower() == 'status':
            filtered_json = filter_issues_by_status(filtered_json, v_strip)
        if n_strip.lower() == 'created':
            filtered_json = filter_issues_by_date(filtered_json, v_strip)

    return filtered_json


def filter_issues_by_type(parsed_json, filtered_value):
    """
    Filters issues by type.
    """

    filtered_json = []
    for issue in parsed_json:
        j_type = issue['type']
        if j_type is not None and j_type.strip().lower()==filtered_value:
            filtered_json.append(issue)

    return filtered_json


def filter_issues_by_priority(parsed_json, filtered_value):
    """
    Filters issues based on priority.
    """

    filtered_json = []
    for issue in parsed_json:
        j_prior = issue['priority']
        if j_prior is not None and j_prior.strip().lower()==filtered_value:
            filtered_json.append(issue)

    return filtered_json


def filter_issues_by_user():
    """
    Filters issues based on users.
    """

    pass


def filter_issues_by_date(parsed_json, filtered_value):
    """
    Filters issues based on date.
    """

    value = []
    case_num = 0
    today = datetime.date.today()
    if filtered_value == 'today':
        value = [today]
        case_num = 1
    elif filtered_value == 'this_week':
        this_monday = today - datetime.timedelta(today.weekday())
        value = [this_monday]
        value.append(this_monday+datetime.timedelta(1))
        value.append(this_monday+datetime.timedelta(2))
        value.append(this_monday+datetime.timedelta(3))
        value.append(this_monday+datetime.timedelta(4))
        value.append(this_monday+datetime.timedelta(5))
        value.append(this_monday+datetime.timedelta(6))
        case_num = 1
    elif filtered_value == 'last_week':
        this_monday = today - datetime.timedelta(today.weekday())
        value = [this_monday-datetime.timedelta(7)]
        value.append(this_monday-datetime.timedelta(6))
        value.append(this_monday-datetime.timedelta(5))
        value.append(this_monday-datetime.timedelta(4))
        value.append(this_monday-datetime.timedelta(3))
        value.append(this_monday-datetime.timedelta(2))
        value.append(this_monday-datetime.timedelta(1))
        case_num = 1
    elif filtered_value == 'this_month':
        value = [today]
        case_num = 2
    elif filtered_value == 'last_month':
        first_day = datetime.date(day=1, month=today.month, year=today.year)
        last_day_prev_month = first_day - datetime.timedelta(days=1)
        value = [last_day_prev_month]
        case_num = 2
    elif filtered_value == 'this_year':
        value = [today]
        case_num = 3
    elif filtered_value == 'last_year':
        last_year_from_today = today - datetime.timedelta(days=365)
        value = [last_year_from_today]
        case_num = 3

    filtered_json = []
    for issue in parsed_json:
        json_date = issue['created'].strip().lower()
        b_ok = False
        if case_num == 1:
            # for today, this week, and last week filtering
            if json_date is not None:
                j_date_obj =  datetime.datetime.strptime(json_date, '%m-%d-%Y')
                j_date_convert =  datetime.datetime.strftime(j_date_obj, '%Y-%m-%d')
                for val in value:
                    if j_date_convert == str(val):
                        b_ok = True
                        break

        elif case_num == 2:
            # for this month and last month filtering
            if json_date is not None:
                j_date_obj =  datetime.datetime.strptime(json_date, '%m-%d-%Y')
                j_date_convert =  datetime.datetime.strftime(j_date_obj, '%Y-%m')
                for val in value:
                    v_mm_yyyy = datetime.datetime.strftime(val, '%Y-%m')
                    if j_date_convert == v_mm_yyyy:
                        b_ok = True
                        break

        else:
            # for this year, and last year filtering
            if json_date is not None:
                j_date_obj =  datetime.datetime.strptime(json_date, '%m-%d-%Y')
                j_date_convert =  datetime.datetime.strftime(j_date_obj, '%Y')
                for val in value:
                    v_yyyy = datetime.datetime.strftime(val, '%Y')
                    if j_date_convert == v_yyyy:
                        b_ok = True
                        break

        if b_ok == True:
            filtered_json.append(issue)

    return filtered_json

def filter_issues_by_status(parsed_json, filtered_value):
    """
    Filters issues based on status.
    """

    filtered_json = []
    for issue in parsed_json:
        j_status = issue['status']
        if j_status is not None and j_status.strip().lower()==filtered_value:
            filtered_json.append(issue)

    return filtered_json

def filter_changesets_by_date():
    """
    Filters issues based on date/time.
    """

    pass

def filter_changesets_by_user():
    """
    Filters issues based on user.
    """

    pass

