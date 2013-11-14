"""
Module for filtering various Bitbucket data.

Handles:
    - Filtering changesets by time/user/date.
    - Filtering issues by type.
    - Filtering issues by priority.
    - Filtering issues by user.
    - Filtering issues by date.
    - Filtering issues by status.

Place holder code for views:
    # get filtering name value pairs from request query string
    name_val_dict = {}
    filterNameValues = {}
    for n, v in request.GET.iteritems():
        name_val_dict[n] = v
        filterNameValues[n] = v

    # We need to parse this before in the future
    data['filterNameValues'] = filterNameValues

In bitissues:
    # Parse assignee
    data['assignee'] = ''
    data['assignee_avatar'] = ''
    if 'responsible' in issue:
        data['assignee'] = issue['responsible']['display_name']
        data['assignee_avatar'] = issue['responsible']['avatar']

"""
import simplejson as json
import datetime

def filter_issues(name_val_dict, parsed_json):
    """
    Main filter dispatcher for issues
    """

    filtered_json = parsed_json
    for name, value in name_val_dict.iteritems():
        n_strip = name.strip().lower()
        v_strip = value.strip().lower()
        if n_strip == 'type':
            filtered_json = filter_issues_by_type(filtered_json, v_strip)
        if n_strip == 'priority':
            filtered_json = filter_issues_by_priority(filtered_json, v_strip)
        if n_strip == 'status':
            filtered_json = filter_issues_by_status(filtered_json, v_strip)
        if n_strip == 'created':
            filtered_json = filter_issues_by_date(filtered_json, v_strip)
        if n_strip == 'assignee':
            filtered_json = filter_issues_by_user(filtered_json, v_strip)

    return filtered_json


def filter_issues_by_type(parsed_json, filtered_value):
    """
    Filters issues by type.
    """

    filtered_value = filtered_value.lower()
    filtered_json = []
    for issue in parsed_json:
        if 'type' in issue:
            if issue['type'].strip().lower()==filtered_value:
                filtered_json.append(issue)

    return filtered_json


def filter_issues_by_priority(parsed_json, filtered_value):
    """
    Filters issues based on priority.
    """

    filtered_value = filtered_value.lower()
    filtered_json = []
    for issue in parsed_json:
        if 'priority' in issue:
            if issue['priority'].strip().lower()==filtered_value:
                filtered_json.append(issue)

    return filtered_json


def filter_issues_by_user(parsed_json, filtered_value):
    """
    Filters issues based on users.
    """

    filtered_value = filtered_value.lower()
    filtered_json = []
    for issue in parsed_json:
        if 'assignee' in issue:
            j_assignee = issue['assignee']
            if j_assignee.strip().lower()==filtered_value:
                filtered_json.append(issue)
            elif filtered_value == 'unassigned' and j_assignee == '':
                filtered_json.append(issue)

    return filtered_json


def filter_issues_by_date(parsed_json, filtered_value):
    """
    Filters issues based on date.
    """

    filtered_value = filtered_value.lower()
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
        if 'created' in issue:
            json_date = issue['created'].strip().lower()
            b_ok = False
            if case_num == 1:
                # for today, this week, and last week filtering
                j_date_obj = datetime.datetime.strptime(json_date, '%m-%d-%Y')
                j_date_convert = datetime.datetime.strftime(j_date_obj, '%Y-%m-%d')
                for val in value:
                    if j_date_convert == str(val):
                        b_ok = True
                        break

            elif case_num == 2:
                # for this month and last month filtering
                j_date_obj = datetime.datetime.strptime(json_date, '%m-%d-%Y')
                j_date_convert = datetime.datetime.strftime(j_date_obj, '%Y-%m')
                for val in value:
                    v_mm_yyyy = datetime.datetime.strftime(val, '%Y-%m')
                    if j_date_convert == v_mm_yyyy:
                        b_ok = True
                        break

            else:
                # for this year, and last year filtering
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

    filtered_value = filtered_value.lower()
    filtered_json = []
    for issue in parsed_json:
        if 'status' in issue:
            if issue['status'].strip().lower()==filtered_value:
                filtered_json.append(issue)

    return filtered_json

def filter_changesets_by_date(parsed_json, filtered_value):
    """
    Filters issues based on date/time.
    """

    filtered_value = filtered_value.lower()
    filtered_json = []
    # TODO when date format is defined in parse changeset method
    filtered_json = parsed_json

    return filtered_json

def filter_changesets_by_user(parsed_json, filtered_value):
    """
    Filters issues based on user.
    """

    filtered_value = filtered_value.lower()
    filtered_json = []
    for changeset in parsed_json:
        if 'author' in changeset:
            j_author = changeset['author']
            if j_author.strip().lower()==filtered_value:
                filtered_json.append(changeset)

    return filtered_json

