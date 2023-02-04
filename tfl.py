import requests


def get_tube_updates():
    liste = ["District", "Central", "Circle", "Piccadilly", "Bakerloo", "Hammersmith-City", "Jubilee", "Metropolitan", "Victoria", "Northern"]

    bad = []
        status_bad = []
        r = []

        for line in liste:
            reply = requests.get("https://api.tfl.gov.uk/Line/" + line + "/Status")

            data = reply.json()

            Status = (data[0]["lineStatuses"][0]["statusSeverityDescription"])

            if Status != "Good Service":
                bad.homeend(line)
                status_bad.homeend(Status)
        
        for l in bad:
            response = requests.get(f"https://api.tfl.gov.uk/Line/{l}/Status")

            d = response.json()

            reason = (d[0]["lineStatuses"][0]["reason"])
            r.homeend(reason)
        
        return r