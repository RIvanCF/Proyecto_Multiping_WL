from speedtest import Speedtest
st = Speedtest()
st.get_servers([])
print("Ping: ", st.results.ping)

