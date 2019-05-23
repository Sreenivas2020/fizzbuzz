
import create_ticket

def gethostcount():
    r_json = create_ticket.response.json()
    ticket = r_json["response"]["serviceTicket"]
    header = {"content-type": "application/json", "X-Auth-Token":ticket}
    controller='devnetapi.cisco.com/sandbox/apic_em'
    url = "https://" + controller + "/api/v1/host/count"
    response = requests.get(url, headers=header, verify=False)
    counts = response.json()["response"]
    return counts
print(gethostcount())
