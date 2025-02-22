def rateLimiter(timestamps, ipAddresses, limit, timewindow):
    result = []
    ip_requests = {}

    for i in range(len(timestamps)):
        ts = timestamps[i]
        ip = ipAddresses[i]

        if ip not in ip_requests:
            ip_requests[ip] = []

        requests = ip_requests[ip]

        while requests and (ts - requests[0] > timewindow):
            requests.pop(0)

        if len(requests) < limit:
            requests.append(ts)
            result.append(1)
        else:
            result.append(0)
    return result

print(rateLimiter([1600000000000, 1600000000000, 1600000000001],["56.75.0.49", "62.2.159.38", "62.2.159.38"],2,10))