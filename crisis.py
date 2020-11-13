import pandas as pd
import csv

class Organization:
    
    def __init__(self, name, contact, email, phone, address, website, state,
                 crisis, counseling, peer, health, addiction, homelessness,
                 advocacy, medication, other, notes, etc):
        self.name = name
        self.contact = contact
        self.email = email
        self.phone = phone
        self.address = address
        self.website = website
        self.state = state
        self.crisis = crisis
        self.counseling = counseling
        self.peer = peer
        self.health = health
        self.addiction = addiction
        self.homelessness = homelessness
        self.advocacy = advocacy
        self.medication = medication
        self.other = other
        self.notes = notes
        self.etc = etc

    def to_dict(self):
        return {
            'name': self.name,
            'contact': self.contact,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'website': self.website,
            'state': self.state,
            'crisis': self.crisis,
            'counseling': self.counseling,
            'peer': self.peer,
            'health': self.health,
            'addiction': self.addiction,
            'homelessness': self.homelessness,
            'advocacy': self.advocacy,
            'medication': self.medication,
            'other': self.other,
            'notes': self.notes,
            'etc': self.etc,
            }


if __name__ == "__main__":
    orglist=[]
    with open('crisis.csv') as f:
        reader = csv.reader(f)
        next(reader, None)
        for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r in reader:
            orglist.append(Organization(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r))

    df = pd.DataFrame.from_records([s.to_dict() for s in orglist])
    df.to_html()
