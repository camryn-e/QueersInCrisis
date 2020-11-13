import pandas as pd
import csv

## From https://stackoverflow.com/questions/50807744/apply-css-class-to-pandas-dataframe-using-to-html
## Set up minimum HTML required for DataTable in iFrame
## You need to double the braces for proper Python rendering of javascript
## function
html_string = '''
<html lang="en-us">
 <link rel="shortcut icon" href='https://clubrunner.blob.core.windows.net/00000305556/Favicon/favicon.ico?time=637407227082223373' />
  <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
  <link href="http://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css" rel="stylesheet" type="text/css">
  <script src="http://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){{
            $('.dataframe').DataTable( {{
                paging: true,
                stateSave: true,
                searching: true
            }});
         }});
    </script>
<style>
title.hidden {{
  visibility: hidden;
}}
html {{
  font-family: 'Open Sans', Helvetica, Arial, sans-serif;
}}
</style>
<!-- Hidden Title -->
<title class="hidden">Crisis Resource Table</title>
  <body>
    {table}
  </body>
</html>
'''

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

    ## Save df as an HTML table with customized style
    ## "display" is a data.tables default with striped rows
    ## you don't need table_id, but might be helpful for other iFrame approaches
    with open('docs/crisis-resources-datatable.html', 'w') as f:
        f.write(html_string.format(table=df.to_html(index=False, \
         classes='display', escape=False, table_id="CRtable")))
        f.close()
