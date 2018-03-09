"""Template tags for performance module."""

from django import template

register = template.Library()


@register.simple_tag
def get_service_names(services):
    """Return a string with comma separated service names."""
    return ', '.join([x.name for x in services])


@register.simple_tag
def is_filtered(request):
    """Return a boolean value signifying if the request has filters or not."""
    return ('env' in request.GET and request.GET.get('env') != 'All') or \
        ('ver' in request.GET and request.GET.get('ver') != 'All') or \
        ('tenant' in request.GET and request.GET.get('tenant') != 'All') or \
        ('service' in request.GET and request.GET.get('service') != 'All')


@register.simple_tag
def get_critical_observation_for_test(service):
    """Return a dict with critical points for each request."""
    all_requests = []
    for load in service.load_users:
        requests = [x.request for x in load.test_results]
        all_requests += requests
    all_requests = list(set(all_requests))
    critical_points = {}
    for request in all_requests:
        points = []
        for user_load in service.load_users:
            found = False
            for test_result in user_load.test_results:
                if test_result.request == request:
                    found = True
                    if int(test_result.min_time) > 100:
                        points.append("%s ms" % test_result.min_time)
                    else:
                        points.append('')
                    if int(test_result.median_time) > 1000:
                        points.append("%s ms" % test_result.median_time)
                    else:
                        points.append('')
                    if int(test_result.err_percentage) > 10:
                        points.append("%s " % test_result.err_percentage+'%')
                    else:
                        points.append('')
                    break
            if not found:
                points += ['NA', 'NA', 'NA']
        if [x for x in points if x and x != 'NA'] != []:
            critical_points.update({request: points})
    return critical_points
