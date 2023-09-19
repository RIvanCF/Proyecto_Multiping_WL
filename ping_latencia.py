from pythonping import ping

def ping_host(host):
    ping_result = ping(target=host, count=2, timeout=3)

    return {
        'host': host,
        'min_latency': ping_result.rtt_min_ms,
        'max_latency': ping_result.rtt_max_ms,
        'packet_loss': ping_result.packet_loss
    }

hosts = [
    '10.6.1.100',
    '10.1.2.100'''
]

for host in hosts:
    print(ping_host(host))